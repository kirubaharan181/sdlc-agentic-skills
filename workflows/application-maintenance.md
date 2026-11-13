# Application Maintenance

> **Purpose:** operate and improve a live application

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to operate and improve a live application. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Triage maintenance demand** — complete the relevant mapped stages and retain evidence.
2. **Diagnose impact** — complete the relevant mapped stages and retain evidence.
3. **Patch/update safely** — complete the relevant mapped stages and retain evidence.
4. **Verify and publish knowledge** — complete the relevant mapped stages and retain evidence.
5. **Plan maintenance release** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 167, 168, 169, 170, 171, 172, 173, 174, 176, 178, 179, 180. Accountable roles: production-support-engineer, technical-support-engineer, backend-engineer, release-manager. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
