from pathlib import Path
import json, re, sys
from semantic_quality import find_near_duplicates
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
if (len(st),len(skills),len(agents),len(wfs)) != (190,20,74,23):
    errors.append(f'exact counts required: found {len(st)} stages, {len(skills)} skills, {len(agents)} agents, {len(wfs)} workflows')
if len(skillids)!=20 or len(agentids)!=74 or len(wids)!=23: errors.append('duplicate registry IDs')
for x in st:
    for k in ['stage_name','category_id','primary_role','skills','agents','workflow_ids','purpose','execution_instructions','deliverable_artifacts','quality_criteria','dependencies','inputs','outputs','quality_gate','validation_method','handoff_requirements']:
        if not x.get(k):errors.append(f"stage {x.get('stage_id')}: missing {k}")
    for k in x.get('skills',[]):
        if k not in skillids:errors.append(f"stage {x['stage_id']}: unknown skill {k}")
    for a in x.get('agents',[]):
        if a not in agentids:errors.append(f"stage {x['stage_id']}: unknown agent {a}")
    for w in x.get('workflow_ids',[]):
        if w not in wids:errors.append(f"stage {x['stage_id']}: unknown workflow {w}")
    if 'maintenance' in x.get('workflow_ids',[]): errors.append(f"stage {x['stage_id']}: stale maintenance workflow reference")
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
    p=R/'agents'/f"{a['agent_id']}.md"
    if not p.exists(): errors.append(f"agent {a['agent_id']}: missing role contract")
    elif len(p.read_text(encoding='utf-8').split()) < 180: errors.append(f"agent {a['agent_id']}: role contract is not substantive")
    for required in ['purpose','scope','responsibilities','inputs','outputs','tools','permissions','escalation_conditions']:
        if not a.get(required): errors.append(f"agent {a['agent_id']}: missing registry {required}")
stage_sets=[]
for w in wfs:
    if not w.get('approval_gates') or not w.get('outputs'):errors.append(f"workflow {w['workflow_id']}: missing gates/outputs")
    for a in w.get('responsible_agents',[]):
        if a not in agentids:errors.append(f"workflow {w['workflow_id']}: unknown agent {a}")
    for s in w.get('required_skills',[]):
        if s not in skillids:errors.append(f"workflow {w['workflow_id']}: unknown skill {s}")
    for sid in w.get('stages',[]):
        if sid not in ids: errors.append(f"workflow {w['workflow_id']}: unknown stage {sid}")
    stage_set=tuple(w.get('stages',[]))
    if stage_set in stage_sets: errors.append(f"workflow {w['workflow_id']}: identical stage set")
    stage_sets.append(stage_set)
    p=R/'workflows'/f"{w['workflow_id']}.md"
    if not p.exists() or len(p.read_text(encoding='utf-8').split()) < 130: errors.append(f"workflow {w['workflow_id']}: missing or insubstantial contract")
# Duplicate/filler detector: compare domain-bearing first sections, excluding shared policy phrases.
def domain_body(path):
    text=path.read_text(encoding='utf-8').lower()
    text=re.sub(r'^---.*?---','',text,flags=re.S)
    text=re.sub(r'#.*\n','',text)
    for phrase in ['inspect the repository','evidence record','least privilege','human approval','standard handoff']:
        text=text.replace(phrase,'')
    return re.sub(r'\s+',' ',text).strip()
docs=[]
for folder in ['agents','workflows']:
    docs.extend((R/folder).glob('*.md'))
seen={}
for p in docs:
    body=domain_body(p)
    key=hash(body)
    if key in seen: errors.append(f'duplicate domain content: {p.relative_to(R)} and {seen[key].relative_to(R)}')
    seen[key]=p
for p in (R/'skills').rglob('SKILL.md'):
    text=p.read_text(encoding='utf-8')
    if len(text.split()) < 280: errors.append(f'{p.relative_to(R)}: skill is not substantive')
    if 'execute assigned stages' in text.lower() or 'project-approved tools' in text.lower(): errors.append(f'{p.relative_to(R)}: generic filler detected')
