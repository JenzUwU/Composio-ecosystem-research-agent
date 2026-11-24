"""Builds a compact, human/LLM-readable evidence digest from pass-2 results.

    python -m agent.digest            -> data/evidence_digest.md
    python -m agent.digest --sample   -> also (re)draws the verification sample

The digest is what the adjudication step (stage 3) reads: per app it lists every
page fetched (status, render path, size), and the top snippet per signal with its
source URL. Adjudication may only cite URLs that appear in this digest or that are
explicitly marked as found by manual search.
"""
from __future__ import annotations

import argparse
import json
import random

from . import config


def draw_sample(apps, per_category=3, seed=42):
    rng = random.Random(seed)
    by_cat = {}
    for a in apps:
        by_cat.setdefault(a["category"], []).append(a["id"])
    sample = []
    for cat in sorted(by_cat):
        sample += sorted(rng.sample(by_cat[cat], per_category))
    return sorted(sample)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", action="store_true")
    args = ap.parse_args()
    apps = json.loads((config.DATA / "apps.json").read_text(encoding="utf-8"))
    if args.sample:
        ids = draw_sample(apps)
        (config.VERIFY / "verification_sample.json").write_text(json.dumps({
            "method": "random.Random(42): 3 apps drawn per category before adjudication",
            "app_ids": ids,
            "apps": [a["name"] for a in apps if a["id"] in ids],
        }, indent=1), encoding="utf-8")
        print("sample:", ids)

    res = json.loads((config.DATA / "research_results_pass2.json").read_text(encoding="utf-8"))
    lines = []
    for r in res:
        lines.append(f"\n## [{r['id']}] {r['app_name']} — {r['category']}")
        lines.append(f"heuristic: auth={r['auth_methods']} api={r['api_type']} access={r['credential_access']} "
                     f"mcp={r['mcp_available']} verdict={r['buildability_verdict']} llms_txt={bool(r['llms_txt'])}")
        for p in r["pages"]:
            lines.append(f"  page {p['status']} {p['via']} {p['chars']}c {p['url']}" + (f" ERR {p['error']}" if p.get('error') else ""))
        for e in r["evidence"]:
            lines.append(f"  - {e['field']} | {e['claim']} | {e['source_url']}\n      “{e['snippet'][:260]}”")
    out = config.DATA / "evidence_digest.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print("wrote", out, len(lines), "lines")


if __name__ == "__main__":
    main()
