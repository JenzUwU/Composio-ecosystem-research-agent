"""Stage 5: validate citations, merge the final dataset, and measure accuracy.

    python -m agent.evidence_validator

Inputs : data/research_results_pass1.json, data/research_results_pass2.json (crawler),
         data/llm_adjudicated_results.json (Groq), data/composio_toolkits.json (Composio),
         verification/ground_truth.json (30-app ground-truth sample)
Outputs: data/research_results.json (alias of pass 2), data/verified_results.json (final
         dataset, Groq fields + evidence status), verification/verification_report.json

Scoring rules (stated on the page too):
  - auth_methods are compared as coarse classes {OAuth2, Key/Token, Basic, Other}, because
    "API key" vs "personal access token" vs "bearer token" is mostly naming, not substance.
    exact class-set match = correct; overlapping but different = partial; else incorrect.
  - api_type: same set = correct; overlap = partial; else incorrect.
  - credential_access: exact = correct; same coarse group (self-serve vs gated) = partial.
  - mcp_available, buildability_verdict: exact match only.
  - ground-truth fields that are null are not scored.
  - "accuracy" = correct / scored. "lenient accuracy" = (correct + partial) / scored.
"""
from __future__ import annotations

import json
from urllib.parse import urlparse

from . import config
from .fetcher import _cache_path
from .research_agent import reg_domain, vendor_domains

FIELDS = ["auth_methods", "api_type", "credential_access", "mcp_available", "buildability_verdict"]
AUTH_CLASS = {"OAuth2": "OAuth2", "API Key": "Key/Token", "Personal Access Token": "Key/Token",
              "Bearer Token": "Key/Token", "Basic": "Basic", "Other": "Other"}


def load(p):
    return json.loads(p.read_text(encoding="utf-8"))


def url_status(url: str) -> str:
    if url.startswith("composio:"):
        return "Composio catalog record (SDK)"
    cp = _cache_path(url)
    if cp.exists():
        c = load(cp)
        if c.get("ok") and len(c.get("text", "")) > 200:
            return "Verified (page fetched by agent)"
        return f"Fetch failed ({c.get('status') or c.get('error')})"
    return "Cited (not fetched by agent)"


def coarse_access(v):
    if not v:
        return None
    return "self-serve" if v.startswith("Self-serve") else ("unclear" if v == "Unclear" else "gated")


def judge(field: str, pred, truth) -> str:
    if field == "auth_methods":
        p, t = {AUTH_CLASS.get(x, "Other") for x in (pred or [])}, {AUTH_CLASS.get(x, "Other") for x in truth}
        return "correct" if p == t else ("partial" if p & t else "incorrect")
    if field == "api_type":
        p, t = set(pred or []), set(truth)
        return "correct" if p == t else ("partial" if p & t else "incorrect")
    if field == "credential_access":
        if pred == truth:
            return "correct"
        return "partial" if coarse_access(pred) == coarse_access(truth) and coarse_access(truth) != "unclear" else "incorrect"
    return "correct" if pred == truth else "incorrect"


def score(stage: str, preds: dict, truth: list, fields=FIELDS) -> dict:
    per = {f: {"correct": 0, "partial": 0, "incorrect": 0} for f in fields}
    rows, covered = [], 0
    for t in truth:
        p = preds.get(t["id"])
        if p is None:
            continue
        covered += 1
        for f in fields:
            if t.get(f) is None:
                continue
            v = judge(f, p.get(f), t[f])
            per[f][v] += 1
            if v != "correct":
                rows.append({"id": t["id"], "app": t["app_name"], "field": f, "verdict": v,
                             "predicted": p.get(f), "truth": t[f]})
    c = sum(x["correct"] for x in per.values())
    pa = sum(x["partial"] for x in per.values())
    n = c + pa + sum(x["incorrect"] for x in per.values())
    return {"stage": stage, "apps_covered": covered, "claims_scored": n, "correct": c, "partial": pa,
            "incorrect": n - c - pa, "accuracy": round(c / n, 3) if n else None,
            "lenient_accuracy": round((c + pa) / n, 3) if n else None, "per_field": per, "misses": rows}


