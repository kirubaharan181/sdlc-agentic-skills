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
**Test Strategy** (complete). Purpose: decide what to test, at which level and to what depth, based on risk, so that release confidence is justified.

Entry criteria: Scope and requirements are known; Risk areas are identified with the product owner; Environments and test data availability are known

Inputs: requirements and acceptance criteria; risk assessment; architecture overview; environment and data constraints

Procedure:
1. List features and quality attributes in scope; rank by business impact and likelihood of failure.
2. Choose test levels per risk (unit, integration, contract, end-to-end, performance, security, accessibility) and say what each will not cover.
3. Define entry and exit criteria, including pass thresholds and defect severity rules.
4. Define environments, data, tools and who owns each activity.
5. Map each high risk to at least one planned test; list residual risk accepted.
6. Get the strategy reviewed by engineering and the product owner and baseline it.

Deliverables: test strategy document; risk-to-test matrix; entry and exit criteria; accepted-gap list

Acceptance: Every high risk maps to a planned test Exit criteria are measurable Out-of-scope areas are listed with reasons Owners and environments are named

Validation: Review by engineering lead and product owner.

- manual: trace each high risk in the risk list to a test in the matrix expect: no high risk without a test or an accepted gap
- manual: confirm every exit criterion has a number or a yes/no check expect: none are phrased as 'adequate' or 'good enough'

Failure modes:
- Strategy lists tools but not risks | detect: Risk-to-test matrix missing | respond: Return to risk ranking
- Exit criteria are vague | detect: Criteria contain no threshold | respond: Rewrite with measurable thresholds
- Only the happy path is planned | detect: No negative or failure scenarios in matrix | respond: Add failure-mode tests for high-risk areas

ILLUSTRATIVE: A payments feature ranks refund calculation as highest risk. The strategy puts heavy unit and contract testing there, a small set of end-to-end journeys, a load test for peak hour, and records that localization beyond two currencies is out of scope.

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
**Unit Testing** (complete). Purpose: prove each unit of logic behaves correctly in isolation and keep that proof fast and trustworthy.

Entry criteria: Code under test builds locally and in CI; Unit boundaries and seams for isolating dependencies exist; Test framework is chosen by the repository

Inputs: code under test; acceptance criteria and edge cases; test framework and conventions; coverage baseline

Procedure:
1. List behaviors per unit, including boundaries, invalid input and error paths.
2. Write tests that isolate external dependencies with fakes or stubs, one behavior per test, with descriptive names.
3. Run tests and confirm each new test fails when the behavior is broken (mutate the code or revert the fix).
4. Remove time, randomness and ordering dependence so tests are deterministic.
5. Run the whole unit suite in CI and record counts, duration and coverage change.
6. Report skipped or quarantined tests with owner and reason.

Deliverables: unit test files; test run report; coverage report with change; skipped-test list

Acceptance: Every new behavior has a test that fails without the change Suite is deterministic across three consecutive runs No test depends on network, clock or ordering Skipped tests are listed with owners

Validation: Rerun in CI and compare with the local run.

- `pytest -q --maxfail=1 --cov --cov-report=term-missing   # example for Python; use the project's runner` expect: exit 0; failed 0; coverage not below baseline
- `for i in 1 2 3; do pytest -q -p no:randomly || break; done` expect: three green runs in a row

Failure modes:
- Tests pass but assert nothing | detect: Mutating the code leaves tests green | respond: Strengthen assertions; mark stage FAIL until mutation is caught
- Flaky test | detect: Intermittent failure across reruns | respond: Fix or quarantine with owner and expiry; do not retry-until-green
- Coverage met by trivial tests | detect: High coverage with weak assertions | respond: Review assertions on critical paths

ILLUSTRATIVE: A price-rounding function gets tests for exact cents, half-up cases, negative amounts and zero. Reverting the rounding fix makes two tests fail, which proves they check behavior.

