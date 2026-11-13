# Disaster Recovery

> **Purpose:** prove recoverability against RTO/RPO objectives

## Trigger and required inputs
A request requires the controlled lifecycle to prove recoverability against RTO/RPO objectives.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Confirm RTO/RPO

**Accountable role:** cloud-engineer

**Execution:** Set business-approved recovery time and point objectives for each critical service/data set. Workflow-specific control: Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.

**Required evidence:**
- RTO/RPO matrix
- business impact rationale
- workflow-specific safety/control evidence

**Exit criteria:** Objectives are measurable, owned and aligned to business impact.

### 2. Prepare isolated recovery

**Accountable role:** database-administrator

**Execution:** Provision clean recovery identities, network and compute isolated from the compromised/failed environment. Workflow-specific control: Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.

**Required evidence:**
- recovery environment plan
- identity/network controls
- access audit
- workflow-specific safety/control evidence

**Exit criteria:** Recovery environment is isolated and access is verified.

### 3. Restore/fail over

**Accountable role:** sre

**Execution:** Restore from selected backup or fail over using documented sequence; capture elapsed time and replication position. Workflow-specific control: Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.

**Required evidence:**
- restore/failover log
- backup identity
- elapsed time
- workflow-specific safety/control evidence

**Exit criteria:** Recovery completes within target or gap is formally recorded.

### 4. Validate integrity

**Accountable role:** incident-manager

**Execution:** Run database checks, application smoke tests and business reconciliation before reopening traffic. Workflow-specific control: Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.

**Required evidence:**
- integrity report
- application validation
- business reconciliation
- workflow-specific safety/control evidence

**Exit criteria:** Data and application state are accepted by owners.

### 5. Measure gaps

**Accountable role:** incident-manager

**Execution:** Compare actual recovery time/data loss with objectives and prioritize resilience improvements. Workflow-specific control: Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.

**Required evidence:**
- RTO/RPO result
- gap register
- improvement actions
- workflow-specific safety/control evidence

**Exit criteria:** Each gap has owner, target date and next exercise.


## Stage set and accountable roles
Stage IDs: 147, 148, 149, 159, 160, 163, 165, 166
Accountable roles: cloud-engineer, database-administrator, sre, incident-manager
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.
**Recovery:** Measure actual RTO/RPO during rehearsal; isolate recovery credentials and environment; validate restored data integrity and application dependencies before declaring recovery.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
