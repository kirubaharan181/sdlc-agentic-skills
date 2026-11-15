from pathlib import Path
import json, re, sys
from semantic_quality import find_near_duplicates
import registry_io
R=Path(__file__).resolve().parents[1]
errors=[]
def load(p):
    try:return json.loads((R/p).read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'{p}: invalid JSON: {e}');return {}
_all=registry_io.load_all(Path(__file__).resolve().parents[1])
st=_all['stages']
skills=_all['skills']; agents=_all['agents']; wfs=_all['workflows']
ids=[x.get('stage_id') for x in st]
# JSON Schema validation of every resolved registry record.
try:
    import jsonschema
except ImportError:
    errors.append('jsonschema is required: pip install jsonschema')
    jsonschema = None
if jsonschema:
    for kind, records, idkey in (('stage', st, 'stage_id'), ('agent', agents, 'agent_id'), ('workflow', wfs, 'workflow_id'), ('skill', skills, 'skill_id')):
        schema = json.loads((R / 'registry' / 'schemas' / f'{kind}.schema.json').read_text(encoding='utf-8'))
        validator = jsonschema.Draft202012Validator(schema)
        for rec in records:
            for err in validator.iter_errors(rec):
                where = '/'.join(str(x) for x in err.absolute_path) or '(record)'
                errors.append(f"schema {kind} {rec.get(idkey)}: {where}: {err.message[:140]}")
    agent_ids = {a['agent_id'] for a in agents}
    for rec in st:
        if rec.get('approval_required') and not rec.get('approval_rationale'):
            errors.append(f"stage {rec['stage_id']}: approval_required without approval_rationale")
        if rec.get('approval_required') and not rec.get('approver'):
            errors.append(f"stage {rec['stage_id']}: approval_required without a named human approver")
        if rec.get('approver') and not rec.get('approval_required'):
            errors.append(f"stage {rec['stage_id']}: approver set but approval_required is false")
        if rec.get('approver') in agent_ids:
            errors.append(f"stage {rec['stage_id']}: approver '{rec['approver']}' is an agent; approvers must be human roles")
        raci = rec.get('raci') or {}
        roles = [raci.get('accountable'), *raci.get('responsible', []), *raci.get('consulted', []), *raci.get('informed', [])]
        for r in roles:
            if r not in agent_ids:
                errors.append(f"stage {rec['stage_id']}: RACI role '{r}' is not a registered role")
        if len(roles) != len(set(roles)):
            errors.append(f"stage {rec['stage_id']}: a role appears more than once in the RACI")
    used = {r for rec in st for r in [rec['raci']['accountable'], *rec['raci']['responsible']]}
    for a in sorted(agent_ids - used):
        errors.append(f"orphan role: '{a}' is neither accountable nor responsible for any stage")
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
for sk in skills:
    p=R/sk['path']
    if not p.exists():errors.append(f"missing skill file {sk['path']}");continue
    t=p.read_text(encoding='utf-8')
    fm = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not fm:
        errors.append(f"{sk['skill_id']}: invalid frontmatter"); continue
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", fm.group(1), re.M))
    name, desc = meta.get("name", ""), meta.get("description", "")
    if name != sk["skill_id"] or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"{sk['skill_id']}: frontmatter name must equal the skill id (lowercase, hyphens, <=64 chars)")
    if any(w in name for w in ("anthropic", "claude")):
        errors.append(f"{sk['skill_id']}: name contains a reserved word")
    if not desc or len(desc) > 1024 or re.search(r"[<>]", desc):
        errors.append(f"{sk['skill_id']}: description must be 1-1024 chars with no XML tags")
    if re.match(r"(?i)(i|you|we)\b", desc) or "use when" not in desc.lower():
        errors.append(f"{sk['skill_id']}: description must be third person and say what the skill does and 'Use when ...'")
    body_lines = t.count("\n")
    if body_lines > 500:
        errors.append(f"{sk['skill_id']}: SKILL.md has {body_lines} lines (limit 500); move detail to reference files")
    for sec in ("Procedure", "Stages covered"):
        if f"## {sec}" not in t:
            errors.append(f"{sk['skill_id']}: missing section {sec}")
    for link in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", t):
        if link.startswith("http"):
            continue
        target = (p.parent / link).resolve()
        if not target.exists():
            errors.append(f"{sk['skill_id']}: broken link {link}")
        elif target.suffix == ".md" and target.parent.name == "reference":
            if re.search(r"\]\((?!http|#)[^)]*\.md", target.read_text(encoding="utf-8")):
                errors.append(f"{sk['skill_id']}: reference file links to another file (references must be one level deep)")
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
    if not w.get('outputs'):errors.append(f"workflow {w['workflow_id']}: missing outputs")
    for a in w.get('responsible_agents',[]):
        if a not in agentids:errors.append(f"workflow {w['workflow_id']}: unknown agent {a}")
    for s in w.get('required_skills',[]):
        if s not in skillids:errors.append(f"workflow {w['workflow_id']}: unknown skill {s}")
    for sid in w.get('stages',[]):
        if sid not in ids: errors.append(f"workflow {w['workflow_id']}: unknown stage {sid}")
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
    if len(text.split()) < 100 or len(re.findall(r'(?m)^\d+\. ', text)) < 3: errors.append(f'{p.relative_to(R)}: skill needs a procedure of at least 3 steps')
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

