# Production-Grade SDLC Library Rebuild — Codex / Claude Code Execution Brief

> **Execution mode:** implement the repository changes, not merely propose a plan.  
> **Target runtimes:** OpenAI Codex, Claude Code, and other Markdown-compatible agent runtimes.  
> **Canonical counts to preserve:** 190 SDLC stages, 15 domain skills + 5 cross-cutting skills, 74 specialist role contracts, 23 workflows, 7 platform capability declarations.

## Mission

Rebuild the content layer of this repository so every skill, specialist role, workflow, stage playbook, registry entry, and supporting document is genuinely useful in professional software delivery.

The current implementation has a serious content-generation defect: many files differ only by title while sharing generic responsibilities, inputs, outputs, tools, stage mappings, approval gates, and completion criteria. The generator in `scripts/bootstrap_library.py` is part of the root cause. **Do not solve this by editing only the Markdown files. Fix the canonical source data and the generator so future regeneration cannot reintroduce generic content.**

A skill must be usable as an execution instruction when loaded by Codex or Claude Code into a real repository. A role must behave like a bounded specialist contract. A workflow must represent its own real lifecycle, not a renamed copy of another workflow.

## Non-negotiable engineering rules

1. Start by inspecting the entire repository, current branch, working tree, existing registries, scripts, tests, CI, adapters, and all current Markdown files. Read project-level `AGENTS.md`, `CLAUDE.md`, `CODEX.md`, and other local instructions if present.
2. Preserve canonical IDs and the intended counts unless a documented migration is required. Never silently delete, rename, or renumber stages, skills, roles, workflows, or adapters.
3. Use the registries as the source of truth. Generated Markdown must be reproducible from canonical data.
4. Do not use a single generic template with only the role/workflow name substituted. Shared structure is acceptable; domain decisions, procedures, responsibilities, artifacts, tools, gates, and examples must be specific.
5. Do not invent project tools, commands, approvals, test results, metrics, customer evidence, or completed actions. Detect the actual repository stack and use only installed/available tools.
6. Prefer existing project conventions and the smallest safe change. Do not introduce dependencies without a concrete need.
7. Never expose secrets or personal/customer data. Do not run destructive, production, billing, IAM, public-publishing, or irreversible actions without explicit approval from an authorized human.
8. Do not claim a test passed unless it was actually executed and its result is available.
9. Keep Codex/Claude compatibility portable. Do not make the canonical skill depend on proprietary tool syntax, hidden APIs, or one vendor's command names. Explain runtime-specific alternatives only where necessary.
10. Do not mark a stage or workflow as fully mapped until every referenced ID resolves in the canonical registries and validators prove it.

## Required deliverables

### A. Twenty executable skills

Keep these 15 domain skill IDs and five cross-cutting skill IDs:

