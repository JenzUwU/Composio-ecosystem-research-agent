"""Composio catalog cross-check for the 100 apps (secondary evidence, never primary).

    python -m agent.composio_enrich            # uses cached catalog if present
    python -m agent.composio_enrich --refresh  # re-pulls the catalog via the SDK

For each app it records whether Composio already ships a toolkit, which auth schemes
Composio's catalog lists, its tool count, and how that compares with the auth methods
our crawler found in the vendor's official docs.

Important: a Composio toolkit existing does NOT prove the vendor's API is publicly
accessible to any developer (Composio may hold a partner app or managed credentials).
Official documentation remains the primary evidence; this is a cross-check.

Writes data/composio_toolkits.json. Does not modify any crawler output.
"""
from __future__ import annotations

import argparse
import json
import re
from urllib.parse import urlparse

from . import config
from .research_agent import reg_domain, vendor_domains

RAW = config.DATA / "composio_catalog_raw.json"
OUT = config.DATA / "composio_toolkits.json"

AUTH_MAP = {
    "OAUTH2": "OAuth2", "OAUTH1": "Other", "API_KEY": "API Key", "BEARER_TOKEN": "Bearer Token",
    "BASIC": "Basic", "BASIC_WITH_JWT": "Basic", "NO_AUTH": "None",
}

# Manual aliases where the brief's name differs from Composio's naming. Each is a
# name-normalisation hint only; the match is still verified against the live catalog.
ALIASES = {
    "Lark (Larksuite)": ["lark", "larksuite"], "WhatsApp Business": ["whatsapp"],
    "Meta Ads": ["metaads", "facebookads", "metamarketing"], "LinkedIn Ads": ["linkedinads", "linkedin"],
    "Threads (Meta)": ["threads"], "Magento (Adobe Commerce)": ["magento", "adobecommerce"],
    "Salesforce Commerce Cloud": ["salesforcecommercecloud", "sfcc"], "Amazon Selling Partner": ["amazonsellingpartner", "amazonsp", "amazonsellercentral"],
    "MongoDB Atlas": ["mongodbatlas", "mongodb"], "Monday.com": ["monday", "mondaycom"], "Zoho CRM": ["zohocrm", "zoho"],
    "YouTube Transcript": ["youtubetranscript", "transcriptapi"], "Otter AI": ["otterai", "otter"],
    "Mermaid CLI": ["mermaidcli", "mermaid"], "Paygent Connect": ["paygentconnect", "paygent"],
    "Help Scout": ["helpscout"], "SE Ranking": ["seranking"], "Bright Data": ["brightdata"],
    "Waterfall.io": ["waterfall", "waterfallio"], "systeme.io": ["systemeio", "systeme"],
}


# Review decisions (documented): catalog matches that look right by name/domain but
# are a different product. These apps are treated as having NO Composio toolkit.
REJECTED_MATCHES = {
    "Salesforce Commerce Cloud": "Matched 'salesforce' only via the shared salesforce.com domain; that toolkit covers Sales Cloud, not Commerce Cloud.",
    "YouTube Transcript": "Matched 'youtube_transcript' whose app_url is youtubetranscript.dev; the brief's app is transcriptapi.com, a different vendor.",
    "Mermaid CLI": "Matched 'mermaid_chart_mcp' (Mermaid Chart SaaS); the brief's app is the open-source mermaid-cli tool.",
}


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def map_auth(schemes) -> list[str]:
    out = []
    for s in schemes or []:
        m = AUTH_MAP.get(str(s).upper(), "Other")
        if m not in out:
            out.append(m)
    return out


def load_catalog(refresh: bool) -> list[dict]:
    if RAW.exists() and not refresh:
        return json.loads(RAW.read_text(encoding="utf-8"))
    from .composio_client import ComposioResearchClient
    items = ComposioResearchClient().list_toolkits(limit=1000)
    RAW.write_text(json.dumps(items, default=str), encoding="utf-8")
    return items


