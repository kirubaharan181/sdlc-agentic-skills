# Production Release

> **Purpose:** release an exact approved artifact progressively

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to release an exact approved artifact progressively. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Confirm artifact/readiness** — complete the relevant mapped stages and retain evidence.
2. **Obtain change approval** — complete the relevant mapped stages and retain evidence.
3. **Progressively roll out** — complete the relevant mapped stages and retain evidence.
4. **Validate health/business outcomes** — complete the relevant mapped stages and retain evidence.
5. **Confirm or roll back** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 126, 127, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139, 86, 109. Accountable roles: release-manager, deployment-engineer, sre, product-owner. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