| Domain | Skill ID | Required domain-specific execution focus |
|---|---|---|
| Business / Product | `business-product-management` | opportunity framing, market/customer research, product discovery, business case, prioritization, measurable outcomes |
| Requirements / UX | `requirements-design` | elicitation, functional/NFR quality, user research, journeys, prototypes, accessibility, acceptance criteria |
| Architecture | `technical-architecture` | system boundaries, quality attributes, options/trade-offs, API/data/cloud/security/integration architecture, ADRs |
| Project / Agile | `project-agile-management` | charter, WBS, estimates, capacity, sprint flow, dependencies, RAID, stakeholders, change control |
| Engineering Governance | `engineering-governance` | repository setup, branching, developer environment, standards, configuration, secrets, contributor docs |
| Implementation | `software-implementation` | frontend/backend/mobile/API/database/auth/integration/data/AI implementation, errors, caching, developer tests |
| Code Review | `code-review-quality` | PR review, correctness, architecture, static analysis, dependencies, coverage, merge readiness, technical debt |
| QA | `quality-assurance` | test strategy, unit/integration/API/UI/E2E, regression, smoke, compatibility, accessibility, performance, UAT, defects |
| Security | `application-security` | threat modeling, SAST/DAST/SCA, container/IaC security, authorized penetration tests, remediation, retesting |
| DevOps / Platform | `devops-platform` | CI/CD, builds, artifacts, containers, Kubernetes, IaC, configuration, provisioning, network/CDN, pipeline security |
| Release | `release-deployment` | release planning, readiness, change approvals, staging, migrations, production rollout, DNS/TLS, rollback, smoke |
| Cloud Operations | `cloud-hosting-operations` | compute, database, storage, DNS, TLS, networking, backups, DR, HA, autoscaling, cost and maintenance |
| SRE / Observability | `sre-observability` | logs, metrics, traces, alerts, uptime, SLIs/SLOs, capacity, incidents, RCA, postmortems, reliability |
| Maintenance / Support | `maintenance-support` | L1-L3 triage, diagnosis, bug fixes, patches, dependency/DB maintenance, support knowledge, maintenance releases |
| Enterprise Governance | `enterprise-governance` | engineering/quality/security/access governance, compliance, audit, docs/change governance, vendors, FinOps, improvement |
| Cross-cutting | `master-orchestration` | request classification, workflow selection, dependency graph, bounded delegation, gate tracking, truthful reporting |
| Cross-cutting | `evidence-quality-gates` | evidence schema, reproducibility, gate states, independent verification, waivers, audit trail |
| Cross-cutting | `secure-change-control` | risk classification, authorization, least privilege, segregation, blast radius, rollback, human approvals |
| Cross-cutting | `definition-of-done` | task-type-specific completion criteria for features, bugs, APIs, DB, infrastructure, security, releases, incidents, docs |
| Cross-cutting | `incident-command` | severity, commander roles, impact, containment, communications, recovery, post-incident learning |

Every `SKILL.md` must be written as an instruction set an agent can execute, not as a high-level description. Include:

- Valid YAML frontmatter with a concise, searchable `name` and an accurate `description` that tells the runtime when to load the skill.
- Purpose, scope, when to use, when not to use, required inputs, preconditions, assumptions and constraints.
- A concrete ordered procedure with decision points and expected outcomes.
- Domain-specific tool selection guidance. First inspect manifests and existing project tools; provide alternatives only when the primary tool is unavailable.
- Concrete artifacts/files to create or update, including expected content and traceability.
- Validation commands or test techniques chosen from the actual project stack; do not hardcode a framework that may not exist.
- Security/privacy rules, least-privilege boundaries and actions requiring human approval.
- Failure handling, retry/rollback guidance, escalation conditions and handoff contract.
- A task-specific Definition of Done, quality checklist and at least one realistic worked example.
- Related stages, workflows, agents and skills using valid canonical IDs.

Avoid vague steps such as “perform assigned work”, “use approved tools”, “produce evidence”, or “validate the output” unless followed by precise domain-specific instructions explaining what to inspect, what to do, what evidence to retain, and how to decide pass/fail.

### B. Seventy-four specialist role contracts

For every entry in `registry/AGENT_REGISTRY.json`, make its matching `agents/<agent-id>.md` a genuine role contract. At minimum include:

- Mission and specialist domain; explicit scope and non-scope.
- Accountabilities and concrete responsibilities, written for that role.
- Inputs, preconditions, outputs and artifact expectations.
- Required skills, required knowledge and role-specific tools.
- Decision authority, permissions and least-privilege boundaries.
- What the role must not do; segregation-of-duties and self-approval restrictions.
- Dependencies, collaboration points and expected upstream/downstream roles.
- Handoff format, escalation triggers and approval requirements.
- Role-specific Definition of Done, quality signals and realistic example.
- Execution instructions for Codex/Claude: inspect the repository first, follow local instructions, plan bounded changes, make edits, run real checks, report exact evidence and never claim unexecuted work.

The same broad role family may share a structure, but the responsibility and artifact content must be distinct. For example:

