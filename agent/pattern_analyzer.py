"""Computes every statistic shown on the case-study page directly from
data/verified_results.json (no hand-typed numbers), and writes them to
data/analysis.json and dashboard/data.js.

    python -m agent.pattern_analyzer
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

from . import config

AUTH = ["OAuth2", "API Key", "Personal Access Token", "Basic", "Bearer Token", "Other"]
VERDICTS = ["Ready to build", "Buildable with limitations", "Requires outreach / partnership",
            "Not currently feasible", "Insufficient evidence"]
ACCESS = ["Self-serve (free)", "Self-serve (free trial / sandbox)", "Self-serve (paid plan required)",
          "Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated", "Unclear"]


def pct(n, d):
    return round(100 * n / d) if d else 0


def main():
    rows = json.loads((config.DATA / "verified_results.json").read_text(encoding="utf-8"))
    report = json.loads((config.VERIFY / "verification_report.json").read_text(encoding="utf-8"))
    N = len(rows)
    cats = list(dict.fromkeys(r["category"] for r in rows))

    auth_counts = Counter(m for r in rows for m in r["auth_methods"])
    multi_auth = [r["app_name"] for r in rows if len(r["auth_methods"]) > 1]
    access_counts = Counter(r["credential_access"] for r in rows)
    verdict_counts = Counter(r["buildability_verdict"] for r in rows)
    blocker_counts = Counter()
    for r in rows:
        blocker_counts[r["blocker_category"]] += 1
    mcp_counts = Counter(r["mcp_available"] for r in rows)
    rest = sum("REST" in r["api_type"] for r in rows)
    gql = sum("GraphQL" in r["api_type"] for r in rows)
    no_api = sum(not ({"REST", "GraphQL"} & set(r["api_type"])) for r in rows)
    llms = sum(bool(r["llms_txt"]) for r in rows)
    self_serve = sum(r["credential_access"].startswith("Self-serve") for r in rows)
    self_serve_free = sum(r["credential_access"] in ("Self-serve (free)", "Self-serve (free trial / sandbox)") for r in rows)

    by_cat = []
    for c in cats:
        cr = [r for r in rows if r["category"] == c]
        n = len(cr)
        by_cat.append({
            "category": c, "n": n,
            "oauth": sum("OAuth2" in r["auth_methods"] for r in cr),
            "key_or_token": sum(bool({"API Key", "Personal Access Token", "Basic"} & set(r["auth_methods"])) for r in cr),
            "self_serve": sum(r["credential_access"].startswith("Self-serve") for r in cr),
            "gated": sum(r["credential_access"] in ("Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated") for r in cr),
            "ready": sum(r["buildability_verdict"] == "Ready to build" for r in cr),
            "limited": sum(r["buildability_verdict"] == "Buildable with limitations" for r in cr),
            "outreach": sum(r["buildability_verdict"] == "Requires outreach / partnership" for r in cr),
            "infeasible": sum(r["buildability_verdict"] in ("Not currently feasible", "Insufficient evidence") for r in cr),
            "mcp_official": sum(r["mcp_available"] == "Official" for r in cr),
            "verdicts": {v: [r["app_name"] for r in cr if r["buildability_verdict"] == v] for v in VERDICTS},
        })

    gated_set = ("Admin approval / app review", "Enterprise-only", "Partnership / contact-sales gated")
    easy_wins = [r["app_name"] for r in rows if r["buildability_verdict"] == "Ready to build"
                 and r["credential_access"] in ("Self-serve (free)", "Self-serve (free trial / sandbox)")]
    easy_no_mcp = [r["app_name"] for r in rows if r["buildability_verdict"] == "Ready to build" and r["mcp_available"] != "Official"]
    partnerships = [{"app": r["app_name"], "blocker": r["primary_blocker"]} for r in rows
                    if r["buildability_verdict"] == "Requires outreach / partnership"]
    good_api_hard_access = [r["app_name"] for r in rows if {"REST", "GraphQL"} & set(r["api_type"])
                            and r["credential_access"] in gated_set]
    investigate = [{"app": r["app_name"], "why": r["primary_blocker"]} for r in rows
                   if r["buildability_verdict"] in ("Insufficient evidence", "Not currently feasible")]

    oauth_heavy = sorted(by_cat, key=lambda c: -c["oauth"] / c["n"])
    selfserve_rank = sorted(by_cat, key=lambda c: -c["self_serve"] / c["n"])

    analysis = {
        "n": N,
        "headline": {
            "ready": verdict_counts["Ready to build"],
            "limited": verdict_counts["Buildable with limitations"],
            "outreach": verdict_counts["Requires outreach / partnership"],
            "infeasible": verdict_counts["Not currently feasible"],
            "insufficient": verdict_counts["Insufficient evidence"],
            "self_serve": self_serve, "self_serve_free": self_serve_free,
            "oauth": auth_counts["OAuth2"], "api_key_like": sum(bool({"API Key", "Personal Access Token", "Basic"} & set(r["auth_methods"])) for r in rows),
            "multi_auth": len(multi_auth), "rest": rest, "graphql": gql, "no_api": no_api,
            "mcp_official": mcp_counts["Official"], "mcp_third": mcp_counts["Third-party/community"],
            "mcp_none": mcp_counts["None found"], "llms_txt": llms,
        },
        "auth_counts": {k: auth_counts[k] for k in AUTH},
        "access_counts": {k: access_counts[k] for k in ACCESS},
        "verdict_counts": {k: verdict_counts[k] for k in VERDICTS},
        "blocker_counts": dict(blocker_counts.most_common()),
        "mcp_counts": dict(mcp_counts),
        "by_category": by_cat,
        "oauth_rank": [(c["category"], c["oauth"], c["n"]) for c in oauth_heavy],
        "selfserve_rank": [(c["category"], c["self_serve"], c["n"]) for c in selfserve_rank],
        "multi_auth_apps": multi_auth,
        "easy_wins": easy_wins, "easy_no_official_mcp": easy_no_mcp,
        "partnerships": partnerships, "good_api_hard_access": good_api_hard_access,
        "investigate": investigate,
        "composio": {
            "with_toolkit": sum(1 for r in rows if (r.get("composio") or {}).get("has_toolkit")),
            "without_toolkit": [r["app_name"] for r in rows if not (r.get("composio") or {}).get("has_toolkit")],
            "net_new_buildable": [r["app_name"] for r in rows if not (r.get("composio") or {}).get("has_toolkit")
                                  and r["buildability_verdict"] in ("Ready to build", "Buildable with limitations")],
            "by_category": {c: sum(1 for r in rows if r["category"] == c and (r.get("composio") or {}).get("has_toolkit")) for c in cats},
        },
        "confidence_counts": dict(Counter(r["confidence"] for r in rows)),
    }
    (config.DATA / "analysis.json").write_text(json.dumps(analysis, indent=1), encoding="utf-8")
    slim = [{k: r[k] for k in ("id", "app_name", "category", "description", "auth_methods", "credential_access",
                                "api_type", "api_breadth", "mcp_available", "mcp_detail", "llms_txt", "buildability_verdict",
                                "primary_blocker", "blocker_category", "evidence", "confidence", "requires_human_review",
                                "in_verification_sample", "agent_pass2", "notes", "llm_model", "tools_called",
                                "unsupported_citations")} for r in rows]
    composio = None
    ck, conn = config.DATA / "composio_toolkits.json", config.LOGS / "composio_connectivity.json"
    if ck.exists() and conn.exists():
        ckrows = json.loads(ck.read_text(encoding="utf-8"))
        by_id = {r["id"]: r for r in ckrows}
        for r in slim:
            c = by_id.get(r["id"], {})
            r["composio"] = {"has_toolkit": c.get("composio_toolkit"), "slug": (c.get("toolkits") or [{}])[0].get("slug") if c.get("composio_toolkit") else None,
                             "tools": (c.get("toolkits") or [{}])[0].get("tools_count") if c.get("composio_toolkit") else None,
                             "auth": c.get("composio_auth"), "agreement": c.get("auth_agreement"),
                             "confidence": c.get("match_confidence"), "rejected": c.get("rejection_reason")}
        composio = {"connectivity": json.loads(conn.read_text(encoding="utf-8")),
                    "no_toolkit_ready": [r["app_name"] for r in slim if not r["composio"]["has_toolkit"] and r["buildability_verdict"] in ("Ready to build", "Buildable with limitations")]}
    groq = {}
    for k, f in (("connectivity", "groq_connectivity.json"), ("integration", "groq_composio_integration.json")):
        fp = config.LOGS / f
        if fp.exists():
            d = json.loads(fp.read_text(encoding="utf-8"))
            d.pop("available_models", None)
            groq[k] = d
    payload = {"analysis": analysis, "rows": slim, "verification": report, "composio": composio, "groq": groq}
    (config.DASH / "data.js").write_text("window.DATA = " + json.dumps(payload) + ";\n", encoding="utf-8")
    print(json.dumps(analysis["headline"], indent=1))
    print("blockers:", analysis["blocker_counts"])


if __name__ == "__main__":
    main()
