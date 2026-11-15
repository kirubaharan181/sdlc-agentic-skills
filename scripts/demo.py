#!/usr/bin/env python3
"""Print the execution plan the library gives for a workflow: ordered steps, parallel groups, owners, approvals.

Everything printed comes from the registries; nothing is simulated or executed.
    python3 scripts/demo.py [workflow-id]        default: production-release
    python3 scripts/demo.py --list
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io  # noqa: E402


def plan(workflow_id: str) -> str:
    data = registry_io.load_all(ROOT)
    wf = next((w for w in data["workflows"] if w["workflow_id"] == workflow_id), None)
    if wf is None:
        raise SystemExit(f"unknown workflow '{workflow_id}'; try --list")
    stages = {s["stage_id"]: s for s in data["stages"]}
    names = {a["agent_id"]: a["name"] for a in data["agents"]}
    out = [f"Workflow: {wf['workflow_id']}", f"Trigger: {wf['trigger']}", ""]
    out.append("Entry criteria:")
    out += [f"  - {x}" for x in wf["entry_criteria"]]
    out.append("")
    levels: dict[int, list[dict]] = {}
    for s in wf["steps"]:
        levels.setdefault(s["level"], []).append(s)
    for lv in sorted(levels):
        group = levels[lv]
        out.append(f"Step group {lv}" + ("  (these can run in parallel)" if len(group) > 1 else ""))
        for s in group:
            st = stages[s["stage"]]
            appr = f"  APPROVAL: {st['approver']}" if st["approval_required"] else ""
            out.append(f"  [{s['stage']:>3}] {st['stage_name']}  owner: {names[s['owner']]}  status: {st['status']}{appr}")
    out.append("")
    if wf["decisions"]:
        out.append("Decisions:")
        out += [f"  - after {d['after']}: {d['question']}  " + ", ".join(f"{k} -> {v}" for k, v in d["branches"].items()) for d in wf["decisions"]]
        out.append("")
    if wf["failure_paths"]:
        out.append("Failure paths:")
        out += [f"  - at {f['at']}: {f['condition']} -> {f['action']} (go to {f['goto']})" for f in wf["failure_paths"]]
        out.append("")
    out.append("Exit criteria:")
    out += [f"  - {x}" for x in wf["exit_criteria"]]
    done = sum(1 for s in wf["steps"] if stages[s["stage"]]["status"] == "complete")
    out.append("")
    n_steps, n_appr, n_left = len(wf["steps"]), len(wf["approval_points"]), len(wf["steps"]) - done
    out.append(f"{n_steps} steps, {n_appr} human approvals, {done} steps with complete stage content, {n_left} still stub.")
    return "\n".join(out) + "\n"


def main(argv: list[str]) -> int:
    if argv[:1] == ["--list"]:
        for w in registry_io.load_workflow_doc(ROOT)["workflows"]:
            print(f"{w['workflow_id']:<38} {len(w['steps']):>3} steps")
        return 0
    sys.stdout.write(plan(argv[0] if argv else "production-release"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