stage_by_id = {item["stage_id"]: item for item in st}
workflow_by_id = {item["workflow_id"]: item for item in wfs}
covered = set()
sets_seen = {}
for w in wfs:
    wid = w["workflow_id"]
    step_ids = [s["stage"] for s in w["steps"]]
    covered |= set(step_ids)
    if len(step_ids) != len(set(step_ids)):
        errors.append(f"workflow {wid}: a stage appears in more than one step")
    key = tuple(sorted(step_ids))
    if key in sets_seen:
        errors.append(f"workflow {wid}: identical stage list to {sets_seen[key]} (workflows must be distinct)")
    sets_seen[key] = wid
    for s in w["steps"]:
        stage = stage_by_id.get(s["stage"])
        if not stage:
            errors.append(f"workflow {wid}: unknown stage {s['stage']}")
            continue
        raci = stage["raci"]
        if s["owner"] not in [raci["accountable"], *raci["responsible"]]:
            errors.append(f"workflow {wid}: step {s['stage']} owner '{s['owner']}' is not accountable or responsible for that stage")
        if s["owner"] in w.get("excluded_roles", []):
            errors.append(f"workflow {wid}: role '{s['owner']}' is excluded from this workflow but owns step {s['stage']}")
        for n in s["needs"]:
            if n not in step_ids:
                errors.append(f"workflow {wid}: step {s['stage']} needs {n}, which is not a step of this workflow")
    # acyclic dependency graph
    needs_of = {s["stage"]: [n for n in s["needs"] if n in step_ids] for s in w["steps"]}
    state = {}
    def _visit(node, trail=()):
        if state.get(node) == 2:
            return
        if node in trail:
            errors.append(f"workflow {wid}: dependency cycle through {node}")
            return
        for n in needs_of.get(node, []):
            _visit(n, trail + (node,))
        state[node] = 2
    for node in needs_of:
        _visit(node)
    def _target_ok(tgt):
        if isinstance(tgt, int):
            return tgt in step_ids
        if tgt in ("end", "abort"):
            return True
        return tgt.startswith("workflow:") and tgt.split(":", 1)[1] in workflow_by_id
    for d in w["decisions"]:
        if d["after"] not in step_ids:
            errors.append(f"workflow {wid}: decision after {d['after']} which is not a step")
        for label, tgt in d["branches"].items():
            if not _target_ok(tgt):
                errors.append(f"workflow {wid}: decision branch '{label}' -> {tgt!r} does not resolve")
    for f in w["failure_paths"]:
        if f["at"] not in step_ids:
            errors.append(f"workflow {wid}: failure path at {f['at']} which is not a step")
        if not _target_ok(f["goto"]):
            errors.append(f"workflow {wid}: failure path goto {f['goto']!r} does not resolve")
    for h in w["handoff_workflows"]:
        if h not in workflow_by_id:
            errors.append(f"workflow {wid}: hands off to unknown workflow '{h}'")
    # a workflow that includes a production-changing stage must surface its approval
    for s in w["steps"]:
        if stage_by_id[s["stage"]].get("approval_required") and not any(a["stage"] == s["stage"] for a in w["approval_points"]):
            errors.append(f"workflow {wid}: approval stage {s['stage']} missing from approval_points")
if covered != set(stage_by_id):
    errors.append(f"stages in no workflow: {sorted(set(stage_by_id) - covered)}")
npd = workflow_by_id.get("new-product-development")
if not npd or len(npd["steps"]) != 190:
    errors.append("new-product-development must contain all 190 stages")
for item in st:
    if sorted(item["workflow_ids"]) != sorted(w["workflow_id"] for w in wfs if item["stage_id"] in w["stages"]):
        errors.append(f"stage {item['stage_id']}: workflow_ids disagree with workflow membership")

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

