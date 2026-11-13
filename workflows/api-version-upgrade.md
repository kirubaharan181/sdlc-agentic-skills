# Api Version Upgrade

> **Purpose:** evolve an API while protecting consumers

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to evolve an API while protecting consumers. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Inventory consumers** — complete the relevant mapped stages and retain evidence.
2. **Design version and migration** — complete the relevant mapped stages and retain evidence.
3. **Implement compatibility** — complete the relevant mapped stages and retain evidence.
4. **Run contract/security tests** — complete the relevant mapped stages and retain evidence.
5. **Publish and deprecate** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 27, 57, 81, 105, 132, 13, 14, 67, 69, 80, 81, 109, 126, 127, 131, 176. Accountable roles: api-architect, api-engineer, integration-engineer, api-testing-specialist. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
