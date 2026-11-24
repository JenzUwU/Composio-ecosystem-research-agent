# Mapping the Agent-Ready App Ecosystem

Research pipeline built for Composio's AI Product Ops take-home. For **100 apps across 10 categories**, it determines:
- auth methods;
- how a developer gets credentials (self-serve vs gated);
- API surface;
- MCP availability;
- a buildability verdict with its main blocker.

Every claim carries an evidence URL, and the pipeline **measures its own accuracy** against a separately built ground-truth sample.

The deliverable is a single HTML case study at `dashboard/index.html`. Every number on it is generated from the data files.

## What each part really is

| Component | What it is | Reasons? |
|---|---|---|
| Crawler (`agent/orchestrator.py`, `research_agent.py`, `fetcher.py`, `signals.py`) | Rule-based Python crawler: fetches official docs, follows auth/getting-started links, renders JS-only pages, matches regex signals, queries the official MCP Registry API | **No.** Deterministic, not an autonomous agent |
| Composio stage (`composio_client.py`, `composio_enrich.py`) | Official Composio SDK: catalog lookup for all 100 apps, sessions, tool discovery and execution | No. Supplies secondary evidence and tools |
| Groq stage (`groq_client.py`, `llm_adjudicator.py`, `composio_tools.py`) | Groq LLM reads each app's evidence, **calls Composio and page-reading tools through a tool-calling loop**, then outputs strict-schema JSON | **Yes.** The reasoning step |
| Validator (`evidence_validator.py`) | Checks every citation was really fetched, logs crawler-to-Groq changes, scores each stage against ground truth | No |
| Verification (`verification/`) | Seeded 30-app sample, ground truth built from official pages, blind to Groq output | LLM-assisted ground truth (see note) |

```
apps.json (100 apps + candidate official doc URLs)
   │
   ▼
[Python crawler]  fetch → discover auth links → render JS → regex signals → MCP Registry API     (no AI)
   │   pass 1 = homepage only (baseline) · pass 2 = deep loop
   ├──► [Composio SDK] toolkit catalog: exists? tools? auth schemes?  (secondary evidence)
   ▼
[Groq LLM: research turn]  ──tool call──►  Python executes:  • read_fetched_page (official page re-read)
   ▲                                                       • composio_list_toolkit_tools (Composio SDK)
   └──────────── role:"tool" result ◄────────────────────  • COMPOSIO_GET_TOOL_SCHEMAS (Composio session.execute)
   ▼
[Groq LLM: decision turn]  strict JSON Schema → final fields + citations
   ▼
[Validator]  drop citations not among fetched pages · score every stage vs 30-app ground truth
   ▼
pattern_analyzer → dashboard/data.js → dashboard/index.html
```

## Technologies

- **Python 3.11.** The crawler uses only the standard library: `urllib`, `html.parser` and `concurrent.futures`.
- **Composio Python SDK** `composio==0.34.0`. Method names were verified with `inspect.signature`; see `logs/composio_sdk_surface.txt`.
- **Groq Python SDK** `groq==1.7.0`, using model `openai/gpt-oss-120b`. Strict JSON Schema mode and tool use are both documented for that model.
- **Official MCP Registry API**, used for MCP availability.
- **r.jina.ai** reader, a rendering fallback for JS-only public doc pages. Only public URLs are sent to it.
- **Vanilla HTML/CSS/JS** for the dashboard: no build step, with charts drawn as SVG from `data.js`.

## Configuration

`.env` lives in the project root and is gitignored. Never commit it. Copy `.env.example` and fill in:

```
COMPOSIO_API_KEY=   # Composio dashboard; needs session_management write for sessions
GROQ_API_KEY=       # console.groq.com
```

Optional settings:
- `GROQ_MODEL`
- `GROQ_FALLBACK_MODELS` (default `openai/gpt-oss-20b,qwen/qwen3.8-27b`)
- `GROQ_TPM` (default 8000)
- `COMPOSIO_ALLOW_TRACKING` (default 0, meaning SDK telemetry is off)
- `RESEARCH_*` crawler settings

To add a key without it ever appearing on screen, run this from the project root in PowerShell. It uses hidden input:
```powershell
$s = Read-Host "Enter GROQ_API_KEY" -AsSecureString; $p=[Runtime.InteropServices.Marshal]::SecureStringToBSTR($s); try { $k=[Runtime.InteropServices.Marshal]::PtrToStringBSTR($p); [IO.File]::AppendAllText("$PWD\.env", "GROQ_API_KEY=$k`n", (New-Object Text.UTF8Encoding $false)) } finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($p); Remove-Variable k,s }
```

## Install

```powershell
cd composio-app-research
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

## Run

