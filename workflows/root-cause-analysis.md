# Root Cause Analysis

> **Purpose:** establish causal learning after an incident

## Trigger and required inputs
A request requires the controlled lifecycle to establish causal learning after an incident.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Collect timeline

**Accountable role:** incident-manager

**Execution:** Collect alerts, deploys, traces, logs and operator decisions into a UTC timeline with source references.

**Required evidence:**
- timestamped event timeline
- evidence source index

**Exit criteria:** Timeline is traceable and separates observed facts from interpretation.

### 2. Test causal hypotheses

**Accountable role:** sre

**Execution:** Construct causal hypotheses, test them against independent evidence and identify contributing conditions rather than a single blame target.

**Required evidence:**
- hypothesis/evidence matrix
- causal analysis
- uncertainty notes

**Exit criteria:** Root cause claims have supporting evidence and alternatives are addressed.

### 3. Identify contributors

**Accountable role:** software-architect

**Execution:** Examine technical, process, organizational and external contributors that allowed the event or increased impact.

**Required evidence:**
- contributing-factor map
- control gap analysis

**Exit criteria:** Analysis explains both occurrence and impact amplification.

### 4. Assign corrective actions

**Accountable role:** process-improvement-specialist

**Execution:** Create preventive, detective and recovery actions with measurable outcomes, accountable owners and due dates.

**Required evidence:**
- corrective action register
- priority and owner

**Exit criteria:** Actions address verified contributors and are trackable.

### 5. Verify follow-through

**Accountable role:** process-improvement-specialist

**Execution:** Review action completion evidence and measure recurrence or control effectiveness after an agreed period.

**Required evidence:**
- closure evidence
- effectiveness measure
- residual-risk review

**Exit criteria:** Actions are not closed on status alone; effectiveness is demonstrated.


## Stage set and accountable roles
Stage IDs: 153, 154, 155, 156, 157, 161, 163, 164, 165, 166, 190
Accountable roles: incident-manager, sre, software-architect, process-improvement-specialist
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