- **API Architect:** API style and resource/schema design, OpenAPI/contract governance, versioning/deprecation, compatibility, auth patterns, rate limits, idempotency, consumer migration, API ADRs and contract review.
- **Data Engineer:** ingestion and transformation, batch/stream orchestration, schema evolution, data quality tests, lineage, idempotency/replay, late data, privacy, pipeline observability and recovery.
- **Merge Steward:** branch protections, required status checks, merge queue, conflict resolution, signed/traceable commits, stale approvals, release branch policy and safe merge readiness. This role does not replace the code reviewer.
- **Product Owner:** backlog ordering, value/acceptance decisions, story readiness, scope trade-offs, stakeholder clarification and product acceptance. This role does not own architecture or implementation quality.
- **Security Auditor:** independent control assessment, sampling, evidence sufficiency, finding severity, independence and audit reporting. This role must not audit its own implementation.
- **Backend Engineer:** service/domain implementation, data access, API behavior, error handling, security boundaries, observability and backend tests.
- **QA Lead:** risk-based quality strategy, test coverage, defect severity, exit criteria and independent quality recommendation.

Apply this level of specificity to all 74 roles, not only the examples above.

### C. Twenty-three unique workflow contracts

Every workflow in `registry/WORKFLOW_REGISTRY.json` must have a unique trigger, purpose, stage set, phase sequence, role assignment, required skills, inputs, dependencies, approval gates, outputs, failure path, rollback/compensation, communication plan and completion criteria.

The 23 workflow IDs are:

`new-product-development`, `existing-application-enhancement`, `feature-development`, `bug-fix`, `emergency-hotfix`, `security-vulnerability-remediation`, `dependency-update`, `database-migration`, `api-version-upgrade`, `infrastructure-provisioning`, `environment-configuration`, `ci-cd-pipeline-creation`, `staging-release`, `production-release`, `rollback`, `incident-response`, `root-cause-analysis`, `disaster-recovery`, `performance-optimization`, `technical-debt-reduction`, `documentation-update`, `product-retirement`, `application-maintenance`.

Workflow expectations:

- **Bug fix:** severity/impact triage → reproduction → root cause → minimal fix → regression test → review → controlled release → verification.
- **Emergency hotfix:** incident command → safe mitigation → minimal patch → emergency authorization → expedited tests/review → controlled deploy → recovery verification → retrospective.
- **Security remediation:** validate finding → assess exploitability/impact → assign SLA/owner → fix → independent retest → residual-risk decision → controlled release.
- **Database migration:** schema/data impact → backup/restore rehearsal → migration plan → compatibility/performance/integrity tests → approved window → execution → reconciliation.
- **API version upgrade:** consumer inventory → contract/version design → implementation → contract/security tests → migration guidance → staged publication → deprecation.
- **CI/CD creation:** source-to-artifact flow → trust boundaries → build/test/security/provenance → immutable artifacts → environment protection → failure/recovery tests.
- **Production release:** exact artifact/readiness → change approval → progressive rollout → health thresholds → smoke/business validation → rollback or release confirmation.
- **Rollback:** trigger confirmation → data/state safety assessment → approved rollback/forward-fix → execution → recovery verification → communication.
- **Incident response:** commander/severity → impact/timeline → containment → parallel investigation → recovery verification → operational handoff → postmortem.
- **Disaster recovery:** RTO/RPO → backup/replication readiness → isolated recovery → restore/failover exercise → integrity checks → measured recovery and gaps.
- **Product retirement:** business/EOL approval → consumer/vendor/data inventory → migration/communication → retention/deletion decision → staged shutdown → audit closure.

The remaining workflows must receive equally specific lifecycles. Do not assign the same 15 stage IDs, same five agents or same approval gates to every workflow.

### D. Stage registry and playbooks

- Keep exactly 190 stage IDs, 1 through 190, unless a reviewed migration is explicitly approved.
- Fix the known invalid workflow reference: stage records currently reference `maintenance`, while the workflow registry uses `application-maintenance`. Resolve this consistently and validate all stage-to-workflow references.
- Review each stage's primary role, supporting roles, skill, agent, workflow IDs, inputs, outputs, purpose, execution instructions, deliverables, dependencies, quality criteria, validation method and handoff.
- Replace category-wide generic stage instructions with instructions specific to each stage.
- Regenerate all 15 `STAGE_PLAYBOOK.md` files from the corrected stage registry and relevant skill. Each stage entry must explain the actual task, artifact and verification method.

### E. Generator and source-of-truth architecture

