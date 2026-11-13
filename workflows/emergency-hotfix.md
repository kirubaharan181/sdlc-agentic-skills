# Emergency Hotfix

> **Purpose:** mitigate active customer impact under emergency control

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to mitigate active customer impact under emergency control. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Establish incident command** — complete the relevant mapped stages and retain evidence.
2. **Apply safe mitigation** — complete the relevant mapped stages and retain evidence.
3. **Constrain minimal patch** — complete the relevant mapped stages and retain evidence.
4. **Authorize and deploy expedited fix** — complete the relevant mapped stages and retain evidence.
5. **Verify recovery and retrospective** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 42, 162, 163, 66, 67, 69, 79, 86, 124, 129, 133, 138, 165. Accountable roles: incident-manager, backend-engineer, release-manager, sre. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
