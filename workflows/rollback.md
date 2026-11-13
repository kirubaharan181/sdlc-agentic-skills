# Rollback

> **Purpose:** return service to a known-safe version or forward fix

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to return service to a known-safe version or forward fix. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Confirm trigger** — complete the relevant mapped stages and retain evidence.
2. **Assess data-state safety** — complete the relevant mapped stages and retain evidence.
3. **Authorize rollback/forward fix** — complete the relevant mapped stages and retain evidence.
4. **Execute recovery** — complete the relevant mapped stages and retain evidence.
5. **Verify and communicate** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 42, 137, 133, 132, 138, 147, 163, 165. Accountable roles: incident-manager, deployment-engineer, database-administrator, sre. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
