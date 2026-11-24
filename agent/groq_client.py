"""Groq LLM client (official `groq` SDK, v1.7) with rate-limit handling, strict JSON
Schema output and an OpenAI-style tool-calling loop.

Verified against docs (console.groq.com/docs/quickstart, /structured-outputs,
/tool-use/overview) and the installed SDK:
  - Groq(api_key=...) ; client.chat.completions.create(model=, messages=, ...)
  - response_format={"type": "json_schema", "json_schema": {"name", "strict": True, "schema"}}
    strict mode is documented for gpt-oss-20b/120b (and a few others) and requires
    every property in `required` + additionalProperties: false.
  - Structured outputs cannot be combined with tool use in one request, so the
    research loop uses tool calls first, then a separate strict-JSON request.
  - Errors: groq.RateLimitError, groq.APIStatusError, groq.APIConnectionError, ...

Never logs or prints the API key.
"""
from __future__ import annotations

import json
import logging
import os
import time
from typing import Any, Callable

from . import config

log = logging.getLogger("groq_client")

try:
    from dotenv import load_dotenv
    load_dotenv(config.ROOT / ".env", override=True)
except ImportError:
    pass

# Preference order; the first one present in client.models.list() is used.
PREFERRED_MODELS = ["openai/gpt-oss-120b", "openai/gpt-oss-20b"]
STRICT_SCHEMA_MODELS = {"openai/gpt-oss-20b", "openai/gpt-oss-120b", "qwen/qwen3.8-27b", "meta-models/muse-spark-open"}


class GroqUnavailable(RuntimeError):
    pass


class GroqLLM:
    def __init__(self, model: str | None = None, max_retries: int = 5):
        key = os.getenv("GROQ_API_KEY", "")
        if not key:
            raise GroqUnavailable("GROQ_API_KEY is not set (add it to .env)")
        from groq import Groq
        # SDK has its own retries; we handle 429 ourselves to respect retry-after.
        self.client = Groq(api_key=key, max_retries=0, timeout=120)
        self.max_retries = max_retries
        self.model = model or os.getenv("GROQ_MODEL") or None
        self.usage = {"calls": 0, "prompt_tokens": 0, "completion_tokens": 0}
        self.tpm = int(os.getenv("GROQ_TPM", "8000"))      # free-tier tokens/minute (x-ratelimit-limit-tokens)
        self._window: list[tuple[float, int]] = []         # (time, tokens) of recent calls
        self.fallbacks = [m for m in os.getenv("GROQ_FALLBACK_MODELS", "openai/gpt-oss-20b,qwen/qwen3.8-27b").split(",") if m]
        self.exhausted: set[str] = set()

    def _throttle(self, est: int):
        while True:
            now = time.time()
            self._window = [(t, n) for t, n in self._window if now - t < 60]
            used = sum(n for _, n in self._window)
            if used + est <= int(self.tpm * 0.9) or not self._window:
                return
            time.sleep(max(1.0, 60 - (now - self._window[0][0]) + 0.5))

    # ---------- models ----------
    def list_models(self) -> list[str]:
        return sorted(m.id for m in self.client.models.list().data)

    def pick_model(self) -> str:
        if self.model:
            return self.model
        available = set(self.list_models())
        for m in PREFERRED_MODELS:
            if m in available:
                self.model = m
                return m
        raise GroqUnavailable(f"none of {PREFERRED_MODELS} available; got {sorted(available)[:20]}")

    # ---------- core call with rate-limit handling ----------
    def chat(self, messages: list[dict], **kw) -> Any:
        import groq
        model = kw.pop("model", None) or self.pick_model()
        est = int(len(json.dumps(messages, default=str)) / 3.2) + int(kw.get("max_completion_tokens") or 1000)
        if kw.get("tools"):
            est += int(len(json.dumps(kw["tools"])) / 3.2)
        for attempt in range(self.max_retries + 1):
            self._throttle(est)
            try:
                resp = self.client.chat.completions.create(model=model, messages=messages, **kw)
                self.usage["calls"] += 1
                total = (resp.usage.total_tokens or est) if resp.usage else est
                self._window.append((time.time(), total))
                if resp.usage:
                    self.usage["prompt_tokens"] += resp.usage.prompt_tokens or 0
                    self.usage["completion_tokens"] += resp.usage.completion_tokens or 0
                resp.model_used = model
                return resp
            except groq.RateLimitError as e:
                ra = e.response.headers.get("retry-after") if getattr(e, "response", None) else None
                wait = float(ra) if ra and ra.replace(".", "", 1).isdigit() else min(60, 5 * 2 ** attempt)
                if wait > 120 or "per day" in str(e).lower() or "TPD" in str(e):
                    # daily cap for this model: switch to the next documented strict-schema model
                    self.exhausted.add(model)
                    nxt = next((m for m in self.fallbacks if m not in self.exhausted), None)
                    if not nxt:
                        raise RuntimeError(f"all models exhausted for today: {sorted(self.exhausted)}") from e
                    log.warning("daily limit on %s; switching to %s", model, nxt)
                    model = self.model = nxt
                    continue
                log.warning("rate limited; sleeping %.1fs (attempt %s)", wait, attempt + 1)
                self._window.append((time.time(), self.tpm))  # treat window as full
                time.sleep(wait)
            except (groq.APIConnectionError, groq.APITimeoutError, groq.InternalServerError) as e:
                log.warning("transient groq error %s; retrying", type(e).__name__)
                time.sleep(3 * (attempt + 1))
        raise RuntimeError(f"groq call failed after {self.max_retries + 1} attempts")

    # ---------- structured output ----------
    def structured(self, messages: list[dict], schema: dict, name: str = "result", **kw) -> dict:
        model = kw.pop("model", None) or self.pick_model()
        if model in STRICT_SCHEMA_MODELS:
            rf = {"type": "json_schema", "json_schema": {"name": name, "strict": True, "schema": schema}}
        else:  # documented fallback for other models: JSON object mode (syntax only)
            rf = {"type": "json_object"}
        resp = self.chat(messages, model=model, response_format=rf, **kw)
        out = json.loads(resp.choices[0].message.content)
        self.last_model = getattr(resp, "model_used", model)
        return out

    # ---------- tool-calling loop ----------
    def tool_loop(self, messages: list[dict], tools: list[dict], execute: Callable[[str, dict], Any],
                  max_rounds: int = 4, trace: list | None = None, **kw) -> tuple[str, list[dict]]:
        """Run Groq with tools until it answers without tool calls.
        `execute(name, args)` is called by Python for every requested tool; its result is
        sent back as a role=tool message. Returns (final_text, messages)."""
        trace = trace if trace is not None else []
        for _ in range(max_rounds):
            resp = self.chat(messages, tools=tools, **kw)
            msg = resp.choices[0].message
            calls = msg.tool_calls or []
            entry = {"role": "assistant", "content": msg.content or ""}
            if calls:
                entry["tool_calls"] = [{"id": c.id, "type": "function",
                                        "function": {"name": c.function.name, "arguments": c.function.arguments}} for c in calls]
            messages.append(entry)
            if not calls:
                return msg.content or "", messages
            for c in calls:
                try:
                    args = json.loads(c.function.arguments or "{}")
                except json.JSONDecodeError:
                    args = {}
                t0 = time.time()
                try:
                    result = execute(c.function.name, args)
                    ok = True
                except Exception as e:  # tool errors go back to the model, not up the stack
                    result, ok = {"error": f"{type(e).__name__}: {str(e)[:300]}"}, False
                content = json.dumps(result, default=str)[:6000]
                trace.append({"tool": c.function.name, "arguments": args, "ok": ok,
                              "ms": int(1000 * (time.time() - t0)), "result_excerpt": content[:400]})
                messages.append({"role": "tool", "tool_call_id": c.id, "name": c.function.name, "content": content})
        return "", messages


