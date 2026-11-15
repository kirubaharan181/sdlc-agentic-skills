---
name: code-review-quality
description: Provides a specialist procedure to assess whether a change is correct, maintainable, secure and ready to integrate. Use when the work involves Pull Request Creation, Peer Code Review, Architecture Review, Static Code Analysis, Dependency Review, Code Coverage Review, Coding Standards Validation, Merge Approval and 1 more stages.
---

# Independent engineering review

Assess whether a change is correct, maintainable, secure and ready to integrate.

## Procedure
1. Inspect complete diff, target branch, acceptance criteria and architecture context.
2. Review edge cases, concurrency, data safety, API compatibility, security and dependency risk.
3. Verify test quality and that evidence refers to the exact reviewed commit.
4. Classify findings by severity and recommend merge, changes or block with actionable evidence.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- Git diff/blame
- static analysis
- test/coverage reports
- dependency and security reports

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 68 | Pull Request Creation | stub | Full Stack Engineer |
| 69 | Peer Code Review | complete | Code Reviewer |
| 70 | Architecture Review | stub | Architecture Reviewer |
| 71 | Static Code Analysis | stub | DevSecOps Engineer |
| 72 | Dependency Review | stub | DevSecOps Engineer |
| 73 | Code Coverage Review | stub | Code Reviewer |
| 74 | Coding Standards Validation | stub | Code Reviewer |
| 75 | Merge Approval | stub | Merge Steward |
| 76 | Technical Debt Review | stub | Software Architect |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, bug-fix, dependency-update, emergency-hotfix, existing-application-enhancement, feature-development, new-product-development, security-vulnerability-remediation, technical-debt-reduction.
- Roles: architecture-reviewer, code-reviewer, devsecops-engineer, engineering-governance-specialist, frontend-engineer, full-stack-engineer, license-compliance-specialist, merge-steward, software-architect, unit-testing-specialist.
