# Bug Fix

> **Purpose:** restore a defective behavior with minimal change

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to restore a defective behavior with minimal change. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Triage severity and impact** — complete the relevant mapped stages and retain evidence.
2. **Reproduce and isolate root cause** — complete the relevant mapped stages and retain evidence.
3. **Implement minimal correction** — complete the relevant mapped stages and retain evidence.
4. **Run regression and review** — complete the relevant mapped stages and retain evidence.
5. **Deploy and verify** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 42, 96, 162, 163, 164, 170, 66, 67, 68, 69, 79, 85, 86, 124, 133, 138, 179. Accountable roles: production-support-engineer, backend-engineer, code-reviewer, qa-lead. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
