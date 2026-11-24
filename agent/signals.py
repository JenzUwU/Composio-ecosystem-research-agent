"""Deterministic signal extraction from fetched documentation text.

The agent does NOT decide facts from memory: every signal is a regex hit in a
page that was actually fetched, and each hit is stored with its source URL and a
text snippet so a reviewer can audit it.
"""
from __future__ import annotations

import re

AUTH_PATTERNS = {
    "OAuth2": r"\boauth\s?2(\.0)?\b|\boauth\b|authorization code (grant|flow)|client[_ ]credentials",
    "API Key": r"\bapi[\s_-]?keys?\b|\bx-api-key\b",
    "Basic": r"\bbasic auth(entication)?\b|http basic|authorization: basic",
    "Personal Access Token": r"personal access tokens?|\bPAT\b|private app (access )?tokens?|integration tokens?|api tokens?",
    "Bearer Token": r"\bbearer\b",
    "Other": r"\bhmac\b|request signing|signature[- ]based|\bjwt\b|bot tokens?|service accounts?|key[- ]pair auth",
}

API_PATTERNS = {
    "REST": r"\brest(ful)?\b(\s+api)?|\b(GET|POST|PUT|PATCH|DELETE)\s+/[a-z0-9]|openapi|swagger",
    "GraphQL": r"\bgraphql\b",
    "SDK/CLI": r"\bsdk\b|\bcli\b|npm install|pip install",
    "Webhooks": r"\bwebhooks?\b",
}

ACCESS_PATTERNS = {
    "partner_gated": r"contact (our )?sales|talk to sales|request (api )?access|apply (for|to) (the )?(api|partner|developer)|partner(ship)? program|become a partner|approved partners?|application (review|approval)|by invitation",
    "enterprise": r"enterprise (plan|customers|tier|only|edition)|available (only )?(on|to|for) enterprise|enterprise[- ]only",
    "admin_approval": r"admin(istrator)? (approval|consent|must (approve|enable|install))|app review|requires? (an )?admin|workspace admin",
    "paid_plan": r"paid (plan|subscription|account)|requires? a (paid|pro|premium|business) (plan|subscription|account)|(pro|premium|business|growth) plan (or higher|and above|required)|api (access|add-on) is (available|included) (on|with)",
    "trial": r"free trial|trial account|sandbox (account|environment|org)|developer (sandbox|account|edition|org)|test (mode|account|store)",
    "free": r"free (tier|plan|account|developer account|to sign up)|sign up for free|get started (for )?free|no credit card|free of charge|open[- ]source",
}

MCP_PATTERNS = r"\bmcp\b|model context protocol"
LLMS_TXT = "/llms.txt"

DISCOVERY_HINTS = re.compile(
    r"auth|oauth|api[-_ ]?key|token|credential|getting[-_ ]started|quick[-_ ]?start|introduction|overview|rate[-_ ]limit|access[-_ ]level|developer[-_ ]token|scopes|mcp|graphql|api[-_ ]reference|pricing",
    re.I,
)


def _snip(text: str, m: re.Match, width: int = 150) -> str:
    s = max(0, m.start() - width)
    e = min(len(text), m.end() + width)
    return re.sub(r"\s+", " ", text[s:e]).strip()


def find(text: str, pattern: str, limit: int = 3) -> list[str]:
    out = []
    for m in re.finditer(pattern, text, re.I):
        sn = _snip(text, m)
        if sn not in out:
            out.append(sn)
        if len(out) >= limit:
            break
    return out


def extract(text: str) -> dict:
    """Return {group: {label: [snippets]}} for one page."""
    res = {"auth": {}, "api": {}, "access": {}, "mcp": []}
    for k, p in AUTH_PATTERNS.items():
        hits = find(text, p)
        if hits:
            res["auth"][k] = hits
    for k, p in API_PATTERNS.items():
        hits = find(text, p)
        if hits:
            res["api"][k] = hits
    for k, p in ACCESS_PATTERNS.items():
        hits = find(text, p)
        if hits:
            res["access"][k] = hits
    res["mcp"] = find(text, MCP_PATTERNS)
    return res


ACCESS_ORDER = [  # most restrictive signal wins
    ("partner_gated", "Partnership / contact-sales gated"),
    ("enterprise", "Enterprise-only"),
    ("admin_approval", "Admin approval / app review"),
    ("paid_plan", "Self-serve (paid plan required)"),
    ("trial", "Self-serve (free trial / sandbox)"),
    ("free", "Self-serve (free)"),
]


def classify_access(access_hits: dict) -> str:
    for key, label in ACCESS_ORDER:
        if access_hits.get(key):
            return label
    return "Unclear"


def heuristic_verdict(auth: list, api: list, access: str, pages_ok: int) -> tuple[str, str]:
    if pages_ok == 0:
        return "Insufficient evidence", "No official documentation page could be fetched"
    if not ({"REST", "GraphQL"} & set(api)):
        return "Insufficient evidence", "No REST/GraphQL API signal found in fetched docs"
    if not auth:
        return "Insufficient evidence", "No authentication method found in fetched docs"
    if access in ("Partnership / contact-sales gated", "Enterprise-only"):
        return "Requires outreach / partnership", f"Credential access: {access}"
    if access in ("Admin approval / app review", "Self-serve (paid plan required)"):
        return "Buildable with limitations", f"Credential access: {access}"
    if access == "Unclear":
        return "Buildable with limitations", "Credential access path unclear from docs"
    return "Ready to build", "None found"
