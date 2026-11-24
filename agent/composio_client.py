"""Thin, defensive wrapper around the official Composio Python SDK (`composio`, v0.34+).

Method names below were verified against the installed SDK with `inspect.signature`
(see logs/composio_sdk_surface.txt), not guessed:

  Composio()                                   reads COMPOSIO_API_KEY from env
  composio.sessions.create(user_id=..., toolkits=[...]) -> ToolRouterSession
  session.session_id / session.tools() / session.search(query=...) / session.toolkits(...)
  session.execute(tool_slug, arguments=...)
  composio.toolkits.get(slug)                  Composio catalog record for one app
  composio.toolkits.list(limit=..., cursor=...)
  composio.tools.get_raw_composio_tools(toolkits=[...], search=..., limit=...)
  composio.tools.execute(slug, arguments, user_id=..., version=..., dangerously_skip_version_check=...)

Nothing here prints or logs the API key.
"""
from __future__ import annotations

import json
import logging
import os
import time
from typing import Any

from . import config

log = logging.getLogger("composio_client")

try:
    from dotenv import load_dotenv
    load_dotenv(config.ROOT / ".env", override=True)  # always pick up a rotated key
except ImportError:  # python-dotenv optional; plain env vars still work
    pass

DEFAULT_USER_ID = os.getenv("COMPOSIO_USER_ID", "app-research-agent")


class ComposioUnavailable(RuntimeError):
    """Raised when the SDK is not installed or no API key is configured."""


def _to_dict(obj: Any) -> Any:
    """Best-effort conversion of SDK (pydantic / dataclass) responses to JSON-safe data."""
    for attr in ("model_dump", "to_dict", "dict"):
        f = getattr(obj, attr, None)
        if callable(f):
            try:
                return f()
            except Exception:
                pass
    if isinstance(obj, (list, tuple)):
        return [_to_dict(o) for o in obj]
    if isinstance(obj, dict):
        return {k: _to_dict(v) for k, v in obj.items()}
    if isinstance(obj, (str, int, float, bool)) or obj is None:
        return obj
    return repr(obj)


class ComposioResearchClient:
    def __init__(self, api_key: str | None = None, user_id: str = DEFAULT_USER_ID):
        key = api_key or os.getenv("COMPOSIO_API_KEY", "")
        if not key:
            raise ComposioUnavailable("COMPOSIO_API_KEY is not set (add it to .env)")
        try:
            from composio import Composio
        except ImportError as e:
            raise ComposioUnavailable("composio SDK not installed: pip install composio python-dotenv") from e
        # allow_tracking is a real SDKConfig option (composio/sdk.py); default off for this project.
        tracking = os.getenv("COMPOSIO_ALLOW_TRACKING", "0") == "1"
        self.composio = Composio(api_key=key, allow_tracking=tracking)
        self.user_id = user_id
        self.session = None

    # ---------- sessions ----------
    def create_session(self, toolkits: list[str] | None = None):
        kwargs = {"user_id": self.user_id}
        if toolkits:
            kwargs["toolkits"] = toolkits
        self.session = self.composio.sessions.create(**kwargs)
        return self.session

    # ---------- discovery ----------
    def toolkit_info(self, slug: str) -> dict | None:
        """Composio's catalog record for one toolkit, or None if Composio has no such toolkit."""
        try:
            return _to_dict(self.composio.toolkits.get(slug))
        except Exception as e:
            msg = str(e)
            if "404" in msg or "not found" in msg.lower() or "NotFound" in type(e).__name__:
                return None
            raise

    def list_toolkits(self, limit: int = 1000, max_pages: int = 20) -> list[dict]:
        out, cursor = [], None
        for _ in range(max_pages):
            resp = self.composio.toolkits.list(limit=limit, cursor=cursor) if cursor else self.composio.toolkits.list(limit=limit)
            d = _to_dict(resp)
            items = d.get("items", []) if isinstance(d, dict) else d
            out += items
            cursor = d.get("next_cursor") if isinstance(d, dict) else None
            if not cursor or not items:
                break
        return out

    def tools_for_toolkit(self, toolkit: str, limit: int = 50, search: str | None = None) -> list[dict]:
        kw = {"toolkits": [toolkit], "limit": limit}
        if search:
            kw["search"] = search
        return _to_dict(self.composio.tools.get_raw_composio_tools(**kw))

    def session_search(self, query: str) -> Any:
        if self.session is None:
            self.create_session()
        return _to_dict(self.session.search(query=query))

    # ---------- execution ----------
    def execute(self, slug: str, arguments: dict, version: str | None = None) -> dict:
        """Direct tool execution. Without a pinned version the SDK requires an explicit opt-in."""
        kw: dict[str, Any] = {"arguments": arguments, "user_id": self.user_id}
        if version:
            kw["version"] = version
        else:
            kw["dangerously_skip_version_check"] = True
        return _to_dict(self.composio.tools.execute(slug, **kw))

    def session_execute(self, slug: str, arguments: dict) -> dict:
        if self.session is None:
            self.create_session()
        return _to_dict(self.session.execute(slug, arguments=arguments))


