from pathlib import Path
import json, re, sys
R=Path(__file__).resolve().parents[1]
errors=[]
def load(p):
    try:return json.loads((R/p).read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p}: invalid JSON-compatible YAML: {e}');return {}
st=load('registry/SDLC_STAGE_REGISTRY.yaml').get('stages',[])
skills=load('registry/SKILL_REGISTRY.yaml').get('skills',[]); agents=load('registry/AGENT_REGISTRY.yaml').get('agents',[]); wfs=load('registry/WORKFLOW_REGISTRY.yaml').get('workflows',[])
ids=[x.get('stage_id') for x in st]
if ids!=list(range(1,191)):errors.append('stage IDs must be exactly 1..190 in order')
if len(set(ids))!=190:errors.append('duplicate/missing stage IDs')
skillids={x['skill_id'] for x in skills}; agentids={x['agent_id'] for x in agents}; wids={x['workflow_id'] for x in wfs}
for x in st:
    for k in ['stage_name','category_id','primary_role','skills','agents','workflow_ids','purpose','execution_instructions','deliverable_artifacts','quality_criteria','dependencies','inputs','outputs','quality_gate','validation_method','handoff_requirements']:
        if not x.get(k):errors.append(f"stage {x.get('stage_id')}: missing {k}")
    for k in x.get('skills',[]):
        if k not in skillids:errors.append(f"stage {x['stage_id']}: unknown skill {k}")
    for a in x.get('agents',[]):
        if a not in agentids:errors.append(f"stage {x['stage_id']}: unknown agent {a}")
for sk in skills:
    p=R/sk['path']
    if not p.exists():errors.append(f"missing skill file {sk['path']}");continue
    t=p.read_text(encoding='utf-8')
    if not t.startswith('---\n') or 'description:' not in t:errors.append(f"{sk['skill_id']}: invalid frontmatter")
    for sec in ['Purpose','When to use','When not to use','Required inputs','Preconditions','Responsibilities','Step-by-step execution procedure','Decision rules','Engineering principles','Tool requirements','Security constraints','Expected outputs','Output format','Quality checklist','Failure handling','Escalation conditions','Handoff instructions','Examples','Related skills','Related agents','References']:
        if f'## {sec}' not in t:errors.append(f"{sk['skill_id']}: missing section {sec}")
for a in agents:
    for s in a.get('required_skills',[]):
        if s not in skillids:errors.append(f"agent {a['agent_id']}: unknown skill {s}")
for w in wfs:
    if not w.get('approval_gates') or not w.get('outputs'):errors.append(f"workflow {w['workflow_id']}: missing gates/outputs")
    for a in w.get('responsible_agents',[]):
        if a not in agentids:errors.append(f"workflow {w['workflow_id']}: unknown agent {a}")
    for s in w.get('required_skills',[]):
        if s not in skillids:errors.append(f"workflow {w['workflow_id']}: unknown skill {s}")
# credential heuristic
for p in R.rglob('*'):
    if p.is_file() and '.git' not in p.parts and p.suffix in {'.md','.yaml','.json','.py','.csv'}:
        if re.search(r'(AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC )?PRIVATE KEY-----)',p.read_text(encoding='utf-8',errors='ignore')):errors.append(f'possible credential: {p.relative_to(R)}')
if errors:
    print('VALIDATION FAILED');print('\n'.join('- '+e for e in errors));sys.exit(1)
print(f'VALIDATION PASSED: {len(st)} stages, {len(skills)} skills, {len(agents)} agents, {len(wfs)} workflows.')
