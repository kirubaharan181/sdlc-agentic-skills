#!/usr/bin/env python3
"""Generate Atelier's dashboard snapshot from canonical JSON registries."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "stages": "registry/SDLC_STAGE_REGISTRY.json",
    "agents": "registry/AGENT_REGISTRY.json",
    "skills": "registry/SKILL_REGISTRY.json",
    "workflows": "registry/WORKFLOW_REGISTRY.json",
    "platforms": "adapters/capability-matrix.json",
}

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    source = {key: load(path) for key, path in SOURCES.items()}
    stages = source["stages"]["stages"]
    agents = source["agents"]["agents"]
    skills = source["skills"]["skills"]
    workflows = source["workflows"]["workflows"]

    workflow_ids = {item["workflow_id"] for item in workflows}
    agent_ids = {item["agent_id"] for item in agents}
    skill_ids = {item["skill_id"] for item in skills}
    missing_workflows, missing_agents, missing_skills = {}, {}, {}

    for stage in stages:
        for ref in stage.get("workflow_ids", []):
            if ref not in workflow_ids:
                missing_workflows.setdefault(ref, []).append(stage["stage_id"])
        for ref in stage.get("agents", []):
            if ref not in agent_ids:
                missing_agents.setdefault(ref, []).append(stage["stage_id"])
        for ref in stage.get("skills", []):
            if ref not in skill_ids:
                missing_skills.setdefault(ref, []).append(stage["stage_id"])

    def records(mapping):
        return [{"reference_id": key, "stage_ids": ids, "count": len(ids)}
                for key, ids in sorted(mapping.items())]

    audit = {
        "unresolvedStageWorkflowReferences": [
            {"workflow_id": item["reference_id"], "stage_ids": item["stage_ids"], "count": item["count"]}
            for item in records(missing_workflows)
        ],
        "unresolvedStageSkillReferences": records(missing_skills),
        "unresolvedStageAgentReferences": records(missing_agents),
    }
    data = {
        "meta": {
            "name": "Atelier Engineering Command Center",
            "repository": "kirubaharan181/sdlc-agentic-skills",
            "sourceBranch": os.environ.get("GITHUB_REF_NAME", "local"),
            "sourceCommit": os.environ.get("GITHUB_SHA", "local-working-tree"),
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "dataMode": "repository snapshot",
            "audit": audit,
        },
        "stages": stages,
        "agents": agents,
        "skills": skills,
        "workflows": workflows,
        "platforms": source["platforms"]["platforms"],
    }
    output = ROOT / "dashboard" / "data" / "library.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Generated dashboard/data/library.json")
    print("Stages: {}; skills: {}; roles: {}; workflows: {}; platforms: {}".format(
        len(stages), len(skills), len(agents), len(workflows), len(data["platforms"])))
    if any(audit.values()):
        print("Registry audit warnings:")
        for key, values in audit.items():
            for item in values:
                print("- {}: {} ({} stage references)".format(key, item.get("workflow_id", item.get("reference_id")), item["count"]))

if __name__ == "__main__":
    main()