def safe_call(fn, *args, retries: int = 2, **kwargs) -> tuple[bool, Any]:
    """Run an SDK call with retries; return (ok, result_or_error_string). Never raises."""
    last = None
    for attempt in range(retries + 1):
        try:
            return True, fn(*args, **kwargs)
        except ComposioUnavailable as e:
            return False, str(e)
        except Exception as e:  # network / API errors
            last = f"{type(e).__name__}: {str(e)[:400]}"
            status = getattr(e, "status_code", None) or getattr(getattr(e, "response", None), "status_code", None)
            if status in (400, 401, 403, 404, 422):  # permanent: retrying cannot help
                log.warning("composio call failed (HTTP %s, not retried): %s", status, last)
                return False, last
            log.warning("composio call failed (attempt %s): %s", attempt + 1, last)
            time.sleep(1.5 * (attempt + 1))
    return False, last


def connectivity_test(path=None) -> dict:
    """Safe, read-only check: init -> catalog read -> session -> tool discovery. Writes evidence JSON."""
    path = path or (config.LOGS / "composio_connectivity.json")
    report: dict[str, Any] = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "steps": [],
                              "telemetry_enabled": os.getenv("COMPOSIO_ALLOW_TRACKING", "0") == "1", "http": []}

    class _HttpCapture(logging.Handler):  # record real HTTP status lines from the SDK's httpx client
        def emit(self, rec):
            m = rec.getMessage()
            if m.startswith("HTTP Request:"):
                report["http"].append(m.replace("HTTP Request: ", ""))
    _cap = _HttpCapture()
    logging.getLogger("httpx").addHandler(_cap)
    logging.getLogger("httpx").setLevel(logging.INFO)

    def step(name, ok, detail):
        report["steps"].append({"step": name, "ok": ok, "detail": detail})
        log.info("%s: %s", name, "OK" if ok else f"FAILED {detail}")
        return ok

    try:
        import composio
        report["sdk_version"] = getattr(composio, "__version__", None)
    except ImportError:
        report["sdk_version"] = None
    ok, client = safe_call(ComposioResearchClient)
    if not step("init_client", ok, None if ok else client):
        path.write_text(json.dumps(report, indent=1), encoding="utf-8")
        return report
    ok, tk = safe_call(client.toolkit_info, "github")
    step("toolkits.get('github')", ok, {"slug": (tk or {}).get("slug"), "name": (tk or {}).get("name")} if ok and tk else tk)
    ok, sess = safe_call(client.create_session, ["github"])
    step("sessions.create", ok, {"session_id": getattr(sess, "session_id", None)} if ok else sess)
    ok, tools = safe_call(client.tools_for_toolkit, "github", 5)
    step("tools.get_raw_composio_tools(github)", ok, [t.get("slug") for t in tools] if ok else tools)
    if sess is not None and getattr(sess, "session_id", None):
        ok, st = safe_call(sess.tools)
        names = [getattr(t, "name", None) or (t.get("name") if isinstance(t, dict) else repr(t)[:80]) for t in st] if ok else st
        step("session.tools()", ok, names)
        if ok:
            report["session_tools"] = names
        # Read-only execution: a Composio meta tool that returns tool schemas. It touches no
        # external app and needs no connected account. App tools (GITHUB_* etc.) are NOT run.
        args = {"tool_slugs": ["GITHUB_GET_A_REPOSITORY"]}
        n_http = len(report["http"])
        ok, res = safe_call(client.session_execute, "COMPOSIO_GET_TOOL_SCHEMAS", args) if client.session is sess else safe_call(sess.execute, "COMPOSIO_GET_TOOL_SCHEMAS", arguments=args)
        res_d = _to_dict(res) if ok else res
        step("session.execute(COMPOSIO_GET_TOOL_SCHEMAS)", ok and isinstance(res_d, dict) and (res_d.get("error") in (None, "")),
             None if ok else res)
        if ok:
            report["tool_execution"] = {"timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                                        "tool": "COMPOSIO_GET_TOOL_SCHEMAS", "arguments": args,
                                        "why_safe": "read-only Composio metadata; touches no external app; no connected account needed",
                                        "http": report["http"][n_http:], "response_excerpt": json.dumps(res_d, default=str)[:1500]}
            # Real connection state of the GitHub toolkit for this user (read-only query).
            okc, tks = safe_call(sess.toolkits, toolkits=["github"])
            item = (getattr(tks, "items", None) or [None])[0] if okc else None
            conn = getattr(item, "connection", None)
            report["tool_execution"]["github_connection"] = {
                "is_no_auth": getattr(item, "is_no_auth", None), "is_active": getattr(conn, "is_active", None),
                "note": "All GITHUB_* tools need a connected GitHub account; none is connected (connecting needs the account owner's approval), so no app tool was executed."
                if not getattr(conn, "is_active", False) else "A GitHub account is connected, but this test still runs no app tool."}
    logging.getLogger("httpx").removeHandler(_cap)
    # Keep keys written by other steps (catalog_cross_check, limitations, ...) instead of erasing them.
    prev = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    prev.update(report)
    path.write_text(json.dumps(prev, indent=1, default=str), encoding="utf-8")
    return prev


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    print(json.dumps(connectivity_test(), indent=1, default=str))
