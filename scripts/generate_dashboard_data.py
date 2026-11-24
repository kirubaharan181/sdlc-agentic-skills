#!/usr/bin/env python3
"""Generate Atelier's dashboard snapshot from canonical JSON registries."""
from pathlib import Path
from datetime import datetime, timezone
import json
import csv
import os
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import registry_io

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    "stages": "registry/SDLC_STAGE_REGISTRY.json",
    "agents": "registry/AGENT_REGISTRY.json",
    "skills": "registry/SKILL_REGISTRY.json",
    "workflows": "registry/workflows",
    "platforms": "adapters/capability-matrix.json",
}

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def git_commit():
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def latest_quality():
    """Latest recorded SkillEvaluator row per skill, from the committed score history (never invented)."""
    path = ROOT / "reports/skill-quality/SCORE_HISTORY.csv"
    latest = {}
    if path.exists():
        for row in csv.DictReader(path.open(encoding="utf-8", newline="")):
            latest[row["skill"]] = row  # file is append-only; the last row per skill is the latest
    return {sid: {"score": float(r["score"]), "grade": r["grade"], "findings": int(r["findings"]), "date": r["date"],
                  "source_commit": r["source_commit"], "skill_version": r["skill_version"],
                  "evaluator_version": r["evaluator_version"]} for sid, r in latest.items()}


def selector_data() -> dict:
    """Same terms, weights and thresholds as scripts/select_skill.py so the dashboard ranks requests identically."""
    import select_skill
    return {"terms": select_skill._terms(ROOT), "close": select_skill.CLOSE, "incident": list(select_skill.INCIDENT),
            "note": "Deterministic word matching, not understanding. Treat the result as a suggestion and read the skill's When NOT to Use section."}


def main():
    resolved = registry_io.load_all(ROOT)
    source = {"platforms": load(SOURCES["platforms"])}
    stages, agents = resolved["stages"], resolved["agents"]
    skills, workflows = resolved["skills"], resolved["workflows"]

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
    content = registry_io.load_skill_content(ROOT)
    quality = latest_quality()
    for item in skills:
        c = content.get(item["skill_id"])
        if c:
            item.update(version=c["version"], description=c["description"], tags=c["tags"], owns=c["owns"],
                        handoffs=[{"skill": h["skill"], "artifact": h["artifact"], "feedback": bool(h.get("feedback"))} for h in c["handoffs"]],
                        limitations=c["limitations"])
        item["quality"] = quality.get(item["skill_id"])
    tiers = load("registry/risk-tiers.json")
    for stage in stages:
        stage["risk_tier"] = tiers["stage_tiers"].get(str(stage["stage_id"]))
    scores = [q["score"] for q in quality.values()]
    governance = {
        "riskTiers": tiers["tiers"],
        "qualitySummary": {"skillsRecorded": len(scores), "average": round(sum(scores) / len(scores), 1) if scores else None,
                           "lowest": min(scores) if scores else None,
                           "commits": sorted({q["source_commit"] for q in quality.values()}),
                           "evaluators": sorted({q["evaluator_version"] for q in quality.values()}),
                           "dates": sorted({q["date"] for q in quality.values()}),
                           "note": "Recorded evaluator runs from reports/skill-quality/SCORE_HISTORY.csv. A quality score is not publication approval."},
    }
    data = {
        "meta": {
            "name": "Atelier Engineering Command Center",
            "repository": "kirubaharan181/sdlc-agentic-skills",
            "sourceBranch": os.environ.get("GITHUB_REF_NAME", "local"),
            "sourceCommit": git_commit(),
            "generatedAt": datetime.now(timezone.utc).isoformat(),
            "dataMode": "repository snapshot",
            "notice": "Static snapshot generated from the repository registries. Nothing here is live execution; recorded scores are past evaluator runs.",
            "audit": audit,
        },
        "stages": stages,
        "agents": agents,
        "skills": skills,
        "workflows": workflows,
        "platforms": source["platforms"]["platforms"],
        "governance": governance,
        "selector": selector_data(),
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
