# Ci Cd Pipeline Creation

> **Purpose:** create a trusted source-to-artifact delivery path

## Trigger and required inputs
A request requires the controlled lifecycle to create a trusted source-to-artifact delivery path.
- named request and accountable owner
- risk/impact classification and authority
- relevant artifact, immutable revision or environment reference
- acceptance criteria and recovery constraints

## Lifecycle phases
### 1. Map trust boundaries

**Accountable role:** devops-engineer

**Execution:** Identify workflow actors, runner trust, event sources, tokens, secrets, artifacts and deployment environments. Workflow-specific control: Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.

**Required evidence:**
- pipeline threat model
- permission matrix
- untrusted-event map
- workflow-specific safety/control evidence

**Exit criteria:** Every trust boundary has a control owner and least-privilege policy.

### 2. Build/test/scan/provenance

**Accountable role:** platform-engineer

**Execution:** Build reproducibly, run unit/integration/security checks and produce provenance tied to source revision and artifact digest. Workflow-specific control: Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.

**Required evidence:**
- build/test/scan reports
- artifact digest
- provenance attestation
- workflow-specific safety/control evidence

**Exit criteria:** Only the expected source revision produces a verified artifact.

### 3. Protect immutable artifacts

**Accountable role:** devsecops-engineer

**Execution:** Promote the same digest between environments, enforce retention/signing policy and prevent untrusted jobs from overwriting release artifacts. Workflow-specific control: Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.

**Required evidence:**
- artifact promotion policy
- signature/digest verification
- retention controls
- workflow-specific safety/control evidence

**Exit criteria:** Artifact identity is unchanged and verifiable across promotion.

### 4. Exercise recovery

**Accountable role:** automation-qa-engineer

**Execution:** Simulate pipeline/deployment failure and verify rollback, runner isolation, secret revocation and recovery from partial promotion. Workflow-specific control: Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.

**Required evidence:**
- failure-injection log
- recovery result
- secret/access review
- workflow-specific safety/control evidence

**Exit criteria:** Recovery restores a known-good state without exposing credentials.

### 5. Document ownership

**Accountable role:** automation-qa-engineer

**Execution:** Assign pipeline owner, support SLA, permission steward, runbook, dependency update cadence and deprecation path. Workflow-specific control: Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.

**Required evidence:**
- ownership record
- runbook
- maintenance schedule
- workflow-specific safety/control evidence

**Exit criteria:** Every production workflow has an accountable maintainer and escalation path.


## Stage set and accountable roles
Stage IDs: 45, 46, 47, 48, 50, 51, 52, 99, 100, 101, 102, 105, 106, 107, 111, 112, 113, 114, 115, 116, 119, 122, 123, 124, 125, 181, 183
Accountable roles: devops-engineer, platform-engineer, devsecops-engineer, automation-qa-engineer
Required skills: master-orchestration, evidence-quality-gates, secure-change-control

## Dependencies and parallel work
A phase cannot start until its entry criteria and predecessor evidence are accepted; independent read-only analysis may run in parallel against the same immutable baseline.
- Independent QA and security analysis may run in parallel after scope is frozen; both must cite the same candidate revision.

## Approval gates
scope-and-risk, quality-evidence, security-disposition. Sensitive operations require explicit human authorization.

## Failure, rollback and communication
Stop progression when a phase exit criterion fails; preserve diagnostics and state, notify the workflow owner, open a named remediation item, and resume only after the failed criterion is re-tested. Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.
**Recovery:** Treat workflow code, runners, secrets and artifacts as a supply-chain boundary; pin actions, scope permissions, isolate untrusted pull requests and verify artifact provenance.
**Communication:** Publish phase status, decision owner, customer/operational impact and next update time at each gate; communicate material risk immediately.

## Completion criteria
Every required phase has accepted exit evidence or a valid, time-bound waiver approved by the designated authority; residual risk and operational ownership are accepted.
