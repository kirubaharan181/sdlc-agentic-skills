"""Read and write the canonical registries.

Stored registry files are *compact*: a record holds only the fields that differ
from the shared defaults in registry/*-defaults.json (or that cannot be derived).
`load_*` returns fully resolved records; `save_*` strips values that equal the
default or the derivable value, so every fact is stated exactly once.

Resolution rules
  stage     agents, primary_role, supporting_roles  <- derived from `raci`
            approval_required,
            status                                <- stage-defaults.json
            handoff_requirements, dependencies    <- templates in stage-defaults.json,
                                                     filled from the record itself
  agent     non_responsibilities, permissions, dependencies, handoff_rules,
            approval_requirements                 <- role-defaults.json
  workflow  every field is authored in registry/workflows/<id>.json or derived from its steps;
            stage `workflow_ids` are derived from workflow membership (never stored)
An explicit value in a record always wins over the default.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STAGE_FIELDS = ("supporting_roles", "approval_required", "status")
ROLE_FIELDS = ("non_responsibilities", "permissions", "dependencies", "handoff_rules", "approval_requirements")


def _read(root: Path, rel: str) -> dict:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def _write(root: Path, rel: str, obj: dict) -> None:
    (root / rel).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stages
def _derive_stage(rec: dict, d: dict, names: dict[str, str] | None = None) -> dict:
    out = dict(rec)
    raci = out.get("raci")
    if raci:
        out["agents"] = [raci["accountable"], *raci["responsible"]]
        if names:
            out["primary_role"] = names[raci["accountable"]]
            seen: list[str] = []
            for rid in [*raci["responsible"], *raci["consulted"]]:
                if names[rid] not in seen:
                    seen.append(names[rid])
            out["supporting_roles"] = seen
    for f in STAGE_FIELDS:
        out.setdefault(f, copy.deepcopy(d[f]))
    if "handoff_requirements" not in out and out.get("deliverable_artifacts"):
        out["handoff_requirements"] = d["handoff_requirements_template"].format(artifact=out["deliverable_artifacts"][0])
    if "dependencies" not in out:
        out["dependencies"] = [
            t.format(stage_name=out["stage_name"], primary_role=out["primary_role"]) for t in d["dependencies_template"]
        ]
    return out


def _compact_stage(rec: dict, d: dict) -> dict:
    out = dict(rec)
    out.pop("workflow_ids", None)  # derived from registry/workflows/*.json
    if out.get("raci"):  # agents, primary_role, supporting_roles are derived from raci
        for f in ("agents", "primary_role", "supporting_roles"):
            out.pop(f, None)
    for f in STAGE_FIELDS:
        if out.get(f) == d[f]:
            out.pop(f, None)
    derived = _derive_stage({k: v for k, v in rec.items() if k not in ("handoff_requirements", "dependencies")}, d, None)
    for f in ("handoff_requirements", "dependencies"):
        if out.get(f) == derived.get(f):
            out.pop(f, None)
    return out


def load_stage_doc(root: Path = ROOT, with_workflows: bool = True) -> dict:
    doc = _read(root, "registry/SDLC_STAGE_REGISTRY.json")
    d = _read(root, "registry/stage-defaults.json")
    names = {a["agent_id"]: a["name"] for a in _read(root, "registry/AGENT_REGISTRY.json")["agents"]}
    doc["stages"] = [_derive_stage(s, d, names) for s in doc["stages"]]
    if with_workflows:
        membership: dict[int, list[str]] = {}
        for w in load_workflow_sources(root):
            for st in w["steps"]:
                membership.setdefault(st["stage"], []).append(w["workflow_id"])
        for s in doc["stages"]:
            s["workflow_ids"] = membership.get(s["stage_id"], [])
    return doc


def save_stage_doc(doc: dict, root: Path = ROOT) -> None:
    d = _read(root, "registry/stage-defaults.json")
    out = {k: v for k, v in doc.items() if k != "generated_on"}
    out["stages"] = [_compact_stage(s, d) for s in doc["stages"]]
    _write(root, "registry/SDLC_STAGE_REGISTRY.json", out)


# ---------------------------------------------------------------- agents
def load_agent_doc(root: Path = ROOT) -> dict:
    doc = _read(root, "registry/AGENT_REGISTRY.json")
    d = _read(root, "registry/role-defaults.json")
    doc["agents"] = [{**{f: copy.deepcopy(d[f]) for f in ROLE_FIELDS}, **a} for a in doc["agents"]]
    return doc


def save_agent_doc(doc: dict, root: Path = ROOT) -> None:
    d = _read(root, "registry/role-defaults.json")
    out = dict(doc)
    out["agents"] = [{k: v for k, v in a.items() if not (k in ROLE_FIELDS and v == d[k])} for a in doc["agents"]]
    _write(root, "registry/AGENT_REGISTRY.json", out)


# ------------------------------------------------------------- workflows
def load_workflow_sources(root: Path = ROOT) -> list[dict]:
    """Hand-authored workflow definitions: registry/workflows/<id>.json (the only place membership is stated)."""
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((root / "registry" / "workflows").glob("*.json"))]


def _levels(steps: list[dict]) -> dict[int, int]:
    ids = {s["stage"] for s in steps}
    needs = {s["stage"]: [n for n in s["needs"] if n in ids] for s in steps}
    level: dict[int, int] = {}

    def lv(i: int) -> int:
        if i not in level:
            level[i] = 1 + max((lv(n) for n in needs[i]), default=0)
        return level[i]

    for i in ids:
        lv(i)
    return level


def resolve_workflow(src: dict, stages_by_id: dict[int, dict]) -> dict:
    steps = src["steps"]
    level = _levels(steps)
    by_level: dict[int, list[int]] = {}
    for s in steps:
        by_level.setdefault(level[s["stage"]], []).append(s["stage"])
    parallel = [sorted(v) for _, v in sorted(by_level.items()) if len(v) > 1]
    approvals = [
        {"stage": s["stage"], "approver": stages_by_id[s["stage"]]["approver"], "condition": stages_by_id[s["stage"]].get("approval_condition", "always")}
        for s in steps if stages_by_id[s["stage"]].get("approval_required")
    ]
    skills: list[str] = []
    for s in steps:
        for k in stages_by_id[s["stage"]]["skills"]:
            if k not in skills:
                skills.append(k)
    owners: list[str] = []
    for s in steps:
        if s["owner"] not in owners:
            owners.append(s["owner"])
    out = dict(src)
    out["steps"] = [{**s, "level": level[s["stage"]]} for s in steps]
    out["stages"] = [s["stage"] for s in steps]
    out["responsible_agents"] = owners
    out["required_skills"] = skills
    out["approval_points"] = approvals
    out["approval_gates"] = [f"{a['stage']} {stages_by_id[a['stage']]['stage_name']} ({a['approver']}; {a['condition']})" for a in approvals]
    out["parallel_groups"] = parallel
    out["parallel_tasks"] = [f"Stages {', '.join(map(str, g))} can run in parallel." for g in parallel]
    out["dependencies"] = [f"{s['stage']} after {', '.join(map(str, s['needs']))}" for s in steps if s["needs"]]
    out["failure_handling"] = " ".join(f"At {f['at']}: {f['condition']} -> {f['action']}." for f in src["failure_paths"]) or "No stage-specific failure path; halt and escalate per the common failure policy."
    out["completion_criteria"] = " ".join(src["exit_criteria"])
    return out


def load_workflow_doc(root: Path = ROOT) -> dict:
    stages_by_id = {s["stage_id"]: s for s in load_stage_doc(root, with_workflows=False)["stages"]}
    return {"schema_version": "3.0.0", "workflows": [resolve_workflow(w, stages_by_id) for w in load_workflow_sources(root)]}


# ---------------------------------------------------------------- skills
def load_skill_doc(root: Path = ROOT) -> dict:
    return _read(root, "registry/SKILL_REGISTRY.json")


def load_all(root: Path = ROOT) -> dict:
    """Resolved view used by validators, reports and the dashboard."""
    return {
        "stages": load_stage_doc(root)["stages"],
        "skills": load_skill_doc(root)["skills"],
        "agents": load_agent_doc(root)["agents"],
        "workflows": load_workflow_doc(root)["workflows"],
    }
