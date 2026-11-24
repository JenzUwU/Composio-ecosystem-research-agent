/* =========================================================
   Skyline — vanilla port of the React <ContributionSkyline>
   (contribution-skyline.tsx). Same scene idea: one grid of boxes that
   is a flat heat map seen from above (2D) and an isometric skyline seen
   from the corner (3D). Switching swings one camera while bars rise in
   a wave, column by column.

   Adapted for this report:
   - Generic grid (cols × rows) instead of a 53-week calendar: here
     10 categories × 10 apps. No dates, so no streak/calendar stats.
   - Several metrics; switching metric eases every bar to its new height.
   - Monochrome palette only (greys → black) to match Monochrome Signal.
   - value === null means "no data" — drawn as an empty slab, never as 0-is-good.

   API:  Skyline.mount(element, { cols, rows, colLabels, rowLabels, metrics })
         metrics[i] = { key, label, unit, unitPlural, cells[], stats[], hint }
         cells[j]   = { col, row, value|null, name, sub, note }
   ========================================================= */
(function () {
  "use strict";

  const clamp01 = (v) => (v > 0 ? (v < 1 ? v : 1) : 0);
  const lerp = (a, b, t) => a + (b - a) * t;
  const easeInOutCubic = (x) => { const t = clamp01(x); return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };
  const easeOutCubic = (x) => 1 - Math.pow(1 - clamp01(x), 3);
  const smoothstep = (a, b, x) => { const t = clamp01((x - a) / (b - a)); return t * t * (3 - 2 * t); };

  const WAVE = 0.42;
  const riseAt = (t, col, cols, row, rows) => {
    const d = (cols > 1 ? col / (cols - 1) : 0) * 0.36 + (rows > 1 ? row / (rows - 1) : 0) * 0.06;
    return easeOutCubic((t - d) / (1 - WAVE));
  };
  const YAW_3D = Math.PI / 4, ELEV_3D = (34 * Math.PI) / 180;
  const YAW_RANGE = [(8 * Math.PI) / 180, (82 * Math.PI) / 180];
  const ELEV_RANGE = [(18 * Math.PI) / 180, (62 * Math.PI) / 180];
  const camera = (e, dYaw = 0, dElev = 0) => {
    const yaw = Math.min(YAW_RANGE[1], Math.max(0, lerp(0, YAW_3D + dYaw, e)));
    const elev = lerp(Math.PI / 2, Math.min(ELEV_RANGE[1], Math.max(ELEV_RANGE[0], ELEV_3D + dElev)), e);
    return { cs: Math.cos(yaw), sn: Math.sin(yaw), se: Math.sin(elev), ce: Math.cos(elev) };
  };
  const project = (c, x, y, z) => [x * c.cs - y * c.sn, (x * c.sn + y * c.cs) * c.se - z * c.ce];
  const barHeight = (v, max, scale) => (v > 0 && max > 0 ? 0.4 + Math.pow(v / max, 0.85) * 7.2 * scale : 0.2);
  const levelOf = (v, busy) => (!(v > 0) ? 0 : busy <= 0 ? 4 : 1 + Math.min(3, Math.floor((v / busy) * 4)));

  // Monochrome: empty, then light → heavy. Black only, per the brief.
  // light → dark blue ramp; level 3 is the page accent (#0000DD)
  const SWATCHES = ["#DADAFB", "#A6A6F3", "#5C5CE9", "#0000DD", "#00006B"];
  const LEVEL_NAMES = ["No data / zero", "Light", "Moderate", "Heavy", "Heaviest"];
  const FG = [23, 23, 23], BG = [241, 241, 239];
  const hex = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
  const COLS = SWATCHES.map(hex);
  const rgb = (r, g, b) => "rgb(" + Math.round(r) + "," + Math.round(g) + "," + Math.round(b) + ")";
  const esc = (v) => String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  const pointInQuad = (p, o, x, y) => {
    let sign = 0;
    for (let k = 0; k < 4; k++) {
      const ax = p[o + k * 2], ay = p[o + k * 2 + 1], bx = p[o + ((k + 1) % 4) * 2], by = p[o + ((k + 1) % 4) * 2 + 1];
      const cross = (bx - ax) * (y - ay) - (by - ay) * (x - ax);
      if (Math.abs(cross) < 1e-9) continue;
      const s = cross > 0 ? 1 : -1;
      if (sign === 0) sign = s; else if (s !== sign) return false;
    }
    return sign !== 0;
  };
  const quadPath = (ctx, p, o) => {
    ctx.moveTo(p[o], p[o + 1]); ctx.lineTo(p[o + 2], p[o + 3]); ctx.lineTo(p[o + 4], p[o + 5]); ctx.lineTo(p[o + 6], p[o + 7]); ctx.closePath();
  };

  function mount(root, opts) {
    const { cols, rows, colLabels = [], rowLabels = [], metrics = [] } = opts;
    const n = cols * rows;
    let metricIdx = 0;
    let view = "3d";

    root.classList.add("sky");
    root.innerHTML = `
      <header class="sky-head">
        <div class="sky-seg" role="group" aria-label="Metric">
          ${metrics.map((m, i) => `<button type="button" data-metric="${i}" aria-pressed="${i === 0}">${esc(m.label)}</button>`).join("")}
        </div>
        <div class="sky-seg sky-view" role="group" aria-label="Chart view">
          <button type="button" data-view="2d" aria-pressed="false" title="Flat heat map">2D</button>
          <button type="button" data-view="3d" aria-pressed="true" title="3D skyline">3D</button>
        </div>
      </header>
      <div class="sky-wrap">
        <div class="sky-stage"><canvas tabindex="0" role="img"></canvas></div>
        <div class="sky-tip" role="tooltip" aria-hidden="true"></div>
      </div>
      <div class="sky-stats"></div>
      <div class="sky-foot">
        <span class="sky-hint"></span>
        <div class="sky-legend"><span>Less</span>${SWATCHES.map((c, i) => `<button type="button" data-level="${i}" aria-pressed="false" title="${LEVEL_NAMES[i]}" aria-label="Highlight ${LEVEL_NAMES[i].toLowerCase()}" style="background:${c}"></button>`).join("")}<span>More</span></div>
      </div>
      <p class="sr-only" aria-live="polite"></p>`;

    const stage = root.querySelector(".sky-stage");
    const canvas = root.querySelector("canvas");
    const tip = root.querySelector(".sky-tip");
    const live = root.querySelector("[aria-live]");
    const ctx = canvas.getContext("2d");
    const reduceMq = { matches: false }; // reduced-motion gating removed on request: always animate
    let reduced = reduceMq.matches;

    // scene state
    let t = 0, target = 0, entered = false;
    let yaw = 0, elev = 0, yawGoal = 0, elevGoal = 0;
    let W = 0, H2 = 0, H3 = 0, Hmax = 0, lastH = -1, dpr = 1, gutter = 34;
    const font = '500 10px "JetBrains Mono", ui-monospace, monospace';
    const cx = new Float32Array(n), cy = new Float32Array(n);
    const hgt = new Float32Array(n), hgtGoal = new Float32Array(n), zs = new Float32Array(n);
    const lv = new Uint8Array(n), hover = new Float32Array(n), dim = new Float32Array(n);
    const polys = new Float32Array(n * 24), faces = new Uint8Array(n);
    const order = Array.from({ length: n }, (_, i) => i);
    let cellsByIdx = new Array(n).fill(null);
    let legendLevel = -1, hovered = -1, pinned = -1, activeIdx = -1, raf = 0, last = 0;
    for (let c = 0; c < cols; c++) for (let r = 0; r < rows; r++) { const i = c * rows + r; cx[i] = c; cy[i] = r; }

    const M = () => metrics[metricIdx];
    const noun = (v) => (v === 1 ? M().unit : M().unitPlural || M().unit + "s");

    function loadMetric(first) {
      cellsByIdx = new Array(n).fill(null);
      M().cells.forEach((c) => { if (c.col < cols && c.row < rows) cellsByIdx[c.col * rows + c.row] = c; });
      const vals = cellsByIdx.map((c) => (c && c.value > 0 ? c.value : 0));
      const nz = vals.filter((v) => v > 0).sort((a, b) => a - b);
      const busy = nz.length ? nz[Math.floor(0.95 * (nz.length - 1))] : 0;
      const max = nz.length ? nz[nz.length - 1] : 0;
      for (let i = 0; i < n; i++) {
        lv[i] = levelOf(vals[i], busy);
        hgtGoal[i] = barHeight(vals[i], max, opts.heightScale || 0.85);
        if (first || reduced) hgt[i] = hgtGoal[i];
      }
      root.querySelectorAll("[data-metric]").forEach((b) => b.setAttribute("aria-pressed", String(+b.dataset.metric === metricIdx)));
      root.querySelector(".sky-stats").innerHTML = (M().stats || []).map((s) =>
        `<div class="sky-stat"><span class="label">${esc(s.label)}</span><b>${esc(s.value)}</b><span class="sky-stat-unit">${esc(s.unit || "")}</span><span class="sky-stat-sub">${esc(s.sub || "")}</span></div>`).join("");
      updateHint();
      canvas.setAttribute("aria-label", `${M().label} for ${n} apps in ${cols} categories, shown as a ${view === "3d" ? "3D skyline" : "heat map"}. Use the arrow keys to read individual apps.`);
      if (activeIdx >= 0) renderTip();
      kick();
    }
    function updateHint() {
      root.querySelector(".sky-hint").textContent = (M().hint ? M().hint + " · " : "") + (view === "3d" ? "Drag to orbit · double-click to reset" : "Hover a cell · arrow keys to explore");
    }

    const extent = (cam, e, full) => {
      const w = lerp(0.78, 0.9, e), off = (1 - w) / 2;
      let minx = Infinity, maxx = -Infinity, miny = Infinity, maxy = -Infinity;
      const add = (x, y, z) => { const p = project(cam, x, y, z); if (p[0] < minx) minx = p[0]; if (p[0] > maxx) maxx = p[0]; if (p[1] < miny) miny = p[1]; if (p[1] > maxy) maxy = p[1]; };
      for (let i = 0; i < n; i++) {
        const x0 = cx[i] + off, y0 = cy[i] + off, z = full ? Math.max(hgt[i], hgtGoal[i]) * e : zs[i];
        add(x0, y0, z); add(x0 + w, y0, z); add(x0, y0 + w, z); add(x0 + w, y0 + w, 0); add(x0, y0 + w, 0); add(x0 + w, y0, 0);
      }
      add(0, rows + 1.4 * e, 0); add(cols, rows + 1.4 * e, 0);
      return { minx, maxx, miny, maxy };
    };

    function relayout() {
      const w = Math.round(stage.clientWidth);
      if (!w) return;
      W = w; gutter = W < 520 ? 0 : 34;
      dpr = Math.min(2, window.devicePixelRatio || 1);
      const b2 = extent(camera(0), 0, true);
      H2 = Math.min(24 + ((b2.maxy - b2.miny) / (b2.maxx - b2.minx)) * (W - gutter - 4), 380);
      const b3 = extent(camera(1), 1, true);
      const natural = ((b3.maxy - b3.miny) / (b3.maxx - b3.minx)) * (W - 40) + 40;
      H3 = Math.max(Math.min(natural, W * 0.72, 520), Math.min(natural, 260));
      Hmax = Math.ceil(Math.max(H2, H3));
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(Hmax * dpr);
      canvas.style.width = W + "px"; canvas.style.height = Hmax + "px";
      lastH = -1;
      draw();
    }

    function draw() {
      if (!W) return;
      const e = easeInOutCubic(t);
      const cam = camera(e, yaw, elev);
      const Hc = lerp(H2, H3, e);
      if (Math.abs(Hc - lastH) > 0.2) { stage.style.height = Hc.toFixed(1) + "px"; lastH = Hc; }
      for (let i = 0; i < n; i++) zs[i] = riseAt(t, cx[i], cols, cy[i], rows) * hgt[i];
      const b = extent(cam, e, false);
      const pad = lerp(4, 20, e), left = pad + gutter * (1 - e), top = pad + 18 * (1 - e);
      const aw = W - left - pad, ah = Hc - top - pad;
      const bw = Math.max(1e-6, b.maxx - b.minx), bh = Math.max(1e-6, b.maxy - b.miny);
      const s = Math.min(aw / bw, ah / bh);
      const ox = left + (aw - bw * s) / 2 - b.minx * s, oy = top + (ah - bh * s) / 2 - b.miny * s;
      const { cs, sn, se, ce } = cam;
      const px = (x, y) => ox + (x * cs - y * sn) * s;
      const py = (x, y, z) => oy + ((x * sn + y * cs) * se - z * ce) * s;

      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, Hmax);
      order.sort((a, c) => (cx[a] + 0.5) * sn + (cy[a] + 0.5) * cs - ((cx[c] + 0.5) * sn + (cy[c] + 0.5) * cs));

      const w = lerp(0.82, 0.9, e), off = (1 - w) / 2, lift = 0.7 * e;
      const edgeA = 0.55 * e; // light edges keep black boxes readable in 3D
      for (let k = 0; k < n; k++) {
        const i = order[k];
        const x0 = cx[i] + off, y0 = cy[i] + off, x1 = x0 + w, y1 = y0 + w;
        const z = zs[i] + hover[i] * lift, o = i * 24;
        polys[o] = px(x0, y0); polys[o + 1] = py(x0, y0, z);
        polys[o + 2] = px(x1, y0); polys[o + 3] = py(x1, y0, z);
        polys[o + 4] = px(x1, y1); polys[o + 5] = py(x1, y1, z);
        polys[o + 6] = px(x0, y1); polys[o + 7] = py(x0, y1, z);
        polys[o + 8] = px(x0, y1); polys[o + 9] = py(x0, y1, 0);
        polys[o + 10] = px(x1, y1); polys[o + 11] = py(x1, y1, 0);
        polys[o + 12] = polys[o + 4]; polys[o + 13] = polys[o + 5];
        polys[o + 14] = polys[o + 6]; polys[o + 15] = polys[o + 7];
        polys[o + 16] = px(x1, y0); polys[o + 17] = py(x1, y0, 0);
        polys[o + 18] = polys[o + 10]; polys[o + 19] = polys[o + 11];
        polys[o + 20] = polys[o + 4]; polys[o + 21] = polys[o + 5];
        polys[o + 22] = polys[o + 2]; polys[o + 23] = polys[o + 3];
        const tall = z * ce * s;
        let f = 0;
        if (tall > 0.35 && w * cs * s > 0.35) f |= 1;
        if (tall > 0.35 && w * sn * s > 0.35) f |= 2;
        faces[i] = f;

        let [r, g, bl] = COLS[lv[i]];
        const d = dim[i];
        if (d > 0.002) { const E = COLS[0]; r += (E[0] - r) * 0.8 * d; g += (E[1] - g) * 0.8 * d; bl += (E[2] - bl) * 0.8 * d; }
        const hv = hover[i];
        // side faces: light level → darker sides; dark level → lighter sides so the form still reads
        const dark = 0.299 * r + 0.587 * g + 0.114 * bl < 90; // perceived luminance, works for coloured ramps
        const sideL = dark ? [r + 38, g + 38, bl + 38] : [r * 0.84, g * 0.84, bl * 0.84];
        const sideR = dark ? [r + 18, g + 18, bl + 18] : [r * 0.68, g * 0.68, bl * 0.68];
        const edge = "rgba(" + BG.join(",") + "," + edgeA.toFixed(3) + ")";
        if (f & 1) { ctx.beginPath(); quadPath(ctx, polys, o + 8); ctx.fillStyle = rgb(...sideL); ctx.fill(); if (edgeA > 0.02) { ctx.strokeStyle = edge; ctx.lineWidth = 0.6; ctx.stroke(); } }
        if (f & 2) { ctx.beginPath(); quadPath(ctx, polys, o + 16); ctx.fillStyle = rgb(...sideR); ctx.fill(); if (edgeA > 0.02) { ctx.strokeStyle = edge; ctx.lineWidth = 0.6; ctx.stroke(); } }
        ctx.beginPath(); quadPath(ctx, polys, o);
        ctx.fillStyle = rgb(r, g, bl); ctx.fill();
        if (edgeA > 0.02 && dark) { ctx.strokeStyle = edge; ctx.lineWidth = 0.6; ctx.stroke(); }
        if (hv > 0.02) { ctx.strokeStyle = "rgba(23,23,23," + (0.95 * hv).toFixed(3) + ")"; ctx.lineWidth = 2; ctx.stroke(); }
      }

      // labels: top + left in 2D, front edge in 3D; they fade, never pop
      ctx.font = font;
      const a2 = 1 - smoothstep(0, 0.4, e), a3 = smoothstep(0.62, 1, e);
      if (a2 > 0.004) {
        ctx.fillStyle = "rgba(95,95,92," + a2.toFixed(3) + ")";
        ctx.textAlign = "center"; ctx.textBaseline = "bottom";
        for (let c = 0; c < cols; c++) if (colLabels[c]) ctx.fillText(colLabels[c], px(c + 0.5, -0.2), py(c + 0.5, -0.2, 0) - 3);
        ctx.textAlign = "right"; ctx.textBaseline = "middle";
        if (gutter > 0) for (let r = 0; r < rows; r += 1) if (rowLabels[r] && (r % 3 === 0 || r === rows - 1)) ctx.fillText(rowLabels[r], px(0, r + 0.5) - 6, py(0, r + 0.5, 0));
      }
      if (a3 > 0.004) {
        ctx.fillStyle = "rgba(95,95,92," + a3.toFixed(3) + ")";
        ctx.textAlign = "left"; ctx.textBaseline = "top";
        for (let c = 0; c < cols; c++) if (colLabels[c]) ctx.fillText(colLabels[c], px(c + 0.5, rows + 0.3), py(c + 0.5, rows + 0.3, 0) + 2);
      }

      if (activeIdx >= 0) {
        const i = activeIdx, z = zs[i] + hover[i] * lift;
        const tx = px(cx[i] + 0.5, cy[i] + 0.5);
        const ty = Math.min(py(cx[i] + off, cy[i] + off, z), py(cx[i] + off + w, cy[i] + off, z), py(cx[i] + off, cy[i] + off + w, z));
        const half = tip.offsetWidth / 2;
        const c = Math.min(W - half - 2, Math.max(half + 2, tx));
        // Above the cell by default. If that would cover the column labels or run past the top
        // of the stage (top rows), flip below the cell's base instead, arrow pointing up.
        const labelBand = 22;
        const below = ty - 10 - tip.offsetHeight < labelBand;
        if (below) {
          const by = Math.max(py(cx[i] + off, cy[i] + off + w, 0), py(cx[i] + off + w, cy[i] + off + w, 0), py(cx[i] + off + w, cy[i] + off, 0));
          tip.style.transform = "translate(" + (c - half).toFixed(1) + "px," + (by + 10).toFixed(1) + "px)";
        } else {
          tip.style.transform = "translate(" + (c - half).toFixed(1) + "px," + (ty - 10).toFixed(1) + "px) translateY(-100%)";
        }
        tip.classList.toggle("below", below);
        tip.style.setProperty("--arrow", (tx - c + half).toFixed(1) + "px");
      }
    }

    function tick(now) {
      raf = 0;
      const dt = Math.min(0.05, Math.max(0, (now - last) / 1000)); last = now;
      let moving = false;
      if (t !== target) {
        const step = reduced ? 1 : (dt * 1000) / (opts.duration || 1300);
        t = target > t ? Math.min(target, t + step) : Math.max(target, t - step);
        moving = true;
      }
      const ko = reduced ? 1 : 1 - Math.exp(-dt * 12);
      yaw += (yawGoal - yaw) * ko; elev += (elevGoal - elev) * ko;
      if (Math.abs(yawGoal - yaw) > 1e-4 || Math.abs(elevGoal - elev) > 1e-4) moving = true; else { yaw = yawGoal; elev = elevGoal; }
      const kg = reduced ? 1 : 1 - Math.exp(-dt * 6);
      const kh = reduced ? 1 : 1 - Math.exp(-dt * 16), kd = reduced ? 1 : 1 - Math.exp(-dt * 10);
      for (let i = 0; i < n; i++) {
        if (hgt[i] !== hgtGoal[i]) { hgt[i] = Math.abs(hgtGoal[i] - hgt[i]) < 0.005 ? hgtGoal[i] : hgt[i] + (hgtGoal[i] - hgt[i]) * kg; moving = true; }
        const hg = i === activeIdx ? 1 : 0, dg = legendLevel >= 0 && lv[i] !== legendLevel ? 1 : 0;
        if (hover[i] !== hg) { hover[i] = Math.abs(hg - hover[i]) < 0.003 ? hg : hover[i] + (hg - hover[i]) * kh; moving = true; }
        if (dim[i] !== dg) { dim[i] = Math.abs(dg - dim[i]) < 0.003 ? dg : dim[i] + (dg - dim[i]) * kd; moving = true; }
      }
      draw();
      if (moving) raf = requestAnimationFrame(tick);
    }
    function kick() { if (raf) return; last = performance.now(); raf = requestAnimationFrame(tick); }

    function describe(i) {
      const c = cellsByIdx[i];
      if (!c) return "No app in this cell";
      const v = c.value == null ? (c.note || "No data") : `${c.value} ${noun(c.value)}`;
      return `${c.name}: ${v}${c.sub ? " · " + c.sub : ""}`;
    }
    function renderTip() {
      const c = cellsByIdx[activeIdx];
      if (!c) { tip.innerHTML = "<strong>Empty cell</strong>"; return; }
      const v = c.value == null ? esc(c.note || "No data") : `${c.value} ${esc(noun(c.value))}`;
      tip.innerHTML = `<strong>${esc(c.name)}</strong><span>${v}${c.sub ? " · " + esc(c.sub) : ""}</span>`;
    }
    function refreshActive() {
      const next = hovered >= 0 ? hovered : pinned;
      if (next === activeIdx) return;
      activeIdx = next;
      if (next >= 0) { renderTip(); tip.style.opacity = "1"; tip.setAttribute("aria-hidden", "false"); }
      else { tip.style.opacity = "0"; tip.setAttribute("aria-hidden", "true"); }
      kick();
    }
    const hit = (x, y) => {
      for (let k = n - 1; k >= 0; k--) {
        const i = order[k], o = i * 24;
        if (pointInQuad(polys, o, x, y)) return i;
        if (faces[i] & 1 && pointInQuad(polys, o + 8, x, y)) return i;
        if (faces[i] & 2 && pointInQuad(polys, o + 16, x, y)) return i;
      }
      return -1;
    };
    const local = (ev) => { const r = canvas.getBoundingClientRect(); return [ev.clientX - r.left, ev.clientY - r.top]; };

    let drag = null;
    canvas.addEventListener("pointerdown", (ev) => {
      if (ev.button !== 0) return;
      const can = target === 1;
      drag = { id: ev.pointerId, x: ev.clientX, y: ev.clientY, yaw: yawGoal, elev: elevGoal, moved: false, orbit: can, mouse: ev.pointerType === "mouse" };
      if (can) try { canvas.setPointerCapture(ev.pointerId); } catch (e) { /* optional */ }
    });
    canvas.addEventListener("pointermove", (ev) => {
      if (drag && drag.orbit && ev.pointerId === drag.id) {
        const dx = ev.clientX - drag.x, dy = ev.clientY - drag.y;
        if (drag.moved || Math.hypot(dx, dy) > 4) {
          drag.moved = true;
          yawGoal = Math.min(YAW_RANGE[1] - YAW_3D, Math.max(YAW_RANGE[0] - YAW_3D, drag.yaw + dx * 0.006));
          if (drag.mouse) elevGoal = Math.min(ELEV_RANGE[1] - ELEV_3D, Math.max(ELEV_RANGE[0] - ELEV_3D, drag.elev + dy * 0.004));
          canvas.style.cursor = "grabbing"; hovered = -1; refreshActive(); kick();
          return;
        }
      }
      if (ev.pointerType !== "mouse") return;
      const [x, y] = local(ev), i = hit(x, y);
      if (i !== hovered) { hovered = i; refreshActive(); }
      canvas.style.cursor = target === 1 ? "grab" : i >= 0 ? "pointer" : "default";
    });
    canvas.addEventListener("pointerup", (ev) => {
      if (!drag || ev.pointerId !== drag.id) return;
      const moved = drag.moved; drag = null;
      if (canvas.hasPointerCapture(ev.pointerId)) canvas.releasePointerCapture(ev.pointerId);
      canvas.style.cursor = target === 1 ? "grab" : "default";
      if (moved) return;
      const [x, y] = local(ev), i = hit(x, y);
      pinned = i === pinned ? -1 : i;
      if (ev.pointerType !== "mouse") hovered = -1;
      refreshActive();
      if (i >= 0 && cellsByIdx[i] && opts.onCellClick) opts.onCellClick(cellsByIdx[i]);
    });
    canvas.addEventListener("pointercancel", () => { drag = null; });
    canvas.addEventListener("pointerleave", () => { if (drag) return; hovered = -1; refreshActive(); });
    canvas.addEventListener("dblclick", () => { yawGoal = 0; elevGoal = 0; kick(); });
    canvas.addEventListener("keydown", (ev) => {
      const keys = ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End", "Escape", "Enter", " "];
      if (!keys.includes(ev.key)) return;
      ev.preventDefault();
      if (ev.key === "Escape") { pinned = -1; hovered = -1; refreshActive(); return; }
      let i = pinned >= 0 ? pinned : activeIdx >= 0 ? activeIdx : 0;
      if ((ev.key === "Enter" || ev.key === " ") && i >= 0) { if (cellsByIdx[i] && opts.onCellClick) opts.onCellClick(cellsByIdx[i]); return; }
      if (pinned >= 0 || activeIdx >= 0) {
        if (ev.key === "ArrowLeft") i -= rows; if (ev.key === "ArrowRight") i += rows;
        if (ev.key === "ArrowUp") i -= 1; if (ev.key === "ArrowDown") i += 1;
        if (ev.key === "Home") i = 0; if (ev.key === "End") i = n - 1;
      }
      i = Math.max(0, Math.min(n - 1, i));
      pinned = i; hovered = -1; refreshActive();
      live.textContent = describe(i);
    });
    canvas.addEventListener("blur", () => { pinned = -1; refreshActive(); });

    function setView(v) {
      view = v;
      root.querySelectorAll("[data-view]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.view === v)));
      updateHint();
      if (!entered) return;
      target = v === "3d" ? 1 : 0;
      if (target === 0) { yawGoal = 0; elevGoal = 0; }
      canvas.style.cursor = target === 1 ? "grab" : "default";
      kick();
    }
    root.querySelectorAll("[data-view]").forEach((b) => b.addEventListener("click", () => setView(b.dataset.view)));
    root.querySelectorAll("[data-metric]").forEach((b) => b.addEventListener("click", () => { metricIdx = +b.dataset.metric; loadMetric(false); }));
    const legend = root.querySelector(".sky-legend");
    legend.querySelectorAll("[data-level]").forEach((b) => {
      const L = +b.dataset.level;
      const set = (v) => { legendLevel = v; legend.querySelectorAll("[data-level]").forEach((x) => x.setAttribute("aria-pressed", String(+x.dataset.level === v))); kick(); };
      b.addEventListener("mouseenter", () => set(L));
      b.addEventListener("focus", () => set(L));
      b.addEventListener("blur", () => set(-1));
      b.addEventListener("click", () => set(legendLevel === L ? -1 : L));
    });
    legend.addEventListener("mouseleave", () => { legendLevel = -1; legend.querySelectorAll("[data-level]").forEach((x) => x.setAttribute("aria-pressed", "false")); kick(); });

    loadMetric(true);
    relayout();
    // the skyline rises out of the flat map the first time it scrolls into view
    const enter = () => { if (entered) return; entered = true; if (reduced) t = view === "3d" ? 1 : 0; setView(view); };
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver((es) => { if (es.some((x) => x.isIntersecting)) { enter(); io.disconnect(); } }, { threshold: 0.35 });
      io.observe(stage);
    } else enter();
    new ResizeObserver(() => { if (Math.round(stage.clientWidth) !== W) relayout(); }).observe(stage);
    if (reduceMq.addEventListener) reduceMq.addEventListener("change", () => { reduced = reduceMq.matches; kick(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);

    return { setView, setMetric: (i) => { metricIdx = i; loadMetric(false); } };
  }

  window.Skyline = { mount };
})();