TEST_SCHEMA = {
    "type": "object",
    "properties": {
        "app": {"type": "string"},
        "auth_methods": {"type": "array", "items": {"type": "string", "enum": ["OAuth2", "API Key", "Basic", "Personal Access Token", "Bearer Token", "Other"]}},
        "confidence": {"type": "string", "enum": ["High", "Medium", "Low"]},
    },
    "required": ["app", "auth_methods", "confidence"],
    "additionalProperties": False,
}


def connectivity_test() -> dict:
    out: dict[str, Any] = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "steps": []}
    try:
        import groq
        out["sdk_version"] = groq.__version__
    except ImportError:
        out["sdk_version"] = None

    def step(name, ok, detail=None):
        out["steps"].append({"step": name, "ok": ok, "detail": detail})
        return ok

    try:
        llm = GroqLLM()
        step("init_client", True)
    except Exception as e:
        step("init_client", False, f"{type(e).__name__}: {e}")
        return out
    try:
        models = llm.list_models()
        out["available_models"] = models
        step("models.list", True, f"{len(models)} models")
        model = llm.pick_model()
        out["selected_model"] = model
        out["strict_json_schema_documented"] = model in STRICT_SCHEMA_MODELS
        step("select_model", True, model)
    except Exception as e:
        step("models.list", False, f"{type(e).__name__}: {str(e)[:300]}")
        return out
    try:
        r = llm.chat([{"role": "user", "content": "Reply with exactly: pong"}], max_completion_tokens=200)
        step("chat.completions.create", True, (r.choices[0].message.content or "").strip()[:80])
    except Exception as e:
        step("chat.completions.create", False, f"{type(e).__name__}: {str(e)[:300]}")
    snippet = ("Authenticate with OAuth 2.0 for public apps. For scripts, create an API key "
               "in Settings and pass it in the X-Api-Key header.")
    try:
        j = llm.structured([{"role": "system", "content": "Extract only what the text states."},
                            {"role": "user", "content": f"App: DemoApp. Docs text: {snippet}"}],
                           TEST_SCHEMA, name="auth_probe", max_completion_tokens=800)
        valid = set(j) == {"app", "auth_methods", "confidence"}
        out["structured_output_supported"] = valid
        step("structured_output(json_schema strict)", valid, j)
    except Exception as e:
        out["structured_output_supported"] = False
        step("structured_output(json_schema strict)", False, f"{type(e).__name__}: {str(e)[:300]}")
    out["usage"] = llm.usage
    return out


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    rep = connectivity_test()
    (config.LOGS / "groq_connectivity.json").write_text(json.dumps(rep, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: v for k, v in rep.items() if k != "available_models"}, indent=1, default=str))
    print("models available:", len(rep.get("available_models", [])))
