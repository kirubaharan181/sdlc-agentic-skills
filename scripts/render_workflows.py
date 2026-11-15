"""Render workflows/<id>.md from the resolved workflow records.  Generated; do not edit the output."""
from __future__ import annotations


def _target(t) -> str:
    if isinstance(t, int):
        return f"S{t}"
    if t == "end":
        return "DONE"
    if t == "abort":
        return "ABORT"
    return "WF_" + t.split(":", 1)[1].replace("-", "_")


def mermaid(w: dict, stages_by_id: dict[int, dict]) -> str:
    lines = ["flowchart TD"]
    ids = {s["stage"] for s in w["steps"]}
    # A 190-node diagram is unreadable; draw the diagram only for workflows that fit on a screen.
    if len(ids) > 30:
        return ""
    for s in w["steps"]:
        name = stages_by_id[s["stage"]]["stage_name"].replace('"', "'")
        shape = ('{{"%d %s"}}' if stages_by_id[s["stage"]].get("approval_required") else '["%d %s"]') % (s["stage"], name)
        lines.append(f"  S{s['stage']}{shape}")
    for s in w["steps"]:
        for n in s["needs"]:
            lines.append(f"  S{n} --> S{s['stage']}")
    for d in w["decisions"]:
        for label, tgt in d["branches"].items():
            lines.append(f"  S{d['after']} -. {label} .-> {_target(tgt)}")
    for f in w["failure_paths"]:
        g = f["goto"]
        if g != f["at"]:
            lines.append(f"  S{f['at']} -. fail .-> {_target(g)}")
    extra = {t for d in w["decisions"] for t in d["branches"].values() if not isinstance(t, int)} | {f["goto"] for f in w["failure_paths"] if not isinstance(f["goto"], int)}
    for t in sorted(extra, key=str):
        lines.append(f"  {_target(t)}(({_target(t).replace('WF_', 'run workflow: ')}))")
    return "\n".join(lines)


def render(w: dict, stages_by_id: dict[int, dict]) -> str:
    out = [f"# {w['name']}", "", "> Generated from `registry/workflows/" + w["workflow_id"] + ".json`. Edit the source, then run `python scripts/build.py`.", "",
           f"**Purpose.** {w['purpose']}", "", f"**Trigger.** {w['trigger']}", "", "## Entry criteria", *[f"- {x}" for x in w["entry_criteria"]], "",
           "## Required inputs", *[f"- {x}" for x in w["required_inputs"]], ""]
    diagram = mermaid(w, stages_by_id)
    if diagram:
        out += ["## Flow", "", "Solid arrows are dependencies, dotted arrows are decisions and failure paths, hexagons need human approval.", "", "```mermaid", diagram, "```", ""]
    out += ["## Steps", "", "| # | Stage | Owner (accountable or responsible) | Needs | Notes |", "|---:|---|---|---|---|"]
    if len(w["steps"]) > 30:
        out.insert(len(out) - 2, "")
    for s in w["steps"]:
        st = stages_by_id[s["stage"]]
        flags = []
        if s.get("optional"):
            flags.append("optional")
        if st.get("approval_required"):
            flags.append(f"approval: {st['approver']}")
        note = "; ".join(filter(None, [s.get("note", ""), *flags]))
        out.append(f"| {s['stage']} | {st['stage_name']} | `{s['owner']}` | {', '.join(map(str, s['needs'])) or '-'} | {note} |")
    out += [""]
    if w["parallel_groups"]:
        out += ["## Parallel work", *[f"- Stages {', '.join(map(str, g))}" for g in w["parallel_groups"][:12]], ""]
    if w["approval_points"]:
        out += ["## Human approval points", "", "| Stage | Approver | When |", "|---:|---|---|"]
        out += [f"| {a['stage']} {stages_by_id[a['stage']]['stage_name']} | `{a['approver']}` | {a['condition']} |" for a in w["approval_points"]]
        out += ["", "Rationale for each approval is in `docs/governance/APPROVAL_POLICY.md` and the stage's `approval_rationale`.", ""]
    if w["decisions"]:
        out += ["## Decision points", *[f"- After {d['after']} - {d['question']} " + "; ".join(f"**{k}** -> {v}" for k, v in d["branches"].items()) for d in w["decisions"]], ""]
    if w["failure_paths"]:
        out += ["## Failure and remediation", "", "| At stage | Condition | Action | Go to |", "|---:|---|---|---|"]
        out += [f"| {f['at']} | {f['condition']} | {f['action']} | {f['goto']} |" for f in w["failure_paths"]]
        out += [""]
    out += ["## Outputs", *[f"- {x}" for x in w["outputs"]], "", "## Exit criteria", *[f"- {x}" for x in w["exit_criteria"]], "",
            "## Communication", w["communication_plan"], ""]
    if w["handoff_workflows"]:
        out += ["## Hands off to", *[f"- [{h}]({h}.md)" for h in w["handoff_workflows"]], ""]
    out += ["Any FAIL, BLOCKED or INCONCLUSIVE gate halts the steps that depend on it; see `orchestrator/` for the common failure policy.", ""]
    return "\n".join(out)
