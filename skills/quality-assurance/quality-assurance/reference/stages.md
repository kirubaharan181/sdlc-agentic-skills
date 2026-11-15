# Risk-based verification: stage reference

## Contents
- [77 Test Strategy](#77)
- [78 Test Planning](#78)
- [79 Unit Testing](#79)
- [80 Integration Testing](#80)
- [81 API Testing](#81)
- [82 UI Testing](#82)
- [83 Functional Testing](#83)
- [84 End-to-End Testing](#84)
- [85 Regression Testing](#85)
- [86 Smoke Testing](#86)
- [87 Sanity Testing](#87)
- [88 Cross-browser Testing](#88)
- [89 Mobile Compatibility Testing](#89)
- [90 Accessibility Testing](#90)
- [91 Performance Testing](#91)
- [92 Load Testing](#92)
- [93 Stress Testing](#93)
- [94 Soak Testing](#94)
- [95 UAT](#95)
- [96 Defect Management](#96)
- [97 Test Sign-off](#97)

## 77
**Test Strategy** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Select risk-based test levels and map each critical product risk to an oracle and accountable test owner.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; risk-to-test coverage matrix

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Every high-impact risk has an explicit test level and measurable exit condition.

Validation: Independent QA review and acceptance decision. Review coverage against top user and failure scenarios.
Gate: 08-077. Approval: none required

## 78
**Test Planning** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Sequence test cases by dependency, environment readiness and risk; define fixtures, entry criteria and execution windows.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; test execution plan and environment matrix

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Test data, environment, owners and exit criteria are ready before execution.

Validation: Independent QA review and acceptance decision. Review plan completeness and fixture reproducibility.
Gate: 08-078. Approval: none required

## 79
**Unit Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Isolate pure logic with deterministic fixtures and cover boundaries, invariants and failure results.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; unit test suite and boundary assertions

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Tests fail when behavior breaks and do not depend on external services.

Validation: Independent QA review and acceptance decision. Run focused unit suite and inspect assertion quality.
Gate: 08-079. Approval: none required

## 80
**Integration Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Verify service, database, queue and adapter contracts with isolated dependencies.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; integration contract report and environment setup

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Partial failures, retries, transaction boundaries and schema compatibility are exercised.

Validation: Independent QA review and acceptance decision. Run integration suite with dependency health and cleanup evidence.
Gate: 08-080. Approval: none required

## 81
**API Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Exercise OpenAPI success, validation, authorization, pagination, idempotency and error cases.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; API request collection and contract report

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Response schemas and status behavior match the published contract.

Validation: Independent QA review and acceptance decision. Run contract and negative-case suite against the exact build.
Gate: 08-081. Approval: none required

## 82
**UI Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Verify component states, keyboard interaction, validation feedback and responsive layout.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; UI interaction report and screenshots

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Critical controls work at supported viewports without console or accessibility blockers.

Validation: Independent QA review and acceptance decision. Run browser tests and inspect captured screenshots/traces.
Gate: 08-082. Approval: none required

## 83
**Functional Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Trace each business requirement to positive, negative, alternate and exception scenarios.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; functional test matrix and results

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Every in-scope business rule has an observed expected result.

Validation: Independent QA review and acceptance decision. Review traceability and execute critical business paths.
Gate: 08-083. Approval: none required

## 84
**End-to-End Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Exercise complete user journeys across UI, APIs, persistence and external side effects with synthetic data.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; E2E journey report and trace bundle

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Journey state is correct across boundaries and recovery works.

Validation: Independent QA review and acceptance decision. Run critical journeys and reconcile resulting state across services.
Gate: 08-084. Approval: none required

## 85
**Regression Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Select impacted behavior using code dependencies, API/data changes and historical defect evidence.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; regression scope and comparison report

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Previously accepted critical behavior remains stable on the candidate build.

Validation: Independent QA review and acceptance decision. Compare targeted suite results with the baseline candidate.
Gate: 08-085. Approval: none required

## 86
**Smoke Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Check release-blocking startup, health, authentication and critical transaction paths after deployment.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; smoke report and health snapshot

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Critical paths meet thresholds before broader testing proceeds.

Validation: Independent QA review and acceptance decision. Run smoke suite against the deployed artifact.
Gate: 08-086. Approval: none required

## 87
**Sanity Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Verify the narrow changed area and immediate dependencies after a small patch.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; sanity checklist and focused test result

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. The targeted fix works and adjacent behavior remains stable.

Validation: Independent QA review and acceptance decision. Execute the bounded checklist on the exact patch.
Gate: 08-087. Approval: none required

## 88
**Cross-browser Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Run identical critical journeys across the supported browser/OS matrix and compare rendering and interaction.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; browser compatibility matrix and screenshots

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. No supported browser has a critical functional or layout regression.

Validation: Independent QA review and acceptance decision. Run matrix tests and attach browser/version evidence.
Gate: 08-088. Approval: none required

## 89
**Mobile Compatibility Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Verify responsive layout, touch targets, orientation, OS permissions and network transitions on supported devices.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; device compatibility matrix and recordings

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Critical flows work on the supported device/OS matrix.

Validation: Independent QA review and acceptance decision. Run emulator and representative physical-device tests.
Gate: 08-089. Approval: none required

## 90
**Accessibility Testing** (stub). Purpose: verify inclusive access against applicable WCAG criteria.

Inputs: target standard and conformance level; supported browsers/devices and assistive tech; critical user journeys

Procedure:
1. Inspect semantic structure, accessible names, headings, landmarks, labels and error associations.
2. Test keyboard-only operation, focus order/visibility, dialogs and escape behavior.
3. Check contrast, zoom/reflow, reduced motion and screen-reader announcements.
4. Combine automated scans with manual assistive-technology testing; log criterion-level failures.
5. Check semantic names, keyboard-only operation, focus management, contrast, zoom and screen-reader announcements.

Deliverables: accessibility audit; manual test evidence; defect and remediation list; WCAG criterion-level audit and manual test evidence

Acceptance: Automated scans are not treated as full conformance proof. Critical journeys work without pointer input. Findings cite criterion, impact and reproduction. Critical journeys pass manual assistive-technology checks.

Validation: Independent accessibility specialist review. Run automated scans plus keyboard and screen-reader verification.
Gate: 08-090. Approval: none required

## 91
**Performance Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Measure representative workload latency, throughput, saturation and error rate against service objectives.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; performance baseline and profile report

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. p50/p95/p99 and resource use meet agreed thresholds under representative load.

Validation: Independent QA review and acceptance decision. Compare equivalent before/after runs with workload pinned.
Gate: 08-091. Approval: none required

## 92
**Load Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Ramp concurrency and request mix to expected peak and observe throughput, queue depth and latency percentiles.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; load profile and capacity result

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. System sustains forecast peak plus agreed headroom without SLO breach.

Validation: Independent QA review and acceptance decision. Run controlled load ramp and retain telemetry.
Gate: 08-092. Approval: none required

## 93
**Stress Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Increase load beyond expected capacity to identify saturation point and failure mode.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; stress curve and degradation report

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Overload is bounded, shedding is graceful and recovery occurs after load drops.

Validation: Independent QA review and acceptance decision. Run approved stress profile in an isolated environment.
Gate: 08-093. Approval: none required

## 94
**Soak Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Sustain representative load long enough to expose leaks, queue growth and resource drift.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; soak run and resource trend report

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Memory, handles, queues and latency remain stable through the agreed duration.

Validation: Independent QA review and acceptance decision. Review time-series trends and post-run resource recovery.
Gate: 08-094. Approval: none required

## 95
**UAT** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Validate real business workflows with authorized users against agreed acceptance examples.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; UAT scripts and business acceptance record

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. Business owner accepts outcomes or records named defects and conditions.

Validation: Independent QA review and acceptance decision. Capture user execution evidence and explicit acceptance decision.
Gate: 08-095. Approval: uat-acceptor (always)

## 96
**Defect Management** (stub). Purpose: control defects from reproduction through verified closure.

Inputs: defect report and affected build; severity/priority policy; reproduction environment

Procedure:
1. Reproduce on a named build and capture minimal steps, expected/actual behavior and logs.
2. Assess impact, exploitability, affected users and workaround; assign severity separately from priority.
3. Link root cause and fix commit to regression coverage.
4. Verify fix on the target build and close only with reproducible evidence.

Deliverables: defect ticket; severity rationale; root cause and fix link; retest report

Acceptance: Reproduction is reliable. Severity rationale reflects impact. Closure includes fix-version retest and regression protection.

Validation: QA owner verifies closure.
Gate: 08-096. Approval: none required

## 97
**Test Sign-off** (stub). Purpose: prepare a controlled decision with sufficient evidence and independent authority.

Inputs: decision request and accountable sponsor; impact/risk assessment; supporting evidence and alternatives

Procedure:
1. Check the decision request is complete, in scope and owned by an authorized requester.
2. Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
3. Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
4. Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

Deliverables: decision record; evidence index; conditions and waiver log

Acceptance: Decision authority is verified. Conditions are measurable, owned and time-bound. No missing or failed critical evidence is silently waived.

Validation: Independent approval record and audit trail.
Gate: 08-097. Approval: none required
