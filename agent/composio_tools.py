"""Bridge: Composio SDK tools  <->  Groq tool calling.

Composio's session.tools() already returns OpenAI-style function definitions
({"type": "function", "function": {name, description, parameters}}), which is the
format Groq's tool-use API documents. The conversion here is therefore explicit and
small, and it is unit-tested (tests/test_groq_composio.py):

  1. keep only allow-listed, READ-ONLY tools (never MANAGE_CONNECTIONS, MULTI_EXECUTE,
     REMOTE_BASH, REMOTE_WORKBENCH: those can create connections or run code);
  2. trim long descriptions (Groq free tier is 8K tokens/min; COMPOSIO_SEARCH_TOOLS alone
     is ~7.4K chars, so it is excluded for budget reasons);
  3. drop the optional `session_id` parameter (the SDK session injects it);
  4. validate the result is a JSON-Schema object Groq accepts.

Tools offered to Groq:
  - COMPOSIO_GET_TOOL_SCHEMAS  (Composio meta tool, executed via session.execute)
  - composio_list_toolkit_tools (project tool; runs Composio SDK tools.get_raw_composio_tools)
  - read_fetched_page          (project tool; reads an official page the crawler already fetched)
"""
from __future__ import annotations

import copy
import json
import re
from typing import Any

from .fetcher import _cache_path

READ_ONLY_COMPOSIO_TOOLS = {"COMPOSIO_GET_TOOL_SCHEMAS"}
MAX_DESC = 400


def convert_composio_tool(tool: dict) -> dict:
    """Composio session tool (OpenAI format) -> Groq tool definition."""
    if tool.get("type") != "function" or "function" not in tool:
        raise ValueError(f"unexpected Composio tool shape: {list(tool)}")
    fn = copy.deepcopy(tool["function"])
    params = fn.get("parameters") or {"type": "object", "properties": {}}
    props = params.get("properties", {})
    props.pop("session_id", None)
    if "required" in params:
        params["required"] = [r for r in params["required"] if r in props]
    params.setdefault("type", "object")
    desc = re.sub(r"\s+", " ", fn.get("description", "")).strip()
    return {"type": "function", "function": {
        "name": fn["name"], "description": desc[:MAX_DESC], "parameters": params}}


LOCAL_TOOLS = [
    {"type": "function", "function": {
        "name": "read_fetched_page",
        "description": "Return text snippets around the given keywords from an official documentation page that the crawler already fetched for this app. Only URLs listed in the app context are allowed.",
        "parameters": {"type": "object", "properties": {
            "url": {"type": "string", "description": "One of the fetched page URLs from the context."},
            "keywords": {"type": "array", "items": {"type": "string"}, "description": "1-4 keywords, e.g. 'oauth', 'api key', 'sandbox', 'partner'."}},
            "required": ["url", "keywords"]}}},
    {"type": "function", "function": {
        "name": "composio_list_toolkit_tools",
        "description": "List tools Composio's catalog exposes for a toolkit slug (Composio SDK tools.get_raw_composio_tools). Use to gauge API breadth / what operations exist. Optional search text filters results.",
        "parameters": {"type": "object", "properties": {
            "toolkit": {"type": "string", "description": "Composio toolkit slug from the context, e.g. 'hubspot'."},
            "search": {"type": "string", "description": "Optional filter, e.g. 'list' or 'read'."}},
            "required": ["toolkit"]}}},
]


class ToolExecutor:
    """Executes the tools Groq asks for. Python decides; the LLM only requests."""

    def __init__(self, composio_client, allowed_urls: set[str], allowed_toolkits: set[str]):
        self.cc = composio_client
        self.allowed_urls = allowed_urls
        self.allowed_toolkits = allowed_toolkits
        self.session = None

    def groq_tools(self) -> list[dict]:
        tools = list(LOCAL_TOOLS)
        if self.cc is not None:
            if self.session is None:
                self.session = self.cc.create_session()
            for t in self.session.tools():
                if t["function"]["name"] in READ_ONLY_COMPOSIO_TOOLS:
                    tools.append(convert_composio_tool(t))
        return tools

    def __call__(self, name: str, args: dict) -> Any:
        if name == "read_fetched_page":
            return self._read_page(args.get("url", ""), args.get("keywords") or [])
        if name == "composio_list_toolkit_tools":
            slug = (args.get("toolkit") or "").lower()
            if slug not in self.allowed_toolkits:
                return {"error": f"toolkit '{slug}' is not in this app's Composio catalog record"}
            tools = self.cc.tools_for_toolkit(slug, limit=15, search=args.get("search") or None)
            return {"toolkit": slug, "returned": len(tools),
                    "tools": [{"slug": t.get("slug"), "desc": (t.get("description") or "")[:90]} for t in tools]}
        if name in READ_ONLY_COMPOSIO_TOOLS:
            if self.session is None:
                self.session = self.cc.create_session()
            slugs = [s for s in (args.get("tool_slugs") or []) if isinstance(s, str)][:3]
            res = self.session.execute(name, arguments={"tool_slugs": slugs})
            d = res.model_dump() if hasattr(res, "model_dump") else res
            return json.loads(json.dumps(d, default=str))
        return {"error": f"tool '{name}' is not allowed (read-only allowlist)"}

    def _read_page(self, url: str, keywords: list[str]) -> dict:
        if url not in self.allowed_urls:
            return {"error": "URL not in this app's fetched official pages"}
        cp = _cache_path(url)
        if not cp.exists():
            return {"error": "page not in cache"}
        text = json.loads(cp.read_text(encoding="utf-8")).get("text", "")
        out = []
        for kw in keywords[:4]:
            for m in list(re.finditer(re.escape(kw), text, re.I))[:2]:
                out.append(re.sub(r"\s+", " ", text[max(0, m.start() - 220): m.end() + 220]))
        return {"url": url, "snippets": out[:6] or ["(no match)"]}
