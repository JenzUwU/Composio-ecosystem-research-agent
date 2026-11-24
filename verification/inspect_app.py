"""Reviewer helper: grep the cached text of every page the agent fetched for an app.

    python verification/inspect_app.py 3 "oauth|api token|basic"

Used during manual verification to re-read the exact official pages behind a claim.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from agent.fetcher import _cache_path  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
app_id, pattern = int(sys.argv[1]), sys.argv[2]
width = int(sys.argv[3]) if len(sys.argv) > 3 else 140
res = {r["id"]: r for r in json.loads((ROOT / "data/research_results_pass2.json").read_text(encoding="utf-8"))}[app_id]
print(f"== {res['app_name']}")
seen = set()
maxper = int(sys.argv[4]) if len(sys.argv) > 4 else 3
for p in res["pages"]:
    cp = _cache_path(p["url"])
    if not cp.exists():
        continue
    text = json.loads(cp.read_text(encoding="utf-8")).get("text", "")
    hits = list(re.finditer(pattern, text, re.I))
    out = []
    for m in hits:
        key = text[max(0, m.start() - 40): m.end() + 40]
        if key in seen:
            continue
        seen.add(key)
        out.append(re.sub(r"\s+", " ", text[max(0, m.start() - width): m.end() + width]))
        if len(out) >= maxper:
            break
    print(f"-- {p['status']} {p['via']} {len(text)}c {p['url']}  hits={len(hits)}")
    for o in out:
        print("   *", o.encode("ascii", "replace").decode())
