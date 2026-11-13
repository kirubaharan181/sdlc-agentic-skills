# Staging Release

> **Purpose:** promote a release candidate through staging evidence

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to promote a release candidate through staging evidence. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Select immutable candidate** — complete the relevant mapped stages and retain evidence.
2. **Deploy staging** — complete the relevant mapped stages and retain evidence.
3. **Run validation suite** — complete the relevant mapped stages and retain evidence.
4. **Record readiness** — complete the relevant mapped stages and retain evidence.
5. **Promote/reject** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 126, 127, 128, 129, 130, 131, 138, 139, 77, 86, 95, 109. Accountable roles: release-manager, deployment-engineer, qa-lead, application-security-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
