# Database Migration

> **Purpose:** change schema/data safely with reconciled state

## Trigger and required inputs
A request requires the controlled lifecycle to change schema/data safely with reconciled state.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Assess schema/data impact

**Accountable role:** database-architect

**Execution:** Inventory schema consumers, data volume, locks, write patterns, retention and compatibility across old/new application versions. Workflow-specific control: Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.

**Required evidence:**
- schema impact map
- data volume and lock estimate
- compatibility matrix
- workflow-specific safety/control evidence

**Exit criteria:** Application and data owners accept the impact and migration sequence.

### 2. Rehearse backup and restore

**Accountable role:** database-administrator

**Execution:** Take a representative backup, restore it into an isolated environment and measure integrity, duration, permissions and RPO/RTO. Workflow-specific control: Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.

**Required evidence:**
- backup artifact identity
- restore log
- integrity reconciliation
- RPO/RTO result
- workflow-specific safety/control evidence

**Exit criteria:** Restore succeeds and reconciled data meets recovery objectives before production migration.

### 3. Test compatibility and integrity

**Accountable role:** database-engineer

**Execution:** Run old/new application compatibility tests, migration dry-run, constraint checks and representative read/write reconciliation. Workflow-specific control: Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.

**Required evidence:**
- compatibility test report
- dry-run output
- row/count/checksum reconciliation
- workflow-specific safety/control evidence

**Exit criteria:** No unexplained data loss, duplicate key or incompatible consumer behavior remains.

### 4. Execute approved window

**Accountable role:** release-manager

**Execution:** Verify change ticket, approver, backup freshness, operator roles and stop conditions; execute one observable migration step at a time. Workflow-specific control: Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.

**Required evidence:**
- approval and window record
- operator execution log
- pre/post migration checks
- workflow-specific safety/control evidence

**Exit criteria:** Execution remains within the approved window and every step has a recorded outcome.

### 5. Reconcile and monitor

**Accountable role:** release-manager

**Execution:** Compare source/target counts, checksums, constraints and application behavior; monitor latency, errors and replication lag through the observation window. Workflow-specific control: Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.

**Required evidence:**
- reconciliation report
- monitoring snapshot
- residual discrepancy log
- workflow-specific safety/control evidence

**Exit criteria:** Discrepancies are resolved or explicitly accepted by the data owner; service health is stable.


## Stage set and accountable roles
Stage IDs: 26, 58, 91, 122, 132, 137, 147, 148, 67, 79, 80, 91, 129, 130, 131, 133, 138
Accountable roles: database-architect, database-administrator, database-engineer, release-manager
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.
**Recovery:** Require a tested backup and restore, schema compatibility across rolling application versions, migration rehearsal on representative data, row/count/checksum reconciliation, lock/downtime assessment and an approved stop/forward-fix plan.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
