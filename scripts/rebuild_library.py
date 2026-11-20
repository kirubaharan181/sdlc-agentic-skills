"""Canonical, deterministic content generator for the SDLC agentic skills library.

The structured registries plus the metadata below are source-of-truth.  Generated
Markdown is deliberately reproducible; do not edit generated role/workflow/skill
documents by hand.
"""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
import registry_io
import render_workflows
import render_skills
from execution_profiles import stage_profile, role_profile, SKILL_PROFILES

ROOT=Path(__file__).resolve().parents[1]
SKILLS={
'business-product-management':('Business Product Management','Frame opportunities, research customers and markets, define measurable product outcomes, and obtain an evidence-backed investment decision.'),
'requirements-design':('Requirements and Experience Design','Elicit testable requirements and design inclusive user journeys, interfaces, prototypes, and acceptance criteria.'),
'technical-architecture':('Technical Architecture','Make explicit system, API, data, cloud, integration, and security design decisions with trade-offs and ADR evidence.'),
'project-agile-management':('Project and Agile Management','Turn approved scope into a feasible delivery plan with capacity, dependencies, risks, stakeholder alignment, and controlled change.'),
'engineering-governance':('Engineering Governance','Establish a safe repository, contribution model, development environment, configuration, secrets, and engineering standards.'),
'software-implementation':('Software Implementation','Implement bounded product changes across client, service, API, data, integration, authentication, performance, and developer tests.'),
'code-review-quality':('Code Review and Quality','Assess correctness, design fit, maintainability, static findings, dependency risk, coverage, and merge readiness.'),
'quality-assurance':('Quality Assurance','Plan and execute risk-based functional and non-functional verification, manage defects, and make an independent quality recommendation.'),
'application-security':('Application Security','Model threats, assess code/dependencies/runtime exposure, coordinate authorized testing, remediate findings, and retest fixes.'),
'devops-platform':('DevOps and Platform','Build trustworthy source-to-artifact-to-environment delivery systems with immutable artifacts, protected environments, and pipeline security.'),
'release-deployment':('Release and Deployment','Prepare a named release, validate it in staging, obtain authority, deploy progressively, verify health, and recover safely.'),
'cloud-hosting-operations':('Cloud Hosting Operations','Operate compute, data, storage, network, DNS/TLS, backup, resilience, scaling, cost, and maintenance controls.'),
'sre-observability':('SRE and Observability','Instrument services, define SLOs, detect and manage incidents, learn from failures, and improve reliability.'),
'maintenance-support':('Maintenance and Support','Triage customer impact, diagnose and fix defects, maintain dependencies/data, publish support knowledge, and manage lifecycle work.'),
'enterprise-governance':('Enterprise Governance','Run engineering, quality, security, access, compliance, document, change, vendor, FinOps, and improvement governance.'),
'master-orchestration':('Master Orchestration','Classify requests, select a workflow, build a dependency graph, delegate bounded work, enforce gates, and report truthfully.'),
'evidence-quality-gates':('Evidence Quality Gates','Create reproducible evidence, evaluate gate state, separate verification from implementation, and record auditable waivers.'),
'secure-change-control':('Secure Change Control','Classify change risk, apply least privilege and segregation of duties, bound blast radius, prepare rollback, and obtain approvals.'),
'definition-of-done':('Definition of Done','Apply task-type-specific completion criteria for product changes, APIs, data, infrastructure, security, releases, incidents, and documentation.'),
'incident-command':('Incident Command','Coordinate severity, impact, containment, communications, recovery, evidence, and post-incident learning without losing command discipline.')}

