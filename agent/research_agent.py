"""Per-app research agent.

pass 1 ("naive"): fetch only the website/hint from the brief, no JS rendering,
                  no link discovery, no MCP registry. This is the baseline.
pass 2 ("deep"):  fetch the curated official doc seeds + the hint, render JS-heavy
                  pages, follow up to N auth/getting-started links found on those
                  pages, probe /llms.txt, and query the official MCP registry.

Both passes run the same deterministic extractors (signals.py) so that the
difference in accuracy between them is attributable to the research loop only.
"""
from __future__ import annotations

import logging
import re
from urllib.parse import quote, urlparse

from . import config, signals
from .fetcher import fetch, get_json

log = logging.getLogger("agent")
AUTH_ORDER = list(signals.AUTH_PATTERNS)


def hint_url(hint: str) -> str | None:
    token = hint.split(" ")[0].strip()
    if "." not in token:
        return None
    return token if token.startswith("http") else "https://" + token


def reg_domain(host: str) -> str:
    parts = host.lower().split(":")[0].split(".")
    if len(parts) >= 3 and parts[-2] in ("co", "com") and len(parts[-1]) == 2:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


def vendor_domains(app: dict) -> set[str]:
    doms = set()
    for u in [hint_url(app["hint"]) or ""] + app["seed_urls"]:
        if u:
            d = reg_domain(urlparse(u).netloc)
            if d not in ("github.com", "github.io", "stoplight.io", "readme.io", "redoc.ly", "jina.ai"):
                doms.add(d)
    return doms


def name_tokens(name: str) -> list[str]:
    base = re.sub(r"\(.*?\)", "", name).lower()
    base = base.replace(".com", "").replace(".io", "")
    return [t for t in re.split(r"[^a-z0-9]+", base) if t]


def mcp_registry_lookup(app: dict) -> dict:
    """Query the official MCP registry and classify matches as vendor-published or community."""
    toks = name_tokens(app["name"])
    term = toks[0] if toks else app["name"]
    url = f"{config.MCP_REGISTRY}?search={quote(term)}&limit=60"
    data = get_json(url) or {}
    vdoms = vendor_domains(app)
    joined = "".join(toks)
    matches = []
    for entry in data.get("servers", []):
        s = entry.get("server", {})
        name = s.get("name", "")
        lname = name.lower()
        flat = re.sub(r"[^a-z0-9]", "", lname)
        # all tokens must appear in the server name (word-ish match) to count
        if not all(re.search(rf"(^|[^a-z0-9]){re.escape(t)}", lname) for t in toks) and joined not in flat:
            continue
        ns = lname.split("/")[0]
        rev = ".".join(reversed(ns.split(".")))
        gh_org = ns.split(".")[-1] if ns.startswith("io.github.") else ""
        official = reg_domain(rev) in vdoms or (gh_org and joined in re.sub(r"[^a-z0-9]", "", gh_org))
        matches.append({"name": name, "official_namespace": bool(official),
                        "repo": (s.get("repository") or {}).get("url", "")})
    return {"query_url": url, "matches": matches[:15]}


# Composio catalog cross-check lives in agent/composio_enrich.py (official SDK, verified
# method names). It runs as its own stage so the crawler stays key-free and reproducible.


def _candidate_links(page: dict, vdoms: set[str], seen: set[str]) -> list[str]:
    out = []
    for href, text in page.get("links", []):
        if not href.startswith("http") or href in seen:
            continue
        host = urlparse(href).netloc
        if reg_domain(host) not in vdoms:
            continue
        if signals.DISCOVERY_HINTS.search(urlparse(href).path + " " + text):
            out.append(href)
    # prefer auth-related links first
    out.sort(key=lambda u: 0 if re.search(r"auth|oauth|token|key|credential", u, re.I) else 1)
    return out