def run_history() -> dict:
    """Parse logs/adjudication.log for every adjudicator run: apps already done at start, apps
    queued, records at finish and the token usage the Groq client reported. The run with the most
    queued apps is the main run; earlier runs are trials, later runs are retry passes. Usage counts
    successful API responses only (a rejected 400 response reports no usage)."""
    import ast
    import re
    log = config.LOGS / "adjudication.log"
    runs, cur = [], None
    for ln in (log.read_text(encoding="utf-8").splitlines() if log.exists() else []):
        m = re.search(r"^(\S+ \S+) INFO adjudicator: (\d+) done, (\d+) to adjudicate", ln)
        if m:
            cur = {"started": m.group(1)[:19], "done_at_start": int(m.group(2)), "queued": int(m.group(3))}
            runs.append(cur)
            continue
        m = re.search(r"INFO adjudicator: finished: (\d+)/\d+ adjudicated \| usage (\{.*\})", ln)
        if m and cur is not None:
            u = ast.literal_eval(m.group(2))
            cur.update({"records_at_finish": int(m.group(1)), "calls": u.get("calls", 0),
                        "prompt_tokens": u.get("prompt_tokens", 0), "completion_tokens": u.get("completion_tokens", 0)})
    if not runs:
        return {}
    main_i = max(range(len(runs)), key=lambda i: runs[i]["queued"])
    for i, r in enumerate(runs):
        r["kind"] = "trial" if i < main_i else "main" if i == main_i else "retry"
    tot = lambda k: sum(r.get(k, 0) for r in runs)
    return {"runs": runs, "records_after_main_run": runs[main_i].get("records_at_finish"),
            "records_final": runs[-1].get("records_at_finish"),
            "calls": tot("calls"), "prompt_tokens": tot("prompt_tokens"), "completion_tokens": tot("completion_tokens"),
            "total_tokens": tot("prompt_tokens") + tot("completion_tokens"),
            "note": "Usage is summed from the Groq client's own counters in logs/adjudication.log and covers successful responses only; rejected (HTTP 400) generations may have consumed additional unreported tokens."}


