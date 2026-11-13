# Performance Optimization

> **Purpose:** improve measured system performance

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to improve measured system performance. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Baseline workload** — complete the relevant mapped stages and retain evidence.
2. **Profile bottleneck** — complete the relevant mapped stages and retain evidence.
3. **Implement measured improvement** — complete the relevant mapped stages and retain evidence.
4. **Load/regression verify** — complete the relevant mapped stages and retain evidence.
5. **Monitor capacity** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 65, 91, 92, 93, 94, 161, 174, 166. Accountable roles: performance-engineer, backend-engineer, database-engineer, sre. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
