---
name: release-deployment
description: "Use when promoting a build to staging or production: plans, approves, verifies. Do NOT use for building pipelines."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["release", "deployment", "rollback", "change-approval"]
---

# Release and deployment control

## Purpose
Controls how a tested build reaches users: release planning and notes, readiness, change approval, staging and production deployment, migrations, DNS, TLS, load balancing, rollback planning, smoke tests and sign-off. It owns stages 126-139 and never treats an agent as the approver of production changes.

## When to Use
- A release needs planning, readiness review or notes.
- A build must be deployed to staging or production with verification.
- A migration, rollback or cutover plan is needed.

## When NOT to Use
- Creating the pipeline itself: use devops-platform.
- Governing risky production changes in general: use secure-change-control.
- Running day-to-day cloud operations: use cloud-hosting-operations.

## Prerequisites and Requirements
- Test and security sign-off for the build under release.
- A named human approver for production.
- A tested rollback path and a change window.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- release candidate identifier
- test and security sign-offs
- rollback plan

Optional inputs:
- migration scripts
- release notes draft
- traffic and capacity data

Outputs and deliverables:
- release plan and readiness record
- release notes
- approval record with a named human
- deployment and smoke test evidence
- deployment sign-off or rollback record

## Procedure
1. Confirm release scope, candidate digest, compatibility, tests and open risks.
2. Validate staging, migration, backup, monitoring, rollback and communications.
3. Obtain named change authority and execute protected progressive rollout.
4. Verify health/business signals and close or recover with evidence.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Sign-off is for a different build | Stop; require evidence for the candidate. |
| No tested rollback | Block production until one is tested. |
| Migration is not backward compatible | Split into expand then contract releases. |
| Smoke test fails | Roll back by the plan and record the failure. |

## Quality Gates
- [ ] Build identifiers match across evidence
- [ ] A named human approved production
- [ ] Rollback was tested
- [ ] Smoke test result is recorded

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Readiness review
```text
Request: Is release 2.8 ready for production?
Context: Tests passed on build 2.8.0-rc3; security sign-off references rc2.
Agent behavior: Compare build identifiers across evidence, find the mismatch, and mark readiness BLOCKED until the security evidence matches.
Output: Readiness record with BLOCKED status and the missing evidence.
Acceptance: No production approval is requested until identifiers match.
```

### Example 2: Plan a safe migration
```text
Request: Plan the column rename migration.
Context: Hot table, zero downtime required.
Agent behavior: Plan expand and contract: add column, backfill in batches, switch reads, then drop later.
Output: Two-release migration plan with rollback at each step.
Acceptance: Each step is reversible and has a verification query.
```

## Limitations
- Cannot deploy or approve on its own authority: production needs a named human.
- Cannot verify live production without access; it records the checks to run.
- Rollback assumes data compatibility has been tested.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Approver unavailable | Window at risk | Do not proceed; reschedule or use the documented delegate. |
| Smoke test flaky | Unstable check | Fix the check; do not ignore a failure. |
| Release notes incomplete | Changes not tracked | Generate from merged changes and have the owner review. |

## Tools
- release management
- artifact registry
- deployment and health dashboards
- rollback runbooks

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 126 | Release Planning | complete | Release Manager |
| 127 | Release Notes | complete | Release Manager |
| 128 | Release Readiness | complete | Release Manager |
| 129 | Change Approval | complete | Release Manager |
| 130 | Staging Deployment | complete | Deployment Engineer |
| 131 | Staging Validation | complete | QA Lead |
| 132 | Database Migration | complete | Database Administrator |
| 133 | Production Deployment | complete | Deployment Engineer |
| 134 | Domain & DNS | complete | Cloud Engineer |
| 135 | SSL/TLS Setup | complete | Network Engineer |
| 136 | Load Balancer Setup | complete | Network Engineer |
| 137 | Rollback Planning | complete | Release Manager |
| 138 | Production Smoke Test | complete | SRE |
| 139 | Deployment Sign-off | complete | Release Manager |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `cloud-hosting-operations`: deployed release and environment changes
- `sre-observability`: release markers and rollback criteria for monitoring
- `maintenance-support`: release notes and known issues

Receives from:
- `application-security`: security sign-off and open accepted risks
- `definition-of-done`: completion statement for release readiness
- `devops-platform`: deployable artifacts and pipeline run records
- `evidence-quality-gates`: gate decisions for release readiness
- `project-agile-management`: release scope and dependency list
- `quality-assurance`: test sign-off with exit criteria scorecard
- `secure-change-control`: approved change with window and rollback

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: api-version-upgrade, bug-fix, database-migration, disaster-recovery, emergency-hotfix, existing-application-enhancement, feature-development, incident-response, new-product-development, production-release, rollback, staging-release.
- Roles: application-security-engineer, automation-qa-engineer, cloud-engineer, database-administrator, database-engineer, deployment-engineer, devops-engineer, network-engineer, project-manager, qa-lead, release-manager, sre, technical-writer.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