# Semantic execution-depth checks: counts alone do not prove specialist uniqueness.
def extract_section(document, heading):
    match = re.search(rf"(?ms)^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", document)
    return match.group(1).strip() if match else ""

stage_signatures = {
    tuple(re.sub(r"\W+", " ", step.lower()).strip() for step in item.get("execution_instructions", []))
    for item in st
}
if len(stage_signatures) < 60:
    errors.append(f"stage procedures lack sufficient domain variation: {len(stage_signatures)} unique profiles for 190 stages (minimum 60)")
for item in st:
    if len(item.get("execution_instructions", [])) < 3:
        errors.append(f"stage {item.get('stage_id')}: fewer than three executable steps")
    if "decision-ready" in item.get("purpose", "").lower():
        errors.append(f"stage {item.get('stage_id')}: generic purpose template remains")
    if any("inspect current artifacts" in step.lower() for step in item.get("execution_instructions", [])):
        errors.append(f"stage {item.get('stage_id')}: generic execution template remains")

allowed_by_category = {
    "Business, Strategy and Product Management": {"new-product-development","existing-application-enhancement","feature-development","product-retirement","documentation-update"},
    "Requirements Engineering and UI/UX Design": {"new-product-development","existing-application-enhancement","feature-development"},
    "Software, Solution and Technical Architecture": {"new-product-development","existing-application-enhancement","feature-development","infrastructure-provisioning","database-migration","api-version-upgrade","ci-cd-pipeline-creation"},
    "Project, Program and Agile Management": {"new-product-development","existing-application-enhancement","feature-development","technical-debt-reduction","application-maintenance"},
    "Development Environment and Engineering Governance": {"ci-cd-pipeline-creation","infrastructure-provisioning","application-maintenance","dependency-update","environment-configuration"},
    "Software Development and Implementation": {"feature-development","existing-application-enhancement","bug-fix","application-maintenance","emergency-hotfix"},
    "Code Review, Static Analysis and Quality Engineering": {"feature-development","bug-fix","emergency-hotfix","security-vulnerability-remediation","dependency-update","production-release"},
    "Software Testing and Quality Assurance": {"feature-development","bug-fix","production-release","staging-release","application-maintenance"},
    "Cybersecurity, Application Security and Compliance": {"security-vulnerability-remediation","dependency-update","ci-cd-pipeline-creation","infrastructure-provisioning","production-release"},
    "DevOps, CI/CD and Platform Engineering": {"ci-cd-pipeline-creation","infrastructure-provisioning","staging-release","production-release","environment-configuration"},
    "Release Engineering and Deployment Management": {"staging-release","production-release","rollback","database-migration","environment-configuration"},
    "Cloud Infrastructure and Hosting Operations": {"infrastructure-provisioning","disaster-recovery","incident-response","application-maintenance"},
    "Production Monitoring, Observability and SRE": {"incident-response","root-cause-analysis","disaster-recovery","production-release"},
    "Application Maintenance, Technical Support and Customer Success": {"application-maintenance","bug-fix","emergency-hotfix","dependency-update","performance-optimization","incident-response","product-retirement"},
    "Enterprise Governance, Audit, Risk and Continuous Improvement": {"new-product-development","production-release","security-vulnerability-remediation","application-maintenance","product-retirement","documentation-update","root-cause-analysis","technical-debt-reduction","performance-optimization","infrastructure-provisioning","ci-cd-pipeline-creation","environment-configuration","emergency-hotfix"},
}
for item in st:
    allowed = allowed_by_category.get(item.get("category_name"), wids)
    invalid = set(item.get("workflow_ids", [])) - allowed
    if invalid:
        errors.append(f"stage {item.get('stage_id')}: semantically invalid workflow mapping {sorted(invalid)}")
    if item.get("stage_name") == "Client Engagement" and "application-maintenance" in item.get("workflow_ids", []):
        errors.append("Client Engagement must not map to application-maintenance")
    semantic_stage_workflows = {
        "Process Improvement": {"root-cause-analysis","technical-debt-reduction"},
        "Quality Governance": {"production-release","application-maintenance"},
        "Security Governance": {"security-vulnerability-remediation","ci-cd-pipeline-creation"},
        "Access Governance": {"security-vulnerability-remediation","application-maintenance"},
        "Documentation Governance": {"documentation-update","application-maintenance"},
        "Change Governance": {"production-release","emergency-hotfix","application-maintenance"},
        "FinOps Governance": {"infrastructure-provisioning","performance-optimization","application-maintenance"},
        "Vendor Management": {"product-retirement","new-product-development"},
        "Product Lifecycle Management": {"product-retirement","application-maintenance"},
    }
    expected = semantic_stage_workflows.get(item.get("stage_name"))
    if item.get("stage_name") == "Engineering Governance":
        expected = {"ci-cd-pipeline-creation","environment-configuration","application-maintenance"}
    if expected and set(item.get("workflow_ids", [])) != expected:
        errors.append(f"stage {item.get('stage_id')}: incorrect semantic workflow assignment for {item.get('stage_name')}")

