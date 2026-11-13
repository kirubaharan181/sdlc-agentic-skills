# Api Version Upgrade

> **Purpose:** evolve an API while protecting consumers

## Trigger and required inputs
A request requires the controlled lifecycle to evolve an API while protecting consumers.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Inventory consumers

**Accountable role:** api-architect

**Execution:** Find active clients, integrations, SDKs and usage patterns from gateway logs, repositories and owner records; classify migration criticality. Workflow-specific control: Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.

**Required evidence:**
- consumer inventory
- usage evidence
- owner and contact list
- workflow-specific safety/control evidence

**Exit criteria:** No known active consumer is omitted without documented uncertainty.

### 2. Design version and migration

**Accountable role:** api-engineer

**Execution:** Define version boundary, compatibility guarantees, migration examples, dual-support window and deprecation criteria. Workflow-specific control: Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.

**Required evidence:**
- versioning decision
- migration guide
- deprecation timeline
- workflow-specific safety/control evidence

**Exit criteria:** Consumers have a documented migration path and support window.

### 3. Implement compatibility

**Accountable role:** integration-engineer

**Execution:** Implement the new contract while preserving the agreed old behavior; add adapters or version routing where necessary. Workflow-specific control: Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.

**Required evidence:**
- versioned implementation
- compatibility tests
- migration examples
- workflow-specific safety/control evidence

**Exit criteria:** Old and new consumers behave as specified during transition.

### 4. Run contract/security tests

**Accountable role:** api-testing-specialist

**Execution:** Validate schema compatibility, auth scopes, error handling, rate limits and representative consumer contract suites. Workflow-specific control: Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.

**Required evidence:**
- contract report
- security test evidence
- consumer compatibility result
- workflow-specific safety/control evidence

**Exit criteria:** All critical consumer contracts and security controls pass.

### 5. Publish and deprecate

**Accountable role:** api-testing-specialist

**Execution:** Publish the version, migration notice, support dates and usage telemetry; deprecate only after consumer readiness criteria are met. Workflow-specific control: Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.

**Required evidence:**
- release notes
- migration notice
- usage/retirement evidence
- workflow-specific safety/control evidence

**Exit criteria:** Deprecation decision is based on verified usage and approved notice period.


## Stage set and accountable roles
Stage IDs: 27, 57, 81, 105, 132, 13, 14, 67, 69, 80, 81, 109, 126, 127, 131, 176
Accountable roles: api-architect, api-engineer, integration-engineer, api-testing-specialist
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.
**Recovery:** Inventory consumers and usage before changing contracts; publish compatibility policy, migration examples, dual-run/deprecation dates and consumer test evidence.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
