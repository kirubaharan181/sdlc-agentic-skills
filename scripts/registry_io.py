"""Read and write the canonical registries.

Stored registry files are *compact*: a record holds only the fields that differ
from the shared defaults in registry/*-defaults.json (or that cannot be derived).
`load_*` returns fully resolved records; `save_*` strips values that equal the
default or the derivable value, so every fact is stated exactly once.

Resolution rules
  stage     supporting_roles, approval_required   <- stage-defaults.json
            handoff_requirements, dependencies    <- templates in stage-defaults.json,
                                                     filled from the record itself
  agent     non_responsibilities, permissions, dependencies, handoff_rules,
            approval_requirements                 <- role-defaults.json
  workflow  required_inputs, required_skills, dependencies, parallel_tasks,
            communication_plan, completion_criteria <- workflow-defaults.json
An explicit value in a record always wins over the default.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STAGE_FIELDS = ("supporting_roles", "approval_required")
ROLE_FIELDS = ("non_responsibilities", "permissions", "dependencies", "handoff_rules", "approval_requirements")
WORKFLOW_FIELDS = ("required_inputs", "required_skills", "dependencies", "parallel_tasks", "communication_plan", "completion_criteria")


def _read(root: Path, rel: str) -> dict:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def _write(root: Path, rel: str, obj: dict) -> None:
    (root / rel).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- stages
def _derive_stage(rec: dict, d: dict) -> dict:
    out = dict(rec)
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
    for f in STAGE_FIELDS:
        if out.get(f) == d[f]:
            out.pop(f, None)
    derived = _derive_stage({k: v for k, v in out.items() if k not in ("handoff_requirements", "dependencies")}, d)
    for f in ("handoff_requirements", "dependencies"):
        if out.get(f) == derived.get(f):
            out.pop(f, None)
    return out


def load_stage_doc(root: Path = ROOT) -> dict:
    doc = _read(root, "registry/SDLC_STAGE_REGISTRY.json")
    d = _read(root, "registry/stage-defaults.json")
    doc["stages"] = [_derive_stage(s, d) for s in doc["stages"]]
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
def load_workflow_doc(root: Path = ROOT) -> dict:
    doc = _read(root, "registry/WORKFLOW_REGISTRY.json")
    d = _read(root, "registry/workflow-defaults.json")
    doc["workflows"] = [{**{f: copy.deepcopy(d[f]) for f in WORKFLOW_FIELDS}, **w} for w in doc["workflows"]]
    return doc


def save_workflow_doc(doc: dict, root: Path = ROOT) -> None:
    d = _read(root, "registry/workflow-defaults.json")
    out = dict(doc)
    out["workflows"] = [{k: v for k, v in w.items() if not (k in WORKFLOW_FIELDS and v == d[k])} for w in doc["workflows"]]
    _write(root, "registry/WORKFLOW_REGISTRY.json", out)


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
