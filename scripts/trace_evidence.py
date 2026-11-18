#!/usr/bin/env python3
"""Check that evidence and handoff records trace back to the registries, and print the traceability matrix.

  python3 scripts/trace_evidence.py records/*.json     check evidence records (gate_id) and handoff records (handoff_id)
  python3 scripts/trace_evidence.py --templates        check the shipped templates (placeholders allowed, shape enforced)
  python3 scripts/trace_evidence.py --matrix           print stage, gate, approver and risk tier for all stages as CSV

The chain it enforces: requirement or decision -> stage -> gate -> evidence record (exact revision) -> approver.
A record that claims PASS must carry real values; an example must say "example": true and never say PASS.
See docs/governance/EVIDENCE_TRACEABILITY.md.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402

STATUSES = {"NOT_STARTED", "IN_PROGRESS", "PASS", "FAIL", "BLOCKED", "INCONCLUSIVE", "NEEDS_HUMAN_APPROVAL", "WAIVED", "ILLUSTRATIVE_ONLY"}


def _placeholder(v) -> bool:
    return isinstance(v, str) and (v.startswith("<") or v.strip() == "")


def _context(root: Path) -> dict:
    data = registry_io.load_all(root)
    return {"stages": {s["stage_id"]: s for s in data["stages"]},
            "agents": {a["agent_id"] for a in data["agents"]},
            "skills": {s["skill_id"] for s in data["skills"]}}


def check_evidence(rec: dict, ctx: dict, template: bool = False) -> list[str]:
    errs = []
    status = rec.get("status")
    if status not in STATUSES:
        errs.append(f"status '{status}' is not one of {sorted(STATUSES)}")
    if rec.get("example") is True and status == "PASS":
        errs.append("an example record must not say PASS")
    if template:
        for k in ("gate_id", "stage_id", "status", "commit_sha", "executed_by", "evidence", "timestamp", "limitations", "approved_by"):
            if k not in rec:
                errs.append(f"template is missing '{k}'")
        return errs
    stage = ctx["stages"].get(rec.get("stage_id"))
    if stage is None:
        return errs + [f"stage_id {rec.get('stage_id')} does not exist"]
    if rec.get("gate_id") != stage["quality_gate"]:
        errs.append(f"gate_id {rec.get('gate_id')} does not match stage {stage['stage_id']}'s gate {stage['quality_gate']}")
    if status == "PASS":
        for k in ("commit_sha", "executed_by", "timestamp"):
            if _placeholder(rec.get(k)):
                errs.append(f"PASS needs a real '{k}'")
        try:
            dt.datetime.fromisoformat(str(rec.get("timestamp")).replace("Z", "+00:00"))
        except ValueError:
            errs.append("PASS needs an ISO 8601 timestamp")
        items = rec.get("evidence") or []
        if not items:
            errs.append("PASS needs at least one evidence item")
        for i, e in enumerate(items):
            if _placeholder(e.get("path")) or _placeholder(e.get("result")):
                errs.append(f"evidence[{i}] has a placeholder path or result")
        if "limitations" not in rec:
            errs.append("PASS must state limitations (an empty list is allowed)")
        if stage["approval_required"]:
            approver = rec.get("approved_by")
            if not approver or _placeholder(approver):
                errs.append(f"stage {stage['stage_id']} needs approval by {stage['approver']}; approved_by is empty")
            elif approver in ctx["agents"]:
                errs.append(f"approved_by '{approver}' is an agent role; approvers must be humans")
            elif approver == rec.get("executed_by"):
                errs.append("the approver must not be the executor")
    return errs


def check_handoff(rec: dict, ctx: dict, schema, template: bool = False) -> list[str]:
    errs = [f"schema: {'/'.join(str(x) for x in e.absolute_path) or '(record)'}: {e.message[:120]}" for e in schema.iter_errors(rec)]
    if errs or template:
        return errs
    for k in ("from_skill", "to_skill"):
        if rec[k] not in ctx["skills"]:
            errs.append(f"{k} '{rec[k]}' is not a skill")
    for sid in rec["stage_ids"]:
        if sid not in ctx["stages"]:
            errs.append(f"stage {sid} does not exist")
    if rec.get("example") is True and rec["gate_status"] == "PASS":
        errs.append("an example record must not say PASS")
    ap = rec["approval"]
    if ap["required"]:
        if not ap["approver"]:
            errs.append("approval is required but no approver is named")
        elif ap["approver"] in ctx["agents"]:
            errs.append(f"approver '{ap['approver']}' is an agent role; approvers must be humans")
        if not ap.get("risk_tier"):
            errs.append("approval is required, so risk_tier must be set")
    if rec["acceptance"]["accepted_by"] is None and rec["gate_status"] == "PASS":
        errs.append("an unacknowledged handoff is BLOCKED, not PASS (see STANDARD_HANDOFF.md)")
    return errs


def check_file(path: Path, ctx: dict, schema, template: bool = False) -> list[str]:
    try:
        rec = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"invalid JSON: {e}"]
    if "handoff_id" in rec:
        return check_handoff(rec, ctx, schema, template)
    if "gate_id" in rec:
        return check_evidence(rec, ctx, template)
    return ["not an evidence record (gate_id) or a handoff record (handoff_id)"]


def matrix(root: Path = ROOT) -> list[list]:
    ctx = _context(root)
    tiers = json.loads((root / "registry/risk-tiers.json").read_text(encoding="utf-8"))["stage_tiers"]
    rows = [["stage_id", "stage_name", "gate_id", "status", "primary_role", "approval_required", "approver", "risk_tier", "validation_commands"]]
    for sid in sorted(ctx["stages"]):
        s = ctx["stages"][sid]
        rows.append([sid, s["stage_name"], s["quality_gate"], s["status"], s["primary_role"], s["approval_required"], s.get("approver") or "",
                     tiers.get(str(sid), "R0-R1" if not s["approval_required"] else "UNSET"), len(s.get("validation_commands") or [])])
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--templates", action="store_true")
    ap.add_argument("--matrix", action="store_true")
    a = ap.parse_args()
    if a.matrix:
        csv.writer(sys.stdout, lineterminator="\n").writerows(matrix())
        return 0
    import jsonschema
    schema = jsonschema.Draft202012Validator(json.loads((ROOT / "registry/schemas/handoff.schema.json").read_text(encoding="utf-8")))
    ctx = _context(ROOT)
    files = [ROOT / "templates/evidence-record.json", ROOT / "templates/handoff-record.json"] if a.templates else [Path(p) for p in a.paths]
    if not files:
        ap.error("give record paths, --templates or --matrix")
    bad = 0
    for p in files:
        errs = check_file(p, ctx, schema, template=a.templates)
        for e in errs:
            print(f"{p}: {e}")
        bad += bool(errs)
    print(f"TRACE CHECK {'FAILED' if bad else 'PASSED'}: {len(files)} record(s), {bad} with problems.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