ROLE_ACTIONS=[
'portfolio hypotheses, strategic options, investment assumptions and outcome measures','market segments, competitor evidence, pricing signals and research confidence','client goals, commitments, decision logs and relationship risk','product vision, roadmap outcomes, prioritization and value metrics','process models, business rules, stakeholder needs and traceability','backlog order, story acceptance and value-versus-scope decisions','elicitation sessions, requirement ambiguity, NFRs and acceptance tests','research plans, participant evidence, insights and journey pain points','interaction patterns, visual hierarchy, prototypes and design-system alignment','end-to-end solution boundaries, constraints, integration choices and solution ADRs','runtime structure, quality attributes, component boundaries and technical ADRs','capability maps, standards alignment, lifecycle roadmaps and exception decisions','data models, retention, integrity, migration strategy and query trade-offs','resource/schema design, OpenAPI governance, compatibility, versioning and consumer migration','landing-zone design, service selection, resilience, identity and cloud cost trade-offs','security architecture, trust boundaries, controls, abuse cases and residual risk','data domains, lineage, classification, ownership and interoperability','interface contracts, message semantics, failure modes and partner integration lifecycle','charter, WBS, delivery plan, RAID register and delivery reporting','cross-team outcomes, benefits, dependencies, governance cadence and escalation','ceremonies, flow health, impediments, retrospective actions and team norms','delivery metrics, iteration health, dependency coordination and continuous flow improvement','client components, state/accessibility, browser behavior, telemetry and component tests','service/domain behavior, persistence, API behavior, errors, observability and backend tests','vertical slices across client/service/data boundaries and coherent end-user behavior','mobile lifecycle, offline behavior, device permissions, store readiness and mobile tests','API implementation, validation, error model, idempotency, compatibility and contract tests','schema/query implementation, migration safety, transaction behavior, integrity and performance','identity flows, credential handling, session security, authorization enforcement and audit events','external protocols, retries, idempotency, contract drift and integration observability','ingestion, transformation, schema evolution, quality checks, lineage, replay and privacy','model/data lifecycle, evaluation, safety boundaries, inference performance and monitoring','latency budgets, profiling, workload models, bottleneck remediation and performance evidence','risk-based quality strategy, coverage model, defect severity, exit criteria and recommendation','exploratory scenarios, usability defects, acceptance evidence and reproducible defect reports','automation architecture, stable selectors, test data, CI signal quality and flake diagnosis','unit-test isolation, boundary conditions, mutation-resistant assertions and fast feedback','cross-component contracts, test environments, fixtures, failure isolation and compatibility','API contract behavior, auth/error cases, schema compatibility and consumer assertions','critical user journeys, realistic test data, state setup, browser/device reliability and artifacts','throughput/latency/error objectives, workload models, capacity and bottleneck evidence','inclusive design, keyboard/screen-reader behavior, semantic markup and WCAG evidence','behavioral correctness, security regressions, maintainability, tests and review feedback','architecture conformance, quality-attribute impact, coupling and ADR consistency','branch protections, required checks, merge queue, stale approvals, conflicts and traceable merge readiness','threat-model findings, secure coding controls, scan triage, remediation and security verification','pipeline trust boundaries, secret handling, IaC/container policy and supply-chain evidence','authorized test scope, safe exploitation, reproduction evidence and remediation verification','finding validation, exploitability, severity, SLA ownership and risk disposition','control mapping, regulatory obligations, evidence collection and exception tracking','independent audit sampling, evidence sufficiency, finding severity and audit reporting','license inventory, policy compatibility, attribution, obligations and remediation options','CI/CD implementation, build reliability, artifact promotion, deployment automation and runbooks','developer platform capabilities, golden paths, self-service and platform reliability','cloud resources, IAM boundaries, cost signals, resilience and operational readiness','infrastructure modules, desired-state changes, drift, review and safe provisioning','cluster workloads, namespaces, policies, rollout health and capacity','connectivity, segmentation, DNS, load balancing, firewall policy and failure diagnostics','backup/recovery, replication, access, maintenance windows and database health','release scope, readiness, approvals, communications, versioning and release record','deployment execution, rollout signals, environment safety and recovery action','service SLOs, error budgets, toil, incidents and reliability improvements','telemetry design, dashboards, logs/metrics/traces, alert quality and investigation paths','incident command, severity, impact, containment, communications and recovery verification','production triage, runbooks, diagnosis, customer impact and safe escalation','customer support diagnosis, communication, knowledge capture and case resolution','technical narrative, audience needs, accuracy review and maintained documentation','docs-as-code structure, information architecture, linting and publishing automation','engineering policy, control ownership, exceptions and measurable compliance','quality-system controls, auditability, metrics, corrective action and improvement','cloud spend allocation, budgets, forecasts, optimization and cost accountability','supplier evaluation, security/delivery obligations, renewal risk and exit planning','process measurement, root causes, experiments, adoption and sustainable improvement','cross-role scheduling, artifact tracking, meeting decisions and handoff completeness']

def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def dump(p,obj): (ROOT/p).write_text(json.dumps(obj,indent=2)+"\n",encoding='utf-8')
def write(p,text):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+"\n",encoding='utf-8')
def title(s): return s.replace('-',' ').title()
def skills_for(role):
 r=role.lower()
 if any(x in r for x in ['security','penetration','vulnerability','compliance','license']):return ['application-security','evidence-quality-gates']
 if any(x in r for x in ['qa','testing','reviewer','merge']):return ['quality-assurance','code-review-quality','evidence-quality-gates']
 if any(x in r for x in ['devops','platform','cloud','infrastructure','kubernetes','network','administrator','deployment','release']):return ['devops-platform','release-deployment','secure-change-control']
 if any(x in r for x in ['support','incident','sre','observability']):return ['sre-observability','maintenance-support','incident-command']
 if any(x in r for x in ['architect']):return ['technical-architecture','secure-change-control']
 if any(x in r for x in ['product','business','research','ux','design','requirements']):return ['business-product-management','requirements-design']
 if any(x in r for x in ['manager','scrum','agile','coordinator','improvement','governance','finops','vendor']):return ['project-agile-management','enterprise-governance']
 return ['software-implementation','definition-of-done']
