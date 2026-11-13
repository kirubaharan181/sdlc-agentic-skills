# Existing Application Enhancement

> **Purpose:** safely extend an existing product

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to safely extend an existing product. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Assess current behavior** — complete the relevant mapped stages and retain evidence.
2. **Refine compatibility scope** — complete the relevant mapped stages and retain evidence.
3. **Implement bounded enhancement** — complete the relevant mapped stages and retain evidence.
4. **Regression/security review** — complete the relevant mapped stages and retain evidence.
5. **Measure outcome** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 4, 11, 13, 14, 23, 34, 37, 39, 44, 53, 54, 67, 68, 69, 79, 80, 85, 95, 109, 119, 131, 176. Accountable roles: product-owner, software-architect, full-stack-engineer, qa-lead. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