Gate: 08-079. Approval: none required

## 80
**Integration Testing** (complete). Purpose: prove that components work together across their real boundaries, including failure behavior.

Entry criteria: Unit tests for the components pass; A test environment with the real or realistic dependencies exists; Contracts between components are written down

Inputs: component contracts and interfaces; test environment and fixtures; failure scenarios; unit test results

Procedure:
1. Identify integration points: databases, queues, internal and external services.
2. Write tests that exercise each point with real or containerized dependencies and seeded data.
3. Cover failure behavior: timeouts, retries, duplicate delivery, partial failure, schema mismatch.
4. Isolate tests so each creates and cleans its own data and can run in any order.
5. Run in CI with the environment started from scratch; capture logs of failures.
6. Record contract changes and notify consuming teams.

Deliverables: integration test suite; run report with logs; contract change notes; environment definition

Acceptance: Each integration point has a success and a failure test Suite passes from a clean environment Tests do not share state Failures include enough logs to diagnose

Validation: Clean-environment rerun in CI.

- `docker compose -f compose.test.yml up -d --wait && pytest -q tests/integration   # example` expect: exit 0; no skipped tests without owners
- `docker compose -f compose.test.yml down -v` expect: environment removed; rerun from scratch gives the same result

Failure modes:
- Tests pass only on a developer machine | detect: CI run fails on clean environment | respond: Fix environment definition; BLOCKED until CI is green
- Shared test data causes order dependence | detect: Random-order run fails | respond: Isolate data per test
- Mocks replace the real boundary | detect: No test exercises the real client | respond: Add at least one real-boundary test per integration point

ILLUSTRATIVE: An order service and a payment adapter are tested against a containerized payment stub that can return success, decline and timeout. The timeout test shows the order stays pending and is retried once.

Gate: 08-080. Approval: none required

## 81
**API Testing** (complete). Purpose: verify that API behavior matches its contract, including errors, security and compatibility, independently of any user interface.

Entry criteria: API specification or documented contract exists; A test environment with the API is available; Test accounts for each role exist

Inputs: API specification; test environment and data; accounts per role; consumer expectations

Procedure:
1. Derive tests from the contract: every operation, status code, schema and error format.
2. Test authentication and authorization with each role and with no or expired credentials; check access to other users' objects.
3. Test input validation with missing, malformed, oversized and boundary values.
4. Check idempotency, pagination, rate limiting and backward compatibility against the previous version.
5. Run the tests in CI against a clean environment and record results.
6. Report contract differences to the API owner as defects in code or specification.

Deliverables: API test suite; contract conformance results; authorization test results; defect list

Acceptance: Every operation has success and failure tests Authorization is tested for each role and for other users' objects Compatibility with the previous version is checked Suite passes from a clean environment in CI

Validation: Independent rerun in CI.

- `schemathesis run openapi.yaml --base-url https://staging.example.com --checks all   # example contract fuzzer` expect: no failures
- `pytest -q tests/api` expect: all pass

Failure modes:
- Only happy paths tested | detect: No test for 401, 403 or 422 | respond: Add error-case tests
- Object-level access not tested | detect: No test with another user's id | respond: Add authorization tests
- Specification out of date | detect: Tests pass but contract differs | respond: Fix the contract or the code

ILLUSTRATIVE: Tests call each operation with each role. A user reading another user's order id receives 403 as the contract says; an oversized body returns 413; the previous version's fields remain present.

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
**End-to-End Testing** (complete). Purpose: check that complete user journeys work across the real system, with a small stable set of high-value tests.

Entry criteria: The system is deployed to a test environment with realistic integrations; Critical user journeys are listed; Test accounts and data are available

Inputs: critical user journeys; deployed test environment; test accounts and data; end-to-end test framework

