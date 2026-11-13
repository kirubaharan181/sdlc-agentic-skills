# Feature Development

> **Purpose:** deliver one bounded customer capability

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to deliver one bounded customer capability. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Define acceptance** — complete the relevant mapped stages and retain evidence.
2. **Design contracts** — complete the relevant mapped stages and retain evidence.
3. **Implement vertical slice** — complete the relevant mapped stages and retain evidence.
4. **Review and verify** — complete the relevant mapped stages and retain evidence.
5. **Release and learn** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 4, 11, 13, 14, 17, 18, 23, 27, 37, 39, 53, 54, 57, 67, 68, 69, 79, 80, 84, 85, 95, 109, 119, 131, 176. Accountable roles: product-owner, api-architect, full-stack-engineer, automation-qa-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
