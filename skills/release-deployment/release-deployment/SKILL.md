---
name: release-deployment
description: Provides a specialist procedure to promote an approved immutable candidate and verify service recovery. Use when the work involves Release Planning, Release Notes, Release Readiness, Change Approval, Staging Deployment, Staging Validation, Database Migration, Production Deployment and 6 more stages.
---

# Release and deployment control

Promote an approved immutable candidate and verify service recovery.

## Procedure
1. Confirm release scope, candidate digest, compatibility, tests and open risks.
2. Validate staging, migration, backup, monitoring, rollback and communications.
3. Obtain named change authority and execute protected progressive rollout.
4. Verify health/business signals and close or recover with evidence.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

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

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, bug-fix, database-migration, disaster-recovery, emergency-hotfix, existing-application-enhancement, feature-development, incident-response, new-product-development, production-release, rollback, staging-release.
- Roles: application-security-engineer, automation-qa-engineer, cloud-engineer, database-administrator, database-engineer, deployment-engineer, devops-engineer, network-engineer, project-manager, qa-lead, release-manager, sre, technical-writer.
