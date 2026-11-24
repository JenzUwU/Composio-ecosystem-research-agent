"""Stage 4: Groq LLM adjudication with Composio tool calling: the reasoning step.

    python -m agent.llm_adjudicator --only 3,61,92      # trial
    python -m agent.llm_adjudicator --batch-size 10     # all remaining apps (resumable)

Per app:
  1. Build a compact evidence context from the crawler's pass-2 output (fetched official
     pages + matched snippets + MCP registry hits + llms.txt) and the Composio catalog
     record (secondary evidence).
  2. Research turn (Groq + tools): Groq may call read-only tools: re-read a fetched
     official page around keywords, list a Composio toolkit's tools, or fetch Composio
     tool schemas. Python executes every call (composio_tools.ToolExecutor).
  3. Decision turn (Groq, strict JSON Schema): final fields + citations.
  4. Post-validation in Python: citations must be URLs the crawler fetched (or the MCP
     registry / Composio catalog), enums are schema-enforced, and anything unsupported
     is dropped and flagged for human review.

Checkpointed per app to data/llm_adjudicated_results.json (resume skips done apps);
full tool traces in data/llm_traces.jsonl. Never re-crawls.
"""
from __future__ import annotations

import argparse
import json
import logging
import time

from . import config
from .composio_tools import ToolExecutor
from .groq_client import GroqLLM

OUT = config.DATA / "llm_adjudicated_results.json"
TRACES = config.DATA / "llm_traces.jsonl"
FAILED_ATTEMPTS = config.DATA / "llm_failed_attempts.jsonl"   # append-only: every failed Groq attempt, never rewritten
UNRESOLVED = config.DATA / "llm_unresolved.json"              # apps whose retry also failed (no record is fabricated)
log = logging.getLogger("adjudicator")

AUTH = ["OAuth2", "API Key", "Basic", "Personal Access Token", "Bearer Token", "Other"]
ACCESS = ["Self-serve (free)", "Self-serve (free trial / sandbox)", "Self-serve (paid plan required)",
          "Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated", "Unclear"]
VERDICT = ["Ready to build", "Buildable with limitations", "Requires outreach / partnership",
           "Not currently feasible", "Insufficient evidence"]
BLOCKER = ["None", "Paid plan required", "App review / partner approval", "Enterprise / sales contract",
           "No public API", "Admin install / consent", "Insufficient documentation", "Not an HTTP API (CLI/library)"]
MCP = ["Official", "Third-party/community", "None found", "Unclear"]
FIELDS = ["auth_methods", "credential_access", "api_type", "mcp_available", "buildability_verdict", "primary_blocker"]

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "required": ["description", "auth_methods", "credential_access", "api_type", "api_breadth", "mcp_available",
                 "mcp_detail", "buildability_verdict", "primary_blocker", "blocker_category", "evidence",
                 "confidence", "requires_human_review", "notes"],
    "properties": {
        "description": {"type": "string"},
        "auth_methods": {"type": "array", "items": {"type": "string", "enum": AUTH}},
        "credential_access": {"type": "string", "enum": ACCESS},
        "api_type": {"type": "array", "items": {"type": "string", "enum": ["REST", "GraphQL"]}},
        "api_breadth": {"type": "string", "enum": ["Broad", "Moderate", "Narrow", "Unknown"]},
        "mcp_available": {"type": "string", "enum": MCP},
        "mcp_detail": {"type": "string"},
        "buildability_verdict": {"type": "string", "enum": VERDICT},
        "primary_blocker": {"type": "string"},
        "blocker_category": {"type": "string", "enum": BLOCKER},
        "evidence": {"type": "array", "items": {
            "type": "object", "additionalProperties": False, "required": ["field", "claim", "url"],
            "properties": {"field": {"type": "string", "enum": FIELDS}, "claim": {"type": "string"}, "url": {"type": "string"}}}},
        "confidence": {"type": "string", "enum": ["High", "Medium", "Low"]},
        "requires_human_review": {"type": "boolean"},
        "notes": {"type": "string"},
    },
}