Procedure:
1. Choose a small set of journeys that cover the highest business value; leave detail to lower-level tests.
2. Write each test from the user's point of view with stable selectors and explicit waits on conditions, not fixed sleeps.
3. Create the data each test needs and clean it up, so tests run independently and in any order.
4. Run in CI against a fresh deployment and capture screenshots, traces and logs for failures.
5. Treat a flaky test as a defect: fix, quarantine with owner and expiry, or delete.
6. Report which journeys passed and which are not covered.

Deliverables: end-to-end tests; run report with traces; flaky-test register; journey coverage list

Acceptance: Each critical journey has a test Tests are independent and use waits on conditions Failures include screenshots or traces Flaky tests are tracked with owners

Validation: Independent CI rerun.

- `npx playwright test --reporter=line   # example` expect: all journeys pass
- `npx playwright test --repeat-each=3` expect: no intermittent failures

Failure modes:
- Fixed sleeps cause flakiness | detect: Failures vary by timing | respond: Wait on conditions
- Tests depend on each other | detect: Random order fails | respond: Make data independent
- Too many end-to-end tests | detect: Suite takes hours | respond: Move detail to lower levels

ILLUSTRATIVE: Five journeys (sign up, search, add to basket, pay with the sandbox gateway, view order history) run in a fresh environment in eleven minutes, each creating and removing its own data.

Gate: 08-084. Approval: none required

## 85
**Regression Testing** (complete). Purpose: show that existing behavior still works after a change by running a risk-based set of earlier tests.

Entry criteria: A change is ready to test; A regression suite exists with known coverage of critical behavior; Test environment and data are available

Inputs: the change and its impact analysis; regression suite; defect history for the area; test environment

Procedure:
1. Use the impact analysis to select the tests around changed and dependent areas, always including the critical journeys.
2. Run the selected suite; for high-risk changes run the whole suite.
3. Investigate each failure: new defect, outdated test or flaky test, and record which.
4. Add or update tests where the change exposed a gap, including a test for any defect found.
5. Record results with counts, duration and the commit under test.
6. Report coverage gaps that remain.

Deliverables: regression run report; failure analysis; new or updated tests; known gaps

Acceptance: Critical journeys were run on the commit under test Each failure is classified and handled Tests were added for defects found Remaining gaps are stated

Validation: Independent rerun in CI.

- `pytest -q -m regression --junitxml=reports/regression.xml   # example marker` expect: zero failures, or each failure classified in the analysis
- manual: compare selected tests with the impact analysis expect: every impacted area has tests

Failure modes:
- Regression suite run on the wrong commit | detect: Commit id in report differs | respond: Rerun on the correct commit
- Failures dismissed as flaky without proof | detect: No evidence of flakiness | respond: Reproduce or fix
- Suite does not cover the change | detect: Impacted area has no tests | respond: Write tests before sign-off

ILLUSTRATIVE: A change to the discount module selects 140 tests across pricing and checkout. Two fail; one is a real rounding defect, the other an outdated expectation. Both are fixed and the rerun passes.

Gate: 08-085. Approval: none required

## 86
**Smoke Testing** (complete). Purpose: check quickly that a fresh build is stable enough to be worth testing further or deploying.

Entry criteria: A build is deployed to the target environment; A short list of critical checks exists; Test accounts are available

Inputs: deployed build and environment; list of critical checks; test accounts; health endpoints

Procedure:
1. Confirm the deployed version equals the intended build.
2. Run the health checks and the shortest path through each critical function: sign in, one read, one write, one integration.
3. Check logs and error metrics for new errors immediately after deployment.
4. Record PASS or FAIL per check with timestamps and the build id.
5. On any failure, stop further testing or deployment and return the build to the team.
6. Keep the suite under a few minutes so it can run after every deployment.

Deliverables: smoke test results; build identification; error check

Acceptance: Version in the environment equals the intended build All critical checks passed No new error class in logs Suite runs in minutes

Validation: Rerun after any fix.

