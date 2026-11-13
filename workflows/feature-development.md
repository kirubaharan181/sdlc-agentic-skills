# Feature Development

> **Purpose:** deliver one bounded customer capability

## Trigger and required inputs
A request requires the controlled lifecycle to deliver one bounded customer capability.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Define acceptance

**Accountable role:** product-owner

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action.

**Required evidence:**
- baseline and scope record
- assumptions and risk log

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 2. Design contracts

**Accountable role:** api-architect

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 3. Implement vertical slice

**Accountable role:** full-stack-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Review and verify

**Accountable role:** automation-qa-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Release and learn

**Accountable role:** automation-qa-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 3, 4, 5, 6, 7, 8, 11, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 25, 27, 30, 31, 32, 33, 36, 37, 38, 39, 40, 41, 42, 43, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 74, 75, 76, 78, 79, 80, 81, 82, 83, 84, 85, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97
Accountable roles: product-owner, api-architect, full-stack-engineer, automation-qa-engineer
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
