"""Orchestrates the research agent over all 100 apps in checkpointed batches.

    python -m agent.orchestrator --pass 1          # naive baseline
    python -m agent.orchestrator --pass 2          # deep research loop
    python -m agent.orchestrator --pass 2 --only 21,61,81
    python -m agent.orchestrator --composio   # Composio SDK catalog cross-check (needs COMPOSIO_API_KEY)

Results are written after every batch to data/research_results_pass{N}.json and
progress to data/research_progress.json, so an interruption loses at most one batch.
"""
from __future__ import annotations

import argparse
import json
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from . import config
from .research_agent import research


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        handlers=[logging.FileHandler(config.LOGS / "research.log", encoding="utf-8"), logging.StreamHandler()],
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pass", dest="pass_no", type=int, choices=[1, 2], default=2)
    ap.add_argument("--only", help="comma-separated app ids")
    ap.add_argument("--workers", type=int, default=config.WORKERS)
    ap.add_argument("--batch-size", type=int, default=config.BATCH_SIZE)
    ap.add_argument("--composio", action="store_true", help="run the Composio catalog cross-check stage only")
    ap.add_argument("--refresh-catalog", action="store_true")
    args = ap.parse_args()
    setup_logging()
    if args.composio:
        import sys
        from . import composio_enrich
        sys.argv = ["composio_enrich"] + (["--refresh"] if args.refresh_catalog else [])
        composio_enrich.main()
        return
    log = logging.getLogger("orchestrator")

    apps = json.loads((config.DATA / "apps.json").read_text(encoding="utf-8"))
    if args.only:
        ids = {int(x) for x in args.only.split(",")}
        apps = [a for a in apps if a["id"] in ids]

    out_path = config.DATA / f"research_results_pass{args.pass_no}.json"
    results = {}
    if out_path.exists():
        results = {r["id"]: r for r in json.loads(out_path.read_text(encoding="utf-8"))}
    progress_path = config.DATA / "research_progress.json"
    progress = json.loads(progress_path.read_text(encoding="utf-8")) if progress_path.exists() else {}

    batches = [apps[i:i + args.batch_size] for i in range(0, len(apps), args.batch_size)]
    t0 = time.time()
    for bi, batch in enumerate(batches, 1):
        log.info("pass %s batch %s/%s: apps %s-%s", args.pass_no, bi, len(batches), batch[0]["id"], batch[-1]["id"])
        failures = []
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futs = {pool.submit(research, a, args.pass_no): a for a in batch}
            for f in as_completed(futs):
                a = futs[f]
                try:
                    r = f.result()
                    results[a["id"]] = r
                    log.info("  [%3d] %-28s pages_ok=%d auth=%s api=%s access=%s mcp=%s verdict=%s",
                             a["id"], a["name"], r["pages_ok"], r["auth_methods"], r["api_type"],
                             r["credential_access"], r["mcp_available"], r["buildability_verdict"])
                except Exception as e:  # one app never kills the batch
                    failures.append(a["id"])
                    log.exception("  [%3d] %s FAILED: %s", a["id"], a["name"], e)
        ordered = [results[k] for k in sorted(results)]
        out_path.write_text(json.dumps(ordered, indent=1), encoding="utf-8")
        progress[f"pass{args.pass_no}"] = {
            "batches_done": bi, "batches_total": len(batches), "apps_done": len(results),
            "failures": failures, "elapsed_s": round(time.time() - t0, 1),
            "updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        progress_path.write_text(json.dumps(progress, indent=1), encoding="utf-8")
        log.info("checkpoint saved: %s apps, %s failures", len(results), len(failures))
    log.info("pass %s done in %.0fs", args.pass_no, time.time() - t0)


if __name__ == "__main__":
    main()
