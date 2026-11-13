# Product Retirement

> **Purpose:** retire a product with consumer and data obligations closed

## Trigger and required inputs
A request requires the controlled lifecycle to retire a product with consumer and data obligations closed.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Approve EOL

**Accountable role:** product-manager

**Execution:** Confirm product retirement rationale, support end date, legal retention and accountable sponsor approval. Workflow-specific control: Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.

**Required evidence:**
- EOL decision
- notice and retention requirements
- workflow-specific safety/control evidence

**Exit criteria:** Retirement authority and affected-party notice are approved.

### 2. Inventory consumers/data/vendors

**Accountable role:** vendor-management-specialist

**Execution:** Find active clients, integrations, SDKs and usage patterns from gateway logs, repositories and owner records; classify migration criticality. Workflow-specific control: Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.

**Required evidence:**
- consumer inventory
- usage evidence
- owner and contact list
- workflow-specific safety/control evidence

**Exit criteria:** No known active consumer is omitted without documented uncertainty.

### 3. Migrate and communicate

**Accountable role:** compliance-specialist

**Execution:** Move users and data to an approved successor, reconcile completeness and communicate cutover/support dates. Workflow-specific control: Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.

**Required evidence:**
- migration and reconciliation report
- customer notices
- cutover plan
- workflow-specific safety/control evidence

**Exit criteria:** Consumers confirm readiness or receive a supported exception path.

### 4. Stage shutdown

**Accountable role:** technical-support-engineer

**Execution:** Disable access and traffic in controlled steps while monitoring residual usage and preserving required records. Workflow-specific control: Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.

**Required evidence:**
- shutdown checklist
- residual access scan
- traffic/usage evidence
- workflow-specific safety/control evidence

**Exit criteria:** No active critical consumer remains and rollback window is understood.

### 5. Close audit and support

**Accountable role:** technical-support-engineer

**Execution:** Remove residual credentials/infrastructure, complete retention/deletion evidence and transfer remaining support obligations. Workflow-specific control: Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.

**Required evidence:**
- decommission evidence
- deletion/retention record
- support closure
- workflow-specific safety/control evidence

**Exit criteria:** Security, legal and service owners accept closure.


## Stage set and accountable roles
Stage IDs: 9, 10, 180, 185, 188
Accountable roles: product-manager, vendor-management-specialist, compliance-specialist, technical-support-engineer
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition, explicit-human-authorization. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.
**Recovery:** Inventory users, integrations, data, legal retention and supplier dependencies; communicate notice; verify export/migration, access removal, deletion and audit closure.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