SYSTEM = f"""You are the reasoning stage of an evidence-based API research pipeline for Composio (which builds agent toolkits).
You judge ONE app from the evidence given. Rules:
- Use only the evidence in the context and tool results. Never invent URLs, endpoints, prices or restrictions.
- Cite only URLs that appear in the context (fetched pages, MCP registry query, Composio catalog).
- If evidence is insufficient, say so: credential_access "Unclear", mcp "Unclear", verdict "Insufficient evidence", confidence Low, requires_human_review true.
- Regex snippets are noisy: a "Contact sales" button on a marketing/pricing page does NOT mean the API is partner-gated; an
  "API key" mentioned in an SDK sample may not be the app's auth model; "Bearer" usually describes how an OAuth/API token is sent.
- credential_access = how an ordinary developer gets working credentials: free account/key -> "Self-serve (free)"; free trial or
  sandbox -> "Self-serve (free trial / sandbox)"; API only on paid tiers -> "Self-serve (paid plan required)"; needs app review /
  marketplace approval / developer token approval -> "Admin approval / app review"; enterprise contract -> "Enterprise-only";
  partner program or sales contact required for API access -> "Partnership / contact-sales gated".
- A Composio toolkit existing is secondary evidence; it does NOT prove the vendor's API is publicly accessible.
- mcp_available: "Official" only if the vendor publishes/hosts it (vendor docs or vendor namespace in the registry); community-only -> "Third-party/community".
- buildability_verdict: "Ready to build" = documented REST/GraphQL + self-serve credentials; "Buildable with limitations" = paid plan,
  admin install, app review, or narrow API; "Requires outreach / partnership" = gated by partner/enterprise/sales;
  "Not currently feasible" = no public HTTP API; "Insufficient evidence" otherwise.
- blocker_category must be one of {BLOCKER}; "None" when ready to build."""


def build_context(app: dict, crawl: dict, ck: dict | None) -> tuple[str, set[str], set[str]]:
    ok_pages = [p for p in crawl["pages"] if p.get("ok") and p.get("chars", 0) > 200 and not p["url"].endswith("/llms.txt")]
    allowed = {p["url"] for p in ok_pages}
    lines = [f"APP: {app['name']} | category: {app['category']} | brief hint: {app['hint']}",
             f"FETCHED OFFICIAL PAGES ({len(ok_pages)} ok of {len(crawl['pages'])} attempted):"]
    lines += [f"- {p['url']}" for p in ok_pages[:10]]
    failed = [p for p in crawl["pages"] if not p.get("ok")]
    if failed:
        lines.append("FAILED FETCHES: " + "; ".join(f"{p['url']} [{p.get('status') or p.get('error')}]" for p in failed[:4]))
    lines.append("CRAWLER REGEX SIGNALS (noisy; verify):")
    seen = set()
    for e in crawl["evidence"]:
        key = (e["field"], e["claim"])
        if key in seen or e.get("source_type") == "mcp_registry":
            continue
        seen.add(key)
        lines.append(f"- [{e['field']}] {e['claim']} @ {e['source_url']}: \"{e['snippet'][:150]}\"")
        if len(seen) >= 9:
            break
    reg = crawl.get("mcp_registry") or {}
    if reg.get("query_url"):
        allowed.add(reg["query_url"])
        ms = reg.get("matches") or []
        lines.append(f"MCP REGISTRY ({reg['query_url']}): " + (", ".join(f"{m['name']}{' [vendor namespace]' if m['official_namespace'] else ''}" for m in ms[:5]) or "no matches"))
    lines.append(f"llms.txt: {crawl.get('llms_txt') or 'not found'}")
    toolkits = set()
    if ck and ck.get("composio_toolkit"):
        t = ck["toolkits"][0]
        toolkits.add(t["slug"])
        lines.append(f"COMPOSIO CATALOG (secondary): toolkit '{t['slug']}', {t.get('tools_count')} tools, auth schemes {t.get('auth_schemes')}, match {ck['match_confidence']}")
        allowed.add("composio:catalog")
    elif ck and ck.get("rejection_reason"):
        lines.append(f"COMPOSIO CATALOG: no matching toolkit ({ck['rejection_reason']})")
    else:
        lines.append("COMPOSIO CATALOG: no toolkit for this app")
    return "\n".join(lines), allowed, toolkits


def validate(result: dict, allowed: set[str]) -> dict:
    kept, dropped = [], []
    for e in result.get("evidence", []):
        (kept if e["url"] in allowed or e["url"].startswith("composio:") else dropped).append(e)
    result["evidence"] = kept
    result["unsupported_citations"] = dropped
    if dropped:
        result["requires_human_review"] = True
    cited = {e["field"] for e in kept}
    missing = [f for f in ("auth_methods", "credential_access", "api_type") if f not in cited]
    if missing:
        result["requires_human_review"] = True
    result["fields_without_citation"] = missing
    # consistency guards (schema can't express these)
    if not result["api_type"] and result["buildability_verdict"] == "Ready to build":
        result["requires_human_review"] = True
        result["notes"] += " [validator: 'Ready to build' without a documented API type]"
    return result


RETRYABLE_CODES = ("json_validate_failed", "output_parse_failed", "tool_use_failed")


