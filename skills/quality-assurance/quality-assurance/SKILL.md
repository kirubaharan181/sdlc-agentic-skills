---
name: quality-assurance
description: "Use when verifying behavior before release: risk-based testing and defect handling. Do NOT use for fixing defects or security scans."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["testing", "qa", "defects", "regression"]
---

# Risk-based verification

## Purpose
Gives release decision makers honest, reproducible evidence of quality: test strategy and plans, test execution at every level, performance testing, defect management and sign-off. It owns stages 77-97.

## When to Use
- A test strategy or plan is needed for a release.
- Functional, regression, performance or compatibility testing must be run and reported.
- Defects need triage and a sign-off statement.

## When NOT to Use
- Fixing defects: use software-implementation.
- Vulnerability scanning and threat modeling: use application-security.
- Approving release: use release-deployment.

## Prerequisites and Requirements
- Testable acceptance criteria and a risk list.
- A test environment with test data and a known build.
- Access to the build identifier under test.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- acceptance criteria
- build identifier
- test environment

Optional inputs:
- risk register
- past defect data
- usage analytics

Outputs and deliverables:
- test plan with measurable exit criteria
- version-pinned test reports
- defect records with evidence
- sign-off statement with untested areas

## Procedure
1. Derive coverage from user journeys, acceptance criteria, failure modes and risk.
2. Select test levels, fixtures, environments, oracles and exit criteria.
3. Execute positive, negative, boundary and non-functional scenarios with version-pinned evidence.
4. Triage failures and issue a quality recommendation with explicit limitations.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Results are from a different build | Rerun on the release candidate before sign-off. |
| A test is flaky | Fix or quarantine it; never report it as PASS. |
| Exit criterion not met | Report not met; a waiver needs a named owner and expiry. |
| High-risk area untested | List it explicitly in the sign-off. |

## Quality Gates
- [ ] Exit criteria are measurable and each has a result
- [ ] Results name build, environment and data
- [ ] Untested areas are listed
- [ ] Waivers have an owner

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Write exit criteria
```text
Request: Draft exit criteria for the payments release.
Context: High-risk flows: refunds and card changes.
Agent behavior: Trace each high risk to planned tests and define measurable criteria.
Output: Exit criteria: no open critical defects, all high-risk flows automated and passing, load test at 1.5 times peak.
Acceptance: Every high risk maps to at least one test.
```

### Example 2: Report test status
```text
Request: Summarize test status for sign-off.
Context: Load test ran at 1.2 times peak against a 1.5 target.
Agent behavior: Compare results with each criterion, mark the load criterion not met and list the residual risk.
Output: Scorecard: 7 of 8 criteria met; recommendation: release with a condition and a retest date.
Acceptance: Not-met criterion and its owner are stated.
```

## Limitations
- Test results describe only the tested build, data and environment.
- Cannot run tests that require unavailable environments; it records them as BLOCKED.
- Sign-off is a recommendation; a named human decides release.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Environment unavailable | Test environment down | Record BLOCKED, do not substitute results from another environment. |
| Intermittent failure | Race or shared data | Isolate data and rerun with the recorded reason. |
| Acceptance criteria untestable | Vague wording | Return them to requirements-design. |

## Tools
- test runner and CI reports
- test management
- browser/device automation
- performance and accessibility tools

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 77 | Test Strategy | complete | QA Lead |
| 78 | Test Planning | complete | QA Lead |
| 79 | Unit Testing | complete | Unit Testing Specialist |
| 80 | Integration Testing | complete | Integration Testing Specialist |
| 81 | API Testing | complete | API Testing Specialist |
| 82 | UI Testing | complete | Automation QA Engineer |
| 83 | Functional Testing | complete | Manual QA Engineer |
| 84 | End-to-End Testing | complete | E2E Testing Specialist |
| 85 | Regression Testing | complete | Automation QA Engineer |
| 86 | Smoke Testing | complete | Automation QA Engineer |
| 87 | Sanity Testing | complete | Manual QA Engineer |
| 88 | Cross-browser Testing | complete | E2E Testing Specialist |
| 89 | Mobile Compatibility Testing | complete | Automation QA Engineer |
| 90 | Accessibility Testing | complete | Accessibility Testing Specialist |
| 91 | Performance Testing | complete | Performance Testing Specialist |
| 92 | Load Testing | complete | Performance Testing Specialist |
| 93 | Stress Testing | complete | Performance Testing Specialist |
| 94 | Soak Testing | complete | Performance Testing Specialist |
| 95 | UAT | complete | QA Lead |
| 96 | Defect Management | complete | QA Lead |
| 97 | Test Sign-off | complete | QA Lead |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `release-deployment`: test sign-off with exit criteria scorecard
- `software-implementation`: defect reports with evidence
- `enterprise-governance`: test evidence for quality audits

Receives from:
- `code-review-quality`: approved change with review findings
- `requirements-design`: acceptance criteria and risk list for test design
- `software-implementation`: build and acceptance criteria for testing

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: api-version-upgrade, bug-fix, database-migration, dependency-update, emergency-hotfix, environment-configuration, existing-application-enhancement, feature-development, new-product-development, performance-optimization, staging-release, technical-debt-reduction.
- Roles: accessibility-testing-specialist, api-testing-specialist, automation-qa-engineer, e2e-testing-specialist, integration-testing-specialist, manual-qa-engineer, performance-engineer, performance-testing-specialist, qa-lead, quality-governance-specialist, sre, unit-testing-specialist.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
