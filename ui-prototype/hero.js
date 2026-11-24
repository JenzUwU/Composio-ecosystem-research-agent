/* =========================================================
   FIG. 01 — Procedural ecosystem sphere (Canvas 2D, no assets)

   How it works:
   1. A Fibonacci lattice places ~1100 points evenly on a unit sphere.
      Two latitude bands are left empty to give the sphere "strata".
   2. Radial spikes (dotted rays) grow out of random surface points with
      a power-law length distribution, like a data burst.
   3. Three tilted orbital rings and 100 app nodes (10 clusters of 10 =
      10 categories x 10 apps) orbit the sphere. Each node's look comes
      from the real data: filled = adjudicated, hollow = pending,
      blue = flagged for human review (set via window.heroSetNodes).
   4. Every frame, points are rotated (Y spin + X tilt + pointer parallax)
      and projected orthographically to an OFFSCREEN canvas.
   5. The offscreen image is copied to the visible canvas in thin
      horizontal strips with gaps (scanlines). Random "glitch" events
      shift a few strips sideways (pixel displacement), and a slow scan
      band sweeps vertically.
   6. A blue research lens hops between adjudicated nodes and labels the
      app it is "reading" — real names, from the data.
  7. Pointing: while the pointer is over the canvas the spin pauses, the
      parallax is damped, glitches stop and the sphere fades to half strength,
      so nodes stay put and stand out. App nodes are drawn crisp on top of the
      scanlines (never split or shifted). The node nearest the cursor (within
      HIT css px) gets the lens and a blue bracket; click pins it, click again
      (or click empty space) to unpin and resume the tour.
   Off-screen/hidden tab: paused.
   ========================================================= */
