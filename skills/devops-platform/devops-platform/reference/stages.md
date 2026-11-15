# Secure delivery platform: stage reference

## Contents
- [111 CI Pipeline](#111)
- [112 Automated Test Pipeline](#112)
- [113 Build Management](#113)
- [114 Artifact Management](#114)
- [115 Containerization](#115)
- [116 Container Orchestration](#116)
- [117 Infrastructure as Code](#117)
- [118 Configuration Management](#118)
- [119 CD Pipeline](#119)
- [120 Environment Provisioning](#120)
- [121 Network Engineering](#121)
- [122 Database Operations](#122)
- [123 CDN & Edge Configuration](#123)
- [124 Deployment Automation](#124)
- [125 Pipeline Security](#125)

## 111
**CI Pipeline** (complete). Purpose: turn each commit into a repeatable, trusted build-and-check result that gates merging.

Entry criteria: Repository builds from a clean checkout with documented commands; CI runner and secrets store are available; Required checks are agreed (build, tests, lint, security scans)

Inputs: repository and build instructions; required-check list; runner and cache configuration; secret store references

Procedure:
1. Define the pipeline as code in the repository; pin tool and action versions.
2. Run build, unit tests, lint and security scans on every pull request, with least-privilege tokens.
3. Cache dependencies by lockfile hash; never cache secrets.
4. Publish build artifacts with the commit id and a checksum.
5. Protect the default branch: required checks must pass before merge.
6. Measure duration and flake rate; investigate regressions.

Deliverables: pipeline definition; run history; artifact with checksum; branch protection settings

Acceptance: Pipeline runs on every pull request and on the default branch Required checks block merge Actions and tools are pinned Failed runs show the failing step and logs

Validation: A deliberately failing change is blocked from merging.

- `gh run list --limit 5 --json conclusion,headSha` expect: latest run on the default branch concluded success for the current head
- `gh api repos/{owner}/{repo}/branches/main/protection --jq .required_status_checks.contexts` expect: lists every required check

Failure modes:
- Checks are advisory only | detect: A failing PR can still be merged | respond: Enable required status checks
- Unpinned actions or tools | detect: Workflow uses moving tags | respond: Pin to versions or digests
- Secrets exposed to forked PRs | detect: Workflow runs with secrets on fork events | respond: Restrict secrets to trusted events

ILLUSTRATIVE: A new service gets a workflow that builds, tests and scans on each pull request. A test PR with a failing unit test is blocked from merging until fixed.

Gate: 10-111. Approval: none required

## 112
**Automated Test Pipeline** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-112. Approval: none required

## 113
**Build Management** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-113. Approval: none required

## 114
**Artifact Management** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-114. Approval: none required

## 115
**Containerization** (stub). Purpose: package applications as reproducible least-privilege container images.

Inputs: build context and runtime dependencies; base image and vulnerability policy; runtime user, ports and health expectations

Procedure:
1. Use a minimal pinned base image and deterministic build context.
2. Exclude secrets, development tools and unnecessary files from final layers.
3. Run as non-root with explicit ports, health checks and resource expectations.
4. Scan the exact image digest and run startup/shutdown smoke tests.

Deliverables: Dockerfile/image build; image SBOM and scan; runtime configuration; container smoke test

Acceptance: Image is reproducible and free of embedded secrets. Runtime is non-root and least-privilege. Image digest and scan evidence match.

Validation: Inspect final image layers for secrets and run the image with restricted capabilities.

Gate: 10-115. Approval: none required

## 116
**Container Orchestration** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-116. Approval: none required

## 117
**Infrastructure as Code** (complete). Purpose: describe infrastructure as reviewed, versioned code so environments are reproducible and drift is visible.

Entry criteria: Target environments and ownership are defined; State storage and locking are decided; Infra-owner is named

Inputs: environment requirements; current infrastructure inventory; IaC tooling and module standards; state backend configuration

Procedure:
1. Model resources in code with parameters per environment; keep secrets out of code.
2. Run format, validate and policy checks in CI.
3. Produce a plan against the target environment and review the diff, especially deletions and replacements.
4. Apply through the pipeline with the infra-owner's approval for production.
5. Detect drift on a schedule and reconcile by code, not by hand.
6. Record rollback: previous version of the code and state backup.

Deliverables: IaC modules and environment configs; plan output; policy check results; drift report

Acceptance: Plan shows only expected changes Policy checks pass State is remote, locked and backed up Production apply has infra-owner approval

Validation: Infra-owner review of the plan before production apply.

- `terraform fmt -check -recursive && terraform validate   # example; use the project's IaC tool` expect: exit 0
- `terraform plan -detailed-exitcode -out=plan.out` expect: exit 2 means changes pending; review diff; exit 0 means no drift

Failure modes:
- Plan includes unexpected destroys | detect: Plan lists replacements of stateful resources | respond: Stop; review before any apply
- Manual change in console | detect: Drift report shows differences | respond: Reconcile in code; document who changed what
- Secrets in state or code | detect: Scanner finds values | respond: Rotate and move to the secret manager

ILLUSTRATIVE: Adding a database replica changes one module. The plan shows one resource created and none destroyed; the infra-owner approves and drift check afterwards is clean.

Gate: 10-117. Approval: infra-owner (before applying a plan to production; always when the plan destroys resources or changes IAM)

## 118
**Configuration Management** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-118. Approval: none required

## 119
**CD Pipeline** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-119. Approval: none required

## 120
**Environment Provisioning** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-120. Approval: none required

## 121
**Network Engineering** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-121. Approval: infra-owner (for production firewall, security-group or routing changes)

## 122
**Database Operations** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-122. Approval: none required

## 123
**CDN & Edge Configuration** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-123. Approval: none required

## 124
**Deployment Automation** (stub). Purpose: build a secure and reproducible delivery platform.

Inputs: repository and build graph; deployment targets and environment protections; artifact trust and supply-chain policy

Procedure:
1. Map source-to-build-to-artifact-to-environment trust boundaries and required checks.
2. Implement reproducible builds, pinned dependencies, tests, scans and provenance/attestation where supported.
3. Protect credentials, runners, deployment environments and immutable artifact promotion.
4. Exercise failure, rollback and permission boundaries; publish ownership and operational runbook.

Deliverables: pipeline/IaC configuration; artifact provenance; test/security results; runbook and ownership

Acceptance: Build is reproducible and artifacts are immutable/promoted. Secrets and environment permissions are scoped. Failure and rollback behavior is exercised.

Validation: Platform/security review and clean pipeline run.

Gate: 10-124. Approval: none required

## 125
**Pipeline Security** (stub). Purpose: protect CI trust boundaries, credentials and artifact integrity.

Inputs: workflow triggers and runner inventory; token permissions and secret inventory; artifact promotion and deployment policy

Procedure:
1. Map untrusted pull-request events, privileged release events, runners and reusable workflows.
2. Scope GITHUB_TOKEN and third-party action permissions; pin actions to immutable references where policy requires.
3. Keep secrets unavailable to untrusted code and isolate caches/artifacts by trust level.
4. Verify provenance, required gates and deployment environment protection with negative fixtures.

Deliverables: pipeline threat model; workflow permission matrix; policy test report; artifact provenance

Acceptance: Untrusted code cannot access privileged credentials. Artifacts cannot be replaced across trust boundaries. Required checks and environment approvals are enforced.

Validation: Test a fork pull request and prove it cannot read release secrets or alter trusted artifacts.

Gate: 10-125. Approval: none required
