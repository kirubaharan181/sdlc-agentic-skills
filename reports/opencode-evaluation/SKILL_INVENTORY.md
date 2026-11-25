# Skill Inventory — OpenCode Installed Skills

**Repository:** kirubaharan181/sdlc-agentic-skills
**Release:** v1.1.0
**Install location:** `.opencode/skills/` (project scope, copy)
**Install verification:** `python scripts/install.py --target opencode --dest . --check` -> CHECK PASSED: 20/20
**OpenCode auto-detection:** All 20 skills detected and advertised to the model
**Expected count:** 20 | **Discovered count:** 20 | **Missing:** 0 | **Duplicates:** 0 | **Broken:** 0

---

## Complete skill inventory table

| # | Skill name | Group | SKILL.md | Version | Description (purpose) | OpenCode discoverable | Install status |
|---|---|---|---|---|---|---|---|
| 1 | application-security | security | Yes | 1.1.1 | Check a change for security risk: threats, scans, remediation, sign-off. | Yes | Installed, verified |
| 2 | business-product-management | business-product | Yes | 1.1.1 | Assess a business case: strategy, discovery, estimates, approval. | Yes | Installed, verified |
| 3 | cloud-hosting-operations | cloud-hosting | Yes | 1.1.1 | Manage hosted infrastructure: compute, storage, network, DR, cost. | Yes | Installed, verified |
| 4 | code-review-quality | code-review | Yes | 1.1.1 | Assess a pull request for correctness, design, standards, merge readiness. | Yes | Installed, verified |
| 5 | definition-of-done | cross-cutting | Yes | 1.1.1 | Set completion criteria and close on evidence. | Yes | Installed, verified |
| 6 | devops-platform | devops-platform | Yes | 1.1.1 | Automate delivery: CI/CD, containers, IaC, environments. | Yes | Installed, verified |
| 7 | engineering-governance | engineering-governance | Yes | 1.1.1 | Standardize repos: branching, environment, coding rules. | Yes | Installed, verified |
| 8 | enterprise-governance | enterprise-governance | Yes | 1.1.1 | Oversee controls: policy, quality, security, access, change, vendor, cost audits. | Yes | Installed, verified |
| 9 | evidence-quality-gates | cross-cutting | Yes | 1.1.1 | Classify/check/accept/reject evidence for a gate. | Yes | Installed, verified |
| 10 | incident-command | cross-cutting | Yes | 1.1.1 | Command an active incident: severity, roles, comms, timeline, recovery. | Yes | Installed, verified |
| 11 | master-orchestration | cross-cutting | Yes | 1.1.1 | Route multi-skill work to workflows and consolidate results. | Yes | Installed, verified |
| 12 | maintenance-support | maintenance-support | Yes | 1.1.1 | Maintain live software: support tiers, fixes, patches, updates. | Yes | Installed, verified |
| 13 | project-agile-management | project-management | Yes | 1.1.1 | Scope, estimate, run iterations: plans, tracks, governs delivery and risk. | Yes | Installed, verified |
| 14 | quality-assurance | quality-assurance | Yes | 1.1.1 | Verify behavior before release: risk-based testing and defect handling. | Yes | Installed, verified |
| 15 | release-deployment | release-deployment | Yes | 1.1.1 | Promote a build to staging/production: plans, approves, verifies. | Yes | Installed, verified |
| 16 | requirements-design | requirements-design | Yes | 1.1.1 | Elicit, document, validate requirements and UX before design. | Yes | Installed, verified |
| 17 | secure-change-control | cross-cutting | Yes | 1.1.1 | Classify risk for a risky change: approvals, rollback, audit trail. | Yes | Installed, verified |
| 18 | software-implementation | development | Yes | 1.1.1 | Implement features or fixes: build and change application code. | Yes | Installed, verified |
| 19 | sre-observability | sre-observability | Yes | 1.1.1 | Make a service observable/reliable: monitoring, SLOs, alerts. | Yes | Installed, verified |
| 20 | technical-architecture | architecture | Yes | 1.1.1 | Design/review architecture: boundaries, interfaces, trade-offs. | Yes | Installed, verified |

---

## Inventory comparison

- Source of truth: `scripts/install.py --list` (20 skills) matches the README's stated count of 20 skills (15 domain + 5 cross-cutting).
- All 20 source skills were copied into `.opencode/skills/`.
- `--check` confirmed every installed copy is identical to its source (no drift, no missing files).
- Each skill folder contains `SKILL.md` and a `references/` subfolder with `CORE_PROCEDURE.md`, `HANDOFF_CONTRACT.md`, and stage references.
- No missing skills, duplicates, broken installations, missing files, invalid metadata, incorrect folder structures, inconsistent versions, unsupported references, or broken relative paths were found at installation time.

## Relative-reference integrity (spot-checked)

Each SKILL.md references `references/CORE_PROCEDURE.md` and `references/HANDOFF_CONTRACT.md`; domain skills additionally reference `references/stages.md` (or stages-part-*.md for application-security). All referenced files were confirmed present in both source and installed copies. No broken relative paths detected.
