# Database Migration

> **Purpose:** change schema/data safely with reconciled state

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to change schema/data safely with reconciled state. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Assess schema/data impact** — complete the relevant mapped stages and retain evidence.
2. **Rehearse backup and restore** — complete the relevant mapped stages and retain evidence.
3. **Test compatibility and integrity** — complete the relevant mapped stages and retain evidence.
4. **Execute approved window** — complete the relevant mapped stages and retain evidence.
5. **Reconcile and monitor** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 26, 58, 91, 122, 132, 137, 147, 148, 67, 79, 80, 91, 129, 130, 131, 133, 138. Accountable roles: database-architect, database-administrator, database-engineer, release-manager. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