```powershell
.venv\Scripts\python data\build_apps.py                    # 100-app input
.venv\Scripts\python -m agent.orchestrator --pass 1        # naive crawler baseline (~30 s)
.venv\Scripts\python -m agent.orchestrator --pass 2        # deep crawler loop, 5 checkpointed batches (~5 min; ~16 s from cache)
.venv\Scripts\python -m agent.composio_client              # Composio connectivity test  -> logs/composio_connectivity.json
.venv\Scripts\python -m agent.orchestrator --composio      # Composio catalog cross-check -> data/composio_toolkits.json
.venv\Scripts\python -m agent.groq_client                  # Groq connectivity test      -> logs/groq_connectivity.json
.venv\Scripts\python -m tests.test_groq_composio           # Groq<->Composio tool round trip -> logs/groq_composio_integration.json
.venv\Scripts\python -m agent.llm_adjudicator              # Groq adjudication of all apps (resumable, ~100 min on free tier)
.venv\Scripts\python -m agent.failed_attempts_backfill     # copy failures that exist only in logs/adjudication.log into data/llm_failed_attempts.jsonl
.venv\Scripts\python -m agent.llm_adjudicator              # second run = retry pass: only apps without a valid record
.venv\Scripts\python -m agent.schema_check                 # exact schema check of every record -> logs/checkpoint_inspection.json
.venv\Scripts\python verification\build_ground_truth.py    # 30-app ground truth
.venv\Scripts\python -m agent.evidence_validator           # citations + accuracy per stage -> verification/verification_report.json
.venv\Scripts\python -m agent.pattern_analyzer             # stats -> dashboard/data.js
.venv\Scripts\python -m http.server -d dashboard 8000      # open http://localhost:8000
```

**Resuming and retries.**
- `llm_adjudicator` saves after every app and skips apps that already have a record, so a rerun never overwrites a successful record. To redo specific apps on purpose, use `--only 3,61 --redo`.
- If Groq rejects the decision output (`json_validate_failed`, `output_parse_failed` or `tool_use_failed`), the app is retried once with an explicit reminder of the schema.
- Every failed attempt is appended to `data/llm_failed_attempts.jsonl`, with Groq's error code and the rejected generation. Each record keeps an `attempts` list.
- A record is saved only if it passes `agent/schema_check.py`:
  - exact schema: required fields, types, enum values, no extra fields;
  - run metadata present;
  - no positive claim without at least one surviving citation.
- If both attempts fail, the app goes to `data/llm_unresolved.json` and no record is written.

**Rate limits.** On Groq's free tier, `gpt-oss-120b` allows 8K tokens/minute and 200K tokens/day. The client throttles to stay under the per-minute limit, honours `retry-after`, and switches to a documented strict-schema fallback model when a daily cap is hit. Each record names the model that produced it.

## Composio integration: what actually ran

| Step | Call | Result |
|---|---|---|
| Init | `Composio(api_key=…, allow_tracking=False)` | OK |
| Catalog | `composio.toolkits.get("github")` | 200 |
| Discovery | `composio.tools.get_raw_composio_tools(toolkits=["github"])` | 200 |
| Session | `composio.sessions.create(user_id=…, toolkits=["github"])` | 201 (the first key got 403: read-only session permission) |
| Session tools | `session.tools()` | 200. 6 meta tools |
| Execution | `session.execute("COMPOSIO_GET_TOOL_SCHEMAS", …)`: read-only meta tool, part of the connectivity test | 200, `success: true` |
| Connection state | `session.toolkits(toolkits=["github"])` | `is_active: false`: no GitHub account connected |
| Catalog cross-check | `composio.toolkits.list()` (1,883 toolkits) | 79/100 apps have a toolkit; 3 wrong-product matches rejected on review |
| Groq round trip | Groq requested `COMPOSIO_GET_TOOL_SCHEMAS`, Python executed it via the session, and Groq answered from the result | 6/6 checks pass |
| Groq in the 100-app run | Composio tools offered to Groq for every app with a toolkit | Groq **never chose** a Composio tool. All 46 tool calls were `read_fetched_page`. |

**Not done, by design.** No external app account (e.g. GitHub) was connected, so no `GITHUB_*` app tool was executed; connecting needs the account owner's approval. Composio is not used for web search: documentation research is done by the crawler.

**What a toolkit's existence proves.** A Composio toolkit existing does *not* prove a vendor's API is self-serve. Official docs remain primary evidence.

## Verification methodology

