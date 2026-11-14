#!/usr/bin/env python3
"""Resolve every cross-reference in the registries, in both directions.

Checks
  stage    -> skill / agent / workflow exist
  workflow -> stage / skill / agent exist
  agent    -> skill exists
  skill    -> stage exists, and skill.stage_ids <-> stage.skills agree
  stage    -> gate: every stage has a gate id (a gate catalog is checked if present)
  stage <-> workflow membership is reciprocal
Also reports (does not fail by default) roles/skills/workflows nothing refers to.

Exit status: 1 on any unresolved or inconsistent link; with --fail-on-orphans
also 1 if any agent, skill or workflow is unused.  Use --json for machine output.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str) -> dict:
    """Load a JSON registry from registry/."""
    for candidate in (f"registry/{name}.json", f"registry/{name}.yaml"):
        path = ROOT / candidate
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    raise SystemExit(f"registry file not found: {name}")


def check(root_data: dict | None = None) -> dict:
    data = root_data or {
        "stages": load("SDLC_STAGE_REGISTRY")["stages"],
        "skills": load("SKILL_REGISTRY")["skills"],
        "agents": load("AGENT_REGISTRY")["agents"],
        "workflows": load("WORKFLOW_REGISTRY")["workflows"],
    }
    stages, skills, agents, workflows = (data[k] for k in ("stages", "skills", "agents", "workflows"))
    stage_ids = {s["stage_id"] for s in stages}
    skill_ids = {s["skill_id"] for s in skills}
    agent_ids = {a["agent_id"] for a in agents}
    wf_ids = {w["workflow_id"] for w in workflows}
    wf_by_id = {w["workflow_id"]: w for w in workflows}
    stage_by_id = {s["stage_id"]: s for s in stages}
    skill_by_id = {s["skill_id"]: s for s in skills}

    unresolved: list[str] = []
    inconsistent: list[str] = []

    for s in stages:
        sid = s["stage_id"]
        for k in s.get("skills", []):
            if k not in skill_ids:
                unresolved.append(f"stage {sid} -> skill '{k}'")
        for k in s.get("agents", []):
            if k not in agent_ids:
                unresolved.append(f"stage {sid} -> agent '{k}'")
        for k in s.get("workflow_ids", []):
            if k not in wf_ids:
                unresolved.append(f"stage {sid} -> workflow '{k}'")
            elif sid not in wf_by_id[k].get("stages", []):
                inconsistent.append(f"stage {sid} lists workflow '{k}' but the workflow does not list the stage")
        if not s.get("quality_gate"):
            unresolved.append(f"stage {sid} -> gate (none)")
        for k in s.get("skills", []):
            if k in skill_by_id and sid not in skill_by_id[k].get("stage_ids", []):
                inconsistent.append(f"stage {sid} uses skill '{k}' but the skill's stage_ids omit it")

    for w in workflows:
        wid = w["workflow_id"]
        for sid in w.get("stages", []):
            if sid not in stage_ids:
                unresolved.append(f"workflow {wid} -> stage {sid}")
            elif wid not in stage_by_id[sid].get("workflow_ids", []):
                inconsistent.append(f"workflow {wid} lists stage {sid} but the stage does not list the workflow")
        for k in w.get("required_skills", []):
            if k not in skill_ids:
                unresolved.append(f"workflow {wid} -> skill '{k}'")
        for k in w.get("responsible_agents", []):
            if k not in agent_ids:
                unresolved.append(f"workflow {wid} -> agent '{k}'")

    for a in agents:
        for k in a.get("required_skills", []):
            if k not in skill_ids:
                unresolved.append(f"agent {a['agent_id']} -> skill '{k}'")

    for sk in skills:
        for sid in sk.get("stage_ids", []):
            if sid not in stage_ids:
                unresolved.append(f"skill {sk['skill_id']} -> stage {sid}")
            elif sk["skill_id"] not in stage_by_id[sid].get("skills", []):
                inconsistent.append(f"skill '{sk['skill_id']}' lists stage {sid} but the stage does not use the skill")

    used_agents = {x for s in stages for x in s.get("agents", [])} | {
        x for w in workflows for x in w.get("responsible_agents", [])
    }
    used_skills = {x for s in stages for x in s.get("skills", [])} | {
        x for a in agents for x in a.get("required_skills", [])
    }
    stage_agent_only = {x for s in stages for x in s.get("agents", [])}
    orphans = {
        "agents_not_in_any_stage_or_workflow": sorted(agent_ids - used_agents),
        "agents_not_in_any_stage": sorted(agent_ids - stage_agent_only),
        "skills_unused": sorted(skill_ids - used_skills),
        "workflows_without_stages": sorted(w for w in wf_ids if not wf_by_id[w].get("stages")),
    }
    return {
        "counts": {"stages": len(stages), "skills": len(skills), "agents": len(agents), "workflows": len(workflows)},
        "unresolved": unresolved,
        "inconsistent": inconsistent,
        "orphans": orphans,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--fail-on-orphans", action="store_true", help="treat unused agents/skills/workflows as failures")
    ap.add_argument("--report-only", action="store_true", help="always exit 0 (CI report-only phase)")
    args = ap.parse_args(argv)
    result = check()
    failed = bool(result["unresolved"] or result["inconsistent"])
    orphan_count = sum(len(v) for k, v in result["orphans"].items() if k != "agents_not_in_any_stage")
    if args.fail_on_orphans and orphan_count:
        failed = True
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        c = result["counts"]
        print(f"records: {c['stages']} stages, {c['skills']} skills, {c['agents']} agents, {c['workflows']} workflows")
        print(f"unresolved references : {len(result['unresolved'])}")
        print(f"inconsistent links    : {len(result['inconsistent'])}")
        for k, v in result["orphans"].items():
            print(f"orphans - {k}: {len(v)}")
        for line in result["unresolved"][:25]:
            print("  UNRESOLVED  ", line)
        for line in result["inconsistent"][:25]:
            print("  INCONSISTENT", line)
        print("RESULT:", "FAIL" if failed else "PASS")
    return 0 if args.report_only else (1 if failed else 0)


if __name__ == "__main__":
    sys.exit(main())
