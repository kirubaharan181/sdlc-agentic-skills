# Performance Optimization

> **Purpose:** improve measured system performance

## Trigger and required inputs
A request requires the controlled lifecycle to improve measured system performance.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Baseline workload

**Accountable role:** performance-engineer

**Execution:** Complete the baseline workload phase with explicit inputs, accountable owner, recorded decisions and verifiable outcome.

**Required evidence:**
- phase work product
- verification evidence
- handoff record

**Exit criteria:** The accountable owner accepts the output and all blocking issues have an owner.

### 2. Profile bottleneck

**Accountable role:** backend-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 3. Implement measured improvement

**Accountable role:** database-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Load/regression verify

**Accountable role:** sre

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Monitor capacity

**Accountable role:** sre

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 174, 189
Accountable roles: performance-engineer, backend-engineer, database-engineer, sre
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
