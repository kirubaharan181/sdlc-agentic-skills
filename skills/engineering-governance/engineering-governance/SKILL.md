---
name: engineering-governance
description: Provides a specialist procedure to create a secure, reproducible contribution environment. Use when the work involves Repository Setup, Branching Strategy, Development Environment, Coding Standards, Environment Configuration, Secrets Management, Developer Documentation, Engineering Governance.
---

# Repository and engineering operating model

Create a secure, reproducible contribution environment.

## Procedure
1. Inspect ownership, repository state, local instructions, manifests and existing CI.
2. Define branch protection, code ownership, required checks and contribution workflow.
3. Standardize reproducible setup, supported toolchain, environment configuration and documentation.
4. Protect secrets and access; validate onboarding from a clean checkout.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- Git and repository settings
- CI configuration
- secret scanning
- docs-as-code and linting

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 45 | Repository Setup | complete | Platform Engineer |
| 46 | Branching Strategy | complete | Engineering Governance Specialist |
| 47 | Development Environment | complete | Platform Engineer |
| 48 | Coding Standards | complete | Engineering Governance Specialist |
| 49 | Environment Configuration | complete | DevOps Engineer |
| 50 | Secrets Management | complete | DevSecOps Engineer |
| 51 | Developer Documentation | complete | Documentation Engineer |
| 52 | Engineering Governance | complete | Engineering Governance Specialist |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: ci-cd-pipeline-creation, documentation-update, environment-configuration, new-product-development.
- Roles: devops-engineer, documentation-engineer, engineering-governance-specialist, platform-engineer, quality-governance-specialist, software-architect, technical-writer.
