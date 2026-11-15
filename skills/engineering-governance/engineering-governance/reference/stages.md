# Repository and engineering operating model: stage reference

## Contents
- [45 Repository Setup](#45)
- [46 Branching Strategy](#46)
- [47 Development Environment](#47)
- [48 Coding Standards](#48)
- [49 Environment Configuration](#49)
- [50 Secrets Management](#50)
- [51 Developer Documentation](#51)
- [52 Engineering Governance](#52)

## 45
**Repository Setup** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-045. Approval: none required

## 46
**Branching Strategy** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-046. Approval: none required

## 47
**Development Environment** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-047. Approval: none required

## 48
**Coding Standards** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-048. Approval: none required

## 49
**Environment Configuration** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-049. Approval: none required

## 50
**Secrets Management** (complete). Purpose: keep credentials out of source and logs, and make every secret rotatable and owned.

Entry criteria: Inventory of secret types and stores exists or will be created in this stage; Secret manager or vault is available to the team; Named secrets-owner exists

Inputs: repository history and current tree; secret scanner configuration; secret manager inventory; rotation policy

Procedure:
1. Scan the working tree and full history for credentials; record findings without printing secret values.
2. Treat every found credential as compromised: revoke and rotate it before removing it from code.
3. Move runtime secrets to the secret manager; reference them by name, never by value, in config and CI.
4. Add a pre-commit and CI secret scan that fails the build on new findings.
5. Record owner, rotation interval and consumers for each secret.
6. Get the secrets-owner's approval of the inventory and the rotation plan.

Deliverables: secret inventory (names, owners, rotation dates; no values); scan reports; rotation log; CI secret-scan configuration

Acceptance: Scan of history and tree reports zero active secrets or each is rotated CI blocks new secrets Every secret has an owner and a rotation date No secret value appears in the evidence

Validation: Secrets-owner approval, plus a rerun of the scanner on a clean clone.

- `gitleaks detect --source . --redact --report-path reports/secrets.json   # example` expect: exit 0; zero findings or all findings marked rotated
- `git clone --quiet . /tmp/clean && gitleaks detect --source /tmp/clean --redact` expect: exit 0 on the clean clone

Failure modes:
- Credential removed but not rotated | detect: Rotation log has no entry for a found secret | respond: Rotate now; treat as BLOCKED until logged
- Secret value pasted into the report | detect: Report contains an unredacted value | respond: Delete the report, rotate the secret, rerun with redaction
- Scanner not enforced in CI | detect: A test commit with a fake secret passes CI | respond: Fix pipeline configuration before approval

ILLUSTRATIVE: History scan finds a cloud access key committed two years ago. The key is revoked first, a new key is stored in the secret manager, CI is updated to read it by name, and the scanner is added to the pipeline.

Gate: 05-050. Approval: secrets-owner (when rotating or revoking production secrets)

## 51
**Developer Documentation** (stub). Purpose: create a navigable, versioned and traceable specification.

Inputs: validated needs and decisions; document template and audience; source-of-truth repository

Procedure:
1. Organize scope, actors, terminology, requirements, constraints, dependencies and exclusions.
2. Assign stable IDs and link each requirement to source, owner and downstream tests.
3. Document diagrams, examples, exceptions and unresolved decisions in the repository convention.
4. Review clarity, consistency, links, version and change history.

Deliverables: versioned specification; traceability matrix; glossary and decision links

Acceptance: No ambiguous pronouns or unbounded terms remain in normative requirements. IDs are stable and traceable. Links, diagrams and examples render.

Validation: Peer review by product, engineering and QA.

Gate: 05-051. Approval: none required

## 52
**Engineering Governance** (stub). Purpose: establish a secure and reproducible engineering workspace.

Inputs: repository ownership and team model; language/runtime and build manifests; security and contribution policy

Procedure:
1. Inspect repository state, ownership, package manifests, existing CI and local instructions before changes.
2. Define branch protection, review ownership, required checks, reproducible setup and supported toolchain.
3. Keep credentials out of source; use approved secret storage and least-privilege access.
4. Add onboarding and contribution guidance, then validate from a clean checkout.

Deliverables: repository policy; setup instructions; branch protection/check evidence; secret handling guide

Acceptance: A clean contributor can reproduce setup. Protected branches require review and checks. No secret value is committed.

Validation: Repository owner and security review.

Gate: 05-052. Approval: none required
