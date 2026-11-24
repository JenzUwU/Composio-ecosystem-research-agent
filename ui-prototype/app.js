/* =========================================================
   Composio Research — Field Study Nº 001
   Data loading + UI. Vanilla JS, no dependencies.

   DATA SOURCES (first match wins):
     1. window.RESEARCH_DATA            — already-normalised contract (see README)
     2. window.DATA from ../dashboard/data.js — real pipeline output
        (+ ../data/apps.json, when served over HTTP, to list pending apps)
     3. data/sample-data.json           — clearly-labelled demo records
   Force the sample with ?data=sample.
   Missing values stay null and render as "Unknown"/"Pending" — never as a positive claim.
   ========================================================= */
(function () {
  "use strict";

  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => Array.from(el.querySelectorAll(s));
  const esc = (v) => String(v == null ? "" : v).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const arr = (v) => (Array.isArray(v) ? v.filter((x) => x != null && x !== "") : []);
  const pct = (x) => (x == null || isNaN(x) ? "—" : (x * 100).toFixed(1) + "%");

  const VERDICTS = ["Ready to build", "Buildable with limitations", "Requires outreach / partnership", "Not currently feasible", "Insufficient evidence"];
  const VCLASS = { "Ready to build": "v-ready", "Buildable with limitations": "v-limited", "Requires outreach / partnership": "v-outreach", "Not currently feasible": "v-infeasible", "Insufficient evidence": "v-insufficient" };
  const GATED = ["Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated"];

  const state = {
    mode: "none", rows: [], ver: null, raw: null, total: 100, appsListLoaded: false,
    q: "", cat: "", auth: "", mcp: "", build: "", sortKey: "id", sortDir: "asc", open: new Set(),
  };

  /* ---------------- normalisation ---------------- */
  function apiAvailable(types) {
    const t = arr(types).map((x) => String(x).toLowerCase());
    if (!t.length) return null;                                 // unknown, not "no"
    if (t.some((x) => x === "none" || x.includes("no public"))) return false;
    return true;
  }
  function fromPipeline(r) {
    return {
      id: r.id, name: r.app_name || "Unnamed", category: r.category || null,
      description: r.description || null,
      auth_methods: arr(r.auth_methods),
      credential_access: r.credential_access || null,
      api_types: arr(r.api_type), api_available: apiAvailable(r.api_type), api_breadth: r.api_breadth || null,
      mcp_available: r.mcp_available || null, mcp_detail: r.mcp_detail || null,
      buildability: r.buildability_verdict || null,
      blocker: r.primary_blocker || null, blocker_category: r.blocker_category || null,
      evidence: arr(r.evidence).map((e) => ({ field: e.field, claim: e.claim, url: e.source_url, source_type: e.source_type, status: e.verification_status })),
      confidence: r.confidence || null,
      review: !!r.requires_human_review,
      verification_status: r.requires_human_review ? "Flagged for human review" : r.in_verification_sample ? "In ground-truth sample" : "Adjudicated · outside ground-truth sample",
      model: r.llm_model || null, notes: r.notes || null,
      composio: r.composio || null,
      status: "adjudicated",
    };
  }
  function fromGeneric(r) {
    return {
      id: r.id, name: r.name || "Unnamed", category: r.category || null, description: r.description || null,
      auth_methods: arr(r.auth_methods), credential_access: r.credential_access || null,
      api_types: arr(r.api_types), api_available: r.api_available === true ? true : r.api_available === false ? false : null,
      api_breadth: r.api_breadth || null, mcp_available: r.mcp_available || null, mcp_detail: r.mcp_detail || null,
      buildability: r.buildability || null, blocker: r.blocker || null, blocker_category: r.blocker_category || null,
      evidence: arr(r.evidence).map((e) => (typeof e === "string" ? { url: e } : e)).concat(arr(r.evidence_urls).filter((u) => !arr(r.evidence).some((e) => e.url === u)).map((u) => ({ url: u }))),
      confidence: r.confidence || null, review: /review/i.test(r.verification_status || ""),
      verification_status: r.verification_status || null, model: r.model || null, notes: r.notes || null, composio: null,
      status: r.status === "adjudicated" ? "adjudicated" : "pending",
    };
  }
  function pendingFromApp(a) {
    return {
      id: a.id, name: a.name, category: a.category || null, description: null, hint: a.hint || null,
      auth_methods: [], credential_access: null, api_types: [], api_available: null, api_breadth: null,
      mcp_available: null, mcp_detail: null, buildability: null, blocker: null, blocker_category: null,
      evidence: [], confidence: null, review: false, verification_status: "Not yet adjudicated",
      model: null, notes: null, composio: null, status: "pending",
    };
  }

  async function load() {
  if (window.DATA && Array.isArray(window.DATA.rows)) {
    state.mode = "pipeline";
    state.raw = window.DATA;
    state.ver = window.DATA.verification || null;
    state.total = (state.ver && state.ver.applications_total) || 100;
    state.rows = window.DATA.rows.map(fromPipeline);

    try {
      const res = await fetch("/data/apps.json", { cache: "no-store" });
      if (res.ok) {
        const apps = await res.json();
        const have = new Set(state.rows.map((r) => r.id));
        apps.forEach((a) => {
          if (!have.has(a.id)) state.rows.push(pendingFromApp(a));
        });
        state.appsListLoaded = true;
      }
    } catch (e) {
      console.warn("Optional app directory could not be loaded:", e);
    }

    return;
  }

  state.mode = "none";
  state.rows = [];
  console.error("Research data failed to load. Check /dashboard/data.js");
}

  const adjudicated = () => state.rows.filter((r) => r.status === "adjudicated");
  const categories = () => {
    const s = new Set(state.rows.map((r) => r.category).filter(Boolean));
    return Array.from(s);
  };

  /* "Complete" is only claimed when two independent counts in the backend output agree:
     the per-app rows AND the validator's own applications_adjudicated. Anything less is "In progress". */
  function completion() {
    const n = adjudicated().length, T = state.total;
    const reported = state.ver && state.ver.applications_adjudicated != null ? state.ver.applications_adjudicated : null;
    if (state.mode === "sample") return { complete: false, label: "Sample", why: "Sample records, not research" };
    if (n >= T && reported != null && reported >= T) return { complete: true, label: "Complete", why: `${n} adjudicated rows; validator reports ${reported}/${T}` };
    if (n >= T && reported == null) return { complete: false, label: "Unconfirmed", why: "Rows present but no validator count to confirm completion" };
    return { complete: false, label: "In progress", why: `${n} adjudicated rows${reported != null ? `; validator reports ${reported}/${T}` : ""}` };
  }

  // When was the pipeline output last written? (HTTP Last-Modified of data.js; absent on file://)
  async function dataTimestamp() {
    if (state.mode !== "pipeline" || location.protocol === "file:") return null;
    try {
      const r = await fetch("/dashboard/data.js", { method: "HEAD", cache: "no-store" });
      const lm = r.headers.get("Last-Modified");
      return lm ? new Date(lm) : null;
    } catch (e) { return null; }
  }

  /* ---------------- hero + banner ---------------- */
  function renderStatus() {
    const n = adjudicated().length, T = state.total;
    const strip = $("#hero-strip");
    const set = (k, html) => { const el = $(`[data-k="${k}"]`, strip); if (el) el.innerHTML = html; };
    const V = state.ver || {};
    const txt = (k, t) => { const el = $(`[data-k="${k}"]`, strip); if (el) el.textContent = t; };
    set("done", state.mode === "none" ? "—" : `${n}<span class="muted" style="font-size:.5em">/${T}</span>`);
    const chip = $('[data-k="done-chip"]', strip);
    const st = completion();
    chip.textContent = state.mode === "none" ? "No data" : st.label;
    chip.className = "chip " + (st.complete ? "" : "chip-accent");
    chip.title = st.why;
    // valid records = exact-schema check (logs/checkpoint_inspection.json); unresolved = data/llm_unresolved.json
    const ci = V.checkpoint_inspection, unres = Array.isArray(V.applications_unresolved) ? V.applications_unresolved.length : null;
    set("valid", ci ? `${ci.complete_valid}<span class="muted" style="font-size:.5em">/${ci.apps_total}</span>` : "—");
    txt("valid-chip", unres == null ? "—" : `${unres} unresolved`);
    set("sample", V.sample ? `${V.sample.apps}<span class="muted" style="font-size:.5em"> apps</span>` : "—");
    txt("sample-chip", V.sample ? `${V.sample.scorable_claims} claims` : "—");
    const g = (V.stages || []).find((s) => /groq|llm/i.test(s.stage));
    set("acc", g ? `${(g.accuracy * 100).toFixed(1)}<span class="muted" style="font-size:.5em">%</span>` : "—");
    txt("acc-chip", g ? `${(g.lenient_accuracy * 100).toFixed(1)}% partial` : "—");
    const src = { pipeline: "Pipeline output", custom: "Custom JSON", sample: "Sample data", none: "Unavailable" }[state.mode];
    dataTimestamp().then((d) => {
      if (!d) return;
      const when = d.toLocaleString(undefined, { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" });
      $("#foot-source").textContent += ` · DATA.JS ${when.toUpperCase()}`;
    });
    $("#fig-count").textContent = `${T} NODES · ${categories().length || 10} CLUSTERS`;
    $("#foot-source").textContent = `DATA: ${src.toUpperCase()} · ${n}/${T} ADJUDICATED`;

    const b = $("#data-banner");
    let msg = "", cls = "";
    if (state.mode === "sample") msg = "SAMPLE DATA — the records below are invented placeholders showing the data contract. They are not research findings. Real output loads automatically from ../dashboard/data.js.";
    else if (state.mode === "none") msg = "NO DATA LOADED — ../dashboard/data.js was not found and data/sample-data.json could not be fetched (browsers block fetch on file://). Run: python -m http.server 8766 from composio-app-research/ and open /ui-prototype/.";
    else if (n < T) {
      cls = "info";
      msg = `ADJUDICATION IN PROGRESS — ${n} of ${T} apps adjudicated so far. Findings and recommendations describe adjudicated apps only and will update when the pipeline finishes.`;
      if (state.mode === "pipeline" && !state.appsListLoaded) msg += " Serve over HTTP to also list the pending apps in the directory.";
    }
    if (msg) { b.textContent = msg; b.className = "data-banner " + cls; b.hidden = false; } else b.hidden = true;

    // feed the hero figure: 100 slots ordered by category, real names where known
    const pendLg = $(".fig-legend .lg-hollow"); if (pendLg) pendLg.parentElement.hidden = !state.rows.some((r) => r.status === "pending");
    if (window.heroSetNodes) {
      const cats = categories();
      const byCat = cats.map((c) => state.rows.filter((r) => r.category === c).sort((a, b) => a.id - b.id));
      const list = [];
      for (let c = 0; c < 10; c++) for (let k = 0; k < 10; k++) {
        const r = byCat[c] && byCat[c][k];
        list.push(r ? { name: r.name, status: r.status === "adjudicated" ? (r.review ? "review" : "adjudicated") : "pending", verdict: r.buildability } : { status: "pending" });
      }
      window.heroSetNodes(list);
    }
  }

  /* ---------------- 01 overview ---------------- */
  function metric(label, val, chip, desc, meter) {
    const chipHtml = chip ? `<span class="chip ${chip[1] || ""}">${esc(chip[0])}</span>` : "";
    const m = meter != null ? `<div class="meter" aria-hidden="true"><span style="width:${Math.min(100, meter * 100)}%"></span></div>` : "";
    return `<div class="metric reveal"><div class="top"><span class="label">${esc(label)}</span>${chipHtml}</div><div class="val">${val}</div>${m}<p class="desc">${desc}</p></div>`;
  }
  function renderOverview() {
    const v = state.ver || {}, n = adjudicated().length, T = state.total;
    const has = (x) => x != null;
    const flagged = has(v.apps_requiring_human_review) ? v.apps_requiring_human_review : adjudicated().filter((r) => r.review).length;
    const ci = v.checkpoint_inspection, rh = v.run_history || {}, GA = v.groq_attempts || {};
    const unres = Array.isArray(v.applications_unresolved) ? v.applications_unresolved.length : null;
    const g = (v.stages || []).find((s) => /groq|llm/i.test(s.stage)), p2 = (v.stages || []).find((s) => /pass 2/i.test(s.stage));
    $("#metrics").innerHTML = [
      metric("Applications researched", state.mode === "none" ? "—" : `${n}<small>/ ${T}</small>`, completion().complete ? ["Complete"] : [completion().label, "chip-accent"],
        `${categories().length || 10} categories × 10 apps. Every app has a structured, cited Groq record; unknown fields stay unknown.`, T ? n / T : 0),
      metric("Valid records", ci ? `${ci.complete_valid}<small>/ ${ci.apps_total}</small>` : "—", ci ? ["Schema-checked"] : ["Awaiting data", "chip-grey"],
        ci ? `Pass the exact JSON-schema check. ${has(rh.records_after_main_run) ? `${rh.records_after_main_run} after the main run; ` : ""}${GA.apps_with_failed_attempt != null ? `${GA.apps_with_failed_attempt} recovered by retry; ` : ""}${unres != null ? `${unres} unresolved.` : ""}` : "Exact-schema status of every record."),
      metric("Ground-truth sample", v.sample ? `${v.sample.apps}<small> apps</small>` : "—", v.sample ? ["Ground truth"] : ["Awaiting data", "chip-grey"],
        v.sample ? `${v.sample.scorable_claims} scorable claims; ${v.sample.excluded_claims} unsettled claims excluded rather than guessed.` : "Seeded verification sample."),
      metric("Groq exact accuracy", g ? `${(g.accuracy * 100).toFixed(1)}<small>%</small>` : "—", g ? ["Uncorrected"] : ["Awaiting data", "chip-grey"],
        g ? `${(g.lenient_accuracy * 100).toFixed(1)}% counting partial matches, vs ${p2 ? (p2.accuracy * 100).toFixed(1) + "%" : "—"} for the deep crawler. Scored before any review correction.` : "Scored on the ground-truth sample.", g ? g.accuracy : null),
      metric("Distinct sources cited", has(v.distinct_sources_cited) ? v.distinct_sources_cited : "—", has(v.distinct_sources_cited) ? ["Measured"] : ["Awaiting data", "chip-grey"], "Unique evidence URLs behind adjudicated claims."),
      metric("Flagged for human review", state.mode === "none" ? "—" : flagged, ["Needs a person", "chip-accent"], "Apps where the adjudicator's own confidence or citations call for a human check."),
    ].join("");
  }

  /* ---------------- 02 directory ---------------- */
  const cell = (v, pending) => (v ? esc(v) : `<span class="unknown">${pending ? "Pending" : "Unknown"}</span>`);
  function verdictHtml(r) {
    if (r.status === "pending") return `<span class="verdict v-pending unknown">Pending</span>`;
    if (!r.buildability) return `<span class="unknown">Unknown</span>`;
    return `<span class="verdict ${VCLASS[r.buildability] || ""}">${esc(r.buildability)}</span>`;
  }
  function fillSelect(sel, values, extra) {
    const cur = sel.value;
    sel.innerHTML = `<option value="">All</option>` + values.map((v) => `<option value="${esc(v)}">${esc(v)}</option>`).join("") + (extra || "");
    sel.value = cur;
  }
  function setupFilters() {
    const adj = adjudicated(), hasPending = state.rows.some((r) => r.status === "pending");
    fillSelect($("#f-cat"), categories());
    const auths = Array.from(new Set(adj.flatMap((r) => r.auth_methods))).sort();
    const unkLabel = state.rows.some((r) => r.status === "pending") ? "Unknown / pending" : "Unknown";
    fillSelect($("#f-auth"), auths, `<option value="__unknown">${unkLabel}</option>`);
    const mcps = Array.from(new Set(adj.map((r) => r.mcp_available).filter(Boolean)));
    fillSelect($("#f-mcp"), mcps, `<option value="__unknown">${unkLabel}</option>`);
    const vs = VERDICTS.filter((v) => adj.some((r) => r.buildability === v));
    fillSelect($("#f-build"), vs, hasPending ? `<option value="__pending">Pending</option>` : "");
  }
  const VRANK = (r) => (r.status === "pending" ? 99 : r.buildability ? VERDICTS.indexOf(r.buildability) : 50);
  function sortVal(r, k) {
    switch (k) {
      case "name": return r.name.toLowerCase();
      case "category": return (r.category || "~").toLowerCase();
      case "auth": return r.auth_methods.length ? r.auth_methods.join(",").toLowerCase() : "~";
      case "access": return (r.credential_access || "~").toLowerCase();
      case "mcp": return (r.mcp_available || "~").toLowerCase();
      case "buildability": return VRANK(r);
      case "evidence": return r.evidence.length;
      default: return r.id;
    }
  }
  function filtered() {
    const q = state.q.trim().toLowerCase();
    let rows = state.rows.filter((r) => {
      if (state.cat && r.category !== state.cat) return false;
      if (state.auth === "__unknown" ? r.auth_methods.length : state.auth && !r.auth_methods.includes(state.auth)) return false;
      if (state.mcp === "__unknown" ? r.mcp_available : state.mcp && r.mcp_available !== state.mcp) return false;
      if (state.build === "__pending" ? r.status !== "pending" : state.build && r.buildability !== state.build) return false;
      if (q) {
        const hay = [r.name, r.category, r.auth_methods.join(" "), r.credential_access, r.mcp_available, r.buildability, r.blocker, r.description, r.hint].join(" ").toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
    const k = state.sortKey, d = state.sortDir === "asc" ? 1 : -1;
    rows.sort((a, b) => {
      // pending rows sink below researched rows for data-based sorts
      if (!["id", "name", "category"].includes(k) && a.status !== b.status) return a.status === "pending" ? 1 : -1;
      const x = sortVal(a, k), y = sortVal(b, k);
      return (x < y ? -1 : x > y ? 1 : a.id - b.id) * d;
    });
    return rows;
  }
  function evidenceHtml(r) {
    const dl = [
      ["API", r.api_types.length ? r.api_types.join(", ") + (r.api_breadth ? ` · ${r.api_breadth}` : "") : null],
      ["MCP detail", r.mcp_detail],
      ["Blocker", r.blocker],
      ["Confidence", r.confidence],
      ["Status", r.verification_status],
      ["Model", r.model],
      ["Composio", r.composio ? (r.composio.has_toolkit ? `Toolkit "${r.composio.slug}" · ${r.composio.tools != null ? Math.round(r.composio.tools) + " tools" : "tool count unknown"}` : "No toolkit found") : null],
      ["Notes", r.notes],
    ].filter((x) => x[1]).map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join("");
    const ev = r.evidence.length
      ? `<ol>${r.evidence.map((e) => {
          const fetched = /verified|fetched by agent/i.test(e.status || "") && !/not fetched/i.test(e.status || "");
          const safe = /^https?:\/\//i.test(e.url || "") ? e.url : null;
          return `<li><span class="label">${esc(e.field || "source")}${e.source_type ? " · " + esc(e.source_type) : ""}</span>${e.claim ? `<span>${esc(e.claim)}</span>` : ""}${safe ? `<a href="${esc(safe)}" target="_blank" rel="noopener noreferrer">${esc(safe)}</a>` : `<span class="unknown">${esc(e.url || "No URL")}</span>`}<span class="mono small ${fetched ? "st-ok" : "st-warn"}">${esc(e.status || "Status unknown")}</span></li>`;
        }).join("")}</ol>`
      : `<p class="unknown">No evidence URLs recorded.</p>`;
    return `<div class="ev"><div>${r.description ? `<p>${esc(r.description)}</p>` : ""}<dl>${dl}</dl></div><div><p class="label">Evidence — ${r.evidence.length} source${r.evidence.length === 1 ? "" : "s"}</p>${ev}</div></div>`;
  }
  // The directory starts collapsed: the first DIR_LIMIT matching apps, plus a "Show all" toggle below the table.
  const DIR_LIMIT = 10;
  let dirExpanded = false;
  function renderDirectory() {
    const all = filtered(), body = $("#dir-body");
    const n = state.rows.length;
    const collapsible = all.length > DIR_LIMIT;
    const rows = collapsible && !dirExpanded ? all.slice(0, DIR_LIMIT) : all;
    const filteredNote = all.length < n ? ` · ${all.length} ${all.length === 1 ? "matches" : "match"} the filters` : "";
    $("#dir-count").textContent = `Showing ${rows.length} of ${n} apps${filteredNote}` + (state.mode === "sample" ? " · sample records" : "") + (n < state.total ? ` · ${state.total - n} not loaded` : "");
    const wrap = $("#dir-more-wrap"), more = $("#dir-more");
    wrap.hidden = !collapsible || state.mode === "none";
    more.setAttribute("aria-expanded", String(dirExpanded && collapsible));
    $("#dir-more-label").textContent = dirExpanded ? "Show fewer" : all.length < n ? `Show all ${all.length} matching apps` : `Show all ${all.length} apps`;
    if (state.mode === "none") { body.innerHTML = `<tr><td colspan="7" class="empty">No research data available. See the banner above for how to load it.</td></tr>`; return; }
    if (!all.length) { body.innerHTML = `<tr><td colspan="7" class="empty">No apps match these filters. <button class="btn-text" type="button" data-reset>Reset filters</button></td></tr>`; return; }
    body.innerHTML = rows.map((r) => {
      const p = r.status === "pending";
      const open = state.open.has(r.id);
      const auth = r.auth_methods.length ? `<span class="tags">${r.auth_methods.map((a) => `<span class="tag">${esc(a)}</span>`).join("")}</span>` : cell(null, p);
      const evBtn = r.evidence.length
        ? `<button class="ev-btn" type="button" aria-expanded="${open}" aria-controls="ev-${r.id}" data-ev="${r.id}">Evidence · ${r.evidence.length}</button>`
        : `<button class="ev-btn" type="button" disabled>${p ? "Pending" : "None"}</button>`;
      const main = `<tr class="row ${p ? "pending" : ""}">
        <td data-label="Application"><span class="app-name">${esc(r.name)}</span>${r.review ? `<span class="flag" title="Flagged for human review">REVIEW</span>` : ""}<span class="app-sub">${p ? esc(r.hint || "not yet adjudicated") : esc(r.confidence ? r.confidence + " confidence" : "confidence unknown")}</span></td>
        <td data-label="Category" class="cat">${cell(r.category, p)}</td>
        <td data-label="Authentication">${auth}</td>
        <td data-label="Credential access">${cell(r.credential_access, p)}</td>
        <td data-label="MCP">${cell(r.mcp_available, p)}</td>
        <td data-label="Buildability">${verdictHtml(r)}</td>
        <td data-label="Evidence">${evBtn}</td></tr>`;
      return main + (open ? `<tr class="ev-row" id="ev-${r.id}"><td colspan="7">${evidenceHtml(r)}</td></tr>` : "");
    }).join("");
  }
  function syncSortUi() {
    $$(".th-sort").forEach((b) => {
      b.setAttribute("aria-sort", b.dataset.sort === state.sortKey ? (state.sortDir === "asc" ? "ascending" : "descending") : "none");
      b.closest("th").setAttribute("aria-sort", b.getAttribute("aria-sort"));
    });
    const sel = $("#f-sort"), v = `${state.sortKey}:${state.sortDir}`;
    sel.value = Array.from(sel.options).some((o) => o.value === v) ? v : sel.value;
  }
  function bindDirectory() {
    const upd = () => { renderDirectory(); };
    $("#q").addEventListener("input", (e) => { state.q = e.target.value; upd(); });
    [["#f-cat", "cat"], ["#f-auth", "auth"], ["#f-mcp", "mcp"], ["#f-build", "build"]].forEach(([s, k]) =>
      $(s).addEventListener("change", (e) => { state[k] = e.target.value; upd(); }));
    $("#f-sort").addEventListener("change", (e) => { const [k, d] = e.target.value.split(":"); state.sortKey = k; state.sortDir = d; syncSortUi(); upd(); });
    $$(".th-sort").forEach((b) => b.addEventListener("click", () => {
      const k = b.dataset.sort;
      if (state.sortKey === k) state.sortDir = state.sortDir === "asc" ? "desc" : "asc";
      else { state.sortKey = k; state.sortDir = k === "evidence" ? "desc" : "asc"; }
      syncSortUi(); upd();
    }));
    const reset = () => {
      Object.assign(state, { q: "", cat: "", auth: "", mcp: "", build: "", sortKey: "id", sortDir: "asc" });
      $("#q").value = ""; ["#f-cat", "#f-auth", "#f-mcp", "#f-build"].forEach((s) => ($(s).value = "")); $("#f-sort").value = "id:asc";
      syncSortUi(); upd();
    };
    $("#dir-reset").addEventListener("click", reset);
    $("#dir-more").addEventListener("click", () => {
      const wasExpanded = dirExpanded;
      dirExpanded = !dirExpanded; renderDirectory();
      // collapsing from far down the list: bring the table back into view
      if (wasExpanded) $(".table-wrap").scrollIntoView({ block: "nearest", behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" });
      $("#dir-more").focus({ preventScroll: true });
    });
    $("#dir-body").addEventListener("click", (e) => {
      if (e.target.closest("[data-reset]")) return reset();
      const b = e.target.closest("[data-ev]"); if (!b) return;
      const id = Number(b.dataset.ev);
      state.open.has(id) ? state.open.delete(id) : state.open.add(id);
      renderDirectory();
      const nb = $(`[data-ev="${id}"]`); if (nb) nb.focus();
    });
  }

  /* ---------------- 03 methodology + 04 architecture ----------------
     Status lines come from verification_report.json (via data.js): pages_fetched_pass2, models_used,
     tool_calls, sample, review_corrections_applied, checkpoint_inspection, applications_unresolved,
     and the Groq<->Composio round-trip log (DATA.groq.integration). */
  function stageStatus() {
    const v = state.ver || {}, raw = state.raw || {}, n = adjudicated().length, T = state.total;
    const has = state.mode === "pipeline" || state.mode === "custom";
    const S = (k, t) => ({ k, t });
    const integ = raw.groq && raw.groq.integration, checks = integ ? arr(integ.checks) : [];
    const tc = v.tool_calls || {}, byTool = tc.by_tool || {};
    const composioCalls = Object.entries(byTool).filter(([t]) => /composio/i.test(t)).reduce((a, [, c]) => a + c, 0);
    const models = Object.entries(v.models_used || {}).map(([m, c]) => `${c} × ${m.replace("openai/", "")}`).join(" · ");
    const ci = v.checkpoint_inspection, unres = Array.isArray(v.applications_unresolved) ? v.applications_unresolved.length : null;
    const groqDone = n >= T;
    return {
      selection: has ? S("done", `${T} apps · ${categories().length} categories`) : S("pend", "Awaiting data"),
      crawler: v.pages_fetched_pass2 != null ? S("done", `${v.pages_fetched_pass2} pages requested · ${v.pages_ok_pass2} ok`) : S("pend", "Awaiting data"),
      groq: !has ? S("pend", "Awaiting data") : S(groqDone ? "done" : "run", `${n}/${T} adjudicated${models ? " · " + models : ""}`),
      composio: checks.length ? S(checks.every((c) => c.ok) ? "done" : "run", `Round trip ${checks.filter((c) => c.ok).length}/${checks.length} checks passed · ${composioCalls} Composio calls in the 100-app run`) : S("pend", "Awaiting data"),
      truth: v.sample ? S("done", `${v.sample.apps} apps · ${v.sample.scorable_claims} claims · ${v.sample.excluded_claims} excluded`) : S("pend", "Awaiting data"),
      checks: ci ? S(ci.complete_valid >= T && unres === 0 ? "done" : "run", `${v.review_corrections_applied ?? "—"} corrections · ${ci.complete_valid}/${ci.apps_total} schema-valid · ${unres ?? "—"} unresolved`) : S("pend", "Awaiting data"),
      report: state.mode === "pipeline" ? S("done", "data.js → this page & dashboard") : S("pend", "Awaiting data"),
      toolNote: `${tc.total ?? "—"} tool calls${Object.keys(byTool).length ? " (" + Object.entries(byTool).map(([t, c]) => `${t} × ${c}`).join(", ") + ")" : ""}`,
    };
  }
  const CHIP = { done: ["Complete", ""], run: ["In progress", "chip-accent"], pend: ["Pending", "chip-grey"] };
  function renderMethodology() {
    const st = stageStatus();
    const items = [
      ["App dataset preparation", "The application list across 10 categories, each with candidate official documentation URLs.", st.selection],
      ["Python research crawler", "Rule-based, not an agent: discovers official docs, follows auth / getting-started links, renders JS pages, collects evidence and MCP Registry hits.", st.crawler],
      ["Groq LLM adjudication", `Assesses authentication, API access, credential access, MCP availability and buildability from the evidence, as strict-schema JSON. Its only tool use in the run: ${st.toolNote}, re-reading pages already fetched.`, st.groq],
      ["Composio integration", "A separate, live tool-calling demonstration: Groq requests a Composio tool and Python executes it through a Composio session. Not used to research the 100 apps.", st.composio],
      ["Independent ground-truth validation", "A seeded sample, 3 apps per category, checked against official pages blind to Groq's answers. Unsettled claims are excluded.", st.truth],
      ["Corrections & schema validation", "Every record must pass the exact schema check before it is saved. Reviewed values correct the final dataset, never the accuracy score.", st.checks],
      ["Final dashboard & report", "The validator and pattern analyser write data.js; this page and the dashboard compute every figure from it.", st.report],
    ];
    $("#pipeline").innerHTML = items.map(([h, p, s]) => `<li class="reveal"><h3>${esc(h)}</h3><p>${esc(p)}</p><span class="meta">${esc(s.t)}</span><span class="chip ${CHIP[s.k][1]}">${CHIP[s.k][0]}</span></li>`).join("");
  }
  function renderArchitecture() {
    const st = stageStatus(), n = adjudicated().length, T = state.total, v = state.ver || {};
    const raw = state.raw || {}, g = raw.groq && raw.groq.connectivity;
    const models = Object.keys(v.models_used || {}).map((m) => m.replace("openai/", "")).join(" + ");
    const nodes = [
      [`${T} applications`, "Input list with category, hint and candidate doc URLs.", "data/apps.json", st.selection.k],
      ["Python research crawler", "Rule-based crawler: fetch, discover auth links, render, match signals. Not an agent.", "agent/orchestrator.py · fetcher.py · signals.py", st.crawler.k],
      ["Official documentation", "Vendor docs are the primary evidence. MCP availability from the official MCP Registry API.", "data/research_results_pass2.json", st.crawler.k],
      ["Evidence digest", "Per-app bundle of fetched pages, snippets and signals handed to the adjudicator.", "agent/digest.py → data/evidence_digest.md", st.crawler.k],
      ["Groq adjudicator", `The only reasoning step. Strict JSON Schema output${models ? "; models: " + models : ""}. ${st.toolNote}.`, "agent/llm_adjudicator.py · groq_client.py", st.groq.k, true],
      ["Composio integration (separate demo)", "Live round trip: Groq requested COMPOSIO_GET_TOOL_SCHEMAS and Python executed it via session.execute. Plus a catalog cross-check as secondary evidence.", "agent/composio_client.py · composio_tools.py · tests/", st.composio.k],
      ["Schema-checked JSON", `Records saved only after the exact schema check; rejected attempts kept in an append-only history. ${n}/${T} written.`, "agent/schema_check.py → data/llm_adjudicated_results.json", st.checks.k],
      ["Verification & corrections", "Per-stage accuracy on Groq's uncorrected answers against the 30-app ground truth; reviewed values then correct the final dataset.", "agent/evidence_validator.py · verification/", st.truth.k],
      ["HTML report", "This page and the original dashboard — computed in the browser from the data files.", "ui-prototype/ · dashboard/", st.report.k],
    ];
    const lab = { done: "Implemented & ran", run: "In progress", pend: "Pending / partial" };
    $("#arch").innerHTML = nodes.map(([h, p, f, s, reasoning]) =>
      `<div class="node reveal ${reasoning ? "reasoning" : ""}"><div class="n-top"><span><i class="st st-${s === "run" ? "run" : s === "done" ? "done" : "pend"}"></i>${lab[s]}</span></div><h3>${esc(h)}</h3><p>${esc(p)}</p><span class="n-file">${esc(f)}</span></div>`).join("");
    // legend key: show only the states actually present
    const used = new Set(nodes.map((x) => (x[3] === "run" ? "run" : x[3] === "done" ? "done" : "pend")));
    $$(".legend-line [data-st]").forEach((el) => { el.hidden = !used.has(el.dataset.st); });
    if (g) $("#sdk-groq").textContent = `groq ${g.sdk_version} · ${models || g.selected_model}`; else $("#sdk-groq").textContent = "reasoning step";
    const c = raw.composio && raw.composio.connectivity;
    $("#sdk-composio").textContent = c ? `composio ${c.sdk_version}` : "toolkit discovery";
  }

  /* ---------------- 05 findings ---------------- */
  function bars(entries, total, opts = {}) {
    const max = Math.max(1, ...entries.map((e) => e[1]));
    return entries.map(([k, v, red]) => `<div class="bar ${red ? "accent" : ""}"><span>${esc(k)}</span><span class="track" role="img" aria-label="${esc(k)}: ${v} of ${total}"><span class="fill" data-w="${((v / (opts.ofTotal ? total : max)) * 100).toFixed(1)}"></span></span><span class="num">${v}<small>/${total}</small></span></div>`).join("");
  }
  const placeholder = (t) => `<div class="placeholder-box">${esc(t)}</div>`;
  function renderFindings() {
    const adj = adjudicated(), n = adj.length, T = state.total;
    $("#find-intro").innerHTML = n
      ? `Computed from <b>${n} of ${T}</b> apps adjudicated${n < T ? " so far" : ""}${state.mode === "sample" ? " (sample records)" : ""}. ${n < T ? '<span class="stamp">Preliminary</span>' : ""}`
      : "No adjudicated apps yet — charts will appear once results exist.";
    if (!n) { ["#c-auth", "#c-access", "#c-mcp", "#c-build", "#c-cat"].forEach((s) => ($(s).innerHTML = placeholder("Awaiting adjudicated results"))); return; }

    const count = (f) => { const m = new Map(); adj.forEach((r) => f(r).forEach((k) => m.set(k, (m.get(k) || 0) + 1))); return m; };
    const auth = count((r) => (r.auth_methods.length ? r.auth_methods : ["Unknown"]));
    $("#c-auth").innerHTML = bars(Array.from(auth.entries()).sort((a, b) => b[1] - a[1]).map(([k, v]) => [k, v, k === "Unknown"]), n, { ofTotal: true });

    const self = adj.filter((r) => /^self-serve/i.test(r.credential_access || "")).length;
    const gated = adj.filter((r) => GATED.includes(r.credential_access)).length;
    const unk = n - self - gated;
    const access = count((r) => [r.credential_access || "Unknown"]);
    $("#c-access").innerHTML = `<div class="split" role="img" aria-label="Self-serve ${self}, gated ${gated}, unclear ${unk} of ${n}">
      ${self ? `<div class="s-self" style="flex-grow:${self}">SELF-SERVE ${self}</div>` : ""}
      ${gated ? `<div class="s-gate" style="flex-grow:${gated}">GATED ${gated}</div>` : ""}
      ${unk ? `<div class="s-unk" style="flex-grow:${unk}">UNCLEAR ${unk}</div>` : ""}</div>
      <div class="split-legend">${Array.from(access.entries()).sort((a, b) => b[1] - a[1]).map(([k, v]) => `<div><span>${esc(k)}</span><span>${v}/${n}</span></div>`).join("")}</div>`;

    const mcp = count((r) => [r.mcp_available || "Unknown"]);
    $("#c-mcp").innerHTML = bars(Array.from(mcp.entries()).sort((a, b) => b[1] - a[1]).map(([k, v]) => [k, v]), n, { ofTotal: true });

    const vc = VERDICTS.map((v) => [v, adj.filter((r) => r.buildability === v).length, v === "Not currently feasible"]);
    const unkV = adj.filter((r) => !r.buildability).length;
    if (unkV) vc.push(["Unknown", unkV]);
    $("#c-build").innerHTML = bars(vc, n, { ofTotal: true });

    const cats = categories();
    $("#c-cat").innerHTML = cats.map((c) => {
      const all = state.rows.filter((r) => r.category === c);
      const size = Math.max(all.length, state.mode === "pipeline" && !state.appsListLoaded ? 10 : all.length, 1);
      const a = all.filter((r) => r.status === "adjudicated");
      const segs = VERDICTS.map((v) => [v, a.filter((r) => r.buildability === v).length]).filter((x) => x[1]);
      const title = segs.map(([v, k]) => `${v}: ${k}`).join(", ") || "none adjudicated";
      return `<div class="catrow"><span>${esc(c)}</span><span class="n">${a.length}/${size}</span>
        <div class="stack-bar ${a.length ? "" : "empty"}" role="img" aria-label="${esc(c)} — ${esc(title)}">${segs.map(([v, k]) => `<span class="${VCLASS[v]}" style="width:${(k / size) * 100}%" title="${esc(v)}: ${k}"></span>`).join("")}</div></div>`;
    }).join("") + `<div class="cat-legend">${VERDICTS.map((v) => `<span><i class="stack-bar-key ${VCLASS[v]}" style="${legendBg(v)}"></i>${esc(v)}</span>`).join("")}${state.rows.some((r) => r.status === "pending") ? `<span><i style="border-style:dashed"></i>Not yet adjudicated</span>` : ""}</div>`;
    animateBars();
  }
  function legendBg(v) {
    return {
      "Ready to build": "background:#171717",
      "Buildable with limitations": "background:repeating-linear-gradient(135deg,#171717 0 2px,#F1F1EF 2px 4px)",
      "Requires outreach / partnership": "background:repeating-linear-gradient(0deg,#171717 0 1px,#F1F1EF 1px 3px)",
      "Not currently feasible": "background:#0000DD;border-color:#0000DD",
      "Insufficient evidence": "background:#E3E3E0",
    }[v];
  }
  function animateBars() {
    const fills = $$(".fill[data-w]");
    const go = (el) => (el.style.width = el.dataset.w + "%");
    if (!("IntersectionObserver" in window)) return fills.forEach(go);
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { go(e.target); io.unobserve(e.target); } }), { threshold: 0.2 });
    fills.forEach((f) => io.observe(f));
  }

  /* ---------------- 05b skyline (skyline.js) ---------------- */
  const CAT_CODE = {
    "CRM and Sales": "CRM", "Support and Helpdesk": "SUPP", "Communications and Messaging": "COMM",
    "Marketing, Ads, Email and Social": "MKTG", "Ecommerce": "ECOM", "Data, SEO and Scraping": "DATA",
    "Developer, Infra and Data platforms": "DEV", "Productivity and Project Management": "PROD",
    "Finance and Fintech": "FIN", "AI, Research and Media-native": "AI",
  };
  function renderSkyline() {
    const host = $("#skyline");
    if (!host || !window.Skyline) return;
    const cats = categories();
    if (!cats.length || state.mode === "none") { host.innerHTML = placeholder("Awaiting research data"); return; }
    const cols = cats.length, rows = Math.max(...cats.map((c) => state.rows.filter((r) => r.category === c).length));
    const grid = [];
    cats.forEach((c, ci) => state.rows.filter((r) => r.category === c).sort((a, b) => a.id - b.id)
      .forEach((r, ri) => grid.push({ r, col: ci, row: ri })));
    const median = (a) => { if (!a.length) return null; const s = a.slice().sort((x, y) => x - y); const m = s.length >> 1; return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; };
    const top = (list) => list.reduce((b, x) => (x.value > (b ? b.value : -1) ? x : b), null);

    // Metric 1 — evidence sources cited per app (Groq output). Pending apps have no value.
    const ev = grid.map(({ r, col, row }) => ({ col, row, name: r.name, sub: r.category,
      value: r.status === "adjudicated" ? r.evidence.length : null, note: "Not yet adjudicated" }));
    const evVals = ev.filter((c) => c.value != null).map((c) => c.value);
    const evTop = top(ev.filter((c) => c.value != null));
    // Metric 2 — Composio toolkit tool count. No toolkit → null ("no toolkit"), not zero-as-a-score.
    const tk = grid.map(({ r, col, row }) => {
      const c = r.composio;
      const has = c && c.has_toolkit && c.tools != null;
      return { col, row, name: r.name, sub: r.category, value: has ? Math.round(c.tools) : null,
        note: !c ? "Composio not checked" : c.has_toolkit ? "Toolkit found, tool count unknown" : "No Composio toolkit found" };
    });
    const tkVals = tk.filter((c) => c.value != null).map((c) => c.value);
    const tkTop = top(tk.filter((c) => c.value != null));
    const fmt = (x) => (x == null ? "—" : Number.isInteger(x) ? String(x) : x.toFixed(1));

    window.Skyline.mount(host, {
      cols, rows,
      colLabels: cats.map((c) => CAT_CODE[c] || c.split(/[ ,]/)[0].toUpperCase().slice(0, 6)),
      rowLabels: Array.from({ length: rows }, (_, i) => String(i + 1).padStart(2, "0")),
      metrics: [
        { key: "evidence", label: "Evidence sources", unit: "source", unitPlural: "sources", cells: ev,
          hint: "Height = sources the adjudicator cited",
          stats: [
            { label: "Sources cited", value: fmt(evVals.reduce((a, b) => a + b, 0)), unit: "total", sub: `across ${evVals.length} adjudicated apps` },
            { label: "Most-cited app", value: fmt(evTop && evTop.value), unit: "sources", sub: evTop ? evTop.name : "—" },
            { label: "Median per app", value: fmt(median(evVals)), unit: "sources", sub: "adjudicated apps" },
            { label: "Apps with none", value: fmt(evVals.filter((v) => v === 0).length), unit: "apps", sub: "no evidence URL recorded" },
          ] },
        { key: "tools", label: "Composio tools", unit: "tool", unitPlural: "tools", cells: tk,
          hint: "Height = tools in the app's Composio toolkit",
          stats: [
            { label: "Apps with a toolkit", value: fmt(tkVals.length), unit: `/ ${grid.length}`, sub: "Composio catalog cross-check" },
            { label: "Largest toolkit", value: fmt(tkTop && tkTop.value), unit: "tools", sub: tkTop ? tkTop.name : "—" },
            { label: "Median toolkit", value: fmt(median(tkVals)), unit: "tools", sub: "apps with a toolkit" },
            { label: "Tools in total", value: fmt(tkVals.reduce((a, b) => a + b, 0)), unit: "tools", sub: "sum over toolkits" },
          ] },
      ],
      // clicking a box opens that app's row in the directory
      onCellClick: (cell) => {
        const r = state.rows.find((x) => x.name === cell.name);
        if (!r) return;
        state.open.add(r.id); state.q = r.name; $("#q").value = r.name; renderDirectory();
        $("#ecosystem").scrollIntoView({ behavior: "smooth" });
      },
    });
  }

  /* ---------------- 06 verification ----------------
     Source: verification/verification_report.json (DATA.verification): stages (per-stage + per-field
     accuracy on Groq's UNCORRECTED answers), groq_by_model, groq_attempts, failure_history_entries,
     run_history (parsed from logs/adjudication.log), checkpoint_inspection, review_corrections. */
  const STAGE_LABEL = (s) => (/pass 1/i.test(s) ? "Homepage crawler" : /pass 2/i.test(s) ? "Deep crawler" : /groq|llm/i.test(s) ? "Groq adjudication" : s);
  const fmtN = (x) => (x == null ? "—" : Number(x).toLocaleString("en-US"));
  function renderVerification() {
    const v = state.ver, el = $("#ver");
    if (!v || !v.sample) {
      el.innerHTML = `<div class="ver-top">${[
        metric("Ground-truth sample", "—", ["Awaiting data", "chip-grey"], "Apps checked against official pages."),
        metric("Scorable claims", "—", ["Awaiting data", "chip-grey"], "Field-level claims the evidence settles."),
        metric("Unsettled claims", "—", ["Awaiting data", "chip-grey"], "Excluded from scoring."),
        metric("Review corrections", "—", ["Awaiting data", "chip-grey"], "Shown separately from accuracy."),
      ].join("")}</div>`;
      return;
    }
    const stages = arr(v.stages), sampleN = v.sample.apps;
    const groq = stages.find((s) => /groq|llm/i.test(s.stage)), p2 = stages.find((s) => /pass 2/i.test(s.stage));
    const groqFinal = groq && groq.apps_covered >= sampleN;
    const corr = arr(v.review_corrections), rh = v.run_history || {}, GA = v.groq_attempts || {}, ci = v.checkpoint_inspection;
    const unres = Array.isArray(v.applications_unresolved) ? v.applications_unresolved.length : null;
    const tc = v.tool_calls || {};
    el.innerHTML = `
      <div class="ver-top">
        ${metric("Ground-truth sample", sampleN, ["Seeded · 3 per category", "chip-ghost"], "Drawn with a fixed seed before any LLM run, checked blind to Groq's answers.")}
        ${metric("Scorable claims", v.sample.scorable_claims ?? "—", ["Measured"], "Five fields per app, compared by explicit rules.")}
        ${metric("Unsettled claims", v.sample.excluded_claims ?? "—", ["Excluded", "chip-grey"], "Fields official evidence did not settle — not scored, not guessed.")}
        ${metric("Review corrections", corr.length, ["Not in accuracy", "chip-accent"], "Sampled values where Groq was not exactly right; corrected in the final dataset only.")}
      </div>
      <div class="ver-stages reveal">
        ${stages.map((s) => {
          const isGroq = s === groq;
          return `<div class="ver-stage"><div class="name"><b>${esc(STAGE_LABEL(s.stage))}</b><span>${esc(s.stage)} · ${s.apps_covered} of ${sampleN} sample apps · ${s.claims_scored} claims · ${s.partial} partial</span></div>
            <div class="ver-bars">
              <div class="bar ${isGroq ? "accent" : ""}"><span>Exact</span><span class="track"><span class="fill" data-w="${(s.accuracy * 100).toFixed(1)}"></span></span><span class="num">${pct(s.accuracy)}</span></div>
              <div class="bar"><span>Partial</span><span class="track"><span class="fill scan" data-w="${(s.lenient_accuracy * 100).toFixed(1)}"></span></span><span class="num">${pct(s.lenient_accuracy)}</span></div>
            </div>
            <div class="score"><b>${pct(s.accuracy)}</b><span>${s.correct} correct / ${s.claims_scored}</span></div></div>`;
        }).join("")}
        ${groq ? `<div class="ver-stage"><div class="name"><b>Final result · Groq, uncorrected</b><span>${groqFinal ? `Scored on all ${sampleN} sample apps, before any review correction` : `${groq.apps_covered} of ${sampleN} sample apps scored`}</span></div>
          <div class="ver-bars"><div class="placeholder-box" style="padding:12px">${pct(groq.accuracy)} exact · ${pct(groq.lenient_accuracy)} counting partial matches${p2 ? ` · deep crawler ${pct(p2.accuracy)} / ${pct(p2.lenient_accuracy)}` : ""}</div></div>
          <div class="score"><b>${pct(groq.accuracy)}</b><span>${pct(groq.lenient_accuracy)} partial</span></div></div>` : ""}
      </div>
      <div class="ver-note"><span class="dot-accent" aria-hidden="true"></span><p><b>Reviewer:</b> ${esc(v.sample.reviewer || "not recorded")}. Exact = exact match; partial also counts overlapping auth classes or the same self-serve/gated group. Accuracy is always computed on Groq's original answers; the ${corr.length} corrections below never feed back into it.</p></div>
      <div class="ver-cols">
        <div class="panel"><h3>Accuracy by field <span class="muted">exact · correct / scored</span></h3>${fieldTable(stages)}</div>
        <div class="panel"><h3>Model comparison <span class="muted">Groq, uncorrected</span></h3>${modelTable(v)}</div>
      </div>
      <div class="ver-cols">
        <div class="panel"><h3>Failures &amp; retries</h3><ul class="stack">
          <li><b>Valid records after the main run</b><span>${rh.records_after_main_run ?? "—"}</span></li>
          <li><b>Failed apps recovered by retry</b><span>${GA.apps_with_failed_attempt ?? "—"}</span></li>
          <li><b>Valid records after retries</b><span>${ci ? `${ci.complete_valid} / ${ci.apps_total}` : rh.records_final ?? "—"}</span></li>
          <li><b>Unresolved apps</b><span>${unres ?? "—"}</span></li>
          <li><b>Rejected Groq attempts</b><span>${GA.failed_attempts ?? "—"} across ${GA.apps_with_failed_attempt ?? "—"} apps</span></li>
          ${GA.by_code ? `<li><b>By error code</b><span>${Object.entries(GA.by_code).map(([c, k]) => `${esc(c)} × ${k}`).join("<br>")}</span></li>` : ""}
          <li><b>Failure-history entries preserved</b><span>${v.failure_history_entries ?? "—"}</span></li>
        </ul><p class="muted small">A record is saved only after it passes the exact JSON-schema check (required fields, types, enum values, no positive claim without a citation). Every rejected attempt stays in the append-only <code>data/llm_failed_attempts.jsonl</code>.</p></div>
        <div class="panel"><h3>Run &amp; token usage <span class="muted">from logs/adjudication.log</span></h3><ul class="stack">
          <li><b>Successful API calls</b><span>${fmtN(rh.calls)}</span></li>
          <li><b>Input tokens</b><span>${fmtN(rh.prompt_tokens)}</span></li>
          <li><b>Output tokens</b><span>${fmtN(rh.completion_tokens)}</span></li>
          <li><b>Recorded tokens, total</b><span>${fmtN(rh.total_tokens)}</span></li>
          <li><b>Apps per model</b><span>${v.models_used ? Object.entries(v.models_used).map(([k, c]) => `${esc(k)} × ${c}`).join("<br>") : "—"}</span></li>
          <li><b>Tool calls in the 100-app run</b><span>${tc.total ?? "—"}${tc.by_tool ? " · " + Object.entries(tc.by_tool).map(([t, c]) => `${esc(t)} × ${c}`).join(", ") : ""}</span></li>
          <li><b>Unsupported citations dropped</b><span>${v.unsupported_citations_dropped ?? "—"}</span></li>
          <li><b>Apps with fetched official evidence</b><span>${v.applications_with_fetched_official_evidence ?? "—"} / ${v.applications_adjudicated ?? "—"}</span></li>
        </ul><p class="muted small">${esc(rh.note || "")} The Composio tool path was demonstrated in a separate round-trip test; no Composio tool was called while researching the apps.</p></div>
      </div>
      ${corr.length ? `<div class="panel panel-wide corr-panel"><h3>Review corrections <span class="muted">${corr.length} sampled values · shown separately · not counted in accuracy</span></h3>
        <div class="rec-scroll" style="max-height:360px"><table class="mini-table"><tr><th>App</th><th>Field</th><th>Groq said</th><th>Reviewed value</th></tr>
        ${corr.map((c) => `<tr><td>${esc(c.app)}</td><td>${esc(c.field.replace(/_/g, " "))}</td><td class="muted">${esc([].concat(c.groq ?? "—").join(", ") || "—")}</td><td>${esc([].concat(c.reviewed).join(", "))}</td></tr>`).join("")}</table></div></div>` : ""}`;
    animateBars();
  }
  function modelTable(v) {
    const M = v.groq_by_model || {};
    const keys = Object.keys(M);
    if (!keys.length) return '<p class="placeholder">No per-model scores in the report.</p>';
    const catsOf = (ids) => new Set(ids.map((i) => (state.rows.find((r) => r.id === i) || {}).category).filter(Boolean)).size;
    return `<div style="overflow-x:auto"><table class="mini-table"><tr><th>Model</th><th class="num">Apps</th><th class="num">Sample</th><th class="num">Exact</th><th class="num">Partial</th></tr>
      ${keys.map((k) => { const s = M[k]; return `<tr><td>${esc(k.replace("openai/", ""))}</td><td class="num">${s.apps_adjudicated_total}</td><td class="num">${s.apps_covered} <span class="muted">(${catsOf(arr(s.sample_app_ids))} cat.)</span></td><td class="num">${pct(s.accuracy)} <span class="muted">(${s.correct}/${s.claims_scored})</span></td><td class="num">${pct(s.lenient_accuracy)}</td></tr>`; }).join("")}
      </table></div>
      <p class="muted small"><b>Not a fair head-to-head.</b> ${esc(v.groq_by_model_caveat || "")}</p>
      <p class="muted small">Review flags: ${keys.map((k) => `${esc(k.replace("openai/", ""))} ${pct(M[k].review_flag_rate_all_apps)}`).join(" · ")}. "Insufficient evidence": ${keys.map((k) => `${esc(k.replace("openai/", ""))} ${pct(M[k].insufficient_evidence_rate_all_apps)}`).join(" · ")}.</p>`;
  }
  function fieldTable(stages) {
    const fields = ["auth_methods", "api_type", "credential_access", "mcp_available", "buildability_verdict"];
    const label = { auth_methods: "Authentication", api_type: "API type", credential_access: "Credential access", mcp_available: "MCP", buildability_verdict: "Verdict" };
    const short = (s) => (/pass 1/i.test(s) ? "Homepage" : /pass 2/i.test(s) ? "Deep crawler" : /groq|llm/i.test(s) ? "Groq" : s.slice(0, 10));
    const g = stages.find((s) => /groq|llm/i.test(s.stage)), p2 = stages.find((s) => /pass 2/i.test(s.stage));
    const worse = fields.filter((f) => g && p2 && g.per_field[f] && p2.per_field[f] && g.per_field[f].correct < p2.per_field[f].correct);
    const head = `<tr><th>Field</th>${stages.map((s) => `<th class="num">${esc(short(s.stage))}</th>`).join("")}</tr>`;
    const body = fields.map((f) => `<tr${worse.includes(f) ? ' class="row-flag"' : ""}><td>${esc(label[f])}${worse.includes(f) ? ' <span class="chip chip-accent">Groq below crawler</span>' : ""}</td>${stages.map((s) => {
      const p = s.per_field && s.per_field[f];
      if (!p) return `<td class="num">—</td>`;
      const tot = p.correct + p.partial + p.incorrect;
      return `<td class="num">${tot ? Math.round((p.correct / tot) * 100) + "%" : "—"} <span class="muted">(${p.correct}/${tot})</span></td>`;
    }).join("")}</tr>`).join("");
    const mcpNote = worse.includes("mcp_available") ? `<p class="muted small"><b>MCP:</b> Groq got ${g.per_field.mcp_available.correct}/${g.per_field.mcp_available.correct + g.per_field.mcp_available.partial + g.per_field.mcp_available.incorrect}, below the deep crawler's ${p2.per_field.mcp_available.correct}/${p2.per_field.mcp_available.correct + p2.per_field.mcp_available.partial + p2.per_field.mcp_available.incorrect} (which queries the MCP Registry directly). Groq sometimes classified vendor-owned MCP servers as third-party/community or unclear.</p>` : "";
    return `<div style="overflow-x:auto"><table class="mini-table">${head}${body}</table></div>${mcpNote}<p class="muted small">Groq column = Groq's uncorrected answers, scored on the full sample.</p>`;
  }

  /* ---------------- hero dimension tabs (AUTH / API / MCP / BUILDABILITY) ----------------
     Live readout per dimension, counted from the adjudicated rows (auth_methods, api_type,
     mcp_available, buildability_verdict). ARIA tablist: click, hover, or arrow keys / Home / End. */
  const DIMS = {
    auth: { title: "How apps authenticate", note: "multi-select · an app can support several", href: "#findings", link: "Auth findings",
      rows: (adj) => ["OAuth2", "API Key", "Personal Access Token", "Basic", "Bearer Token", "Other"].map((k) => [k, adj.filter((r) => r.auth_methods.includes(k)).length]) },
    api: { title: "Documented API surface", note: "multi-select · REST and GraphQL can coexist", href: "#ecosystem", link: "Browse the dataset",
      rows: (adj) => [["REST", adj.filter((r) => r.api_types.includes("REST")).length], ["GraphQL", adj.filter((r) => r.api_types.includes("GraphQL")).length], ["No documented API", adj.filter((r) => !r.api_types.length).length]] },
    mcp: { title: "MCP server availability", note: "one value per app", href: "#findings", link: "MCP findings",
      rows: (adj) => ["Official", "Third-party/community", "None found", "Unclear"].map((k) => [k, adj.filter((r) => r.mcp_available === k).length]) },
    build: { title: "Can a toolkit be built today?", note: "one verdict per app", href: "#recommendations", link: "Easy wins & blockers",
      rows: (adj) => VERDICTS.map((k) => [k, adj.filter((r) => r.buildability === k).length]) },
  };
  let heroDim = "auth";
  function renderHeroTabs() {
    const panel = $("#ht-panel"); if (!panel) return;
    const adj = adjudicated(), n = adj.length, d = DIMS[heroDim];
    $$(".hero-tags [role=tab]").forEach((t) => { const on = t.dataset.dim === heroDim; t.setAttribute("aria-selected", String(on)); t.tabIndex = on ? 0 : -1; });
    panel.setAttribute("aria-labelledby", "ht-" + heroDim);
    if (!n) { panel.innerHTML = '<p class="placeholder">Awaiting adjudicated results.</p>'; return; }
    const rows = d.rows(adj).filter(([, v]) => v > 0);
    panel.innerHTML = `<div class="hr-head"><span class="label">${esc(d.title)}</span><span class="hr-n mono">${n} apps · ${esc(d.note)}</span></div>
      <ul class="hr-bars">${rows.map(([k, v]) => `<li><span class="hr-k">${esc(k)}</span><span class="hr-bar"><i style="width:${(v / n * 100).toFixed(1)}%"></i></span><b class="mono">${v}</b></li>`).join("")}</ul>
      <a class="hr-link mono" href="${d.href}">${esc(d.link)} →</a>`;
  }
  function bindHeroTabs() {
    const tabs = $$(".hero-tags [role=tab]"); if (!tabs.length) return;
    const go = (dim, focus) => { heroDim = dim; renderHeroTabs(); if (focus) $("#ht-" + dim).focus(); };
    tabs.forEach((t, i) => {
      t.addEventListener("click", () => go(t.dataset.dim));
      t.addEventListener("mouseenter", () => { if (matchMedia("(hover: hover)").matches) go(t.dataset.dim); });
      t.addEventListener("keydown", (e) => {
        const k = { ArrowRight: i + 1, ArrowDown: i + 1, ArrowLeft: i - 1, ArrowUp: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
        if (k === undefined) return;
        e.preventDefault(); go(tabs[(k + tabs.length) % tabs.length].dataset.dim, true);
      });
    });
  }

  /* ---------------- 07 recommendations: three interactive columns + detail ----------------
     Every list is derived from the adjudicated rows (window.DATA.rows ← data/verified_results.json):
       Easy wins  : buildability_verdict === "Ready to build" AND credential_access starts "Self-serve"
                    AND requires_human_review === false. Unknown / unverified rows are never listed here.
       Blockers   : rows grouped by blocker_category (≠ "None"); each app shows primary_blocker + evidence.
                    Plus a derived group for api_breadth === "Narrow" (limited API coverage), if any.
       Outreach   : verdict "Requires outreach / partnership" or "Insufficient evidence", credential_access
                    gated or "Unclear", or a ready-to-build row still flagged requires_human_review.
     Reason + next action are rule-based from those same fields (see outreachReason / nextAction). */
  const SELF = (r) => /^self-serve/i.test(r.credential_access || "");
  const isEasy = (r) => r.buildability === "Ready to build" && SELF(r) && !r.review;
  function outreachReason(r) {
    if (r.buildability === "Insufficient evidence") return ["Evidence too thin", "No verdict could be supported from the fetched official pages."];
    if (r.credential_access === "Partnership / contact-sales gated" || r.buildability === "Requires outreach / partnership") return ["Partnership gated", "API access requires a partner agreement or a sales conversation."];
    if (r.credential_access === "Enterprise-only") return ["Enterprise-only access", "Credentials are only issued on enterprise contracts."];
    if (r.credential_access === "Admin approval / app review") return ["Approval required", "Apps must pass vendor review or admin approval before credentials work."];
    if (r.credential_access === "Unclear") return ["Access model unclear", "The official pages did not settle how a developer obtains credentials."];
    if (r.review) return ["Needs human verification", "The adjudicator flagged this record for review (low confidence or uncited fields)."];
    return null;
  }
  function nextAction(r) {
    if (r.buildability === "Insufficient evidence") return "Locate the official API documentation by hand, then re-run the crawler and adjudicator for this app.";
    if (r.credential_access === "Partnership / contact-sales gated" || r.buildability === "Requires outreach / partnership") return "Contact the vendor's partnerships / BD team to request API or partner-program access.";
    if (r.credential_access === "Enterprise-only") return "Ask the vendor for an enterprise sandbox or design-partner arrangement before scoping a toolkit.";
    if (r.credential_access === "Admin approval / app review") return "Register a developer app and start the vendor's review / approval process early; it gates every user.";
    if (r.credential_access === "Unclear") return "Verify the credential path manually (sign-up flow, pricing and developer pages) before prioritising.";
    if (r.review) return "Spot-check the cited evidence by hand before building; the verdict itself is not yet confirmed.";
    if (r.buildability === "Buildable with limitations") return "Build, documenting the constraint (" + (r.blocker_category || "limitation") + ") in the toolkit's setup notes.";
    if (isEasy(r)) return r.composio && r.composio.has_toolkit ? "Existing Composio toolkit: maintain and check coverage against the documented API." : "No Composio toolkit yet: strong candidate for a new toolkit (self-serve credentials, documented API).";
    return "Review the evidence below before deciding.";
  }
  function opportunity(r) {
    if (isEasy(r)) {
      const api = r.api_types.length ? r.api_types.join(" + ") + " API" : "API";
      const mcp = r.mcp_available === "Official" ? "The vendor already ships an official MCP server, so the edge is managed auth and breadth." : "No official MCP server was found, so a toolkit adds visible value.";
      return `Documented ${api}${r.api_breadth ? " (" + r.api_breadth.toLowerCase() + " surface)" : ""} with ${String(r.credential_access).toLowerCase()} credentials. ${mcp}`;
    }
    const o = outreachReason(r);
    const blk = r.blocker && r.blocker !== "None" ? r.blocker : null;
    return [o ? o[1] : null, blk ? "Recorded blocker: " + blk + "." : null].filter(Boolean).join(" ") || "No blocker recorded.";
  }

  let recSel = null, recTrigger = null; // selected app id + the row button that opened it (an app can appear in two columns)
  function recRow(r, meta) {
    const on = recSel === r.id;
    return `<li><button type="button" class="rec-row${on ? " is-sel" : ""}" data-rec-id="${r.id}" aria-pressed="${on}" aria-controls="rec-detail">
      <span class="rec-name">${esc(r.name)}</span><span class="rec-meta">${esc(meta || "")}</span></button></li>`;
  }
  function firstEvidence(r, fields) {
    const e = r.evidence.find((x) => fields.includes(x.field) && x.url) || r.evidence.find((x) => x.url);
    return e || null;
  }
  const linkHost = (u) => {
    try { const x = new URL(u), p = x.pathname.replace(/\/$/, ""); return x.hostname.replace(/^www\./, "") + (p ? (p.length > 38 ? p.slice(0, 36) + "…" : p) : ""); }
    catch (e) { return u; }
  };
  const evA = (e) => /^https?:/i.test(e.url) ? `<a href="${esc(e.url)}" target="_blank" rel="noopener noreferrer">${esc(linkHost(e.url))}</a>` : `<span class="mono">${esc(e.url)}</span>`;

  function renderRecs() {
    const adj = adjudicated(), n = adj.length, T = state.total;
    const stamp = n < T ? '<span class="stamp">Preliminary</span>' : "";
    const empty = (msg) => `<p class="placeholder">${esc(n ? msg : "Awaiting adjudicated results.")}</p>`;

    const easy = adj.filter(isEasy).sort((a, b) => a.name.localeCompare(b.name));
    const unverifiedReady = adj.filter((r) => r.buildability === "Ready to build" && !isEasy(r)).length;

    const groups = new Map();
    adj.forEach((r) => { if (r.blocker_category && r.blocker_category !== "None") { (groups.get(r.blocker_category) || groups.set(r.blocker_category, []).get(r.blocker_category)).push(r); } });
    const narrow = adj.filter((r) => r.api_breadth === "Narrow");
    const blockerList = Array.from(groups.entries()).sort((a, b) => b[1].length - a[1].length);
    if (narrow.length) blockerList.push(["Limited API coverage (narrow API surface)", narrow]);

    const outreach = adj.map((r) => [r, outreachReason(r)]).filter(([r, o]) => o && !isEasy(r))
      .sort((a, b) => a[1][0].localeCompare(b[1][0]) || a[0].name.localeCompare(b[0].name));

    const easyHtml = easy.length ? `<ul class="rec-rows">${easy.map((r) => recRow(r, (r.auth_methods[0] || "Auth unknown") + " · " + r.credential_access.replace(/^Self-serve \(|\)$/g, ""))).join("")}</ul>` : empty("None among adjudicated apps.");
    const blockHtml = blockerList.length ? blockerList.map(([k, list], gi) => `
      <div class="acc">
        <button type="button" class="acc-btn" aria-expanded="false" aria-controls="acc-p-${gi}" id="acc-b-${gi}">
          <span>${esc(k)}</span><span class="acc-n mono">${list.length}</span><span class="acc-x" aria-hidden="true"></span></button>
        <div class="acc-panel" id="acc-p-${gi}" role="region" aria-labelledby="acc-b-${gi}" hidden>
          <ul class="rec-rows">${list.sort((a, b) => a.name.localeCompare(b.name)).map((r) => {
            const e = firstEvidence(r, ["credential_access", "buildability_verdict", "primary_blocker", "api_type"]);
            return `${recRow(r, r.blocker && r.blocker !== "None" ? r.blocker : r.buildability)}${e ? `<li class="acc-ev mono">evidence: ${evA(e)}</li>` : `<li class="acc-ev mono">no citation recorded</li>`}`;
          }).join("")}</ul>
        </div>
      </div>`).join("") : empty("No blockers recorded among adjudicated apps.");
    const outHtml = outreach.length ? `<ul class="rec-rows">${outreach.map(([r, o]) => recRow(r, o[0])).join("")}</ul>` : empty("None among adjudicated apps.");

    $("#recs").innerHTML = `
      <div class="panel rec-col reveal"><h3>Easy wins ${stamp}<span class="rec-count mono">${easy.length}</span></h3>
        <p class="muted small">Ready to build, self-serve credentials, not flagged for review.${unverifiedReady ? ` ${unverifiedReady} more "ready" apps are listed under Outreach until verified or their access is settled.` : ""}</p>
        <div class="rec-scroll">${easyHtml}</div></div>
      <div class="panel rec-col reveal"><h3>Blockers ${stamp}<span class="rec-count mono">${blockerList.length}</span></h3>
        <p class="muted small">Primary blocker per app, grouped. Expand a group to see the apps and a supporting source.</p>
        <div class="rec-scroll">${blockHtml}</div></div>
      <div class="panel rec-col reveal"><h3>Outreach priorities ${stamp}<span class="rec-count mono">${outreach.length}</span></h3>
        <p class="muted small">Needs a human: gated access, unclear evidence, or an unverified verdict.</p>
        <div class="rec-scroll">${outHtml}</div></div>`;

    $$("#recs .acc-btn").forEach((b) => b.addEventListener("click", () => {
      const open = b.getAttribute("aria-expanded") !== "true";
      b.setAttribute("aria-expanded", String(open));
      $("#" + b.getAttribute("aria-controls")).hidden = !open;
    }));
    $$("#recs .rec-row").forEach((b) => b.addEventListener("click", () => selectRec(+b.dataset.recId, b)));
    renderLimitData();
  }

  function selectRec(id, fromBtn) {
    const box = $("#rec-detail");
    if (recSel === id) { recSel = null; box.hidden = true; box.innerHTML = ""; syncSel(); return; } // click again closes
    recSel = id; recTrigger = fromBtn || recTrigger; syncSel();
    const r = state.rows.find((x) => x.id === id);
    if (!r) return;
    const o = outreachReason(r);
    const ev = r.evidence.filter((e) => e.url);
    box.innerHTML = `
      <header class="rd-head">
        <div><span class="label">${esc(r.category || "")}${r.review ? " · flagged for human review" : ""}</span>
          <h3 id="rec-detail-title" tabindex="-1">${esc(r.name)}</h3></div>
        <span class="verdict ${VCLASS[r.buildability] || ""}">${esc(r.buildability || "Unknown")}</span>
        <button type="button" class="rd-close btn-text" aria-label="Close details for ${esc(r.name)}">Close ✕</button>
      </header>
      <div class="rd-grid">
        <dl class="rd-facts">
          <dt>Authentication</dt><dd>${r.auth_methods.length ? esc(r.auth_methods.join(", ")) : "Unknown"}</dd>
          <dt>Credential access</dt><dd>${esc(r.credential_access || "Unknown")}</dd>
          <dt>API</dt><dd>${r.api_types.length ? esc(r.api_types.join(", ")) : "None documented"}${r.api_breadth ? " · " + esc(r.api_breadth) : ""}</dd>
          <dt>MCP</dt><dd>${esc(r.mcp_available || "Unknown")}</dd>
          <dt>Composio toolkit</dt><dd>${r.composio ? (r.composio.has_toolkit ? "Exists" : "None found") : "Unknown"}</dd>
          <dt>Confidence</dt><dd>${esc(r.confidence || "Unknown")}${r.model ? ` <span class="muted">· ${esc(r.model.replace("openai/", ""))}</span>` : ""}</dd>
        </dl>
        <div class="rd-text">
          <h4 class="label">${isEasy(r) ? "Implementation opportunity" : o ? "Why it needs follow-up · " + esc(o[0]) : "Blocker · " + esc(r.blocker_category && r.blocker_category !== "None" ? r.blocker_category : r.buildability || "unknown")}</h4>
          <p>${esc(opportunity(r))}</p>
          <h4 class="label">Suggested next action</h4>
          <p class="rd-next">${esc(nextAction(r))}</p>
        </div>
        <div class="rd-ev">
          <h4 class="label">Evidence (${ev.length})</h4>
          ${ev.length ? `<ul>${ev.map((e) => `<li><span class="mono rd-f">${esc((e.field || "").replace(/_/g, " "))}</span> ${evA(e)}${e.claim ? `<span class="rd-claim">${esc(e.claim)}</span>` : ""}${e.status ? `<span class="rd-st mono">${esc(e.status)}</span>` : ""}</li>`).join("")}</ul>` : '<p class="placeholder">No evidence URL recorded — treat every field as unverified.</p>'}
        </div>
      </div>`;
    box.hidden = false;
    $(".rd-close", box).addEventListener("click", () => { const btn = recTrigger; selectRec(id); if (btn && btn.isConnected) btn.focus(); });
    box.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "nearest" });
    if (fromBtn) $("#rec-detail-title").focus({ preventScroll: true });
  }
  function syncSel() {
    $$("#recs .rec-row").forEach((b) => { const on = +b.dataset.recId === recSel; b.classList.toggle("is-sel", on); b.setAttribute("aria-pressed", String(on)); });
  }

  // Limitations: one data line per item, computed from the rows / verification report (blank if unavailable).
  function renderLimitData() {
    const adj = adjudicated(), V = state.ver || {};
    const g = (V.stages || []).find((s) => /groq|llm/i.test(s.stage)), p2 = (V.stages || []).find((s) => /pass 2/i.test(s.stage));
    const fld = (s, f) => { const p = s && s.per_field && s.per_field[f]; return p ? `${p.correct}/${p.correct + p.partial + p.incorrect}` : null; };
    const cnt = (f) => adj.filter(f).length;
    const lines = {
      docs: adj.length ? `${cnt((r) => r.blocker_category === "Insufficient documentation")} of ${adj.length} adjudicated apps have "Insufficient documentation" as their primary blocker.` : "",
      auth: fld(g, "auth_methods") ? `Groq auth methods exactly right on ${fld(g, "auth_methods")} sampled apps (coarse classes).` : "",
      gated: adj.length ? `${cnt((r) => GATED.includes(r.credential_access))} apps have gated credential access; credential access was exactly right on ${fld(g, "credential_access") || "—"} sampled apps.` : "",
      evidence: adj.length ? `${cnt((r) => r.credential_access === "Unclear")} apps with unclear access · ${cnt((r) => r.buildability === "Insufficient evidence")} with insufficient evidence — kept out of "Easy wins".` : "",
      mcp: fld(g, "mcp_available") ? `MCP field right on ${fld(g, "mcp_available")} sampled apps for Groq vs ${fld(p2, "mcp_available") || "—"} for the registry-based crawler.` : "",
      llm: V.unsupported_citations_dropped != null ? `${V.unsupported_citations_dropped} unsupported citations dropped · ${cnt((r) => r.review)} apps flagged for human review.` : "",
      human: V.sample ? `Ground truth covers ${V.sample.apps} of ${V.applications_total || T()} apps (${V.sample.scorable_claims} claims, ${V.sample.excluded_claims} excluded); the other ${Math.max(0, (V.applications_total || T()) - V.sample.apps)} apps are Groq-generated findings without independent verification.` : "",
      composio: (() => {
        const tc = V.tool_calls || {}, by = tc.by_tool || {}, integ = state.raw && state.raw.groq && state.raw.groq.integration;
        const cc = Object.entries(by).filter(([t]) => /composio/i.test(t)).reduce((a, [, c]) => a + c, 0);
        const ok = integ ? arr(integ.checks).filter((c) => c.ok).length + "/" + arr(integ.checks).length : null;
        return tc.total != null ? `100-app run: ${tc.total} tool calls, ${cc} to Composio (${Object.entries(by).map(([t, c]) => `${t} × ${c}`).join(", ")})${ok ? ` · separate round-trip test: ${ok} checks passed` : ""}.` : "";
      })(),
      models: (() => {
        const M = V.groq_by_model || {};
        return Object.keys(M).length ? Object.entries(M).map(([k, s]) => `${k.replace("openai/", "")}: ${pct(s.accuracy)} exact on ${s.apps_covered} sample apps (${s.apps_adjudicated_total} apps total)`).join(" · ") : "";
      })(),
      noevidence: (() => {
        // apps where Groq produced no surviving citation; reviewer-added links ("Reviewed value: …") don't count as Groq evidence
        const none = adj.filter((r) => !r.evidence.some((e) => e.url && !/^Reviewed value:/.test(e.claim || "")));
        return adj.length ? (none.length ? `No Groq citation: ${none.map((r) => `${r.name} (${r.buildability || "unknown"} · ${r.credential_access || "unknown"} access${r.evidence.length ? `; ${r.evidence.length} reviewer link` : ""})`).join(" · ")}.` : "Every app has at least one Groq citation.") : "";
      })(),
    };
    function T() { return state.total; }
    $$("[data-lim-data]").forEach((el) => { const t = lines[el.dataset.limData]; el.textContent = t || ""; el.hidden = !t; });
  }

  /* ---------------- navigation & chrome ---------------- */
  function bindChrome() {
    const btn = $("#index-btn"), panel = $("#index-panel");
    const close = () => { panel.hidden = true; btn.setAttribute("aria-expanded", "false"); };
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const open = panel.hidden;
      panel.hidden = !open; btn.setAttribute("aria-expanded", String(open));
      if (open) { const a = $("a", panel); a && a.focus(); }
    });
    panel.addEventListener("click", (e) => { if (e.target.closest("a")) close(); });
    document.addEventListener("click", (e) => { if (!panel.hidden && !panel.contains(e.target)) close(); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && !panel.hidden) { close(); btn.focus(); } });

    // active section
    const links = $$("[data-nav]");
    const secs = $$("main section[id]");
    const setActive = (id) => links.forEach((a) => { const on = a.dataset.nav === id; a.classList.toggle("active", on); on ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current"); });
    const onScroll = () => {
      const y = window.scrollY + window.innerHeight * 0.3;
      let cur = "";
      secs.forEach((s) => { if (s.offsetTop <= y) cur = s.id; });
      setActive(cur === "hero" ? "" : cur);
      const h = document.documentElement.scrollHeight - window.innerHeight;
      $("#progress-bar").style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + "%";
      $("#to-top").hidden = window.scrollY < 700;
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    onScroll();
    $("#to-top").addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
      $(".brand").focus({ preventScroll: true });
    });
  }
  function reveal() {
    const els = $$(".reveal:not(.in)");
    if (!("IntersectionObserver" in window)) return els.forEach((e) => e.classList.add("in"));
    const io = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    els.forEach((e) => io.observe(e));
  }

  /* ---------------- boot ---------------- */
  async function boot() {
    bindChrome();
    bindDirectory();
    await load();
    renderStatus();
    renderOverview();
    setupFilters();
    syncSortUi();
    renderDirectory();
    renderMethodology();
    renderArchitecture();
    renderFindings();
    renderSkyline();
    renderVerification();
    renderRecs();
    bindHeroTabs();
    renderHeroTabs();
    reveal();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
