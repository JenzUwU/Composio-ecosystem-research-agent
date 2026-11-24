"""Exact schema check for Groq adjudication records, plus a checkpoint inspector.

    python -m agent.schema_check            # inspect data/llm_adjudicated_results.json

A record counts as complete only if:
  - every field of the strict SCHEMA used for the Groq decision call is present, with the
    right type and an allowed enum value, and no field outside the schema is in the
    Groq part of the record;
  - the pipeline metadata is present (id, app_name, model, tools_called, adjudicated_at);
  - a record with no surviving citation makes no positive claim (all-unknown only).
Output: logs/checkpoint_inspection.json (complete / malformed / missing / unresolved).
No dependency on the jsonschema package: the checker implements the subset of JSON Schema
that SCHEMA uses (object, array, string, boolean, enum, required, additionalProperties).
"""
from __future__ import annotations

import json
import time

from . import config
from .llm_adjudicator import OUT, SCHEMA, UNRESOLVED

META = {"id": int, "app_name": str, "category": str, "model": str, "tools_called": list, "adjudicated_at": str}
# keys the pipeline adds after the Groq call (not part of the Groq schema)
PIPELINE_KEYS = set(META) | {"research_notes", "unsupported_citations", "fields_without_citation", "attempts", "retried"}
TYPES = {"object": dict, "array": list, "string": str, "boolean": bool}


def _check(value, schema: dict, path: str, errors: list):
    t = schema.get("type")
    if t and not isinstance(value, TYPES[t]):
        errors.append(f"{path}: expected {t}, got {type(value).__name__}")
        return
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} not in enum")
    if t == "array":
        for i, item in enumerate(value):
            _check(item, schema.get("items", {}), f"{path}[{i}]", errors)
    if t == "object":
        for k in schema.get("required", []):
            if k not in value:
                errors.append(f"{path}.{k}: missing required field")
        props = schema.get("properties", {})
        for k, v in value.items():
            if k in props:
                _check(v, props[k], f"{path}.{k}", errors)


def check_record(r: dict) -> list[str]:
    """Return a list of problems; empty list = valid complete record."""
    errors: list[str] = []
    if not isinstance(r, dict):
        return ["record is not an object"]
    groq_part = {k: v for k, v in r.items() if k not in PIPELINE_KEYS}
    _check(groq_part, SCHEMA, "$", errors)
    extra = set(groq_part) - set(SCHEMA["properties"])
    if extra:
        errors.append(f"$: unexpected fields {sorted(extra)}")
    for k, typ in META.items():
        if not isinstance(r.get(k), typ) or (typ is str and not r.get(k)):
            errors.append(f"$.{k}: missing or wrong type (pipeline metadata)")
    # An empty evidence list is acceptable only for an all-unknown record. Any positive claim
    # (an auth method, an API type, a known access route, a verdict other than "Insufficient
    # evidence") must be backed by at least one surviving citation.
    if isinstance(r.get("evidence"), list) and not r["evidence"]:
        positive = (r.get("auth_methods") or r.get("api_type") or r.get("credential_access") != "Unclear"
                    or r.get("buildability_verdict") != "Insufficient evidence")
        if positive:
            errors.append("$.evidence: empty, but the record makes positive claims")
    return errors


def inspect() -> dict:
    apps = json.loads((config.DATA / "apps.json").read_text(encoding="utf-8"))
    recs = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else []
    unresolved = json.loads(UNRESOLVED.read_text(encoding="utf-8")) if UNRESOLVED.exists() else []
    by_id = {}
    dupes = []
    for r in recs:
        if r.get("id") in by_id:
            dupes.append(r.get("id"))
        by_id[r.get("id")] = r
    complete, malformed = [], []
    for r in recs:
        errs = check_record(r)
        (malformed.append({"id": r.get("id"), "app": r.get("app_name"), "errors": errs}) if errs
         else complete.append(r["id"]))
    missing = [{"id": a["id"], "app": a["name"]} for a in apps if a["id"] not in by_id]
    report = {
        "inspected_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "apps_total": len(apps), "records_in_checkpoint": len(recs),
        "complete_valid": len(complete), "malformed": malformed, "duplicate_ids": dupes,
        "missing_no_record": missing,
        "unresolved_after_retry": [{"id": u["id"], "app": u["app"]} for u in unresolved],
        "complete_ids": sorted(complete),
    }
    (config.LOGS / "checkpoint_inspection.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    return report


if __name__ == "__main__":
    rep = inspect()
    print(f"records {rep['records_in_checkpoint']} | complete+valid {rep['complete_valid']} | "
          f"malformed {len(rep['malformed'])} | duplicates {len(rep['duplicate_ids'])} | missing {len(rep['missing_no_record'])} | "
          f"unresolved {len(rep['unresolved_after_retry'])}")
    for m in rep["malformed"]:
        print("  MALFORMED", m["id"], m["app"], m["errors"][:3])
    for m in rep["missing_no_record"]:
        print("  MISSING", m["id"], m["app"])
