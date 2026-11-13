# Emergency Hotfix

> **Purpose:** mitigate active customer impact under emergency control

## Trigger and required inputs
A request requires the controlled lifecycle to mitigate active customer impact under emergency control.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Establish incident command

**Accountable role:** incident-manager

**Execution:** Declare incident severity, appoint commander/operations/comms/scribe roles, open a timestamped timeline and define a single source of truth. Workflow-specific control: Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.

**Required evidence:**
- incident declaration
- role assignments
- timeline and comms channel
- workflow-specific safety/control evidence

**Exit criteria:** Command roles and communication cadence are active before mitigation work.

### 2. Apply safe mitigation

**Accountable role:** backend-engineer

**Execution:** Choose the least risky action that reduces customer impact, preserve evidence, document expected side effects and define an immediate reversal trigger. Workflow-specific control: Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.

**Required evidence:**
- mitigation decision
- before/after state
- reversal trigger
- workflow-specific safety/control evidence

**Exit criteria:** Impact is reduced without violating data integrity or access controls.

### 3. Constrain minimal patch

**Accountable role:** release-manager

**Execution:** Limit the hotfix to the incident-causing path, avoid broad dependency or schema changes, and add a targeted regression test. Workflow-specific control: Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.

**Required evidence:**
- hotfix diff
- targeted regression
- risk assessment
- workflow-specific safety/control evidence

**Exit criteria:** Patch scope is bounded and independently reviewed.

### 4. Authorize and deploy expedited fix

**Accountable role:** sre

**Execution:** Obtain named emergency authorization, verify artifact identity and required tests, deploy to the smallest safe cohort and monitor stop signals. Workflow-specific control: Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.

**Required evidence:**
- emergency approval
- artifact digest
- rollout and monitoring log
- workflow-specific safety/control evidence

**Exit criteria:** Authorized approver and rollback owner are recorded; rollout meets canary thresholds.

### 5. Verify recovery and retrospective

**Accountable role:** sre

**Execution:** Verify customer-facing recovery, monitor recurrence, close incident communications and schedule a blameless review with action owners. Workflow-specific control: Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.

**Required evidence:**
- recovery evidence
- final incident update
- retrospective/action register
- workflow-specific safety/control evidence

**Exit criteria:** Recovery is verified and every corrective action has an owner and due date.


## Stage set and accountable roles
Stage IDs: 66, 67, 69, 70, 71, 73, 74, 75, 76, 175, 177, 187
Accountable roles: incident-manager, backend-engineer, release-manager, sre
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.
**Recovery:** Incident commander owns severity and scope; patch must be minimal, independently reviewed, tested against the incident, explicitly authorized and followed by normal regression and retrospective work.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