def match(app: dict, catalog: list[dict]) -> tuple[list[dict], str]:
    keys = {norm(re.sub(r"\(.*?\)", "", app["name"])), norm(app["name"])} | set(ALIASES.get(app["name"], []))
    by_name = [t for t in catalog if norm(t.get("name")) in keys or norm(t.get("slug")) in keys]
    if by_name:
        return by_name, "name/slug"
    vd = vendor_domains(app)
    by_dom = [t for t in catalog if (t.get("meta") or {}).get("app_url")
              and reg_domain(urlparse(t["meta"]["app_url"]).netloc or "x") in vd]
    if by_dom:
        return by_dom, "vendor domain"
    # MCP-flavoured toolkits (e.g. otter_ai_mcp) share a prefix with the app
    pref = [t for t in catalog if any(norm(t.get("slug")).startswith(k) and len(k) >= 5 for k in keys)]
    return pref, ("slug prefix" if pref else "none")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    catalog = [t for t in load_catalog(args.refresh) if not (t.get("deprecated") or {}).get("is_deprecated")]
    apps = json.loads((config.DATA / "apps.json").read_text(encoding="utf-8"))
    crawl = {r["id"]: r for r in json.loads((config.DATA / "research_results_pass2.json").read_text(encoding="utf-8"))}

    rows = []
    for a in apps:
        found, how = match(a, catalog)
        found = sorted(found, key=lambda t: -float((t.get("meta") or {}).get("tools_count") or 0))
        rejected = REJECTED_MATCHES.get(a["name"])
        if rejected:
            how = "rejected on review"
        primary = found[0] if (found and not rejected) else None
        vd = vendor_domains(a)
        app_url = ((primary or {}).get("meta") or {}).get("app_url") or ""
        domain_ok = bool(app_url) and reg_domain(urlparse(app_url).netloc or "x") in vd
        confidence = ("none" if not primary else
                      "strong" if how == "name/slug" and domain_ok else
                      "medium" if how == "name/slug" or domain_ok else "weak")
        ck_auth = map_auth(primary.get("auth_schemes")) if primary else []
        crawler_auth = crawl[a["id"]]["auth_methods"]
        comparable = [x for x in ck_auth if x not in ("None",)]
        if not primary:
            agreement = "no Composio toolkit"
        elif not crawler_auth:
            agreement = "crawler found no auth"
        elif set(comparable) & set(crawler_auth):
            agreement = "agree" if set(comparable) <= set(crawler_auth) else "partial overlap"
        else:
            agreement = "disagree"
        rows.append({
            "id": a["id"], "app_name": a["name"], "category": a["category"],
            "composio_toolkit": bool(primary), "match_method": how, "match_confidence": confidence,
            "domain_confirmed": domain_ok, "rejection_reason": rejected,
            "toolkits": [{"slug": t.get("slug"), "name": t.get("name"), "type": t.get("toolkit_type"),
                          "auth_schemes": t.get("auth_schemes"), "composio_managed": t.get("composio_managed_auth_schemes"),
                          "no_auth": t.get("no_auth"), "tools_count": (t.get("meta") or {}).get("tools_count"),
                          "app_url": (t.get("meta") or {}).get("app_url")} for t in found[:4]],
            "composio_auth": ck_auth, "crawler_auth": crawler_auth, "auth_agreement": agreement,
            "source": "Composio toolkit catalog via composio SDK toolkits.list()",
        })
    OUT.write_text(json.dumps(rows, indent=1, default=str), encoding="utf-8")

    from collections import Counter
    has = [r for r in rows if r["composio_toolkit"]]
    print(f"catalog size: {len(catalog)} | apps with a Composio toolkit: {len(has)}/100")
    print("match methods:", dict(Counter(r["match_method"] for r in rows)))
    print("match confidence:", dict(Counter(r["match_confidence"] for r in rows)))
    print("medium/weak:", [(r["app_name"], r["toolkits"][0]["app_url"] if r["toolkits"] else None) for r in rows if r["match_confidence"] in ("medium", "weak")])
    print("auth agreement:", dict(Counter(r["auth_agreement"] for r in rows)))
    print("no toolkit:", [r["app_name"] for r in rows if not r["composio_toolkit"]])


if __name__ == "__main__":
    main()
