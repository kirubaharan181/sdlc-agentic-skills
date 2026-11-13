# Documentation Update

> **Purpose:** correct and publish controlled documentation

## Trigger and required inputs
A request requires the controlled lifecycle to correct and publish controlled documentation.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Identify audience/source

**Accountable role:** technical-writer

**Execution:** Identify the reader task, authoritative source, product version and content owner before drafting.

**Required evidence:**
- audience/task brief
- source and version inventory

**Exit criteria:** Every statement can be traced to an implementation or policy owner.

### 2. Draft accurate content

**Accountable role:** documentation-engineer

**Execution:** Write prerequisites, steps, expected output, examples and recovery guidance from verified source behavior.

**Required evidence:**
- draft guide
- validated code examples

**Exit criteria:** Instructions are executable and do not invent product behavior.

### 3. Review links/examples

**Accountable role:** quality-governance-specialist

**Execution:** Run code examples, validate links, check version references and obtain subject-matter review.

**Required evidence:**
- link/code validation report
- SME review

**Exit criteria:** Broken links, stale commands and unsupported claims are resolved.

### 4. Publish

**Accountable role:** quality-governance-specialist

**Execution:** Perform the phase work against the approved design and bounded change; preserve before/after state and keep the operation reversible where possible.

**Required evidence:**
- change/design artifact
- execution log
- review evidence

**Exit criteria:** The intended change is complete and independently checked against its approved scope.

### 5. Set review date

**Accountable role:** quality-governance-specialist

**Execution:** Assign content owner, review cadence and change triggers linked to releases or policy changes.

**Required evidence:**
- owner and review date
- freshness trigger

**Exit criteria:** Published content has an accountable owner and review trigger.


## Stage set and accountable roles
Stage IDs: 186
Accountable roles: technical-writer, documentation-engineer, quality-governance-specialist
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
