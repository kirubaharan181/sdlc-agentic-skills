---
name: cloud-hosting-operations
description: Operates cloud compute, storage, network, DR and cost. Use when managing hosted infrastructure. Do NOT use for pipelines or app changes.
metadata:
  author: kirubaharan181
  version: "1.1.0"
  tags: ["cloud", "infrastructure", "disaster-recovery", "finops"]
---

# Cloud and infrastructure operations

## Purpose
Keeps hosted infrastructure available, recoverable and cost-aware: compute, databases, storage, DNS, certificates, networks, backups, disaster recovery, high availability, scaling, cost and maintenance. It owns stages 140-152.

## When to Use
- Cloud resources need managing, patching or right-sizing.
- Backups, disaster recovery or high availability must be designed or tested.
- Certificates, DNS or network operations need controlled change.

## When NOT to Use
- Building pipelines: use devops-platform.
- Monitoring and alert design: use sre-observability.
- Approving changes: use secure-change-control.

## Prerequisites and Requirements
- Cloud account access at the least privilege needed.
- Resource inventory and ownership tags.
- Recovery objectives (RPO and RTO).
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- resource inventory
- recovery objectives

Optional inputs:
- usage and cost data
- incident history
- change calendar

Outputs and deliverables:
- right-sizing and idle-resource reports
- tested backup and restore records
- disaster recovery and failover test results
- certificate and DNS inventories with expiry
- cost reports by owner

## Procedure
1. Inventory resources, IAM, network, quotas, data classification and dependencies.
2. Validate backup, patch, encryption, DNS/TLS, scaling and failure-domain controls.
3. Apply reviewed IaC/configuration changes with drift and blast-radius checks.
4. Measure availability, capacity, recovery and unit cost; hand off runbooks.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Resource has no owner tag | Report and assign before any change. |
| Backup never restored | Schedule a restore test before relying on it. |
| Commitment purchase proposed | Size from baseline usage and require the budget owner's approval. |
| Destructive change requested | Require human approval under the approval policy. |

## Quality Gates
- [ ] Restores were tested against recovery objectives
- [ ] Every resource has an owner
- [ ] Certificates have expiry monitoring
- [ ] Cost actions have estimates and owners

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Test a restore
```text
Request: Verify we can restore the orders database.
Context: RPO 15 minutes, RTO 60 minutes.
Agent behavior: Restore the latest backup to a scratch instance, run row-count checks, and time the process.
Output: Restore record: completed in 38 minutes, counts match source.
Acceptance: Measured time and loss are compared with the objectives.
```

### Example 2: Find idle spend
```text
Request: Reduce non-production cost.
Context: Environments run around the clock.
Agent behavior: List idle resources with owners, propose schedules, and estimate savings with assumptions.
Output: Action list with owner confirmation steps and estimated saving.
Acceptance: No resource is stopped without owner confirmation.
```

## Limitations
- Cannot act on accounts it cannot reach; it lists the commands to run.
- Cost figures depend on provider prices and usage that change.
- Destructive and production actions need human approval.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Cannot list resources | Insufficient permissions | Request read access; do not use broader credentials. |
| Restore fails | Backup corrupt or incompatible | Treat as an incident risk, fix the backup process and retest. |
| Certificate expiry missed | No monitoring | Replace now and add staged expiry alerts. |

## Tools
- provider-native tools
- IaC
- cloud security posture
- backup, monitoring and cost telemetry

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 140 | Cloud Hosting | complete | Cloud Engineer |
| 141 | Compute Management | complete | Cloud Engineer |
| 142 | Database Hosting | complete | Database Administrator |
| 143 | Storage Management | complete | Cloud Engineer |
| 144 | DNS Management | complete | Network Engineer |
| 145 | SSL Certificate Management | complete | Cloud Engineer |
| 146 | Network Operations | complete | Network Engineer |
| 147 | Backup Management | complete | Database Administrator |
| 148 | Disaster Recovery | complete | SRE |
| 149 | High Availability | complete | Cloud Architect |
| 150 | Auto Scaling | complete | Infrastructure Engineer |
| 151 | Cost Optimization | complete | FinOps Specialist |
| 152 | Infrastructure Maintenance | complete | Infrastructure Engineer |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `sre-observability`: infrastructure telemetry and capacity data
- `maintenance-support`: infrastructure maintenance windows
- `enterprise-governance`: cost and resource evidence

Receives from:
- `devops-platform`: infrastructure definitions
- `release-deployment`: deployed release and environment changes
- `technical-architecture`: cloud design and recovery objectives

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: application-maintenance, database-migration, disaster-recovery, infrastructure-provisioning, new-product-development, product-retirement.
- Roles: cloud-architect, cloud-engineer, database-administrator, finops-specialist, infrastructure-engineer, network-engineer, performance-engineer, sre.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
