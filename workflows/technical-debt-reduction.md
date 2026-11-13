# Technical Debt Reduction

> **Purpose:** reduce a documented debt hotspot without behavior loss

## Trigger and required inputs
Trigger: A request requires the controlled lifecycle to reduce a documented debt hotspot without behavior loss. Inputs: named request and owner, risk/impact classification, relevant artifact or environment reference.

## Lifecycle phases
1. **Identify debt hotspot** — complete the relevant mapped stages and retain evidence.
2. **Plan safe refactor** — complete the relevant mapped stages and retain evidence.
3. **Add characterization tests** — complete the relevant mapped stages and retain evidence.
4. **Review regression** — complete the relevant mapped stages and retain evidence.
5. **Track remaining debt** — complete the relevant mapped stages and retain evidence.

## Stage set and accountable roles
Stage IDs: 70, 76, 175, 37, 67, 69, 79, 85, 190. Accountable roles: software-architect, full-stack-engineer, code-reviewer, qa-lead. Required skills: master-orchestration, evidence-quality-gates, secure-change-control.

## Gates, rollback and communication
Gates: scope-and-risk, quality-evidence, security-disposition. Use the documented rollback, forward-fix, recovery, or compensation plan appropriate to the changed state. Keep request owner, affected operators and approval authority informed at phase boundaries and immediately on material risk.

## Failure path and completion
Stop unsafe progression, preserve diagnostics, communicate impact, create remediation or compensation work, and re-evaluate with new evidence. Complete only when: All required stages have PASS evidence or a valid, time-bound approved waiver; ownership and residual risk are accepted.

## Example
For this workflow, create the evidence bundle before asking for a gate decision; if a prerequisite fails, communicate the impact and execute the documented remediation/compensation route rather than advancing on assumption.
