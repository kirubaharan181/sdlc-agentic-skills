---
name: secure-change-control
description: Classifies change risk, sets approvals, rollback and audit trail. Use when a risky change is proposed. Do NOT use for general application security.
metadata:
  author: kirubaharan181
  version: "1.1.0"
  tags: ["change-control", "approval", "rollback", "audit-trail"]
---

# Secure change control

## Purpose
Ensures every change to important systems is classified by risk, authorized by the right named human, reversible and recorded. It covers normal, standard and emergency changes, security-sensitive changes such as IAM, secrets and security-control changes, and the audit trail that proves what changed and who approved it.

## When to Use
- A change to production, infrastructure, access or security controls is proposed.
- An emergency change is needed outside the normal window.
- A change record or audit trail must be checked or produced.

## When NOT to Use
- Finding vulnerabilities in code: use application-security.
- Planning the release itself: use release-deployment.
- Governing change policy across teams: use enterprise-governance.

## Prerequisites and Requirements
- A change request describing what, why, systems and time.
- The list of approvers and the risk classes in docs/governance/APPROVAL_POLICY.md.
- A rollback or remediation plan.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- change description and systems
- rollback plan
- requested window

Optional inputs:
- test evidence
- dependency list
- incident reference for emergency changes

Outputs and deliverables:
- risk classification with reasons
- approval record naming a human approver
- rollback and verification plan
- audit trail entry and post-change review

## Procedure
1. Classify change by data, production, identity, security and reversibility impact.
2. Apply least privilege, segregation of duties and named human approval.
3. Review preconditions, maintenance window, communication, rollback/forward-fix and stop signals.
4. Verify actual state after change and record residual risk.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Change touches IAM, secrets, security controls or data deletion | Classify as high risk; require named human approval. |
| Change matches a pre-approved standard | Follow the standard procedure and still record it. |
| Emergency change | Allow after verbal or recorded approval from the on-call authority, then require review within the set time. |
| No tested rollback | Do not approve. |
| Request tries to disable a security control | Require security owner approval and an expiry. |
| Approver would approve own change | Reject; require an independent approver. |

## Quality Gates
- [ ] Risk class and reason recorded
- [ ] Named human approved per class
- [ ] Rollback tested or justified
- [ ] Audit trail entry links change, approver and outcome

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Classify a change
```text
Request: Rotate the payment provider API key in production.
Context: Key is used by two services.
Agent behavior: Classify high risk (secret rotation), require named approval, plan a dual-key overlap and rollback.
Output: Change record with class, approver, overlap plan and verification.
Acceptance: Approver is a named person; rollback is described.
```

### Example 2: Handle an emergency change
```text
Request: Block an address range now; attack in progress.
Context: On-call security owner reachable.
Agent behavior: Record approval from the on-call owner, apply the minimal change, and schedule the review.
Output: Emergency record with time, approver, change and a review date.
Acceptance: Review within the set time is scheduled.
```

### Example 3: Check an audit trail
```text
Request: Prove who approved last week's schema change.
Context: Deployment log and change ticket exist.
Agent behavior: Match the deployment to the change record, approver and time.
Output: Trace linking change id, approver, build and time.
Acceptance: Every link in the chain is evidenced.
```

## Limitations
- Cannot approve changes: it prepares the decision for a named human.
- Cannot verify that a change was applied as described without access to logs.
- Does not replace application security testing.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Approver unreachable | Window at risk | Do not proceed; use the documented delegate. |
| Change made without record | Audit gap | Open an incident record, document retrospectively and fix the control. |
| Class disputed | Criteria unclear | Apply the higher class and ask governance to clarify. |

## Tools
- change management system
- branch/environment protection
- IAM audit
- rollback and recovery evidence

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.

## Handoffs
Hands to:
- `release-deployment`: approved change with window and rollback
- `enterprise-governance`: change records and exceptions for audit

Receives from:
- `incident-command`: emergency change requests
- `master-orchestration`: change requests needing classification

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