def research(app: dict, pass_no: int) -> dict:
    vdoms = vendor_domains(app)
    pages, seen = [], set()

    def visit(url, render):
        if url in seen:
            return None
        seen.add(url)
        p = fetch(url, allow_render=render)
        pages.append(p)
        return p

    h = hint_url(app["hint"])
    if pass_no == 1:
        if h:
            visit(h, render=False)
    else:
        for u in app["seed_urls"]:
            visit(u, render=True)
        if h:
            visit(h, render=True)
        # discovery: follow auth / getting-started links from what we fetched
        queue = []
        for p in list(pages):
            if p.get("ok"):
                queue += _candidate_links(p, vdoms, seen)
        for u in list(dict.fromkeys(queue))[: config.MAX_DISCOVERED_LINKS]:
            visit(u, render=True)
        # agent-readiness probe: llms.txt on the docs origin(s)
        origins = {f"{urlparse(u).scheme}://{urlparse(u).netloc}" for u in app["seed_urls"][:2]}
        for o in sorted(origins):
            visit(o + signals.LLMS_TXT, render=False)

    # ---- aggregate signals with evidence ----
    evidence, auth, api, access_hits, mcp_doc = [], {}, {}, {}, []
    llms_txt = None
    for p in pages:
        if not p.get("ok") or not p.get("text"):
            continue
        if p["url"].endswith(signals.LLMS_TXT):
            t = p["text"].lstrip()
            if len(t) > 200 and (t.startswith("#") or t.count("](") >= 3) and "<html" not in t[:500].lower():
                llms_txt = p["url"]
            continue
        sig = signals.extract(p["text"])
        for k, v in sig["auth"].items():
            auth.setdefault(k, []).append((p["url"], v[0]))
        for k, v in sig["api"].items():
            api.setdefault(k, []).append((p["url"], v[0]))
        for k, v in sig["access"].items():
            access_hits.setdefault(k, []).append((p["url"], v[0]))
        if sig["mcp"]:
            mcp_doc.append((p["url"], sig["mcp"][0]))

    def ev(claim, items, field):
        for url, snip in items[:2]:
            evidence.append({"field": field, "claim": claim, "source_url": url, "snippet": snip[:320],
                             "source_type": "official_docs" if reg_domain(urlparse(url).netloc) in vdoms else "third_party",
                             "verification_status": "Agent-extracted (unreviewed)"})

    # Bearer alone usually describes *how* an OAuth/API token is sent; keep it but
    # only as its own method when nothing more specific was found.
    auth_methods = [k for k in AUTH_ORDER if k in auth]
    if "Bearer Token" in auth_methods and len(auth_methods) > 1:
        auth_methods.remove("Bearer Token")
    for k in auth_methods:
        ev(f"Supports {k}", auth[k], "auth_methods")
    api_type = [k for k in ("REST", "GraphQL") if k in api]
    for k in api_type:
        ev(f"{k} API documented", api[k], "api_type")
    access = signals.classify_access(access_hits)
    for k, items in access_hits.items():
        ev(f"Access signal: {k}", items, "credential_access")

    reg = mcp_registry_lookup(app) if pass_no == 2 else {"query_url": None, "matches": []}
    if any(m["official_namespace"] for m in reg["matches"]) or mcp_doc:
        mcp = "Official"
    elif reg["matches"]:
        mcp = "Third-party/community"
    else:
        mcp = "None found" if pass_no == 2 else "Not checked"
    ev("MCP mentioned in vendor docs", mcp_doc, "mcp_available")
    for m in reg["matches"][:3]:
        evidence.append({"field": "mcp_available", "claim": f"MCP registry entry: {m['name']}",
                         "source_url": reg["query_url"], "snippet": m["repo"],
                         "source_type": "mcp_registry", "verification_status": "Agent-extracted (unreviewed)"})

    pages_ok = sum(1 for p in pages if p.get("ok") and not p["url"].endswith(signals.LLMS_TXT))
    verdict, blocker = signals.heuristic_verdict(auth_methods, api_type, access, pages_ok)
    endpoints_hint = sum(len(re.findall(r"\b(GET|POST|PUT|PATCH|DELETE)\s+/", p.get("text", ""))) for p in pages)
    breadth = "Unknown" if not api_type else ("Broad (many endpoints seen)" if endpoints_hint > 40 else "Not measured")

    desc = ""
    for p in pages:
        if p.get("ok") and p.get("title"):
            desc = p["title"]
            break

    confidence = "Low"
    if pages_ok >= 2 and auth_methods and api_type:
        confidence = "Medium"
    if pages_ok >= 3 and auth_methods and api_type and access != "Unclear":
        confidence = "Medium-High"

    return {
        "id": app["id"], "app_name": app["name"], "category": app["category"],
        "description": desc, "auth_methods": auth_methods, "credential_access": access,
        "api_type": api_type, "api_breadth": breadth, "mcp_available": mcp,
        "mcp_registry": reg, "llms_txt": llms_txt,
        "agent_compatibility": ("llms.txt published" if llms_txt else "No llms.txt found") if pass_no == 2 else "Not checked",
        "buildability_verdict": verdict, "primary_blocker": blocker,
        "pages": [{"url": p["url"], "status": p.get("status"), "ok": p.get("ok"), "via": p.get("via"),
                   "chars": len(p.get("text", "")), "error": p.get("error")} for p in pages],
        "pages_ok": pages_ok, "evidence": evidence, "confidence": confidence,
        "requires_human_review": confidence == "Low" or verdict == "Insufficient evidence",
        "pass": pass_no,
    }
