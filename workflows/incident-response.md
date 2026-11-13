# Incident Response

> **Purpose:** contain and recover from an operational incident

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to contain and recover from an operational incident. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Assign commander/severity** — complete the relevant mapped stages and retain evidence.
2. **Assess impact/timeline** — complete the relevant mapped stages and retain evidence.
3. **Contain and investigate** — complete the relevant mapped stages and retain evidence.
4. **Recover and verify** — complete the relevant mapped stages and retain evidence.
5. **Handoff and postmortem** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 158, 162, 163, 164, 165, 167, 168, 169, 138. Accountable roles: incident-manager, sre, observability-engineer, production-support-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
