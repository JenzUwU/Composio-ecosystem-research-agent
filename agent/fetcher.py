"""Polite, cached HTTP fetcher with retries, per-host rate limiting and an
optional rendering fallback for JavaScript-heavy documentation sites.

Every fetch result (including failures) is cached on disk, so re-running a pass
never re-hits a site, and the cache doubles as the audit trail for evidence.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import logging
import re
import threading
import time
import urllib.error
import urllib.request
import zlib
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

from . import config

log = logging.getLogger("fetcher")
_host_locks: dict[str, threading.Lock] = {}
_host_last: dict[str, float] = {}
_global_lock = threading.Lock()


class _TextAndLinks(HTMLParser):
    SKIP = {"script", "style", "noscript", "svg", "head"}
    BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "tr", "br", "section", "article", "pre", "td", "th", "dt", "dd"}

    def __init__(self, base: str):
        super().__init__(convert_charrefs=True)
        self.base = base
        self.parts: list[str] = []
        self.links: list[tuple[str, str]] = []
        self._skip = 0
        self._href: str | None = None
        self._anchor: list[str] = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        if tag in self.SKIP:
            self._skip += 1
        if tag in self.BLOCK:
            self.parts.append("\n")
        if tag == "a":
            href = dict(attrs).get("href")
            if href and not href.startswith(("javascript:", "mailto:", "#")):
                self._href = urljoin(self.base, href)
                self._anchor = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        if tag == "a" and self._href:
            self.links.append((self._href.split("#")[0], " ".join(self._anchor).strip()))
            self._href = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._skip:
            return
        self.parts.append(data)
        if self._href is not None:
            self._anchor.append(data.strip())

    def text(self) -> str:
        t = "".join(self.parts)
        t = re.sub(r"[ \t\r\f\v]+", " ", t)
        t = re.sub(r"\n\s*\n+", "\n", t)
        return t.strip()


def _cache_path(url: str):
    return config.CACHE / (hashlib.sha1(url.encode()).hexdigest()[:16] + ".json")


def _polite_wait(host: str):
    with _global_lock:
        lock = _host_locks.setdefault(host, threading.Lock())
    with lock:
        wait = _host_last.get(host, 0) + config.PER_HOST_DELAY - time.time()
        if wait > 0:
            time.sleep(wait)
        _host_last[host] = time.time()


def _raw_get(url: str, accept: str = "text/html,application/xhtml+xml,text/plain,application/json;q=0.9,*/*;q=0.5"):
    req = urllib.request.Request(url, headers={
        "User-Agent": config.USER_AGENT,
        "Accept": accept,
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.8",
    })
    with urllib.request.urlopen(req, timeout=config.TIMEOUT) as r:
        body = r.read(3_000_000)
        enc = r.headers.get("Content-Encoding", "")
        if enc == "gzip":
            body = gzip.decompress(body)
        elif enc == "deflate":
            body = zlib.decompress(body)
        ctype = r.headers.get("Content-Type", "")
        charset = "utf-8"
        m = re.search(r"charset=([\w-]+)", ctype)
        if m:
            charset = m.group(1)
        return r.status, r.geturl(), ctype, body.decode(charset, errors="replace")


def fetch(url: str, allow_render: bool = True) -> dict:
    """Return {url, final_url, status, ok, text, links, title, via, error}. Cached."""
    cp = _cache_path(url)
    if cp.exists():
        cached = json.loads(cp.read_text(encoding="utf-8"))
        # A cached thin page may still be upgraded by the render fallback later.
        if not (allow_render and config.RENDER_FALLBACK and cached.get("via") == "direct"
                and len(cached.get("text", "")) < config.MIN_USEFUL_TEXT):
            return cached

    result = {"url": url, "final_url": url, "status": None, "ok": False, "text": "",
              "links": [], "title": "", "via": "direct", "error": None,
              "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if not cp.exists():
        host = urlparse(url).netloc
        for attempt in range(config.MAX_RETRIES + 1):
            try:
                _polite_wait(host)
                status, final, ctype, body = _raw_get(url)
                result.update(status=status, final_url=final, ok=200 <= status < 300)
                if "html" in ctype or body.lstrip()[:15].lower().startswith(("<!doctype", "<html")):
                    p = _TextAndLinks(final)
                    p.feed(body)
                    result.update(text=p.text(), links=p.links[:800], title=p.title.strip()[:200])
                else:
                    result["text"] = body[:400_000]
                break
            except urllib.error.HTTPError as e:
                result.update(status=e.code, error=f"HTTP {e.code}")
                if e.code in (429, 500, 502, 503, 504) and attempt < config.MAX_RETRIES:
                    time.sleep(2 * (attempt + 1))
                    continue
                break
            except Exception as e:  # timeouts, DNS, TLS
                result.update(error=f"{type(e).__name__}: {e}"[:300])
                if attempt < config.MAX_RETRIES:
                    time.sleep(1.5 * (attempt + 1))
                    continue
                break
    else:
        result = json.loads(cp.read_text(encoding="utf-8"))

    # Rendering fallback: blocked (403/401/429) or JS-only pages.
    thin = len(result.get("text", "")) < config.MIN_USEFUL_TEXT
    blocked = result.get("status") in (401, 403, 429, None) or result.get("error")
    if allow_render and config.RENDER_FALLBACK and (thin or blocked) and result.get("status") != 404:
        rendered = _render(url)
        if rendered and len(rendered["text"]) > len(result.get("text", "")):
            rendered["direct_status"] = result.get("status")
            result = rendered

    cp.write_text(json.dumps(result), encoding="utf-8")
    return result


_MDLINK = re.compile(r"\[([^\]]{0,120})\]\((https?://[^)\s]+)\)")


def _render(url: str) -> dict | None:
    for attempt in range(config.MAX_RETRIES + 1):
        try:
            _polite_wait("r.jina.ai")
            status, _, _, body = _raw_get(config.RENDER_PREFIX + url, accept="text/plain")
            links = [(u.split("#")[0], t) for t, u in _MDLINK.findall(body)]
            m = re.search(r"^Title:\s*(.+)$", body, re.M)
            title = m.group(1).strip() if m else ""
            ok = 200 <= status < 300 and "Warning: Target URL returned error 404" not in body
            return {"url": url, "final_url": url, "status": status, "ok": ok, "text": body[:400_000],
                    "links": links[:800], "title": title[:200], "via": "render", "error": None,
                    "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < config.MAX_RETRIES:
                time.sleep(6 * (attempt + 1))
                continue
            log.info("render fallback failed %s: HTTP %s", url, e.code)
            return None
        except Exception as e:
            log.info("render fallback failed %s: %s", url, e)
            if attempt < config.MAX_RETRIES:
                time.sleep(2)
                continue
            return None
    return None


def get_json(url: str, headers: dict | None = None) -> dict | None:
    """Uncached-by-HTTP JSON GET, cached on disk by URL (used for registry/API lookups)."""
    cp = _cache_path("json:" + url)
    if cp.exists():
        return json.loads(cp.read_text(encoding="utf-8"))
    req = urllib.request.Request(url, headers={"User-Agent": config.USER_AGENT, "Accept": "application/json", **(headers or {})})
    for attempt in range(config.MAX_RETRIES + 1):
        try:
            _polite_wait(urlparse(url).netloc)
            with urllib.request.urlopen(req, timeout=config.TIMEOUT) as r:
                data = json.loads(r.read().decode("utf-8", errors="replace"))
            cp.write_text(json.dumps(data), encoding="utf-8")
            return data
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < config.MAX_RETRIES:
                time.sleep(3 * (attempt + 1))
                continue
            log.warning("json GET %s -> HTTP %s", url, e.code)
            return None
        except Exception as e:
            if attempt < config.MAX_RETRIES:
                time.sleep(2)
                continue
            log.warning("json GET %s failed: %s", url, e)
            return None
