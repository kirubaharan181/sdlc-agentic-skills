# Infrastructure Provisioning

> **Purpose:** provision reviewed infrastructure from desired state

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to provision reviewed infrastructure from desired state. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Design desired state** — complete the relevant mapped stages and retain evidence.
2. **Review IaC/network/security** — complete the relevant mapped stages and retain evidence.
3. **Plan approved change** — complete the relevant mapped stages and retain evidence.
4. **Provision and verify drift** — complete the relevant mapped stages and retain evidence.
5. **Handoff operations** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 28, 103, 117, 120, 121, 140, 146, 149, 150, 152, 67, 69, 99, 110. Accountable roles: cloud-architect, infrastructure-engineer, network-engineer, cloud-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