for workflow in wfs:
    path = R / "workflows" / f"{workflow['workflow_id']}.md"
    if not path.exists():
        errors.append(f"workflow {workflow['workflow_id']}: missing generated contract {path.relative_to(R)}")
        continue
    doc = path.read_text(encoding="utf-8")
    if len(doc.split()) < 130:
        errors.append(f"workflow {workflow['workflow_id']}: generated contract is not substantive")
    for s in workflow["steps"]:
        if f"| {s['stage']} |" not in doc:
            errors.append(f"workflow {workflow['workflow_id']}: step {s['stage']} missing from generated Markdown")

# stage content (Phase 4): `complete` is only allowed with the full authored contract
import json as _json
_content_files = {int(p_.stem): _json.loads(p_.read_text(encoding="utf-8")) for p_ in (R / "registry" / "stage-content").glob("*.json")}
_REQ = ("purpose", "entry_criteria", "inputs", "procedure", "deliverables", "acceptance_criteria", "validation_method",
        "validation", "failure_modes", "worked_example")
for _sid, _c in _content_files.items():
    if _sid not in stage_by_id:
        errors.append(f"stage-content/{_sid:03d}.json: unknown stage"); continue
    for _k in _REQ:
        if not _c.get(_k):
            errors.append(f"stage {_sid}: complete content missing '{_k}'")
    if len(_c.get("procedure", [])) < 4:
        errors.append(f"stage {_sid}: procedure needs at least 4 ordered steps")
    if len(_c.get("failure_modes", [])) < 2:
        errors.append(f"stage {_sid}: needs at least 2 failure modes")
    if not str(_c.get("worked_example", "")).startswith("ILLUSTRATIVE"):
        errors.append(f"stage {_sid}: worked_example must start with ILLUSTRATIVE (it is not evidence)")
    for _v in _c.get("validation", []):
        if not (("command" in _v) ^ ("check" in _v)) or not _v.get("expect"):
            errors.append(f"stage {_sid}: each validation needs exactly one of command/check and an expect")
        for _bad in re.findall(r"scripts/([\w./-]+\.py)", _v.get("command", "")):
            if not (R / "scripts" / _bad).exists():
                errors.append(f"stage {_sid}: validation command references missing script scripts/{_bad}")
    if _c.get("status") != "complete" or stage_by_id[_sid]["status"] != "complete":
        errors.append(f"stage {_sid}: content present but status is not complete")
for _s in st:
    if _s["status"] == "complete" and _s["stage_id"] not in _content_files:
        errors.append(f"stage {_s['stage_id']}: marked complete without authored content")
_procs = {i: " ".join(c["procedure"]) for i, c in _content_files.items()}
import difflib as _dl
for _a in sorted(_procs):
    for _b in sorted(_procs):
        if _a < _b and _dl.SequenceMatcher(None, _procs[_a], _procs[_b], autojunk=False).ratio() > 0.70:
            errors.append(f"stages {_a} and {_b}: procedures are more than 70% similar")

# role distinctness (Phase 3): contracts must not be near-copies and every role needs a derived footprint
sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_duplication as _dup
_pairs, _ = _dup.near_duplicates(R, 0.85, scope=("agents",))
for a_, b_, r_ in _pairs:
    errors.append(f"role contracts too similar ({r_:.2f} >= 0.85): {a_} <-> {b_}; differentiate or merge (see docs/audit/ROLE_DECISIONS.md)")
for item in agents:
    if "master-orchestration" in item["required_skills"]:
        errors.append(f"{item['agent_id']}: master-orchestration is an entry-point skill, not a role skill")
    if not item.get("permission_tier"):
        errors.append(f"{item['agent_id']}: permission_tier missing")
    rs_ = item["raci_summary"]
    if not (rs_["accountable"] or rs_["responsible"]):
        errors.append(f"{item['agent_id']}: owns no stage (decide assign/merge/remove in ROLE_DECISIONS.md)")

# credential heuristic
for p in R.rglob('*'):
    if p.is_file() and '.git' not in p.parts and p.suffix in {'.md','.yaml','.json','.py','.csv'}:
        if re.search(r'(AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC )?PRIVATE KEY-----)',p.read_text(encoding='utf-8',errors='ignore')):errors.append(f'possible credential: {p.relative_to(R)}')
if errors:
    print('VALIDATION FAILED');print('\n'.join('- '+e for e in errors));sys.exit(1)
print(f'VALIDATION PASSED: {len(st)} stages, {len(skills)} skills, {len(agents)} agents, {len(wfs)} workflows.')