def tool_advice(skill):
 return {'business-product-management':'Inspect existing issue tracker, product analytics and customer-research repository before proposing a research method. Preserve source links and confidence limits.', 'requirements-design':'Inspect existing product docs, design system and accessibility tooling. Write acceptance criteria that can be tested without guessing.', 'technical-architecture':'Inspect service boundaries, manifests, deployment configuration and current ADRs before recommending any technology.', 'software-implementation':'Inspect manifests, test scripts, lint configuration and local instructions; run only commands already supported by the repository.', 'quality-assurance':'Derive checks from the installed test stack and risk profile; retain raw reports, screenshots or request/response traces.', 'application-security':'Use configured scanners first. Authorized active testing needs written scope; do not scan third-party targets or production without approval.', 'devops-platform':'Inspect CI definitions and environment protections before changing pipeline or infrastructure behavior.', 'release-deployment':'Inspect release notes, artifact digest, migration/rollback plan and environment health before requesting release approval.', 'sre-observability':'Inspect current telemetry, dashboards, alerts and runbooks before adding signals or paging rules.'}.get(skill,'Inspect the repository’s manifests, local instructions and existing automation before selecting a tool; document why an available alternative was chosen.')


def main(check=False):
 stage_doc=registry_io.load_stage_doc(ROOT); stages=stage_doc['stages']; agents_doc=registry_io.load_agent_doc(ROOT); workflows={w['workflow_id']:w for w in registry_io.load_workflow_doc(ROOT)['workflows']}; wf=list(workflows.values())
 valid_w=set(workflows); valid_s=set(SKILLS); valid_a={a['agent_id'] for a in agents_doc['agents']}
 # stage contracts: resolve a concrete domain procedure for every canonical stage
 authored=set(registry_io.load_stage_content(ROOT))
 for st in stages:
  sid=st['stage_id']; name=st['stage_name']; skill=st['skills'][0]
  if sid in authored: continue
  profile=stage_profile(st)
  st['purpose']=profile['purpose']
  st['inputs']=profile['inputs']
  st['outputs']=[re.sub('[^a-z0-9]+','-',name.lower()).strip('-')+'-deliverable',*profile['artifacts'][:2]]
  st['execution_instructions']=profile['steps']
  st['deliverable_artifacts']=profile['artifacts']
  st['dependencies']=[f"Approved upstream evidence for {name}",f"Accountable {st['primary_role']} and required stakeholder access","Applicable policy, repository instructions and approved operating window"]
  st['quality_criteria']=profile['criteria']
  st['validation_method']=profile['validation']
  st['handoff_requirements']=f"Transfer {profile['artifacts'][0]} with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role."
 # role registry and specialist contracts
 for a in agents_doc['agents']:
  profile=role_profile(a)
  focus=profile['focus']
  a['purpose']=f"Provide accountable specialist judgment for {focus.lower()}."
  a['scope']=focus
  a['responsibilities']=profile['steps']
  a['inputs']=['approved work item and acceptance criteria',*profile.get('inputs',[]),*profile['artifacts'][:2],'upstream evidence, constraints and named decision authority']
  a['outputs']=profile['artifacts']+['revision-pinned evidence and named handoff']
  a['tools']=profile['tools']
  a['escalation_conditions']=profile['decisions']+['missing authority, unsafe scope or unverified critical evidence']
  a['definition_of_done']=f"{a['name']} has completed the specialist procedure, produced {profile['artifacts'][0]}, attached reproducible evidence, disclosed residual risk and obtained the required independent decision."
  rs=a['raci_summary']
  body=f"""---
agent_id: {a['agent_id']}
name: {a['name']}
description: Load for specialist work in {focus.lower()}; follow the role-specific procedure, decision rules and evidence contract below.
---
# {a['name']}

## Mission and specialist domain
Own specialist judgment for **{focus}**. Your output must be usable by another engineer without relying on private chat context.

## Accountabilities and expected artifacts
{chr(10).join(f"- {x}" for x in profile['steps'])}

## Required inputs
{chr(10).join(f"- {x}" for x in a['inputs'])}

## Role-specific toolchain
{chr(10).join(f"- {x}" for x in profile['tools'])}
Inspect local instructions and existing project configuration first. Use only tools already installed or explicitly approved; do not assume a stack.

## Codex / Claude execution procedure
{chr(10).join(f"{i+1}. {x}" for i,x in enumerate(profile['steps']))}
{len(profile['steps'])+1}. Run the repository-native verification relevant to this role; capture command, exact revision, exit status and report path.
{len(profile['steps'])+2}. Report PASS, FAIL, BLOCKED or INCONCLUSIVE honestly; request independent approval where required.

## Decision rules and non-responsibilities
{chr(10).join(f"- {x}" for x in profile['decisions'])}
{chr(10).join(f"- {x}" for x in a['non_responsibilities'])}
Shared rules for every role (independence, untrusted input, production access) live in [docs/governance/COMMON_ROLE_POLICY.md](../docs/governance/COMMON_ROLE_POLICY.md).

## RACI footprint
- Accountable for stages: {rs['accountable'] and ', '.join(map(str,rs['accountable'])) or 'none'}
- Responsible for stages: {rs['responsible'] and ', '.join(map(str,rs['responsible'])) or 'none'}
- Consulted on: {rs['consulted'] and ', '.join(map(str,rs['consulted'])) or 'none'}
- Permission tier: `{a['permission_tier']}`. {a['permissions']}
- Approvals: {a['approval_requirements']}

## Workflow neighbours
{chr(10).join(f"- {x}" for x in a['dependencies'])}
- {a['handoff_rules']}

## Expected outputs and evidence
{chr(10).join(f"- {x}" for x in profile['artifacts'])}
Evidence must identify source/revision, method or command, executor, timestamp, outcome, limitations and reviewer.

## Definition of Done
{a['definition_of_done']}

## Worked example
{profile['example']}

## Handoff and escalation
Transfer the artifact path/revision, validation evidence, limitations, residual risk, named receiver and next decision. Escalate missing authority, unsafe scope, ambiguous acceptance criteria or failed critical evidence.
"""
  write(f"agents/{a['agent_id']}.md",body)
 # skill docs and stage playbooks
 skill_paths={s['skill_id']:s['path'] for s in registry_io.load_skill_doc(ROOT)['skills']}
 write('skills/_shared/CORE_PROCEDURE.md',render_skills.CORE_PROCEDURE)
 skill_content=registry_io.load_skill_content(ROOT)
 received={}
 for src,c in skill_content.items():
  for h in c['handoffs']: received.setdefault(h['skill'],[]).append((src,h['artifact']))
 for sid in SKILLS:
  matched=[s for s in stages if sid in s['skills']]
  path=Path(skill_paths[sid])
  skill_md,ref_md=render_skills.render_skill(sid,SKILL_PROFILES[sid],matched,agents_doc['agents'],ROOT/path.parent,skill_content.get(sid),sorted(received.get(sid,[])))
  write(path,skill_md)
  if matched:
    for old in (ROOT/path.parent/'references').glob('stages*.md'): old.unlink()
    for fn,txt in (ref_md.items() if isinstance(ref_md,dict) else [('stages.md',ref_md)]): write(path.parent/'references'/fn,txt)
  write(path.parent/'references'/'CORE_PROCEDURE.md',render_skills.CORE_PROCEDURE)
  write(path.parent/'references'/'HANDOFF_CONTRACT.md',(ROOT/'orchestrator/handoff-contracts/STANDARD_HANDOFF.md').read_text(encoding='utf-8'))
  ev=render_skills.render_evidence_example(sid,matched)
  if ev: (ROOT/path.parent/'references'/'examples').mkdir(parents=True,exist_ok=True); (ROOT/path.parent/'references'/'examples'/'evidence-example.json').write_text(ev,encoding='utf-8')
 import skill_graph
 ranges={}
 for sid in SKILLS:
  ids=sorted(s['stage_id'] for s in stages if sid in s['skills'])
  if ids: ranges[sid]=f"{ids[0]}-{ids[-1]}"
 if skill_content: write('docs/architecture/SKILL_SELECTION.md',skill_graph.render_selection_doc(skill_content,ranges))
 # workflow files are rendered from registry/workflows/*.json
 stages_by_id={s['stage_id']:s for s in registry_io.load_stage_doc(ROOT)['stages']}
 for w in wf:
  write(f"workflows/{w['workflow_id']}.md",render_workflows.render(w,stages_by_id))
 registry_io.save_stage_doc(stage_doc,ROOT);registry_io.save_agent_doc(agents_doc,ROOT)
 if check: return

if __name__=='__main__': main()
