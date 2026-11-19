---
name: code-review-quality
description: "Use when assessing a pull request for correctness, design, standards, merge readiness. Do NOT use for writing code."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["code-review", "pull-request", "static-analysis", "quality"]
---

# Independent engineering review

## Purpose
Provides independent review of changes before merge: pull request quality, peer review, architecture conformance, static analysis, dependency and coverage review, standards validation and technical debt. It owns stages 68-76 and keeps reviewers independent of authors.

## When to Use
- A pull request needs review before merge.
- Static analysis, dependency or coverage results need interpreting.
- A change must be checked against agreed architecture or standards.

## When NOT to Use
- Implementing the change: use software-implementation.
- Running the test suites: use quality-assurance.
- Scanning for vulnerabilities: use application-security.

## Prerequisites and Requirements
- A pull request or diff with tests and a description.
- Coding standards and tool configuration (see engineering-governance).
- Reviewer who is not the author.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- diff and description
- test and tool results

Optional inputs:
- architecture decisions
- coverage data
- dependency lock files

Outputs and deliverables:
- review findings split into blockers and suggestions
- tool result summary
- merge decision recommendation
- follow-up debt items

## Procedure
1. Inspect complete diff, target branch, acceptance criteria and architecture context.
2. Review edge cases, concurrency, data safety, API compatibility, security and dependency risk.
3. Verify test quality and that evidence refers to the exact reviewed commit.
4. Classify findings by severity and recommend merge, changes or block with actionable evidence.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Tool configuration weakened in the same change | Review the configuration change separately. |
| New suppression comment added | Require a reason and owner. |
| Coverage falls on changed code | Ask for tests or a recorded decision. |
| Author and reviewer are the same | Reject the review; request an independent one. |

## Quality Gates
- [ ] All tools ran on the change
- [ ] Findings cite file, rule and reason
- [ ] Blockers are separated from suggestions
- [ ] Reviewer is independent

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Review a pull request
```text
Request: Review PR 482 which adds refund handling.
Context: Diff touches payments and orders; tests included.
Agent behavior: Run tool checks, read the diff for error handling and authorization, check coverage on changed lines, and list blockers separately.
Output: Review with one blocker (no ownership check) and two suggestions.
Acceptance: Blocker has a file reference and a fix suggestion.
```

### Example 2: Judge a suppression
```text
Request: The change adds two lint suppressions.
Context: One has a ticket; one hides an unused variable.
Agent behavior: Accept the documented one, reject the other and ask for removal.
Output: Findings with the decision for each.
Acceptance: Each added suppression has a recorded decision.
```

## Limitations
- Cannot find defects in code it was not shown or tests that were not run.
- Does not approve merge by itself: a named human reviewer approves where required.
- Static analysis gives false positives and negatives.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Tool results missing | CI did not run | State that review is incomplete and ask for the results. |
| Diff too large | Mixed concerns | Ask the author to split it. |
| Reviewer disagreement | Standards unclear | Escalate to the engineering lead and record the decision. |

## Tools
- Git diff/blame
- static analysis
- test/coverage reports
- dependency and security reports

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 68 | Pull Request Creation | complete | Full Stack Engineer |
| 69 | Peer Code Review | complete | Code Reviewer |
| 70 | Architecture Review | complete | Architecture Reviewer |
| 71 | Static Code Analysis | complete | DevSecOps Engineer |
| 72 | Dependency Review | complete | DevSecOps Engineer |
| 73 | Code Coverage Review | complete | Code Reviewer |
| 74 | Coding Standards Validation | complete | Code Reviewer |
| 75 | Merge Approval | complete | Merge Steward |
| 76 | Technical Debt Review | complete | Software Architect |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `quality-assurance`: approved change with review findings
- `software-implementation`: blocker findings for rework
- `engineering-governance`: recurring findings as proposed rules

Receives from:
- `software-implementation`: pull request with tests and notes

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, bug-fix, dependency-update, emergency-hotfix, existing-application-enhancement, feature-development, new-product-development, security-vulnerability-remediation, technical-debt-reduction.
- Roles: architecture-reviewer, code-reviewer, devsecops-engineer, engineering-governance-specialist, frontend-engineer, full-stack-engineer, license-compliance-specialist, merge-steward, software-architect, unit-testing-specialist.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
