#!/usr/bin/env python3
"""Scaffold and check a new skill draft without touching the built library (standard library + jsonschema).

  python3 scripts/new_skill.py new my-new-skill        create registry/skill-drafts/my-new-skill.json with TODO placeholders
  python3 scripts/new_skill.py check my-new-skill      schema, no TODO left, trigger-first description, references, overlap warnings
  python3 scripts/new_skill.py checklist my-new-skill  the manual steps that promote a finished draft into the library

A draft is never read by build.py, validate.py or the installer. `check` passing means the draft is well-formed, not that the skill is good:
run SkillEvaluator on the built skill and review its content before promoting it.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402

DRAFTS = ROOT / "registry" / "skill-drafts"
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
T = "TODO: replace this placeholder text"


def scaffold(sid: str, author: str) -> dict:
    return {
        "skill_id": sid, "version": "0.1.0", "author": author,
        "description": "TODO: Use when <trigger>: <what it covers>. Do NOT use for <boundary>.",
        "tags": ["todo"], "keywords": [f"todo-keyword-{i}" for i in range(1, 9)],
        "purpose": T + " (what the skill does and why it is separate from the others, at least 80 characters of real text)",
        "when_to_use": [T, T], "when_not_to_use": [T + " (name the skill to use instead)", T + " (name the skill to use instead)"],
        "prerequisites": [T, T], "inputs": {"required": [T], "optional": []}, "outputs": [T, T],
        "decision_rules": [{"situation": T, "action": T} for _ in range(3)], "quality_gates": [T, T, T],
        "examples": [{"title": T, "request": T, "context": T, "behavior": T, "output": T, "acceptance": T} for _ in range(2)],
        "limitations": [T, T, T], "troubleshooting": [{"error": T, "cause": T, "resolution": T} for _ in range(3)],
        "handoffs": [{"skill": "master-orchestration", "artifact": T}], "owns": ["todo-responsibility"],
    }


def problems(sid: str) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    path = DRAFTS / f"{sid}.json"
    if not path.exists():
        return [f"no draft at {path.relative_to(ROOT)}"], warns
    d = json.loads(path.read_text(encoding="utf-8"))
    try:
        import jsonschema
        schema = json.loads((ROOT / "registry/schemas/skill-content.schema.json").read_text(encoding="utf-8"))
        errs += [f"schema: {'/'.join(map(str, e.path)) or '(root)'}: {e.message[:120]}" for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
    except ImportError:
        warns.append("jsonschema not installed: schema not checked (pip install jsonschema)")
    blob = json.dumps(d)
    if "TODO" in blob or "todo-" in blob or '"todo"' in blob:
        errs.append("placeholders remain (search the draft for TODO / todo-)")
    if d.get("skill_id") != sid or not ID_RE.match(sid):
        errs.append("skill_id must equal the file name and be lowercase kebab-case")
    desc = d.get("description", "")
    if not desc.startswith("Use when") or "Do NOT use" not in desc:
        errs.append('description must start with "Use when" and include "Do NOT use for ..."')
    existing = registry_io.load_skill_content(ROOT)
    if sid in existing:
        errs.append(f"{sid} already exists in registry/skill-content")
    for h in d.get("handoffs", []):
        if h.get("skill") not in existing:
            errs.append(f"handoff to unknown skill: {h.get('skill')}")
    mine = {k.lower() for k in d.get("keywords", [])}
    for other, c in existing.items():
        shared = mine & {k.lower() for k in c["keywords"]}
        if len(shared) >= 3:
            warns.append(f"keyword overlap with {other}: {', '.join(sorted(shared))} (check it is not a duplicate skill)")
    return errs, warns


def checklist(sid: str) -> str:
    return f"""Promoting {sid} into the library (manual; review each step):
 1. Move registry/skill-drafts/{sid}.json to registry/skill-content/{sid}.json and set version to 1.0.0 (or your first release number).
 2. Add an entry to registry/SKILL_REGISTRY.json: skill_id, path skills/<group>/{sid}/SKILL.md, and the stage_ids it covers.
 3. Map the skill into the stages that use it (registry/stage-content/ and registry/stage-defaults.json) and add it to a workflow if needed.
 4. Add its risk tier in registry/risk-tiers.json if it governs risk-tier stages.
 5. Run: python3 scripts/build.py   (generates SKILL.md, references, dist and the selection guide)
 6. Update the skill version lock: see docs/governance/SKILL_VERSIONING.md and scripts/check_skill_versions.py.
 7. Update counts that mention 20 skills (tests/test_governance.py, README, dashboard nav) and add a CHANGELOG entry.
 8. Run: make all, then skillevaluator quality-check and tier1 --no-llm on skills/<group>/{sid}/ (see docs/quality/QUALITY_MANAGEMENT.md).
 9. Record the score with scripts/check_quality_regression.py --add (all traceability options) only from a real evaluator run.
10. Open a pull request; do not claim publication eligibility."""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["new", "check", "checklist"])
    ap.add_argument("skill_id")
    ap.add_argument("--author", default="your-name")
    a = ap.parse_args()
    if not ID_RE.match(a.skill_id):
        ap.error("skill id must be lowercase kebab-case, e.g. data-pipeline-review")
    if a.action == "new":
        if a.skill_id in registry_io.load_skill_content(ROOT) or (DRAFTS / f"{a.skill_id}.json").exists():
            sys.exit(f"{a.skill_id} already exists (library or draft)")
        DRAFTS.mkdir(parents=True, exist_ok=True)
        (DRAFTS / f"{a.skill_id}.json").write_text(json.dumps(scaffold(a.skill_id, a.author), indent=2) + "\n", encoding="utf-8")
        print(f"Created registry/skill-drafts/{a.skill_id}.json. Fill every TODO, then: python3 scripts/new_skill.py check {a.skill_id}")
        return 0
    if a.action == "checklist":
        print(checklist(a.skill_id))
        return 0
    errs, warns = problems(a.skill_id)
    for w in warns:
        print("WARNING:", w)
    for e in errs:
        print("ERROR:", e)
    print("DRAFT CHECK FAILED" if errs else "DRAFT CHECK PASSED (well-formed; not a quality judgement)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
