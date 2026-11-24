"""Copy failed Groq attempts recorded only in logs/adjudication.log into the append-only
data/llm_failed_attempts.jsonl, so every failed attempt is kept as structured data.

    python -m agent.failed_attempts_backfill

The first full run predates per-attempt logging; its failures exist only as log lines.
This reads those lines (the log itself is not modified) and appends one JSON line per
failure that is not already in the file. Idempotent: safe to run twice.
"""
from __future__ import annotations

import ast
import json
import re

from . import config

LOG = config.LOGS / "adjudication.log"
OUT = config.DATA / "llm_failed_attempts.jsonl"
LINE = re.compile(r"^(\S+ \S+) ERROR adjudicator: \[\s*(\d+)\] (.+?) failed: Error code: (\d+) - (\{.*\})\s*$")


def main():
    seen = set()
    if OUT.exists():
        for ln in OUT.read_text(encoding="utf-8").splitlines():
            r = json.loads(ln)
            seen.add((r["id"], r["at"]))
    added = 0
    with OUT.open("a", encoding="utf-8") as f:
        for ln in LOG.read_text(encoding="utf-8").splitlines():
            m = LINE.match(ln)
            if not m:
                continue
            at, i, name, status, body = m.groups()
            if (int(i), at) in seen:
                continue
            try:
                err = ast.literal_eval(body).get("error", {})
            except Exception:
                err = {"message": body[:600]}
            f.write(json.dumps({"id": int(i), "app": name, "attempt": 1, "phase": "decision", "model": None,
                                "at": at, "status": "failed", "http_status": int(status), "code": err.get("code"),
                                "message": str(err.get("message", ""))[:600],
                                "failed_generation": str(err.get("failed_generation", ""))[:4000],
                                "source": "logs/adjudication.log (first full run, before per-attempt logging)"},
                               ensure_ascii=False) + "\n")
            added += 1
    print(f"backfilled {added} failed attempts into {OUT.name}")


if __name__ == "__main__":
    main()
