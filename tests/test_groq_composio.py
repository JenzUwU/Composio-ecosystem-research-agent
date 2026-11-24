"""Reproducible integration test: Groq tool calling -> Composio SDK execution -> Groq.

    python -m tests.test_groq_composio

1. Offline: convert real Composio session tool schemas to Groq format and assert shape.
2. Live: ask Groq a question it can only answer by calling a Composio tool, execute the
   requested tool via the Composio session in Python, return the result, and record
   Groq's final answer. Writes logs/groq_composio_integration.json. Fails loudly; never
   fakes a success.
"""
from __future__ import annotations

import json
import logging
import sys
import time

from agent import config
from agent.composio_client import ComposioResearchClient
from agent.composio_tools import READ_ONLY_COMPOSIO_TOOLS, ToolExecutor, convert_composio_tool
from agent.groq_client import GroqLLM


def main() -> int:
    logging.basicConfig(level=logging.WARNING)
    report = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "checks": []}

    def check(name, ok, detail=None):
        report["checks"].append({"check": name, "ok": bool(ok), "detail": detail})
        print(("PASS " if ok else "FAIL ") + name)
        return ok

    cc = ComposioResearchClient()
    session = cc.create_session(["github"])
    raw = session.tools()
    check("composio session.tools() returned tools", len(raw) > 0, [t["function"]["name"] for t in raw])

    # ---- 1. conversion ----
    src = next(t for t in raw if t["function"]["name"] == "COMPOSIO_GET_TOOL_SCHEMAS")
    conv = convert_composio_tool(src)
    fn = conv["function"]
    ok = (conv["type"] == "function" and fn["parameters"]["type"] == "object"
          and "session_id" not in fn["parameters"]["properties"]
          and "tool_slugs" in fn["parameters"]["properties"] and len(fn["description"]) <= 400
          and all(r in fn["parameters"]["properties"] for r in fn["parameters"].get("required", [])))
    check("conversion: Composio schema -> Groq tool schema", ok,
          {"before_chars": len(json.dumps(src)), "after_chars": len(json.dumps(conv)), "params": list(fn["parameters"]["properties"])})
    blocked = [t["function"]["name"] for t in raw if t["function"]["name"] not in READ_ONLY_COMPOSIO_TOOLS]
    check("allowlist excludes write/exec meta tools", "COMPOSIO_REMOTE_BASH_TOOL" in blocked and "COMPOSIO_MANAGE_CONNECTIONS" in blocked, blocked)

    # ---- 2. live round trip ----
    ex = ToolExecutor(cc, allowed_urls=set(), allowed_toolkits={"github"})
    ex.session = session
    tools = ex.groq_tools()
    llm = GroqLLM()
    trace: list = []
    msgs = [{"role": "system", "content": "You are a research assistant. Use the provided tools to get facts; do not guess."},
            {"role": "user", "content": "Using Composio, find which input fields are REQUIRED for the tool GITHUB_GET_A_REPOSITORY. Answer in one sentence."}]
    final, msgs = llm.tool_loop(msgs, tools, ex, max_rounds=3, trace=trace, reasoning_effort="low", max_completion_tokens=1200)
    report["model"] = llm.model
    report["tool_trace"] = trace
    report["final_answer"] = final
    report["usage"] = llm.usage
    called = [t["tool"] for t in trace]
    check("groq requested a tool call", len(trace) > 0, called)
    check("python executed it via Composio and it succeeded", any(t["ok"] for t in trace), [t["result_excerpt"][:160] for t in trace])
    check("groq answer grounded in tool result (mentions owner and repo)", "owner" in final.lower() and "repo" in final.lower(), final)

    out = config.LOGS / "groq_composio_integration.json"
    out.write_text(json.dumps(report, indent=1, default=str), encoding="utf-8")
    print("evidence ->", out)
    return 0 if all(c["ok"] for c in report["checks"]) else 1


if __name__ == "__main__":
    sys.exit(main())
