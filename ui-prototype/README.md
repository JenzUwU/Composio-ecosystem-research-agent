# ui-prototype — Field Study Nº 001 (editorial case study)

Single-page HTML case study for the 100-app research. It uses vanilla HTML, CSS and JS. There is no framework and no build step. The design direction is "Monochrome Signal": a Swiss grid, neo-brutalist borders, a pixel display type and scanline accents. A single restrained blue accent (`#334EAC`, with `#7096D1` / `#BAD6EB` / `#D0E3FF` / `#081F5C` defined as tokens in `styles.css`) marks active states, indicators and the hero lens.

All animation runs regardless of the OS "reduce motion" setting (removed on request). Animations still pause when off-screen or in a hidden tab.

This folder is self-contained. It **reads** pipeline output and never writes to it. Nothing outside `ui-prototype/` was changed, apart from a preview entry in the workspace's `.claude/launch.json`.

## Files

| File | Purpose |
|---|---|
| `index.html` | Page structure: hero plus 8 sections (Overview, Ecosystem, Methodology, Architecture, Findings, Verification, Recommendations, Source) |
| `styles.css` | Whole visual system. Responsive at 1440 / 1180 / 900 / 640 px |
| `hero.js` | Procedural canvas illustration (FIG. 01), described below |
| `glyph-bg.js` | WebGL glyph field behind the page. A plain-JS port of the React `<GlyphBackground>` (`backgrounds-glyph.tsx`, the same shader). It only shows in the margins outside the 1440px layout. Click a margin to send a red wave. It pauses when there are no margins, when the tab is hidden, or when reduced motion is on |
| `skyline.js` | Plain-JS port of the React `<ContributionSkyline>`, in black and grey only. A 10×10 grid (categories × apps) that morphs from a flat heat map into a 3D skyline. You can switch between two real metrics: evidence sources cited, and Composio toolkit tool count. Hover shows the app. Drag orbits the view and double-click resets it. Arrow keys walk the grid. Clicking a box opens that app in the directory |
| `app.js` | Data loading and normalisation, directory (search, filters, sort, evidence), charts, navigation |
| `data/sample-data.json` | 4 invented demo records showing the data contract. **Not research** |

## Caching

Asset links carry a `?v=` version, so browsers don't mix old HTML with new CSS. Bump it in `index.html` after editing CSS or JS.

## Run

Serve the **project root** (`composio-app-research/`), so the page can reach `../dashboard/data.js` and `../data/apps.json`:

```powershell
cd composio-app-research
python -m http.server 8766
# open http://localhost:8766/ui-prototype/
```

Opening `index.html` directly from disk (`file://`) still works with the real data, because `data.js` is a script tag. Browsers block `fetch` on `file://`, though, so two things change:
- the pending-app list from `apps.json` cannot be loaded;
- the sample JSON fallback cannot be loaded.

The banner says which of these applies.

## Where the data comes from

`app.js` uses the first source that is available:

1. **`window.RESEARCH_DATA`**: already-normalised data in the contract below. Define it in a script tag before `app.js`.
2. **`window.DATA`** from `../dashboard/data.js`: the real pipeline output, written by `agent/pattern_analyzer.py`. Rows are mapped by `fromPipeline()` in `app.js`. When the page is served over HTTP, `../data/apps.json` adds any app not yet adjudicated as a **Pending** row.
3. **`data/sample-data.json`**: demo only. A red banner labels it as sample data.

Add `?data=sample` to the URL to force the sample.

To connect new backend output, either:
- regenerate `dashboard/data.js` (`python -m agent.pattern_analyzer`); the page picks it up on reload; or
- emit JSON in the contract below and load it as `window.RESEARCH_DATA`.

### Record contract (`apps[]`)

```json
{
  "id": 1, "name": "…", "category": "…", "description": "…",
  "auth_methods": ["OAuth2"], "credential_access": "Self-serve (free)",
  "api_types": ["REST"], "api_available": true,
  "mcp_available": "Official", "buildability": "Ready to build",
  "blocker": null, "blocker_category": "None",
  "evidence": [{ "field": "auth_methods", "claim": "…", "url": "https://…", "source_type": "official", "status": "Verified (page fetched by agent)" }],
  "evidence_urls": [],
  "confidence": "High", "verification_status": "…",
  "status": "adjudicated"
}
```

Missing values stay `null` or `[]` and render as **Unknown** or **Pending**. They are never shown as a positive result. `api_available` is only `true` when an API type is recorded.

The optional `verification` object uses the same shape as `DATA.verification`: `sample`, `stages[]` with `per_field` breakdowns, and so on. Without it, section 06 shows "Awaiting data".

## Honesty rules built into the UI

- The **Complete** badge only shows when two backend counts agree: the number of adjudicated rows, and the validator's `applications_adjudicated`. Otherwise the badge reads In progress or Unconfirmed, and hovering it shows both numbers. The Data source cell shows when `data.js` was last written.
- Targets (100 apps, 10 categories) are labelled as targets. Completed counts come from the data.
- While fewer than 100 apps are adjudicated:
  - findings and recommendations carry a **Preliminary** stamp;
  - a banner states how many apps are adjudicated.
- The final Groq score shows **Awaiting final evaluation** until the Groq stage has scored every ground-truth sample app.
- Pipeline and methodology statuses are derived from the data: complete, in progress or pending. The human re-check stays **Pending** while the reviewer note says it has not been done.
- The GitHub link is a placeholder until the repository is published. No URL is invented.

## How the hero illustration works (`hero.js`)

1. A Fibonacci lattice places about 1,600 points evenly on a sphere. Two latitude bands are left empty, which gives the sphere visible strata.
2. 150 dotted radial spikes grow from random surface points. Their lengths follow a power law and they "breathe" slowly.
3. Three tilted orbital rings surround the sphere, plus **100 app nodes** in 10 clusters, one cluster per category. Each node reflects the real data:
   - filled = adjudicated;
   - hollow = pending;
   - blue = flagged for human review.
4. Each frame:
   - points are rotated (Y spin, X tilt, pointer parallax);
   - points are projected orthographically onto an offscreen canvas;
   - the offscreen image is copied to the visible canvas in thin horizontal strips, which produces the scanlines;
   - random glitch events shift a few strips sideways (pixel displacement), and a scan band sweeps down the figure.
5. A blue research lens moves between adjudicated nodes and labels each one with the real app name and its verdict. Clicking the figure jumps to the next node.
6. Seeded RNG makes the figure identical on every load. Animation pauses when the figure is off-screen or the tab is hidden.

## Known gaps

- No GitHub URL yet, because the repository has no remote. Section 08 says so.
- Fonts (Silkscreen, Space Grotesk, Geist, JetBrains Mono) load from Google Fonts. Offline, the page falls back to system fonts.
- The brand mark in the nav is redrawn from the pixel symbol supplied as a reference. It is not an official Composio logo asset.