role_procedures = {}
for item in agents:
    path = R / "agents" / f"{item['agent_id']}.md"
    if path.exists():
        doc = path.read_text(encoding="utf-8")
        procedure = extract_section(doc, "Codex / Claude execution procedure")
        if not procedure or len(procedure.split()) < 45:
            errors.append(f"{item['agent_id']}: role-specific execution procedure is missing or too shallow")
        role_procedures[item["agent_id"]] = procedure
        if "perform assigned workflow stages" in doc.lower():
            errors.append(f"{item['agent_id']}: generic role filler remains")
near_role_duplicates = find_near_duplicates(role_procedures, threshold=0.94)
for left, right, score in near_role_duplicates:
    errors.append(f"near-duplicate specialist procedures: {left} and {right} ({score:.2f})")
if len({re.sub(r"\W+", " ", p.lower()).strip() for p in role_procedures.values()}) < 60:
    errors.append("fewer than 60 distinct specialist execution procedures")

phase_instructions = []
for workflow in wfs:
    contracts = workflow.get("phase_contracts", [])
    if len(contracts) != len(workflow.get("phases", [])) or not contracts:
        errors.append(f"workflow {workflow['workflow_id']}: phase contracts do not match lifecycle phases")
    for phase in contracts:
        for field in ["phase","instruction","evidence","exit_criteria","owner"]:
            if not phase.get(field):
                errors.append(f"workflow {workflow['workflow_id']}: phase contract missing {field}")
        phase_instructions.append(phase.get("instruction", ""))
    path = R / "workflows" / f"{workflow['workflow_id']}.md"
    if path.exists():
        doc = path.read_text(encoding="utf-8").lower()
        if "complete the relevant mapped stages" in doc:
            errors.append(f"workflow {workflow['workflow_id']}: generic phase filler remains")
        if doc.count("**execution:**") != len(contracts):
            errors.append(f"workflow {workflow['workflow_id']}: Markdown phase execution count mismatch")
if len(set(phase_instructions)) < 40:
    errors.append(f"workflow phase guidance lacks variation: {len(set(phase_instructions))} unique instructions")

# credential heuristic
for p in R.rglob('*'):
    if p.is_file() and '.git' not in p.parts and p.suffix in {'.md','.yaml','.json','.py','.csv'}:
        if re.search(r'(AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC )?PRIVATE KEY-----)',p.read_text(encoding='utf-8',errors='ignore')):errors.append(f'possible credential: {p.relative_to(R)}')
if errors:
    print('VALIDATION FAILED');print('\n'.join('- '+e for e in errors));sys.exit(1)
print(f'VALIDATION PASSED: {len(st)} stages, {len(skills)} skills, {len(agents)} agents, {len(wfs)} workflows.')