(function () {
  "use strict";
  const canvas = document.getElementById("hero-canvas");
  if (!canvas || !canvas.getContext) return;
  const ctx = canvas.getContext("2d");
  const off = document.createElement("canvas");
  const octx = off.getContext("2d");
  const reduceMq = { matches: false }; // reduced-motion gating removed on request: always animate

  const INK = "23,23,23", RED = "#0000DD", BG = "#F1F1EF";

  // deterministic RNG so the figure is stable between reloads
  let seed = 7;
  const rnd = () => ((seed = (seed * 16807) % 2147483647) - 1) / 2147483646;

  // 1. sphere lattice
  const N = 1600, GOLD = Math.PI * (3 - Math.sqrt(5));
  const sphere = [];
  for (let i = 0; i < N; i++) {
    const y = 1 - (2 * (i + 0.5)) / N;
    if (Math.abs(y - 0.34) < 0.035 || Math.abs(y + 0.41) < 0.03) continue; // strata gaps
    const r = Math.sqrt(1 - y * y), th = i * GOLD;
    sphere.push([Math.cos(th) * r, y, Math.sin(th) * r]);
  }

  // 2. spikes
  const spikes = [];
  for (let i = 0; i < 150; i++) {
    const u = rnd() * 2 - 1, t = rnd() * Math.PI * 2, r = Math.sqrt(1 - u * u);
    const len = 0.06 + Math.pow(rnd(), 2.6) * 0.62;
    spikes.push({ d: [Math.cos(t) * r, u, Math.sin(t) * r], len, ph: rnd() * 6.28 });
  }

  // 3. orbits
  const orbits = [
    { r: 1.32, tx: 1.15, tz: 0.25, dash: 0 },
    { r: 1.5, tx: -0.55, tz: 0.9, dash: 1 },
    { r: 1.18, tx: 0.15, tz: -1.2, dash: 0 },
  ];

  // app nodes: 10 clusters x 10
  let nodes = [];
  function buildNodes(list) {
    nodes = [];
    for (let i = 0; i < 100; i++) {
      const c = Math.floor(i / 10), k = i % 10;
      const lon = (c / 10) * Math.PI * 2 + (k - 4.5) * 0.07;
      const lat = Math.sin(c * 1.7) * 0.55 + (k % 2 ? 0.09 : -0.09) + (k - 4.5) * 0.02;
      const R = 1.42 + ((k * 37) % 10) * 0.012;
      const info = (list && list[i]) || { status: "pending" };
      nodes.push({
        p: [Math.cos(lat) * Math.cos(lon) * R, Math.sin(lat) * R, Math.cos(lat) * Math.sin(lon) * R],
        c, info,
      });
    }
  }
  buildNodes(null);
  window.heroSetNodes = function (list) {
    buildNodes(list);
    lensPool = nodes.map((n, i) => i).filter((i) => nodes[i].info.status !== "pending");
    if (!lensPool.length) lensPool = nodes.map((n, i) => i);
    lensIdx = 0; lensT = 0;
    if (!running) frame(performance.now());
  };

  // state
  let W = 0, H = 0, dpr = 1, cx = 0, cy = 0, S = 1;
  let rotY = 0.6, tilt = -0.32, px = 0, py = 0, tpx = 0, tpy = 0;
  let glitches = [], scanY = 0, last = 0, running = false, visible = true;
  let lensPool = nodes.map((n, i) => i), lensIdx = 0, lensT = 0, lensPos = null;
  const HIT = 20; // css px pick radius
  let inside = false, mx = -1e9, my = -1e9, hoverIdx = -1, pinnedIdx = -1, lastProj = null;

  function pick(proj) {
    // nearest node within HIT px; a small bonus for nodes in front breaks near-ties
    let best = -1, bestScore = Infinity;
    const R = HIT * dpr;
    for (let i = 0; i < proj.length; i++) {
      const d = Math.hypot(proj[i][0] - mx, proj[i][1] - my);
      if (d > R) continue;
      const score = d - proj[i][2] * 3 * dpr;
      if (score < bestScore) { bestScore = score; best = i; }
    }
    return best;
  }

  function resize() {
    const rect = canvas.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.max(1, Math.round(rect.width * dpr));
    H = Math.max(1, Math.round(rect.height * dpr));
    canvas.width = off.width = W;
    canvas.height = off.height = H;
    cx = W * 0.5; cy = H * 0.47;
    S = Math.min(W, H) * 0.27;
    if (!running) frame(performance.now());
  }

  function project(p, ry, rx) {
    // rotate around Y
    const cY = Math.cos(ry), sY = Math.sin(ry);
    let x = p[0] * cY + p[2] * sY, z = -p[0] * sY + p[2] * cY, y = p[1];
    // tilt around X
    const cX = Math.cos(rx), sX = Math.sin(rx);
    const y2 = y * cX - z * sX, z2 = y * sX + z * cX;
    return [cx + x * S, cy - y2 * S, z2];
  }

  function drawScene(t) {
    octx.fillStyle = BG; octx.fillRect(0, 0, W, H);
    const ry = rotY + px * 0.12, rx = tilt + py * 0.08; // small parallax: big values made nodes slide away from the cursor
    const u = dpr * Math.max(0.55, Math.min(1, S / (190 * dpr))); // thinner marks on small figures

    // orbits
    for (const o of orbits) {
      octx.beginPath();
      let prev = null;
      for (let i = 0; i <= 96; i++) {
        const a = (i / 96) * Math.PI * 2;
        let p = [Math.cos(a) * o.r, 0, Math.sin(a) * o.r];
        // ring tilt
        const cz = Math.cos(o.tz), sz = Math.sin(o.tz), cxx = Math.cos(o.tx), sxx = Math.sin(o.tx);
        p = [p[0] * cz - p[1] * sz, p[0] * sz + p[1] * cz, p[2]];
        p = [p[0], p[1] * cxx - p[2] * sxx, p[1] * sxx + p[2] * cxx];
        const q = project(p, ry * 0.6, rx);
        if (o.dash && i % 2) { prev = null; continue; }
        if (prev) { octx.moveTo(prev[0], prev[1]); octx.lineTo(q[0], q[1]); }
        prev = q;
      }
      octx.strokeStyle = `rgba(${INK},.38)`; octx.lineWidth = u; octx.stroke();
    }

    // sphere dots
    for (const p of sphere) {
      const q = project(p, ry, rx);
      const f = (q[2] + 1) / 2; // 0 back .. 1 front
      const s = (1 + f * 1.8) * u;
      octx.fillStyle = `rgba(${INK},${(0.2 + f * 0.8).toFixed(3)})`;
      octx.fillRect(q[0] - s / 2, q[1] - s / 2, s, s);
    }

    // spikes (dotted rays, breathing)
    for (const sp of spikes) {
      const L = sp.len * (0.82 + 0.18 * Math.sin(t * 0.0012 + sp.ph));
      const steps = Math.max(2, Math.round(L * 30));
      for (let k = 1; k <= steps; k++) {
        const m = 1 + (k / steps) * L;
        const q = project([sp.d[0] * m, sp.d[1] * m, sp.d[2] * m], ry, rx);
        const f = (q[2] + 1.6) / 3.2;
        const s = (1 + f * 1.4) * u;
        octx.fillStyle = `rgba(${INK},${(0.15 + f * 0.75).toFixed(3)})`;
        octx.fillRect(q[0] - s / 2, q[1] - s / 2, s, s);
      }
    }

    // nodes: links to surface + intra-cluster chains
    const proj = nodes.map((n) => project(n.p, ry * 0.6, rx));
    octx.lineWidth = u * 0.8;
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i], q = proj[i];
      const len = Math.hypot(n.p[0], n.p[1], n.p[2]);
      const a = project([n.p[0] / len, n.p[1] / len, n.p[2] / len], ry * 0.6, rx);
      const f = (q[2] + 1.5) / 3;
      octx.strokeStyle = `rgba(${INK},${(0.06 + f * 0.25).toFixed(3)})`;
      octx.beginPath(); octx.moveTo(a[0], a[1]); octx.lineTo(q[0], q[1]);
      if (i % 10 !== 9) { const r = proj[i + 1]; octx.moveTo(q[0], q[1]); octx.lineTo(r[0], r[1]); }
      octx.stroke();
    }
    nodeU = u;
    return proj;
  }

  // App nodes are drawn on the visible canvas AFTER the scanlines, so they stay crisp
  // squares (not split into "=" strips) and sit exactly where the pointer hit-test expects.
  let nodeU = 1;
  function drawNodes(proj, focus) {
    const u = nodeU;
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i], q = proj[i];
      const f = (q[2] + 1.5) / 3, s = (4 + f * 4) * u;
      const st = n.info.status;
      const alpha = 0.4 + f * 0.6;
      if (st === "review") { ctx.fillStyle = RED; ctx.globalAlpha = alpha; ctx.fillRect(q[0] - s / 2, q[1] - s / 2, s, s); ctx.globalAlpha = 1; }
      else if (st === "adjudicated") { ctx.fillStyle = `rgba(${INK},${alpha.toFixed(3)})`; ctx.fillRect(q[0] - s / 2, q[1] - s / 2, s, s); }
      else {
        ctx.fillStyle = BG; ctx.fillRect(q[0] - s / 2, q[1] - s / 2, s, s);
        ctx.strokeStyle = `rgba(${INK},${alpha.toFixed(3)})`; ctx.lineWidth = u;
        ctx.strokeRect(q[0] - s / 2 + u / 2, q[1] - s / 2 + u / 2, s - u, s - u);
      }
    }
    // hovered / pinned node: bracket outline so you can see exactly what you are pointing at
    if (focus >= 0 && (hoverIdx === focus || pinnedIdx === focus)) {
      const q = proj[focus], h = 9 * dpr;
      ctx.strokeStyle = RED; ctx.lineWidth = 1.5 * dpr;
      ctx.strokeRect(q[0] - h, q[1] - h, 2 * h, 2 * h);
    }
  }

  function composite(t, proj, animate) {
    ctx.fillStyle = BG; ctx.fillRect(0, 0, W, H);
    const step = Math.max(2, Math.round(3 * dpr)), band = Math.max(1, Math.round(2 * dpr));
    // scan band position
    scanY = animate ? (t * 0.06 * dpr) % (H * 1.4) - H * 0.2 : -9999;
    const pointing = inside || pinnedIdx >= 0;
    ctx.globalAlpha = pointing ? 0.5 : 1; // background recedes while pointing; nodes stay full strength
    for (let y = 0; y < H; y += step) {
      let dx = 0;
      if (!pointing) {
        for (const g of glitches) if (y >= g.y && y < g.y + g.h) dx += g.dx;
        if (Math.abs(y - scanY) < 26 * dpr) dx += Math.sin(y * 0.15) * 3 * dpr;
      }
      ctx.drawImage(off, 0, y, W, band, dx, y, W, band);
    }
    ctx.globalAlpha = 1;
    // scan line marker
    if (animate && scanY > 0 && scanY < H) {
      ctx.fillStyle = "rgba(0,0,221,.6)";
      ctx.fillRect(0, scanY, W * 0.06, Math.max(1, dpr));
      ctx.fillRect(W * 0.94, scanY, W * 0.06, Math.max(1, dpr));
    }

    // research lens (crisp, drawn after scanlines)
    const focus = !lensPool.length ? -1 : pinnedIdx >= 0 ? pinnedIdx : hoverIdx >= 0 ? hoverIdx : lensPool[lensIdx % lensPool.length];
    drawNodes(proj, focus);
    if (focus < 0) return;
    const target = proj[focus];
    if (!lensPos) lensPos = [target[0], target[1]];
    const k = !animate ? 1 : (pinnedIdx >= 0 || hoverIdx >= 0) ? 0.45 : 0.12; // snap fast when pointing
    lensPos[0] += (target[0] - lensPos[0]) * k;
    lensPos[1] += (target[1] - lensPos[1]) * k;
    const [lx, ly] = lensPos, r = 22 * dpr;
    ctx.strokeStyle = RED; ctx.lineWidth = 1.5 * dpr;
    ctx.beginPath(); ctx.arc(lx, ly, r, 0, Math.PI * 2); ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(lx - r - 8 * dpr, ly); ctx.lineTo(lx - r + 6 * dpr, ly);
    ctx.moveTo(lx + r - 6 * dpr, ly); ctx.lineTo(lx + r + 8 * dpr, ly);
    ctx.moveTo(lx, ly - r - 8 * dpr); ctx.lineTo(lx, ly - r + 6 * dpr);
    // handle
    ctx.moveTo(lx + r * 0.72, ly + r * 0.72); ctx.lineTo(lx + r * 1.5, ly + r * 1.5);
    ctx.stroke();
    const info = nodes[focus].info;
    const label = (info.name ? info.name : "PENDING NODE").toUpperCase();
    const sub = info.verdict ? info.verdict.toUpperCase() : (info.status === "pending" ? "NOT YET ADJUDICATED" : "");
    ctx.font = `500 ${10 * dpr}px "JetBrains Mono", monospace`;
    const tx = Math.min(lx + r * 1.6, W - 190 * dpr), ty = ly + r * 1.6 + 14 * dpr;
    const w = Math.max(ctx.measureText(label).width, ctx.measureText(sub).width) + 14 * dpr;
    ctx.fillStyle = "#171717"; ctx.fillRect(tx, ty - 12 * dpr, w, (sub ? 30 : 17) * dpr);
    ctx.fillStyle = BG; ctx.fillText(label, tx + 7 * dpr, ty);
    if (sub) { ctx.fillStyle = "#bdbdba"; ctx.fillText(sub, tx + 7 * dpr, ty + 13 * dpr); }
    if (pinnedIdx >= 0) { ctx.fillStyle = RED; ctx.fillRect(tx, ty - 12 * dpr, 3 * dpr, (sub ? 30 : 17) * dpr); } // pinned marker
  }

  function frame(t) {
    const animate = !reduceMq.matches;
    const dt = last ? Math.min(64, t - last) : 16; last = t;
    if (animate) {
      if (!inside && pinnedIdx < 0) rotY += dt * 0.00012; // hold still while pointing
      px += (tpx - px) * 0.05; py += (tpy - py) * 0.05;
      // glitch events
      if (Math.random() < 0.025) {
        glitches.push({ y: Math.random() * H, h: (4 + Math.random() * 30) * dpr, dx: (Math.random() - 0.5) * 38 * dpr, ttl: 4 + Math.random() * 10 });
      }
      glitches = glitches.filter((g) => --g.ttl > 0);
      if (!inside && pinnedIdx < 0) lensT += dt;
      if (lensT > 2600) { lensT = 0; lensIdx++; }
    } else glitches = [];
    const proj = drawScene(t);
    lastProj = proj;
    hoverIdx = inside ? pick(proj) : -1;
    canvas.style.cursor = hoverIdx >= 0 ? "pointer" : "default";
    composite(t, proj, animate);
    if (animate && visible && !document.hidden) { running = true; requestAnimationFrame(frame); }
    else running = false;
  }

  function kick() { if (!running && visible && !document.hidden && !reduceMq.matches) { last = 0; running = true; requestAnimationFrame(frame); } }

  function setPointer(e) {
    const r = canvas.getBoundingClientRect();
    // map css px -> canvas px using the real ratio (canvas may be scaled by CSS)
    mx = (e.clientX - r.left) * (W / r.width);
    my = (e.clientY - r.top) * (H / r.height);
    tpx = ((e.clientX - r.left) / r.width - 0.5) * 2;
    tpy = ((e.clientY - r.top) / r.height - 0.5) * 2;
  }
  canvas.addEventListener("pointermove", (e) => {
    inside = true; setPointer(e);
    if (lastProj) { hoverIdx = pick(lastProj); canvas.style.cursor = hoverIdx >= 0 ? "pointer" : "default"; } // instant feedback
    if (!running) frame(performance.now());
  });
  canvas.addEventListener("pointerleave", () => { inside = false; hoverIdx = -1; tpx = 0; tpy = 0; mx = my = -1e9; canvas.style.cursor = "default"; });
  canvas.addEventListener("click", (e) => {
    setPointer(e);
    const hit = lastProj ? pick(lastProj) : -1;
    if (hit >= 0) pinnedIdx = pinnedIdx === hit ? -1 : hit; // toggle pin on the node under the cursor
    else if (pinnedIdx >= 0) pinnedIdx = -1;                 // click empty space: unpin
    else { lensIdx++; lensT = 0; }                           // nothing under cursor: next node in the tour
    if (!running) frame(performance.now());
  });

  new ResizeObserver(resize).observe(canvas);
  if ("IntersectionObserver" in window) {
    new IntersectionObserver((es) => { visible = es[0].isIntersecting; kick(); }).observe(canvas);
  }
  document.addEventListener("visibilitychange", kick);
  (reduceMq.addEventListener ? reduceMq.addEventListener("change", () => { resize(); kick(); }) : null);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { if (!running) frame(performance.now()); });
  resize(); kick();
})();
