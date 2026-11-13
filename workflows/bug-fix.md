# Bug Fix

> **Purpose:** restore a defective behavior with minimal change

## Trigger and required inputs
A request requires the controlled lifecycle to restore a defective behavior with minimal change.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Triage severity and impact

**Accountable role:** production-support-engineer

**Execution:** Classify urgency using customer impact, blast radius, data integrity and security exposure; assign incident/request owner, severity, response SLA and stop conditions.

**Required evidence:**
- severity rationale
- affected-version/cohort list
- owner and response timeline

**Exit criteria:** Severity and escalation owner are accepted; unsafe changes are prohibited until impact is understood.

### 2. Reproduce and isolate root cause

**Accountable role:** backend-engineer

**Execution:** Reproduce on the affected revision/environment, correlate logs and recent changes, and isolate the smallest failing condition without modifying production state.

**Required evidence:**
- minimal reproduction
- correlated diagnostics
- hypothesis log

**Exit criteria:** A root-cause hypothesis is supported by reproducible evidence or explicitly marked inconclusive.

### 3. Implement minimal correction

**Accountable role:** code-reviewer

**Execution:** Change only the failing behavior, preserve existing contracts, add a regression assertion and avoid unrelated refactoring.

**Required evidence:**
- minimal patch
- regression test
- diff risk note

**Exit criteria:** The regression test fails before the fix and passes after it; unrelated behavior remains unchanged.

### 4. Run regression and review

**Accountable role:** qa-lead

**Execution:** Run focused and impacted regression suites, inspect the exact diff, and obtain independent review for correctness, security and compatibility.

**Required evidence:**
- test report
- review findings
- unresolved-risk list

**Exit criteria:** Critical regression and review findings are closed or explicitly block release.

### 5. Deploy and verify

**Accountable role:** qa-lead

**Execution:** Promote the approved artifact, deploy using the authorized change path, and verify health and user-facing behavior against stop thresholds.

**Required evidence:**
- deployment record
- health metrics
- customer verification

**Exit criteria:** Service behavior and health remain within thresholds for the agreed observation window.


## Stage set and accountable roles
Stage IDs: 42, 96, 162, 163, 164, 170, 66, 67, 68, 69, 79, 85, 86, 124, 133, 138, 179
Accountable roles: production-support-engineer, backend-engineer, code-reviewer, qa-lead
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
