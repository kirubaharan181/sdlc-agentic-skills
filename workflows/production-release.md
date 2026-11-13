# Production Release

> **Purpose:** release an exact approved artifact progressively

## Trigger and required inputs
A request requires the controlled lifecycle to release an exact approved artifact progressively.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Confirm artifact/readiness

**Accountable role:** release-manager

**Execution:** Verify candidate digest, change list, test/security evidence, migrations, observability, release notes and rollback readiness. Workflow-specific control: Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.

**Required evidence:**
- release manifest
- readiness checklist
- open-risk disposition
- workflow-specific safety/control evidence

**Exit criteria:** All mandatory readiness checks are complete against the exact candidate.

### 2. Obtain change approval

**Accountable role:** deployment-engineer

**Execution:** Present impact, schedule, approver, operator, communication, stop criteria and recovery plan to the designated authority. Workflow-specific control: Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.

**Required evidence:**
- change ticket
- approval record
- communication plan
- workflow-specific safety/control evidence

**Exit criteria:** Approval is explicit, scoped and valid for the planned window.

### 3. Progressively roll out

**Accountable role:** sre

**Execution:** Deploy to a canary or smallest supported cohort, observe health/business metrics and expand only when thresholds remain healthy. Workflow-specific control: Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.

**Required evidence:**
- cohort rollout log
- canary metrics
- go/no-go decision
- workflow-specific safety/control evidence

**Exit criteria:** Each expansion has evidence and stop thresholds are not breached.

### 4. Validate health/business outcomes

**Accountable role:** product-owner

**Execution:** Check service SLIs, key user journeys, transaction integrity and business metrics against pre-release baseline. Workflow-specific control: Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.

**Required evidence:**
- post-release SLI report
- journey verification
- business outcome check
- workflow-specific safety/control evidence

**Exit criteria:** No material regression is hidden by infrastructure-only health checks.

### 5. Confirm or roll back

**Accountable role:** product-owner

**Execution:** Compare observed signals with stop thresholds; record go/no-go decision and execute authorized recovery if breached. Workflow-specific control: Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.

**Required evidence:**
- release disposition
- rollback/forward-fix evidence
- stakeholder update
- workflow-specific safety/control evidence

**Exit criteria:** Decision is recorded with authority and final system state verified.


## Stage set and accountable roles
Stage IDs: 126, 127, 128, 129, 132, 133, 134, 135, 136, 137, 138, 139, 86, 109
Accountable roles: release-manager, deployment-engineer, sre, product-owner
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.
**Recovery:** Promote the exact immutable artifact digest; use progressive rollout/canary where supported; define health and business stop thresholds; require named change authority and rollback owner.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