class AdjudicationFailed(Exception):
    """Both attempts failed (or a non-retryable error). Carries every attempt for the log."""
    def __init__(self, msg, attempts):
        super().__init__(msg)
        self.attempts = attempts


def _attempt_record(app, n, model, e=None, phase="decision"):
    """Describe one attempt. For a failure, keep Groq's error code and the rejected generation."""
    rec = {"attempt": n, "phase": phase, "model": model, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "status": "ok" if e is None else "failed"}
    if e is not None:
        body = getattr(e, "body", None)
        err = body.get("error", body) if isinstance(body, dict) else {}
        rec.update({"error_type": type(e).__name__, "code": (err or {}).get("code") or next((c for c in RETRYABLE_CODES if c in str(e)), None),
                    "message": str((err or {}).get("message") or e)[:600],
                    "failed_generation": str((err or {}).get("failed_generation") or "")[:4000]})
        with FAILED_ATTEMPTS.open("a", encoding="utf-8") as f:
            f.write(json.dumps({"id": app["id"], "app": app["name"], **rec}, ensure_ascii=False) + "\n")
    return rec


def adjudicate(app, crawl, ck, llm: GroqLLM, cc) -> dict:
    context, allowed, toolkits = build_context(app, crawl, ck)
    ex = ToolExecutor(cc, allowed_urls=allowed, allowed_toolkits=toolkits)
    tools = ex.groq_tools()
    if not toolkits:
        tools = [t for t in tools if t["function"]["name"] != "composio_list_toolkit_tools"]
    trace: list = []
    msgs = [{"role": "system", "content": SYSTEM},
            {"role": "user", "content": context + "\n\nRESEARCH STEP: call at most 2 tools if they would resolve an uncertainty "
             "(e.g. re-read a fetched page for 'oauth', 'api key', 'sandbox', 'partner', 'pricing'). If no tool is needed, reply with research notes (max 80 words)."}]
    # one research turn: Groq either requests tools (executed by Python) or writes notes
    notes, msgs = llm.tool_loop(msgs, tools, ex, max_rounds=1, trace=trace, reasoning_effort="low", max_completion_tokens=700)
    msgs.append({"role": "user", "content": "DECISION STEP: output the final JSON for this app. Cite only URLs from the context."})
    # structured outputs cannot be combined with tools, so tools are not passed here
    clean = [m for m in msgs if m["role"] != "tool" and not m.get("tool_calls")]
    tool_summary = "\n".join(f"TOOL {t['tool']}({json.dumps(t['arguments'])[:120]}) -> {t['result_excerpt'][:350]}" for t in trace)
    if tool_summary:
        clean.insert(2, {"role": "user", "content": "TOOL RESULTS:\n" + tool_summary})
    attempts = []
    try:
        result = llm.structured(clean, SCHEMA, name="app_adjudication", reasoning_effort="low", max_completion_tokens=2200)
        attempts.append(_attempt_record(app, 1, getattr(llm, "last_model", llm.model)))
    except Exception as e:
        attempts.append(_attempt_record(app, 1, getattr(llm, "last_model", llm.model), e))
        # Groq validates strict-schema output after generation. Observed 400s in the full run:
        #   json_validate_failed (bad enum value / missing field), output_parse_failed (prose, not JSON),
        #   tool_use_failed (model tried to call a tool in the tool-less decision turn).
        # Retry once with an explicit reminder; any other error is raised.
        code = next((c for c in RETRYABLE_CODES if c in str(e)), None)
        if code is None:
            raise AdjudicationFailed(f"non-retryable error: {e}", attempts) from e
        log.warning("[%s] %s, retrying once: %s", app["name"], code, str(e)[:200])
        clean.append({"role": "user", "content": "Your previous output was rejected (" + code + "). Do NOT call any tool. "
                      "Output ONLY one JSON object containing EVERY required field (including notes). Use ONLY these exact enum values: "
                      f"mcp_available {MCP}; credential_access {ACCESS}; buildability_verdict {VERDICT}; blocker_category {BLOCKER}; "
                      f"auth_methods items {AUTH}; api_type items ['REST','GraphQL']; api_breadth ['Broad','Moderate','Narrow','Unknown']."})
        try:
            result = llm.structured(clean, SCHEMA, name="app_adjudication", reasoning_effort="low", max_completion_tokens=3000)
        except Exception as e2:
            attempts.append(_attempt_record(app, 2, getattr(llm, "last_model", llm.model), e2))
            raise AdjudicationFailed(f"retry failed: {e2}", attempts) from e2
        attempts.append(_attempt_record(app, 2, getattr(llm, "last_model", llm.model)))
        result["notes"] = (result.get("notes") or "") + f" [retried after Groq 400 {code}]"
    result = validate(result, allowed)
    result.update({"id": app["id"], "app_name": app["name"], "category": app["category"],
                   "model": getattr(llm, "last_model", llm.model), "research_notes": notes[:900],
                   "tools_called": [{"tool": t["tool"], "ok": t["ok"]} for t in trace],
                   "attempts": attempts, "retried": len(attempts) > 1,
                   "adjudicated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())})
    with TRACES.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"id": app["id"], "app": app["name"], "trace": trace, "notes": notes}, default=str) + "\n")
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only")
    ap.add_argument("--batch-size", type=int, default=10)
    ap.add_argument("--max-apps", type=int, default=100)
    ap.add_argument("--redo", action="store_true", help="re-adjudicate apps already done (with --only)")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                        handlers=[logging.FileHandler(config.LOGS / "adjudication.log", encoding="utf-8"), logging.StreamHandler()])
    logging.getLogger("httpx").setLevel(logging.WARNING)

    apps = json.loads((config.DATA / "apps.json").read_text(encoding="utf-8"))
    crawl = {r["id"]: r for r in json.loads((config.DATA / "research_results_pass2.json").read_text(encoding="utf-8"))}
    ckp = config.DATA / "composio_toolkits.json"
    ck = {r["id"]: r for r in json.loads(ckp.read_text(encoding="utf-8"))} if ckp.exists() else {}
    done = {r["id"]: r for r in json.loads(OUT.read_text(encoding="utf-8"))} if OUT.exists() else {}

    todo = [a for a in apps if (args.only is None or a["id"] in {int(x) for x in args.only.split(",")})
            and (args.redo or a["id"] not in done)][: args.max_apps]
    from .schema_check import check_record
    unresolved = {u["id"]: u for u in json.loads(UNRESOLVED.read_text(encoding="utf-8"))} if UNRESOLVED.exists() else {}

    def mark_unresolved(a, reason, attempts):
        prev = unresolved.get(a["id"], {}).get("attempts", [])
        unresolved[a["id"]] = {"id": a["id"], "app": a["name"], "status": "unresolved", "reason": str(reason)[:600],
                               "attempts": prev + attempts}
        UNRESOLVED.write_text(json.dumps([unresolved[k] for k in sorted(unresolved)], indent=1), encoding="utf-8")
        log.error("[%3d] %s UNRESOLVED: %s", a["id"], a["name"], str(reason)[:200])

    log.info("%d done, %d to adjudicate", len(done), len(todo))
    llm = GroqLLM()
    try:
        from .composio_client import ComposioResearchClient
        cc = ComposioResearchClient()
    except Exception as e:
        log.warning("Composio unavailable, running without Composio tools: %s", e)
        cc = None

    for i in range(0, len(todo), args.batch_size):
        for a in todo[i:i + args.batch_size]:
            t0 = time.time()
            try:
                r = adjudicate(a, crawl[a["id"]], ck.get(a["id"]), llm, cc)
                errs = check_record(r)
                if errs:  # never mark a record complete unless it passes the exact schema check
                    mark_unresolved(a, "schema check failed: " + "; ".join(errs[:5]), r.get("attempts", []))
                    continue
                done[a["id"]] = r
                if unresolved.pop(a["id"], None) is not None:
                    UNRESOLVED.write_text(json.dumps([unresolved[k] for k in sorted(unresolved)], indent=1), encoding="utf-8")
                log.info("[%3d] %-26s %-32s %-30s tools=%s model=%s %.0fs", a["id"], a["name"], r["buildability_verdict"],
                         r["credential_access"], [t["tool"] for t in r["tools_called"]], r["model"], time.time() - t0)
            except RuntimeError as e:
                if "exhausted" in str(e):
                    log.error("stopping: %s (resume later; progress is saved)", e)
                    OUT.write_text(json.dumps([done[k] for k in sorted(done)], indent=1), encoding="utf-8")
                    return
                log.exception("[%3d] %s failed: %s", a["id"], a["name"], e)
            except AdjudicationFailed as e:
                mark_unresolved(a, e, e.attempts)
            except Exception as e:  # research-turn or network failure: one attempt, logged, unresolved
                log.exception("[%3d] %s failed: %s", a["id"], a["name"], e)
                mark_unresolved(a, e, [_attempt_record(a, 1, getattr(llm, "last_model", llm.model), e, phase="research/other")])
            OUT.write_text(json.dumps([done[k] for k in sorted(done)], indent=1), encoding="utf-8")  # per-app checkpoint
        log.info("batch checkpoint: %d/100 adjudicated | usage %s", len(done), llm.usage)
    log.info("finished: %d/100 adjudicated | usage %s", len(done), llm.usage)


if __name__ == "__main__":
    main()
