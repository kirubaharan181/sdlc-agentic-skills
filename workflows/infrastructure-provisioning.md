# Infrastructure Provisioning

> **Purpose:** provision reviewed infrastructure from desired state

## Trigger and required inputs
A request requires the controlled lifecycle to provision reviewed infrastructure from desired state.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Design desired state

**Accountable role:** cloud-architect

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible. Workflow-specific control: Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.

**Required evidence:**
- change/design artifact
- execution log
- review evidence
- workflow-specific safety/control evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 2. Review IaC/network/security

**Accountable role:** infrastructure-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 3. Plan approved change

**Accountable role:** network-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible. Workflow-specific control: Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.

**Required evidence:**
- change/design artifact
- execution log
- review evidence
- workflow-specific safety/control evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Provision and verify drift

**Accountable role:** cloud-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Handoff operations

**Accountable role:** cloud-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 28, 47, 48, 51, 99, 103, 110, 116, 117, 120, 121, 122, 123, 140, 141, 142, 143, 144, 145, 146, 149, 150, 151, 152, 189
Accountable roles: cloud-architect, infrastructure-engineer, network-engineer, cloud-engineer
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.
**Recovery:** Review IaC plan, state locking, IAM/network exposure, cost/quota and drift; require approved change window and tested recovery before apply.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
