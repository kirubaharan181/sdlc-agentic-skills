# Rollback

> **Purpose:** return service to a known-safe version or forward fix

## Trigger and required inputs
A request requires the controlled lifecycle to return service to a known-safe version or forward fix.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Confirm trigger

**Accountable role:** incident-manager

**Execution:** Validate the rollback trigger against telemetry, customer impact and release timeline; distinguish transient noise from sustained failure. Workflow-specific control: Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.

**Required evidence:**
- trigger evidence
- impact statement
- decision owner
- workflow-specific safety/control evidence

**Exit criteria:** Rollback is justified by a defined threshold and authorized decision.

### 2. Assess data-state safety

**Accountable role:** deployment-engineer

**Execution:** Check schema compatibility, writes after release, irreversible side effects, external messages and backup/restore state before reverting. Workflow-specific control: Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.

**Required evidence:**
- data compatibility assessment
- side-effect inventory
- recovery options
- workflow-specific safety/control evidence

**Exit criteria:** Chosen recovery will not corrupt or silently discard committed data.

### 3. Authorize rollback/forward fix

**Accountable role:** database-administrator

**Execution:** Present blast radius, data risk, recovery time and options to the incident/change authority; record the selected path. Workflow-specific control: Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.

**Required evidence:**
- recovery decision
- approval record
- operator assignments
- workflow-specific safety/control evidence

**Exit criteria:** Named authority accepts the selected rollback or forward-fix path.

### 4. Execute recovery

**Accountable role:** sre

**Execution:** Restore the last known-good version or apply a bounded forward fix, then reconcile data and dependencies. Workflow-specific control: Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.

**Required evidence:**
- recovery execution log
- artifact/version identity
- data reconciliation
- workflow-specific safety/control evidence

**Exit criteria:** System returns to a known-good state with integrity verified.

### 5. Verify and communicate

**Accountable role:** sre

**Execution:** Validate customer journeys, service health and data integrity; issue factual status and document residual risk. Workflow-specific control: Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.

**Required evidence:**
- recovery verification
- final status update
- follow-up actions
- workflow-specific safety/control evidence

**Exit criteria:** Service owner confirms recovery and accepts remaining risk.


## Stage set and accountable roles
Stage IDs: 42, 137, 133, 132, 138, 147, 163, 165
Accountable roles: incident-manager, deployment-engineer, database-administrator, sre
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.
**Recovery:** Check data/schema compatibility and irreversible side effects before rollback; choose rollback versus forward-fix explicitly; verify user-facing recovery and preserve incident evidence.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
