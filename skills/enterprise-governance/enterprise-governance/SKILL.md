---
name: enterprise-governance
description: "Use when overseeing controls: policy, quality, security, access, change, vendor, cost audits. Do NOT use to do the audited work."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["governance", "audit", "compliance", "finops"]
---

# Enterprise engineering governance

## Purpose
Provides independent oversight across the engineering organization: governance of engineering, quality, security, access, compliance, documentation, change, vendors and cost, and process improvement. It owns stages 181-190 and verifies controls from system evidence rather than from descriptions.

## When to Use
- Policies need turning into testable controls and measured compliance.
- An audit, access review or vendor review is needed.
- Governance gaps need owners, dates and verified closure.

## When NOT to Use
- Doing the audited work itself: use the specialist skill.
- Approving a production change: use secure-change-control.
- Setting up one repository: use engineering-governance.

## Prerequisites and Requirements
- Read access to the evidence the review needs.
- A control framework or policy set.
- Agreed scope of review.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- policy or control framework
- evidence sources
- scope

Optional inputs:
- previous findings
- exceptions register
- cost and vendor data

Outputs and deliverables:
- control catalogue with data sources
- compliance or audit report with samples
- findings with owners and dates
- exception register with expiry
- improvement actions verified for effect

## Procedure
1. Map policy obligations to accountable owners, repositories and evidence sources.
2. Sample operating evidence and distinguish design from operating effectiveness.
3. Manage risk-based exceptions with compensating controls and expiry.
4. Report control health, supplier/cost/access issues and corrective action closure.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Control cannot be measured | Rewrite it as testable or drop it. |
| Finding closed by statement only | Reopen and require fresh evidence. |
| Exception has no expiry | Add expiry and a renewal decision. |
| Auditor lacks access | Reduce scope formally or request access. |

## Quality Gates
- [ ] Evidence comes from systems, not descriptions
- [ ] Samples cover the review period
- [ ] Findings have owners and dates
- [ ] Closure is verified

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Review access
```text
Request: Run a quarterly access review for the production database.
Context: Role list and an access export are available.
Agent behavior: Compare actual access with approved roles, flag excess, and require owner confirmation.
Output: Access review report with removals and owners.
Acceptance: Every excess access has an owner decision.
```

### Example 2: Audit change records
```text
Request: Check that production deployments have change records.
Context: A month of deployments is available.
Agent behavior: Reconcile deployments to records and list gaps.
Output: Reconciliation with 6 of 410 unrecorded deployments and actions.
Acceptance: Each gap has an owner and a fix date.
```

## Limitations
- Findings reflect only the evidence provided and the period sampled.
- Does not certify compliance with any standard.
- Risk acceptance is decided by a named human.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Evidence outdated | Dated outside the period | Collect current evidence. |
| Repeated finding | Root cause not fixed | Escalate for a structural fix. |
| Scope too large | Too many systems | Sample by risk and state the sampling method. |

## Tools
- GRC/control repository
- audit workpapers
- repository policy settings
- FinOps/vendor evidence

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 181 | Engineering Governance | complete | Engineering Governance Specialist |
| 182 | Quality Governance | complete | Quality Governance Specialist |
| 183 | Security Governance | complete | Security Auditor |
| 184 | Access Governance | complete | Compliance Specialist |
| 185 | Compliance Auditing | complete | Security Auditor |
| 186 | Documentation Governance | complete | Documentation Engineer |
| 187 | Change Governance | complete | Engineering Governance Specialist |
| 188 | Vendor Management | complete | Vendor Management Specialist |
| 189 | FinOps Governance | complete | FinOps Specialist |
| 190 | Process Improvement | complete | Process Improvement Specialist |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `engineering-governance`: policy requirements and control gaps
- `project-agile-management`: improvement actions for planning
- `evidence-quality-gates`: evidence sets for quality evaluation

Receives from:
- `application-security`: security evidence for audit
- `business-product-management`: contract and compliance obligations register
- `cloud-hosting-operations`: cost and resource evidence
- `engineering-governance`: repository control inventory
- `evidence-quality-gates`: evidence assessments for audits
- `maintenance-support`: patch and lifecycle evidence
- `project-agile-management`: change and risk records for audit
- `quality-assurance`: test evidence for quality audits
- `secure-change-control`: change records and exceptions for audit
- `sre-observability`: SLO and incident evidence for review

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: documentation-update, infrastructure-provisioning, new-product-development, product-retirement, root-cause-analysis.
- Roles: compliance-specialist, documentation-engineer, engineering-coordinator, engineering-governance-specialist, finops-specialist, process-improvement-specialist, program-manager, qa-lead, quality-governance-specialist, release-manager, security-auditor, technical-writer, vendor-management-specialist.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
