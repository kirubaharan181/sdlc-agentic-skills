---
name: quality-assurance
description: Provides a specialist procedure to provide independent evidence about product behavior and residual quality risk. Use when the work involves Test Strategy, Test Planning, Unit Testing, Integration Testing, API Testing, UI Testing, Functional Testing, End-to-End Testing and 13 more stages.
---

# Risk-based verification

Provide independent evidence about product behavior and residual quality risk.

## Procedure
1. Derive coverage from user journeys, acceptance criteria, failure modes and risk.
2. Select test levels, fixtures, environments, oracles and exit criteria.
3. Execute positive, negative, boundary and non-functional scenarios with version-pinned evidence.
4. Triage failures and issue a quality recommendation with explicit limitations.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- test runner and CI reports
- test management
- browser/device automation
- performance and accessibility tools

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 77 | Test Strategy | complete | QA Lead |
| 78 | Test Planning | stub | QA Lead |
| 79 | Unit Testing | complete | Unit Testing Specialist |
| 80 | Integration Testing | complete | Integration Testing Specialist |
| 81 | API Testing | complete | API Testing Specialist |
| 82 | UI Testing | stub | Automation QA Engineer |
| 83 | Functional Testing | stub | Manual QA Engineer |
| 84 | End-to-End Testing | complete | E2E Testing Specialist |
| 85 | Regression Testing | complete | Automation QA Engineer |
| 86 | Smoke Testing | complete | Automation QA Engineer |
| 87 | Sanity Testing | stub | Manual QA Engineer |
| 88 | Cross-browser Testing | stub | E2E Testing Specialist |
| 89 | Mobile Compatibility Testing | stub | Automation QA Engineer |
| 90 | Accessibility Testing | complete | Accessibility Testing Specialist |
| 91 | Performance Testing | complete | Performance Testing Specialist |
| 92 | Load Testing | complete | Performance Testing Specialist |
| 93 | Stress Testing | stub | Performance Testing Specialist |
| 94 | Soak Testing | stub | Performance Testing Specialist |
| 95 | UAT | complete | QA Lead |
| 96 | Defect Management | stub | QA Lead |
| 97 | Test Sign-off | stub | QA Lead |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, bug-fix, database-migration, dependency-update, emergency-hotfix, environment-configuration, existing-application-enhancement, feature-development, new-product-development, performance-optimization, staging-release, technical-debt-reduction.
- Roles: accessibility-testing-specialist, api-testing-specialist, automation-qa-engineer, e2e-testing-specialist, integration-testing-specialist, manual-qa-engineer, performance-engineer, performance-testing-specialist, qa-lead, quality-governance-specialist, sre, unit-testing-specialist.
