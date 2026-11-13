# New Product Development

> **Purpose:** discover to operate a new product

## Trigger and required inputs
A request requires the controlled lifecycle to discover to operate a new product.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Frame opportunity

**Accountable role:** product-manager

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action.

**Required evidence:**
- baseline and scope record
- assumptions and risk log

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 2. Validate requirements

**Accountable role:** software-architect

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action.

**Required evidence:**
- baseline and scope record
- assumptions and risk log

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 3. Design architecture

**Accountable role:** full-stack-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Build and verify

**Accountable role:** qa-lead

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 5. Release and operate

**Accountable role:** release-manager

**Execution:** Complete the release and operate phase with explicit inputs, accountable owner, recorded decisions and verifiable outcome.

**Required evidence:**
- phase work product
- verification evidence
- handoff record

**Exit criteria:** The accountable owner accepts the output and all blocking issues have an owner.


## Stage set and accountable roles
Stage IDs: 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 29, 30, 31, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 188
Accountable roles: product-manager, software-architect, full-stack-engineer, qa-lead, release-manager
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
