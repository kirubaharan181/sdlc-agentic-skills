# Incident Response

> **Purpose:** contain and recover from an operational incident

## Trigger and required inputs
A request requires the controlled lifecycle to contain and recover from an operational incident.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Assign commander/severity

**Accountable role:** incident-manager

**Execution:** Complete the assign commander/severity phase with explicit inputs, accountable owner, recorded decisions and verifiable outcome. Workflow-specific control: Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.

**Required evidence:**
- phase work product
- verification evidence
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** The accountable owner accepts the output and all blocking issues have an owner.

### 2. Assess impact/timeline

**Accountable role:** sre

**Execution:** Establish the phase baseline: verify scope, owner, authority, current state, constraints and stop conditions before taking action. Workflow-specific control: Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.

**Required evidence:**
- baseline and scope record
- assumptions and risk log
- workflow-specific safety/control evidence

**Exit criteria:** Owner confirms the baseline and all blocking unknowns have an owner.

### 3. Contain and investigate

**Accountable role:** observability-engineer

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible. Workflow-specific control: Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.

**Required evidence:**
- change/design artifact
- execution log
- review evidence
- workflow-specific safety/control evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 4. Recover and verify

**Accountable role:** production-support-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.

### 5. Handoff and postmortem

**Accountable role:** production-support-engineer

**Execution:** Verify the resulting state using explicit acceptance criteria, independent signals and affected-consumer checks; record limitations and next owner. Workflow-specific control: Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.

**Required evidence:**
- verification report
- residual risk and decision log
- handoff record
- workflow-specific safety/control evidence

**Exit criteria:** Evidence demonstrates the expected outcome; failures are fixed or explicitly blocked/waived by authority.


## Stage set and accountable roles
Stage IDs: 158, 162, 163, 164, 165, 167, 168, 169, 138
Accountable roles: incident-manager, sre, observability-engineer, production-support-engineer
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.
**Recovery:** Assign commander/scribe/comms roles; maintain timeline and impact; prioritize containment and safe restoration; communicate only verified facts.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
