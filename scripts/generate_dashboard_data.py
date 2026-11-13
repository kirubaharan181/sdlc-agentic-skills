#!/usr/bin/env python3
"""Generate Atelier's dashboard snapshot from canonical JSON-compatible YAML registries."""
from pathlib import Path
from datetime import datetime, timezone
import json
ROOT = Path(__file__).resolve().parents[1]
SOURCES = {"stages":"registry/SDLC_STAGE_REGISTRY.yaml","agents":"registry/AGENT_REGISTRY.yaml","skills":"registry/SKILL_REGISTRY.yaml","workflows":"registry/WORKFLOW_REGISTRY.yaml","platforms":"adapters/capability-matrix.yaml"}
def load(path): return json.loads((ROOT / path).read_text(encoding="utf-8"))
def main():
    s = {k: load(p) for k,p in SOURCES.items()}
    stages=s["stages"]["stages"]; workflows=s["workflows"]["workflows"]; workflow_ids={x["workflow_id"] for x in workflows}; missing={}
    for stage in stages:
        for workflow_id in stage.get("workflow_ids",[]):
            if workflow_id not in workflow_ids: missing.setdefault(workflow_id,[]).append(stage["stage_id"])
    audit={"unresolvedStageWorkflowReferences":[{"workflow_id":k,"stage_ids":v,"count":len(v)} for k,v in sorted(missing.items())],"unresolvedStageSkillReferences":[],"unresolvedStageAgentReferences":[]}
    d = {"meta":{"name":"Atelier Engineering Command Center","repository":"kirubaharan181/sdlc-agentic-skills","sourceBranch":"main","generatedAt":datetime.now(timezone.utc).isoformat(),"dataMode":"repository snapshot","audit":audit},"stages":stages,"agents":s["agents"]["agents"],"skills":s["skills"]["skills"],"workflows":workflows,"platforms":s["platforms"]["platforms"]}
    out=ROOT/"dashboard"/"data"/"library.json";out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("Generated dashboard/data/library.json")
    print("Stages: {}; skills: {}; roles: {}; workflows: {}; platforms: {}".format(len(d["stages"]),len(d["skills"]),len(d["agents"]),len(d["workflows"]),len(d["platforms"])))
if __name__=="__main__": main()
