---
name: software-implementation
description: "Use when implementing features or fixes: builds and changes application code. Do NOT use for design, review or deployment."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["implementation", "backend", "frontend", "api"]
---

# Product implementation

## Purpose
Implements approved designs as working, tested code: front end, back end, mobile, APIs, data, authentication and authorization, integration, real-time, data engineering, ML and error handling. It owns stages 53-67 and aims for small, reviewable changes with tests.

## When to Use
- Approved requirements and designs need to be implemented.
- A defect or enhancement needs a code change with tests.
- An API, schema, integration or model feature must be built.

## When NOT to Use
- Deciding architecture: use technical-architecture.
- Reviewing the change: use code-review-quality.
- Deploying it: use release-deployment.

## Prerequisites and Requirements
- Acceptance criteria and, where relevant, API contracts and designs.
- A working development environment (see engineering-governance).
- Permission to branch and open pull requests.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- acceptance criteria
- existing code context

Optional inputs:
- design files
- API contract
- data samples
- architecture decisions

Outputs and deliverables:
- small pull requests with tests
- updated contracts and schemas
- logging and error handling
- notes on behavior and configuration for reviewers

## Procedure
1. Trace the requested behavior across UI, API, domain logic, persistence and external dependencies.
2. Define compatibility, authorization, error, transaction and observability behavior before coding.
3. Implement the smallest coherent change following local conventions and secure defaults.
4. Run unit/integration/contract checks and record migration, deployment and rollback impact.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Acceptance criteria are unclear | Ask before coding; do not guess behavior. |
| Change touches a contract | Update the contract and check compatibility. |
| Change needs a schema migration | Use backward-compatible steps and flag for review. |
| A secret would be needed | Use the secrets store; never write it to code. |

## Quality Gates
- [ ] Each acceptance criterion has a passing test
- [ ] Inputs validated and authorization checked server-side
- [ ] No secrets or sensitive data in code or logs
- [ ] Change is small enough for review

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Add an endpoint
```text
Request: Add POST /refunds for partial refunds.
Context: Orders and payments modules exist; idempotency is required.
Agent behavior: Validate amount against the original payment, check order ownership, use an idempotency key, and add tests for success, repeat and failure.
Output: Pull request with endpoint, tests and a contract update.
Acceptance: Repeat request has no second effect; failure leaves the order consistent.
```

### Example 2: Fix a bug safely
```text
Request: Orders sometimes show the wrong total with two discount codes.
Context: Reproduced only when codes are applied in a certain order.
Agent behavior: Write a failing test with the exact order, fix the calculation, and run the existing suite.
Output: Failing test first, fix, and a note on root cause.
Acceptance: New test fails before and passes after; no other test breaks.
```

## Limitations
- Cannot run code that needs credentials or services it does not have.
- Does not decide design questions: it raises them to technical-architecture.
- Test results reflect only the environment and data used.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Tests fail on a clean checkout | Missing setup or version mismatch | Run the documented setup, record versions, and fix the guide if needed. |
| Contract and code disagree | Contract not updated | Reconcile with the owner and update both. |
| Change is too large to review | Mixed concerns | Split into separate pull requests. |

## Tools
- language-native build/test/lint
- API and database tools
- static/security scanners
- browser/device tests

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 53 | Frontend Development | complete | Frontend Engineer |
| 54 | Backend Development | complete | Backend Engineer |
| 55 | Full Stack Development | complete | Full Stack Engineer |
| 56 | Mobile Development | complete | Mobile Engineer |
| 57 | API Development | complete | API Engineer |
| 58 | Database Development | complete | Database Engineer |
| 59 | Authentication Development | complete | Authentication and Authorization Engineer |
| 60 | Authorization Development | complete | Authentication and Authorization Engineer |
| 61 | Third-party Integration | complete | Integration Engineer |
| 62 | Real-time Development | complete | Backend Engineer |
| 63 | Data Engineering | complete | Data Engineer |
| 64 | AI/ML Development | complete | AI/ML Engineer |
| 65 | Caching & Optimization | complete | Performance Engineer |
| 66 | Error Handling | complete | Backend Engineer |
| 67 | Developer Testing | complete | Full Stack Engineer |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `code-review-quality`: pull request with tests and notes
- `application-security`: code and dependency changes for scanning
- `quality-assurance`: build and acceptance criteria for testing

Receives from:
- `application-security`: remediation items with severity
- `code-review-quality`: blocker findings for rework
- `engineering-governance`: repository standards, branching rules and environment
- `maintenance-support`: defects and enhancements with reproduction steps
- `project-agile-management`: sprint backlog with acceptance criteria
- `quality-assurance`: defect reports with evidence
- `requirements-design`: wireframes, UI designs and acceptance criteria
- `technical-architecture`: decision records, interface contracts and dependency rules

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: api-version-upgrade, database-migration, existing-application-enhancement, feature-development, new-product-development, performance-optimization.
- Roles: ai-ml-engineer, api-engineer, authentication-and-authorization-engineer, backend-engineer, data-engineer, database-engineer, frontend-engineer, full-stack-engineer, integration-engineer, mobile-engineer, unit-testing-specialist.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
