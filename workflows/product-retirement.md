# Product Retirement

> **Purpose:** retire a product with consumer and data obligations closed

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to retire a product with consumer and data obligations closed. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Approve EOL** — complete the relevant mapped stages and retain evidence.
2. **Inventory consumers/data/vendors** — complete the relevant mapped stages and retain evidence.
3. **Migrate and communicate** — complete the relevant mapped stages and retain evidence.
4. **Stage shutdown** — complete the relevant mapped stages and retain evidence.
5. **Close audit and support** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 9, 10, 134, 144, 147, 148, 167, 177, 180, 185, 187. Accountable roles: product-manager, vendor-management-specialist, compliance-specialist, technical-support-engineer. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
