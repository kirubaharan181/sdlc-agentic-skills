# Environment Configuration

> **Purpose:** apply configuration safely across environments

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to apply configuration safely across environments. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Classify sensitivity** — complete the relevant mapped stages and retain evidence.
2. **Prepare scoped delta** — complete the relevant mapped stages and retain evidence.
3. **Validate resolution** — complete the relevant mapped stages and retain evidence.
4. **Apply protected change** — complete the relevant mapped stages and retain evidence.
5. **Verify/document** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 49, 50, 118, 120, 103, 107, 121, 67, 79, 99, 110, 131. Accountable roles: devops-engineer, application-security-engineer, deployment-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