- Fix `scripts/bootstrap_library.py`; it currently regenerates generic role and workflow records and Markdown files. It must not overwrite curated content with generic templates.
- Introduce a structured, versioned specialist-content source registry if needed. It must contain the role-specific, skill-specific and workflow-specific data required to reproduce generated Markdown.
- Implement deterministic generation and a non-mutating `--check` mode. Running generation twice must produce no diff.
- Do not make generated Markdown the only source of truth.
- Keep all IDs and paths cross-referenced and validated.
- Ensure dashboard counts and content summaries continue to derive from canonical registries, not hardcoded numbers.

### F. Automated quality gates

Add deterministic validation to CI. At minimum:

1. Exact counts: 190 stages, 20 skills, 74 agents and 23 workflows.
2. Unique IDs and valid file paths for every registry entry.
3. Every stage skill, agent and workflow reference resolves.
4. Every workflow stage, agent and skill reference resolves.
5. Every agent's required skill reference resolves.
6. No unknown or orphaned workflow IDs; specifically no stale `maintenance` reference.
7. Required skill frontmatter and sections exist; each skill has substantive content, not a short placeholder.
8. Each agent document has role-specific mission, responsibilities, artifacts, tools, boundaries, escalation and DoD.
9. Each workflow has a distinct stage set and workflow-specific phases/gates/outputs. Flag identical stage arrays and near-identical normalized Markdown for review.
10. Detect repeated generic filler and placeholder language, including “execute assigned stages”, “project-approved tools” without specific guidance, and identical generic inputs/outputs.
11. Detect exact duplicate Markdown after removing title/frontmatter and high-similarity documents after removing common boilerplate.
12. Verify generator determinism: generate, run again, and ensure no file changes.
13. Verify all links and relative paths in generated documents.
14. Keep the existing JSON/YAML, Python, JavaScript and dashboard validation checks passing.

A duplicate detector must not flag legitimate shared safety language as a duplicate. Normalize/remove common policy boilerplate first, then compare the domain-specific body.

### G. Documentation and compatibility

- Explain how to install/use the library with Codex and Claude Code without claiming unverified runtime features.
- Provide a clear example of loading a skill and delegating to a specialist role in each runtime.
- Document canonical vs generated files, registry changes, regeneration and validation commands.
- Include examples showing how a workflow orchestrates multiple roles and skills with evidence gates.
- Update README/dashboard descriptions only when the underlying registry facts have changed. Preserve the current Atelier visual design and typography improvement.

## Required execution sequence

1. Inspect repository and report baseline counts, duplicate clusters, broken references and generator defects.
2. Design and implement canonical role/skill/workflow content data.
3. Correct registry mappings and stage-specific playbooks.
4. Fix generator and add deterministic check mode.
5. Generate all affected Markdown and registry files.
6. Run all existing validation and new content-quality tests.
7. Review the full diff for accidental unrelated changes, generic filler, broken links and incorrect mappings.
8. Fix every introduced failure. Do not hide, skip or weaken a test to obtain green CI.
9. Create a focused feature branch and PR; do not push directly to `main`.
10. Wait for CI, inspect failed job logs, fix failures and rerun.
11. Merge only when checks pass and the diff is reviewed. Verify the final main commit and report exact results.

## Acceptance criteria

The task is complete only when:

- 74 agent files describe 74 distinct specialist contracts.
- 20 skills are executable, domain-specific instructions that Codex/Claude can follow in a real repository.
- 23 workflows have genuinely different, semantically correct stage mappings and lifecycle controls.
- All 190 stage records have valid and meaningful cross-references.
- The `maintenance` / `application-maintenance` mismatch is resolved.
- All 15 stage playbooks are stage-specific and generated from canonical data.
- Re-running bootstrap/generation cannot overwrite curated content with generic filler.
- Duplicate-content and registry-integrity tests run in CI and pass.
- The full validation suite passes with no suppressed failures.
- The PR diff and final commit are reported with links and evidence.

**Do not stop after writing a plan. Execute the audit, make the changes, run the tests, fix failures, and deliver the PR. If the repository or runtime lacks a capability, state the exact limitation and continue with the safe supported work.**
