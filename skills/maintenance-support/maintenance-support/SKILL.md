---
name: maintenance-support
description: "Use when maintaining live software: support tiers, fixes, patches, updates. Do NOT use for new product builds."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["support", "maintenance", "patching", "bug-fixing"]
---

# Service maintenance and customer support

## Purpose
Keeps live software healthy after release: tiered support, bug fixing, patching, dependency updates, database maintenance, performance and debt work, enhancements, feedback, knowledge base, maintenance releases and lifecycle decisions. It owns stages 167-180.

## When to Use
- Support requests, bugs or patches need handling.
- Dependencies, performance or technical debt need planned work.
- A lifecycle or retirement decision for a product is needed.

## When NOT to Use
- Building a new product: use requirements-design and software-implementation.
- Running an active major incident: use incident-command.
- Approving production changes: use secure-change-control.

## Prerequisites and Requirements
- A ticket system and the escalation rules.
- Access to runbooks and the knowledge base.
- Current release and known issues.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- support request or defect
- affected version and environment

Optional inputs:
- logs
- usage data
- customer feedback
- dependency reports

Outputs and deliverables:
- resolved or escalated tickets with full records
- bug fixes and patches with tests
- dependency and patch status
- knowledge base articles
- lifecycle decision records

## Procedure
1. Classify impact, severity, affected versions, workaround and authority.
2. Diagnose with approved read-only evidence and correlate recent changes.
3. Implement the smallest safe fix/patch with regression and compatibility coverage.
4. Verify customer recovery, communicate closure and update support knowledge.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Fix known in knowledge base | Apply it and confirm with the user. |
| Cannot resolve at tier | Escalate with the full record so the user does not repeat details. |
| Patch addresses a vulnerability | Prioritize by severity and exposure and record the deadline. |
| Retirement proposed | Require notice, migration path and sponsor approval. |

## Quality Gates
- [ ] Tickets carry identifiers, steps and time
- [ ] Fixes are confirmed with the user
- [ ] Patches have tests and rollback
- [ ] Retirement has notice and data handling

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Escalate a ticket
```text
Request: User cannot download invoices; L1 has no fix.
Context: Account id and error time are known.
Agent behavior: Escalate with the account id, error time, steps and impact, and tell the user the next update time.
Output: L2 ticket with complete record and user update.
Acceptance: The user is not asked to repeat details.
```

### Example 2: Plan a dependency update
```text
Request: A library has a critical vulnerability.
Context: Used by two services.
Agent behavior: Find affected services, update with tests, plan staged rollout and rollback, and record the deadline.
Output: Patch plan and test evidence.
Acceptance: Deadline and approval are recorded.
```

## Limitations
- Cannot see customer systems it has no access to.
- Does not approve production patches: a named human does.
- Root cause may need tiers beyond its access.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Duplicate tickets | Known issue not linked | Link to the known issue and update the user. |
| Patch breaks behavior | Missing tests | Roll back and add characterization tests. |
| Knowledge base outdated | No owner | Assign owners and review dates. |

## Tools
- ticketing and runbooks
- approved production diagnostics
- dependency/security advisories
- regression test tools

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 167 | L1 Support | complete | Technical Support Engineer |
| 168 | L2 Support | complete | Production Support Engineer |
| 169 | L3 Support | complete | Backend Engineer |
| 170 | Bug Fixing | complete | Backend Engineer |
| 171 | Patch Management | complete | DevOps Engineer |
| 172 | Dependency Updates | complete | Backend Engineer |
| 173 | Database Maintenance | complete | Database Administrator |
| 174 | Performance Optimization | complete | Performance Engineer |
| 175 | Technical Debt Reduction | complete | Backend Engineer |
| 176 | Feature Enhancement | complete | Product Owner |
| 177 | Customer Feedback | complete | Product Manager |
| 178 | Knowledge Base | complete | Technical Writer |
| 179 | Maintenance Release | complete | Release Manager |
| 180 | Product Lifecycle Management | complete | Product Manager |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `software-implementation`: defects and enhancements with reproduction steps
- `sre-observability`: recurring issues as reliability work
- `enterprise-governance`: patch and lifecycle evidence

Receives from:
- `cloud-hosting-operations`: infrastructure maintenance windows
- `incident-command`: customer communications and follow-up tickets
- `release-deployment`: release notes and known issues
- `sre-observability`: reliability and fix backlog

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: application-maintenance, bug-fix, dependency-update, documentation-update, emergency-hotfix, existing-application-enhancement, incident-response, new-product-development, performance-optimization, product-retirement, technical-debt-reduction.
- Roles: backend-engineer, client-engagement-specialist, database-administrator, database-engineer, devops-engineer, devsecops-engineer, frontend-engineer, full-stack-engineer, performance-engineer, product-manager, product-owner, production-support-engineer, release-manager, technical-support-engineer, technical-writer, vendor-management-specialist.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
