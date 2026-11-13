# Dependency Update

> **Purpose:** update a dependency without compatibility regression

## Trigger and required inputs
A request requires the controlled lifecycle to update a dependency without compatibility regression.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Inventory advisories

**Accountable role:** devsecops-engineer

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action. Workflow-specific control: Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.

**Required evidence:**
- baseline and scope record
- assumptions and risk log
- workflow-specific safety/control evidence

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 2. Assess compatibility/license

**Accountable role:** backend-engineer

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action. Workflow-specific control: Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.

**Required evidence:**
- baseline and scope record
- assumptions and risk log
- workflow-specific safety/control evidence

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 3. Update provenance

**Accountable role:** license-compliance-specialist

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible. Workflow-specific control: Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.

**Required evidence:**
- change/design artifact
- execution log
- review evidence
- workflow-specific safety/control evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Regression/security test

**Accountable role:** automation-qa-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Release and monitor

**Accountable role:** automation-qa-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 72, 101, 108, 171, 172, 67, 69, 79, 80, 85, 110, 119, 131, 179
Accountable roles: devsecops-engineer, backend-engineer, license-compliance-specialist, automation-qa-engineer
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.
**Recovery:** Verify provenance, changelog and advisory impact; inspect transitive dependency/license changes; run regression and security checks; pin the resolved version and document rollback.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