def main():
    apps = {a["id"]: a for a in load(config.DATA / "apps.json")}
    p1 = {r["id"]: r for r in load(config.DATA / "research_results_pass1.json")}
    p2 = {r["id"]: r for r in load(config.DATA / "research_results_pass2.json")}
    llm = {r["id"]: r for r in load(config.DATA / "llm_adjudicated_results.json")}
    # Full attempt history per app: failures from earlier runs (data/llm_failed_attempts.jsonl,
    # append-only) followed by the attempts recorded in the saved record. Older failures copied
    # from the log have no model field; it is inferred from the model-switch lines in the log
    # and labelled as inferred. The checkpoint file itself is not modified.
    switches = []
    for ln in (config.LOGS / "adjudication.log").read_text(encoding="utf-8").splitlines():
        if "switching to" in ln and "groq_client" in ln:
            switches.append((ln[:23], ln.split("daily limit on ")[1].split(";")[0], ln.rsplit("switching to ", 1)[1].strip()))
    def infer_model(at):
        cur = None
        for ts, frm, to in switches:
            if ts <= at:
                cur = to
            elif cur is None:
                cur = frm
        return cur
    fa = config.DATA / "llm_failed_attempts.jsonl"
    prior = {}
    for ln in (fa.read_text(encoding="utf-8").splitlines() if fa.exists() else []):
        x = json.loads(ln)
        if x.get("source", "").startswith("logs/"):
            if x.get("model") is None:
                x["model"], x["model_inferred"] = infer_model(x["at"]), True
            prior.setdefault(x["id"], []).append(x)
    for i, r in llm.items():
        hist = [dict(x, run="earlier run") for x in prior.get(i, [])] + [dict(x, run="saving run") for x in r.get("attempts", [])]
        for n, x in enumerate(hist, 1):
            x["attempt"] = n
        r["attempts"], r["retried"] = hist, len(hist) > 1
    ck = {r["id"]: r for r in load(config.DATA / "composio_toolkits.json")}
    gt = load(config.VERIFY / "ground_truth.json")
    truth = gt["apps"]
    (config.DATA / "research_results.json").write_text(json.dumps(list(p2.values()), indent=1), encoding="utf-8")

    final, changes, sources = [], [], set()
    for i in sorted(apps):
        a, r, j = apps[i], p2[i], llm.get(i)
        if j is None:
            continue
        vd = vendor_domains(a)
        ev = []
        for e in j.get("evidence", []):
            host = reg_domain(urlparse(e["url"]).netloc) if e["url"].startswith("http") else ""
            ev.append({"field": e["field"], "claim": e["claim"], "source_url": e["url"],
                       "source_type": "official" if host in vd else ("composio" if e["url"].startswith("composio:") else "third_party"),
                       "verification_status": url_status(e["url"])})
            sources.add(e["url"])
        diff = [{"field": f, "crawler": r.get(f), "groq": j.get(f)} for f in FIELDS if r.get(f) != j.get(f)]
        if diff:
            changes.append({"id": i, "app": a["name"], "changes": diff})
        c = ck.get(i, {})
        final.append({
            "id": i, "app_name": a["name"], "category": a["category"], "website_hint": a["hint"],
            "description": j["description"], "auth_methods": j["auth_methods"], "credential_access": j["credential_access"],
            "api_type": j["api_type"], "api_breadth": j["api_breadth"], "mcp_available": j["mcp_available"],
            "mcp_detail": j["mcp_detail"], "llms_txt": r.get("llms_txt"),
            "buildability_verdict": j["buildability_verdict"], "primary_blocker": j["primary_blocker"] or "None",
            "blocker_category": j["blocker_category"], "evidence": ev, "confidence": j["confidence"],
            "requires_human_review": j["requires_human_review"], "notes": j["notes"],
            "unsupported_citations": j.get("unsupported_citations", []), "fields_without_citation": j.get("fields_without_citation", []),
            "llm_model": j["model"], "tools_called": j.get("tools_called", []),
            "groq_attempts": j.get("attempts", []), "groq_retried": j.get("retried", False),
            "agent_pass2": {f: r.get(f) for f in FIELDS},
            "composio": {"has_toolkit": c.get("composio_toolkit"), "match_confidence": c.get("match_confidence"),
                         "auth": c.get("composio_auth"), "auth_agreement": c.get("auth_agreement"),
                         "toolkit": (c.get("toolkits") or [{}])[0] if c.get("composio_toolkit") else None,
                         "rejected": c.get("rejection_reason")},
            "pages_fetched": len(r["pages"]), "pages_ok": r["pages_ok"],
        })
    # Review corrections: on sampled apps, a settled ground-truth value replaces Groq's
    # answer in the FINAL dataset (logged). Accuracy below is still computed on Groq's
    # uncorrected output, so corrections cannot inflate the reported score.
    sample_ids = {t["id"] for t in truth}
    truth_by_id = {t["id"]: t for t in truth}
    corrections = []
    for f in final:
        f["in_verification_sample"] = f["id"] in sample_ids
        t = truth_by_id.get(f["id"])
        f["review_corrections"] = []
        if not t:
            continue
        for fld in FIELDS:
            if t.get(fld) is not None and judge(fld, f[fld], t[fld]) != "correct":
                c = {"id": f["id"], "app": f["app_name"], "field": fld, "groq": f[fld], "reviewed": t[fld],
                     "evidence": t["evidence_urls"]}
                corrections.append(c)
                f["review_corrections"].append(c)
                f[fld] = t[fld]
                for u in t["evidence_urls"]:
                    f["evidence"].append({"field": fld if fld in ("auth_methods", "api_type", "credential_access", "mcp_available") else "buildability_verdict",
                                          "claim": f"Reviewed value: {t[fld]}", "source_url": u,
                                          "source_type": "official" if u.startswith("http") and reg_domain(urlparse(u).netloc) in vendor_domains(apps[f["id"]]) else "reviewer_check",
                                          "verification_status": url_status(u) if u.startswith("http") else "Reviewer"})
    (config.DATA / "verified_results.json").write_text(json.dumps(final, indent=1), encoding="utf-8")

    ck_preds = {i: {"auth_methods": c["composio_auth"]} for i, c in ck.items() if c.get("composio_toolkit")}
    stages = [score("Pass 1: naive crawler (homepage only)", p1, truth),
              score("Pass 2: deep crawler loop (regex)", p2, truth),
              score("Pass 3: Groq LLM adjudication", llm, truth)]
    composio_auth = score("Composio catalog auth schemes (reference)", ck_preds, truth, fields=["auth_methods"])
    # Per-model scoring. The fallback model took over when gpt-oss-120b hit its daily cap, so the
    # two models saw DIFFERENT apps (120b: lower ids, 20b: higher ids). The split is reported as is,
    # with app counts; it is not a controlled head-to-head comparison.
    by_model = {}
    for m in sorted({r["model"] for r in llm.values()}):
        sub = {i: r for i, r in llm.items() if r["model"] == m}
        s_ = score(f"Groq {m}", sub, truth)
        s_["apps_adjudicated_total"] = len(sub)
        s_["sample_app_ids"] = sorted(t["id"] for t in truth if t["id"] in sub)
        s_["review_flag_rate_all_apps"] = round(sum(1 for r in sub.values() if r["requires_human_review"]) / len(sub), 3)
        s_["insufficient_evidence_rate_all_apps"] = round(sum(1 for r in sub.values() if r["buildability_verdict"] == "Insufficient evidence") / len(sub), 3)
        s_["retried_apps"] = sum(1 for r in sub.values() if r.get("retried"))
        by_model[m] = s_
    unresolved_p = config.DATA / "llm_unresolved.json"
    unresolved = load(unresolved_p) if unresolved_p.exists() else []

    unsupported = sum(len(x["unsupported_citations"]) for x in final)
    report = {
        "applications_total": len(apps), "applications_adjudicated": len(final),
        "applications_with_evidence": sum(1 for x in final if x["evidence"]),
        "applications_with_fetched_official_evidence": sum(1 for x in final if any(
            e["verification_status"].startswith("Verified") and e["source_type"] == "official" for e in x["evidence"])),
        "sample": {"apps": len(truth), "scorable_claims": sum(1 for t in truth for f in FIELDS if t.get(f) is not None),
                   "excluded_claims": sum(1 for t in truth for f in FIELDS if t.get(f) is None),
                   "method": gt["meta"]["method"], "reviewer": gt["meta"]["reviewer"]},
        "scoring_rules": __doc__.split("Scoring rules (stated on the page too):")[1].strip(),
        "stages": stages, "composio_auth_reference": composio_auth,
        "groq_by_model": by_model,
        "run_history": run_history(),
        "failure_history_entries": sum(1 for _ in (config.DATA / "llm_failed_attempts.jsonl").open(encoding="utf-8")) if (config.DATA / "llm_failed_attempts.jsonl").exists() else 0,
        "checkpoint_inspection": json.loads((config.LOGS / "checkpoint_inspection.json").read_text(encoding="utf-8")) if (config.LOGS / "checkpoint_inspection.json").exists() else None,
        "groq_attempts": {"failed_attempts": sum(1 for x in final for t in x["groq_attempts"] if t["status"] == "failed"),
                          "apps_with_failed_attempt": sum(1 for x in final if any(t["status"] == "failed" for t in x["groq_attempts"])),
                          "by_code": {c: sum(1 for x in final for t in x["groq_attempts"] if t.get("code") == c)
                                      for c in sorted({t.get("code") for x in final for t in x["groq_attempts"] if t["status"] == "failed"})}},
        "groq_by_model_caveat": "Models were not assigned at random: gpt-oss-20b only adjudicated apps after gpt-oss-120b hit its daily token cap, so each model's sample apps differ (ids and category mix). Small n per model; treat as indicative.",
        "applications_unresolved": [{"id": u["id"], "app": u["app"], "reason": u["reason"]} for u in unresolved],
        "claims_changed_crawler_to_groq": sum(len(c["changes"]) for c in changes),
        "apps_changed_crawler_to_groq": len(changes),
        "unsupported_citations_dropped": unsupported,
        "review_corrections_applied": len(corrections),
        "review_corrections": corrections,
        "apps_requiring_human_review": sum(1 for x in final if x["requires_human_review"]),
        "pages_fetched_pass2": sum(len(r["pages"]) for r in p2.values()),
        "pages_ok_pass2": sum(r["pages_ok"] for r in p2.values()),
        "distinct_sources_cited": len(sources),
        "models_used": {m: sum(1 for x in final if x["llm_model"] == m) for m in sorted({x["llm_model"] for x in final})},
        "tool_calls": {"total": sum(len(x["tools_called"]) for x in final),
                       "by_tool": {t: sum(1 for x in final for c in x["tools_called"] if c["tool"] == t)
                                   for t in sorted({c["tool"] for x in final for c in x["tools_called"]})},
                       "failed": sum(1 for x in final for c in x["tools_called"] if not c["ok"])},
        "crawler_to_groq_changes": changes,
    }
    (config.VERIFY / "verification_report.json").write_text(json.dumps(report, indent=1, default=str), encoding="utf-8")
    for s in stages + [composio_auth]:
        print(f"{s['stage']}: {s['correct']}/{s['claims_scored']} correct = {s['accuracy']} | +partial {s['lenient_accuracy']} | apps {s['apps_covered']}")
    for m, s_ in by_model.items():
        print(f"  by model {m}: {s_['correct']}/{s_['claims_scored']} = {s_['accuracy']} | +partial {s_['lenient_accuracy']} | sample apps {s_['apps_covered']} | all apps {s_['apps_adjudicated_total']}")
    print("adjudicated:", len(final), "| review:", report["apps_requiring_human_review"], "| unsupported citations dropped:", unsupported)


if __name__ == "__main__":
    main()