- **Sample.** 30 apps, 3 per category, drawn with `random.Random(42)` before any LLM run (`verification/verification_sample.json`).
- **Ground truth.** Built in `verification/build_ground_truth.py` from the official pages the crawler fetched (`verification/inspect_app.py`), plus existence checks of vendor MCP repos, packages and endpoints. It was done blind to Groq's answers. Fields the evidence didn't settle are `null` and not scored.
- **Who reviewed it.** The ground truth was prepared with LLM assistance from the fetched official pages and vendor MCP sources, blind to Groq's answers. **It has not yet been re-checked by a person.**
- **Scoring** (`agent/evidence_validator.py`):
  - Auth is compared as coarse classes: {OAuth2, Key/Token, Basic, Other}.
  - API type uses set comparison.
  - Credential access is exact; same self-serve/gated group counts as partial.
  - MCP and verdict are exact.
  - Every stage (crawler pass 1, pass 2, Groq, and Composio's catalog auth as a reference) is scored against the same truth.
- **Results** are in `verification/verification_report.json` and section 07 of the page.

### Results (30-app sample, 144 scored claims, Groq output *before* any review correction)

| Stage | Exact | Exact + partial |
|---|---|---|
| Pass 1: naive crawler (homepage only) | 43/144 = 29.9% | 37.5% |
| Pass 2: deep crawler (regex) | 66/144 = 45.8% | 61.1% |
| Groq adjudication (both models) | 90/144 = 62.5% | 78.5% |
| Composio catalog auth (reference, auth field only, 23 apps) | 14/22 = 63.6% | 90.9% |

**Per field, Groq exact.**
- Auth: 17/29.
- API type: 27/30.
- Credential access: 12/27.
- MCP: 15/30, **worse than the deep crawler's 23/30**. Groq often downgraded an official vendor MCP server to "Third-party/community" or "Unclear".
- Verdict: 19/28.

**Per model.**

| Model | Apps adjudicated | Sample apps | Exact | Exact + partial | Review-flag rate | "Insufficient evidence" rate |
|---|---|---|---|---|---|---|
| `openai/gpt-oss-120b` | 56 | 18 | 48/87 = 55.2% | 75.9% | 14% | 5% |
| `openai/gpt-oss-20b` | 44 | 12 | 42/57 = 73.7% | 82.5% | 34% | 16% |

This is **not** a controlled comparison. The 20b model only took over when 120b hit its daily token cap, so the two models saw different apps:
- 120b: lower ids, including the CRM, Support, Comms and Ecommerce samples;
- 20b: higher ids, including Productivity and Finance.

With 12 to 18 sample apps each, the gap is within noise and confounded by app mix. Do not read it as "20b is more accurate". 20b also flagged more apps for review and answered "Insufficient evidence" more often.

**Review corrections.** On the 30 sample apps, 54 field values where Groq was not exactly right were replaced by the reviewed value in `data/verified_results.json`. Each one is listed in `verification_report.json` → `review_corrections`. They are **not** counted in the accuracy above. The other 70 apps are Groq's unreviewed output.

**Failures.**
- 9 Groq attempts were rejected across 8 apps: 7 `json_validate_failed`, 1 `output_parse_failed`, 1 `tool_use_failed`.
- All 8 apps got a valid record on retry. 0 unresolved.
- Final checkpoint: 100/100 records pass the exact schema check.

**Tokens** (from `logs/adjudication.log`, successful calls only):
- 211 calls;
- 364,028 prompt tokens + 69,364 completion tokens = 433,392 total, across the trial, main and retry runs.

## Data files

| File | Contents |
|---|---|
| `data/apps.json` | 100 apps, category, brief hint, candidate official doc URLs |
| `data/research_results_pass1.json` / `_pass2.json` | Crawler output (pages + status, regex signals, snippets) |
| `data/composio_toolkits.json` | Per-app Composio catalog cross-check |
| `data/llm_adjudicated_results.json` | Groq output per app (fields, citations, model, tools called) |
| `data/llm_traces.jsonl` | Every Groq tool call with arguments and result excerpt |
| `data/verified_results.json` | Final dataset (Groq fields + citation status + crawler + Composio + attempt history; sample apps reviewer-corrected) |
| `data/llm_failed_attempts.jsonl` | Append-only log of every rejected Groq attempt (error code + rejected generation) |
| `logs/checkpoint_inspection.json` | Exact-schema status of every record (complete / malformed / missing / unresolved) |
| `logs/archive_pre_audit/` | Test evidence logs as they were before the final test rerun |
| `verification/ground_truth.json` | 30-app ground truth |
| `verification/verification_report.json` | Accuracy per stage, misses, changes, unsupported citations |
| `logs/*.json` | Real SDK test results (Composio, Groq, round trip) |

## Known limitations

- **Unconfirmed review.** The ground truth was prepared with LLM assistance and has not yet been re-checked by a person. The sample is 30 apps, so accuracy has wide error bars.
- **Free-tier model mix.** Groq's free tier caps daily tokens, so 44 apps were adjudicated by the fallback `gpt-oss-20b`. The model is recorded per app. Per-model accuracy is confounded by app mix (see above).
- **Only 30 apps are verified.** The headline counts for the other 70 apps carry the measured error rate (62.5% exact on the sample).
- **MCP field.** Groq is less accurate than the crawler's registry lookup on MCP (15/30 vs 23/30). Treat MCP counts as indicative.
- **Composio tools in the run.** In the 100-app run Groq never chose a Composio tool. The Groq to Composio tool path is demonstrated by the round-trip test, not by the research run.
- **Failure model attribution.** The 8 first-run failures were logged before per-attempt logging existed. Their model is inferred from the model-switch time in the log and marked `model_inferred`.
- **Mixed timestamps.** Log timestamps are local time (IST). JSON timestamps are UTC (`Z`).
- **Credential access is the hardest field.** It lives in pricing and partner pages, not API references.
- **No docs found for 4 apps.** fanbasis, iPayX, Waterfall.io and Consensus had no official API docs found.
- **Docs change.** The research reflects 24 Nov 2026.
- **Not yet deployed.** It's ready for GitHub Pages: publish the `dashboard/` folder.
#   C o m p o s i o - e c o s y s t e m - r e s e a r c h - a g e n t  
 