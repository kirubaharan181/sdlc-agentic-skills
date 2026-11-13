# Release and deployment control — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 126. Release Planning

**Purpose:** prepare and execute a controlled release or migration

**Procedure:**
- Confirm immutable candidate, included changes, compatibility and outstanding risk.
- Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
- Obtain change authority and communicate schedule, impact, owners and stop conditions.
- Deploy progressively, verify health and business signals, then confirm or execute recovery.

**Inputs:** release candidate digest and scope, change approvals and readiness evidence, rollback/recovery and communication plan
**Artifact:** release manifest
**Verification:** Change authority approval and post-deploy verification.
**Handoff:** Transfer release manifest with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 127. Release Notes

**Purpose:** communicate the exact behavior and operational impact of a release

**Procedure:**
- Group changes by user-visible capability, fixes, security and operational impact.
- Describe behavior changes, compatibility/deprecation and required customer actions accurately.
- Include known issues, upgrade notes and links to support guidance.
- Verify every statement against the approved candidate and obtain product/support review.

**Inputs:** approved change list and issue links, target audience and supported version, known issues and rollout schedule
**Artifact:** versioned release notes
**Verification:** Compare release notes with the merged change list and candidate digest.
**Handoff:** Transfer versioned release notes with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 128. Release Readiness

**Purpose:** decide whether an immutable candidate is safe to promote

**Procedure:**
- Verify artifact provenance, required checks, open defects and change scope.
- Review migration compatibility, backup freshness, monitoring, runbooks and support readiness.
- Check approvals, operator coverage, communication and stop/rollback thresholds.
- Record go/no-go with conditions and named authority.

**Inputs:** candidate digest and scope, test/security/operations evidence, migration, backup and rollback plan
**Artifact:** release readiness checklist
**Verification:** Re-fetch candidate digest and verify readiness evidence before requesting change approval.
**Handoff:** Transfer release readiness checklist with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 129. Change Approval

**Purpose:** prepare a controlled decision with sufficient evidence and independent authority

**Procedure:**
- Check the decision request is complete, in scope and owned by an authorized requester.
- Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
- Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
- Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

**Inputs:** decision request and accountable sponsor, impact/risk assessment, supporting evidence and alternatives
**Artifact:** decision record
**Verification:** Independent approval record and audit trail.
**Handoff:** Transfer decision record with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 130. Staging Deployment

**Purpose:** prepare and execute a controlled release or migration

**Procedure:**
- Confirm immutable candidate, included changes, compatibility and outstanding risk.
- Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
- Obtain change authority and communicate schedule, impact, owners and stop conditions.
- Deploy progressively, verify health and business signals, then confirm or execute recovery.

**Inputs:** release candidate digest and scope, change approvals and readiness evidence, rollback/recovery and communication plan
**Artifact:** release manifest
**Verification:** Change authority approval and post-deploy verification.
**Handoff:** Transfer release manifest with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 131. Staging Validation

**Purpose:** prepare and execute a controlled release or migration

**Procedure:**
- Confirm immutable candidate, included changes, compatibility and outstanding risk.
- Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
- Obtain change authority and communicate schedule, impact, owners and stop conditions.
- Deploy progressively, verify health and business signals, then confirm or execute recovery.

**Inputs:** release candidate digest and scope, change approvals and readiness evidence, rollback/recovery and communication plan
**Artifact:** release manifest
**Verification:** Change authority approval and post-deploy verification.
**Handoff:** Transfer release manifest with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 132. Database Migration

**Purpose:** change schema and data with rehearsed recovery and integrity controls

**Procedure:**
- Inventory schema consumers, write paths, locks, data volume and rolling-version compatibility.
- Design expand/backfill/contract or equivalent safe sequence with pre/post integrity checks.
- Rehearse backup and isolated restore; measure RPO/RTO and migration duration.
- Execute only after approval, reconcile counts/checksums and monitor application behavior.

**Inputs:** schema consumers and compatibility matrix, representative data volume and backup policy, approved migration window and recovery objectives
**Artifact:** migration plan and scripts
**Verification:** Rehearse on representative data and reconcile row counts/checksums before approving the production window.
**Handoff:** Transfer migration plan and scripts with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 133. Production Deployment

