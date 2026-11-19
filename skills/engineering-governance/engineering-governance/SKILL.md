---
name: engineering-governance
description: "Use when starting or standardizing repos: branching, environment, coding rules. Do NOT use for enterprise audit or application code."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["repository", "standards", "branching", "environments"]
---

# Repository and engineering operating model

## Purpose
Gives teams a safe, repeatable engineering baseline: protected repositories, branching rules, reproducible environments, coding standards, configuration and secrets handling. It owns stages 45-52 and the repository-level controls that other skills rely on.

## When to Use
- A repository, branching model or development environment must be set up.
- Coding standards, configuration or secrets handling need defining and enforcing.
- Repository controls must be checked for drift.

## When NOT to Use
- Organization-wide audit and policy: use enterprise-governance.
- Writing feature code: use software-implementation.
- Building delivery pipelines: use devops-platform.

## Prerequisites and Requirements
- Repository platform access at the level needed to read or change settings.
- A decision on language and tooling, or a request to propose one.
- A secrets store, or a stated plan for one.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- repository or project name and owners
- language and tooling choices

Optional inputs:
- release cadence
- existing standards
- security baseline

Outputs and deliverables:
- repository with README, licence, code owners and protection
- branching and merge rules
- reproducible development environment
- coding standard with tool configuration
- configuration and secrets handling design

## Procedure
1. Inspect ownership, repository state, local instructions, manifests and existing CI.
2. Define branch protection, code ownership, required checks and contribution workflow.
3. Standardize reproducible setup, supported toolchain, environment configuration and documentation.
4. Protect secrets and access; validate onboarding from a clean checkout.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Main branch can be pushed to directly | Enable protection requiring review and passing checks. |
| A secret is found in the repository | Revoke and rotate first, then clean history per policy. |
| Style is argued in review | Adopt an automatic formatter. |
| Rules exist only in a document | Enforce them in settings or CI. |

## Quality Gates
- [ ] A newcomer can build and run from the README
- [ ] Main branch is protected
- [ ] Secrets are not in the repository
- [ ] Formatter and linter run in CI and block on errors

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Set up a new repository
```text
Request: Create the repository for the notifications service.
Context: Team of six, weekly releases, Python.
Agent behavior: Create it with README, licence and code owners, protect main, add CI, enable secret scanning and grant team access.
Output: Repository checklist with settings evidence and a clean-checkout build result.
Acceptance: Fresh clone builds with documented commands.
```

### Example 2: Remove a committed secret
```text
Request: A scanner found a token in the repository.
Context: Token has production read access.
Agent behavior: Mark the action as needing human approval for rotation, advise revoking first, then plan history clean-up.
Output: Incident note with revoke, rotate and clean-up steps and owner.
Acceptance: Token revoked before any clean-up; no secret value appears in the note.
```

## Limitations
- Cannot change platform settings without access; it will list the required changes instead.
- Rotation of production secrets needs human approval.
- Cannot verify that a rule is followed in other repositories without access to them.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Cannot read branch protection | Missing admin permission | Ask an owner for read access or the exported settings. |
| Setup steps fail on a clean machine | Undocumented dependency or version | Pin versions, fix the guide and retest. |
| Formatter conflicts with existing code | Large diff on adoption | Apply it in a separate commit with no other changes. |

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

## Handoffs
Hands to:
- `software-implementation`: repository standards, branching rules and environment
- `devops-platform`: repository and configuration conventions for pipelines
- `enterprise-governance`: repository control inventory

Receives from:
- `code-review-quality`: recurring findings as proposed rules
- `enterprise-governance`: policy requirements and control gaps

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: ci-cd-pipeline-creation, documentation-update, environment-configuration, new-product-development.
- Roles: devops-engineer, documentation-engineer, engineering-governance-specialist, platform-engineer, quality-governance-specialist, software-architect, technical-writer.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