- `curl -fsS https://staging.example.com/version` expect: returns the intended build id
- `pytest -q -m smoke   # example marker` expect: all smoke tests pass in under the agreed time

Failure modes:
- Smoke test passes on the old build | detect: Version mismatch | respond: Redeploy and rerun
- Suite grows slow | detect: Duration above target | respond: Trim to critical paths
- Failure ignored | detect: FAIL with testing continued | respond: Stop and return the build

ILLUSTRATIVE: After deployment to staging, the smoke suite confirms the version, signs in, reads an order, creates a test order and calls the payment stub, all within ninety seconds.

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
**Accessibility Testing** (complete). Purpose: verify that people using assistive technology and keyboards can complete the key journeys, against a named standard.

Entry criteria: Target standard and level are named (for example WCAG 2.2 AA); Key journeys and a testable build exist; Access to a screen reader and keyboard-only testing is available

Inputs: build or staging URL; list of key journeys; target accessibility standard; design system components in use

Procedure:
1. Run an automated accessibility scan on each key page and record results; treat it as partial coverage only.
2. Test each key journey with the keyboard alone: focus order, visible focus, no keyboard traps, skip links.
3. Test with at least one screen reader: names, roles, states, form labels and error messages are announced correctly.
4. Check contrast, text resizing to 200 percent, reflow at narrow widths, motion and time limits.
5. Log each defect with the success criterion, steps, assistive technology used and severity.
6. Retest fixes and publish a conformance statement that lists what was and was not tested.

Deliverables: automated scan report; manual test log per journey; defect list mapped to criteria; conformance statement with scope

Acceptance: Each key journey was completed with keyboard only and with a screen reader No open critical or serious defect on a key journey Defects cite the success criterion Statement lists untested areas

Validation: Independent accessibility specialist review.

- `npx playwright test tests/a11y --reporter=line   # example: axe-based checks in the project's test runner` expect: no serious or critical violations on the key pages
- manual: complete each key journey with keyboard only and with a screen reader and record the result expect: every journey completed; defects logged

Failure modes:
- Only automated scans were run | detect: Manual log is empty | respond: Mark INCONCLUSIVE; automated tools find a minority of issues
- Defect fixed visually but not for assistive technology | detect: Retest with the screen reader still fails | respond: Reopen with the technology named
- Custom component without semantics | detect: Role or name missing in the accessibility tree | respond: Use a native element or add correct roles and states

ILLUSTRATIVE: Keyboard testing of a checkout form finds that the date picker traps focus. A screen reader reads the error summary but not the field names. Both are logged against the relevant criteria and fixed, then retested.

Gate: 08-090. Approval: none required

## 91
**Performance Testing** (complete). Purpose: find out how the system performs under expected and peak use against stated objectives, and where it degrades first.

Entry criteria: Performance objectives are defined (latency, throughput, error rate); A production-like test environment and data volume exist; Workload model is available

Inputs: performance objectives; workload model from production data; production-like environment; monitoring

Procedure:
1. Model the workload from real traffic: operation mix, think times and data distribution.
2. Prepare data volumes close to production and warm the system as in production.
3. Run baseline, expected-peak and stress scenarios; capture latency percentiles, throughput, errors and resource use.
4. Find the first bottleneck by correlating results with metrics, profiles and database behavior.
5. Fix or record the bottleneck, rerun, and compare to the baseline with the same workload.
6. Report against the objectives, including limits of the test environment.

Deliverables: workload model; test results with percentiles; bottleneck analysis; comparison with baseline

Acceptance: Results are stated per objective The workload comes from production data Bottlenecks are identified with evidence Environment differences from production are listed

Validation: Performance engineer review.

- `k6 run --out json=reports/perf.json loadtest/peak.js   # example` expect: p95 latency and error rate meet thresholds
- manual: compare the test environment's size and data volume with production expect: differences listed in the report