**Purpose:** prepare and execute a controlled release or migration

**Procedure:**
- Confirm immutable candidate, included changes, compatibility and outstanding risk.
- Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
- Obtain change authority and communicate schedule, impact, owners and stop conditions.
- Deploy progressively, verify health and business signals, then confirm or execute recovery.

**Inputs:** release candidate digest and scope, change approvals and readiness evidence, rollback/recovery and communication plan
**Artifact:** release manifest
**Verification:** Change authority approval and post-deploy verification.
**Handoff:** Transfer release manifest with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 134. Domain & DNS

**Purpose:** configure secure and resilient network edge routing

**Procedure:**
- Verify domain/account ownership and change window.
- Configure records, certificates, ciphers, health checks, routing and origin restrictions.
- Validate propagation, certificate chain/expiry, redirects and failover behavior.
- Document TTL, renewal, rollback and monitoring.

**Inputs:** domain ownership and target topology, certificate and trust requirements, traffic and health-check profile
**Artifact:** DNS/TLS/routing configuration
**Verification:** Network/security review.
**Handoff:** Transfer DNS/TLS/routing configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 135. SSL/TLS Setup

**Purpose:** configure secure and resilient network edge routing

**Procedure:**
- Verify domain/account ownership and change window.
- Configure records, certificates, ciphers, health checks, routing and origin restrictions.
- Validate propagation, certificate chain/expiry, redirects and failover behavior.
- Document TTL, renewal, rollback and monitoring.

**Inputs:** domain ownership and target topology, certificate and trust requirements, traffic and health-check profile
**Artifact:** DNS/TLS/routing configuration
**Verification:** Network/security review.
**Handoff:** Transfer DNS/TLS/routing configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 136. Load Balancer Setup

**Purpose:** configure secure and resilient network edge routing

**Procedure:**
- Verify domain/account ownership and change window.
- Configure records, certificates, ciphers, health checks, routing and origin restrictions.
- Validate propagation, certificate chain/expiry, redirects and failover behavior.
- Document TTL, renewal, rollback and monitoring.

**Inputs:** domain ownership and target topology, certificate and trust requirements, traffic and health-check profile
**Artifact:** DNS/TLS/routing configuration
**Verification:** Network/security review.
**Handoff:** Transfer DNS/TLS/routing configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 137. Rollback Planning

**Purpose:** select a safe recovery path before a release changes production state

**Procedure:**
- Define measurable rollback triggers from customer-facing health and business signals.
- Assess schema compatibility, writes after release, queued events and irreversible side effects.
- Choose rollback, forward-fix or compensation path and identify operator/approver.
- Rehearse the recovery sequence and verify data reconciliation and communication.

**Inputs:** release and migration design, data compatibility and irreversible side-effect inventory, rollback authority and recovery window
**Artifact:** rollback decision tree
**Verification:** Walk through a failed release including schema changes and demonstrate the chosen recovery path.
**Handoff:** Transfer rollback decision tree with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 138. Production Smoke Test

**Purpose:** prepare and execute a controlled release or migration

**Procedure:**
- Confirm immutable candidate, included changes, compatibility and outstanding risk.
- Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
- Obtain change authority and communicate schedule, impact, owners and stop conditions.
- Deploy progressively, verify health and business signals, then confirm or execute recovery.

**Inputs:** release candidate digest and scope, change approvals and readiness evidence, rollback/recovery and communication plan
**Artifact:** release manifest
**Verification:** Change authority approval and post-deploy verification.
**Handoff:** Transfer release manifest with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 139. Deployment Sign-off

**Purpose:** prepare a controlled decision with sufficient evidence and independent authority

**Procedure:**
- Check the decision request is complete, in scope and owned by an authorized requester.
- Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
- Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
- Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

**Inputs:** decision request and accountable sponsor, impact/risk assessment, supporting evidence and alternatives
**Artifact:** decision record
**Verification:** Independent approval record and audit trail.
**Handoff:** Transfer decision record with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
