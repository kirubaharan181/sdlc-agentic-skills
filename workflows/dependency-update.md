# Dependency Update

> **Purpose:** update a dependency without compatibility regression

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to update a dependency without compatibility regression. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Inventory advisories** — complete the relevant mapped stages and retain evidence.
2. **Assess compatibility/license** — complete the relevant mapped stages and retain evidence.
3. **Update provenance** — complete the relevant mapped stages and retain evidence.
4. **Regression/security test** — complete the relevant mapped stages and retain evidence.
5. **Release and monitor** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 72, 101, 108, 171, 172, 67, 69, 79, 80, 85, 110, 119, 131, 179. Accountable roles: devsecops-engineer, backend-engineer, license-compliance-specialist, automation-qa-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
