# Secure delivery platform — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 111. CI Pipeline

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 112. Automated Test Pipeline

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 113. Build Management

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 114. Artifact Management

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 115. Containerization

**Purpose:** package applications as reproducible least-privilege container images

**Procedure:**
- Use a minimal pinned base image and deterministic build context.
- Exclude secrets, development tools and unnecessary files from final layers.
- Run as non-root with explicit ports, health checks and resource expectations.
- Scan the exact image digest and run startup/shutdown smoke tests.

**Inputs:** build context and runtime dependencies, base image and vulnerability policy, runtime user, ports and health expectations
**Artifact:** Dockerfile/image build
**Verification:** Inspect final image layers for secrets and run the image with restricted capabilities.
**Handoff:** Transfer Dockerfile/image build with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 116. Container Orchestration

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 117. Infrastructure as Code

**Purpose:** provision infrastructure through reviewed and policy-checked desired state

**Procedure:**
- Model resources in reusable versioned modules with explicit inputs and outputs.
- Run formatting, validation, security/policy checks and plan against the target workspace.
- Review destructive changes, IAM, network exposure, state locking, quotas and cost.
- Apply only after approval, then detect drift and verify actual state.

**Inputs:** resource requirements and ownership, state backend and environment, security and cost policy
**Artifact:** IaC module and plan
**Verification:** Review plan output for destructive actions and prove policy checks fail on an intentionally unsafe fixture.
**Handoff:** Transfer IaC module and plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 118. Configuration Management

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 119. CD Pipeline

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 120. Environment Provisioning

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 121. Network Engineering

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 122. Database Operations

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 123. CDN & Edge Configuration

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 124. Deployment Automation

**Purpose:** build a secure and reproducible delivery platform

**Procedure:**
- Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
- Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
- Protect credentials, runners, deployment environments and immutable artifact promotion.
- Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

**Inputs:** repository and build graph, deployment targets and environment protections, artifact trust and supply-chain policy
**Artifact:** pipeline/IaC configuration
**Verification:** Platform/security review and clean pipeline run.
**Handoff:** Transfer pipeline/IaC configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 125. Pipeline Security

**Purpose:** protect CI trust boundaries, credentials and artifact integrity

**Procedure:**
- Map untrusted pull-request events, privileged release events, runners and reusable workflows.
- Scope GITHUB_TOKEN and third-party action permissions; pin actions to immutable references where policy requires.
- Keep secrets unavailable to untrusted code and isolate caches/artifacts by trust level.
- Verify provenance, required gates and deployment environment protection with negative fixtures.

**Inputs:** workflow triggers and runner inventory, token permissions and secret inventory, artifact promotion and deployment policy
**Artifact:** pipeline threat model
**Verification:** Test a fork pull request and prove it cannot read release secrets or alter trusted artifacts.
**Handoff:** Transfer pipeline threat model with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