Failure modes:
- Test on tiny data | detect: Database is a fraction of production size | respond: Load production-like volumes
- Averages hide tail latency | detect: Only mean reported | respond: Report p95 and p99
- Load generator is the bottleneck | detect: Generator CPU saturated | respond: Add generators

ILLUSTRATIVE: A peak scenario at 300 requests per second keeps p95 latency at 420 ms against a 500 ms objective until the database connection pool saturates at 380; the report names the pool as the first bottleneck.

Gate: 08-091. Approval: none required

## 92
**Load Testing** (complete). Purpose: establish the maximum load the system sustains and how it behaves beyond it, so capacity limits are known before users find them.

Entry criteria: Performance baseline exists (stage 91); Safe test environment and a way to stop the test exist; Monitoring is in place

Inputs: performance baseline; capacity targets; test environment; stop conditions

Procedure:
1. Define the load profile: step ramp, sustained plateau and, separately, a spike.
2. Increase load in steps and hold each step long enough to see steady state and slow leaks.
3. Record the load at which latency or errors cross the objective and the load at which the system fails.
4. Observe the failure mode: does it degrade gracefully, shed load, or crash and corrupt data.
5. Verify recovery: remove the load and measure time back to normal.
6. Report the sustained maximum with a safety margin, and the bottleneck.

Deliverables: load profiles; capacity limit with safety margin; failure-mode observations; recovery measurements

Acceptance: The sustained maximum and the breaking point are both found Failure behavior is described Recovery time is measured Safety margin is stated

Validation: Performance engineer and service owner review.

- `k6 run --stage 2m:100,5m:100,2m:200,5m:200,2m:400 loadtest/steps.js   # example stepped ramp` expect: the report shows the step where thresholds are crossed
- manual: after the test, time how long latency takes to return to baseline expect: recovery time recorded

Failure modes:
- Test ends at the first failure | detect: Failure mode unobserved | respond: Continue under control to see the failure
- System does not recover | detect: Latency stays high after load removal | respond: Investigate leaks and queues
- Impact on shared systems | detect: Dependencies degraded by the test | respond: Isolate or stub them

ILLUSTRATIVE: Stepped load shows stable operation to 350 requests per second and errors above 420. Beyond that, queues grow; after load stops, the system returns to baseline in three minutes. The stated limit is 300 with a safety margin.

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
**UAT** (complete). Purpose: let the business confirm the delivered solution fits the real need before release.

Entry criteria: The release candidate is deployed to an acceptance environment; Acceptance criteria and UAT scenarios are agreed; Business testers and an acceptance owner are named

Inputs: acceptance criteria; UAT scenarios; acceptance environment and data; named testers

Procedure:
1. Agree the scenarios with the business testers from real work, not only from the specification.
2. Brief the testers, give them realistic data and a way to report issues.
3. Run the scenarios and record result, evidence and tester for each.
4. Triage findings with the product owner into defect, change request or accepted difference.
5. Retest fixes; track open issues to a decision.
6. Obtain the acceptance owner's decision: accept, accept with conditions or reject, recorded with the date.

Deliverables: UAT scenarios and results; issue triage; retest records; acceptance decision

Acceptance: Every scenario has a result and a tester Issues have a decision The acceptance owner's decision is recorded with conditions Testers are business users, not only the delivery team

Validation: Named acceptance owner's decision.

- manual: confirm every UAT scenario row has a result, tester and date expect: none blank
- manual: confirm the build tested equals the release candidate expect: same version

Failure modes:
- Delivery team acts as business testers | detect: No business names in results | respond: Involve real users
- Acceptance given verbally | detect: No record | respond: Record the decision
- Late change requests treated as defects | detect: Scope dispute | respond: Triage with the product owner

ILLUSTRATIVE: Three finance staff run twelve scenarios on the acceptance environment. Two issues are found; one is a defect, the other a change request deferred. The acceptance owner accepts with the deferral recorded.

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
