# Existing Application Enhancement

> **Purpose:** safely extend an existing product

## Trigger and required inputs
A request requires the controlled lifecycle to safely extend an existing product.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Assess current behavior

**Accountable role:** product-owner

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action.

**Required evidence:**
- baseline and scope record
- assumptions and risk log

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 2. Refine compatibility scope

**Accountable role:** software-architect

**Execution:** Complete the refine compatibility scope phase with explicit inputs, accountable owner, recorded decisions and verifiable outcome.

**Required evidence:**
- phase work product
- verification evidence
- handoff record

**Exit criteria:** The accountable owner accepts the output and all blocking issues have an owner.

### 3. Implement bounded enhancement

**Accountable role:** full-stack-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Regression/security review

**Accountable role:** qa-lead

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Measure outcome

**Accountable role:** qa-lead

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 4, 11, 13, 14, 23, 34, 37, 39, 44, 53, 54, 67, 68, 69, 79, 80, 85, 95, 109, 119, 131, 176
Accountable roles: product-owner, software-architect, full-stack-engineer, qa-lead
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested.
**Recovery:** Use the documented rollback, forward-fix, recovery or compensation plan for the changed state.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
