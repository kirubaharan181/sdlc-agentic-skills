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
**Test Planning** (complete). Purpose: plan what will be tested, how, by whom and when, so test effort matches risk and the release decision has evidence.

Entry criteria: Requirements and a release scope exist; The risk list is available; Test environments and data are known or being planned

Inputs: requirements and release scope; risk list; architecture and integrations; environment and data availability

Procedure:
1. Define the test objectives from the release goals and the risks, and the exit criteria that will support the release decision.
2. Choose test levels and types per risk: unit, integration, system, performance, security and accessibility, and say what will be automated.
3. Trace requirements and risks to planned tests so gaps are visible.
4. Plan environments, data and tools, with their lead times and owners.
5. Estimate effort and schedule with the dependencies, and name who does what.
6. Agree how defects will be handled and reported, and review the plan with the product owner and developers.

Deliverables: test plan with objectives and exit criteria; requirement and risk to test traceability; environment and data plan; schedule and responsibilities

Acceptance: Exit criteria are measurable Every high risk has planned tests Environment and data lead times are planned The plan was reviewed by product and engineering

Validation: QA lead plan; product owner agreement on exit criteria.

- manual: check each high-risk item in the risk list maps to at least one planned test expect: none unmapped
- manual: check each exit criterion has a number or a yes-no condition expect: none vague

Failure modes:
- Plan lists activities but no criteria | detect: Release decided by feeling | respond: Add measurable exit criteria
- Environment not ready | detect: Tests blocked | respond: Plan lead times
- Risk not covered | detect: Unmapped high risk | respond: Add tests or accept it formally

ILLUSTRATIVE: A payments release plan lists exit criteria of zero open critical defects, all high-risk flows automated and passing, and a load test at 1.5 times peak; each is traced to a risk in the register.

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
**UI Testing** (complete). Purpose: automate checks of the user interface so that regressions in the main journeys are caught on every change, with tests that are stable.

Entry criteria: Stable user journeys are identified; A test environment with test data exists; A UI automation tool is chosen

Inputs: priority user journeys; design and acceptance criteria; test environment; test data

Procedure:
1. Choose the few journeys that matter most to the business and automate those first, rather than every screen.
2. Find elements with stable test identifiers or accessible roles, not with brittle positions or generated class names.
3. Make each test independent: it creates its own data and does not rely on another test's result.
4. Wait for conditions, never for fixed delays, and keep assertions on what the user sees and can do.
5. Run in CI on every change for the fast set, and nightly for the wider set, capturing screenshots and traces on failure.
6. Track flaky tests, and fix or remove them within an agreed time.

Deliverables: automated journey tests; test data setup; CI configuration with failure artifacts; flaky test list

Acceptance: Core journeys are covered Tests are independent and use stable selectors Failures give a screenshot or trace Flaky tests are tracked with a deadline

Validation: QA lead review.

- `npx --no-install playwright test --reporter=line   # example; use the project's tool` expect: all pass
- `npx --no-install playwright test --repeat-each=5 tests/checkout.spec.ts   # example` expect: no intermittent failure in five runs

Failure modes:
- Flaky test ignored | detect: Intermittent failures in CI | respond: Fix the wait or isolate the data
- Selectors tied to layout | detect: Tests break on cosmetic changes | respond: Use test ids or roles
- Tests depend on order | detect: Fail when run alone | respond: Make them independent

ILLUSTRATIVE: Five journeys are automated: sign up, sign in, search, add to basket and pay. Each creates its own user, waits on visible conditions, and attaches a trace on failure; the checkout test ran five times without a flake.

Gate: 08-082. Approval: none required

## 83
**Functional Testing** (complete). Purpose: confirm by hands-on exploration that each feature does what the requirements say, including the cases nobody scripted.

Entry criteria: Build is deployed in a test environment; Requirements and acceptance criteria are available; Test data and accounts exist

Inputs: requirements and acceptance criteria; build under test; test data; known issues list

Procedure:
1. Write test cases from each acceptance criterion with the steps, data and expected result.
2. Add cases from boundaries and rules: smallest and largest values, empty input, invalid combinations and permission differences.
3. Execute the cases, recording actual results with evidence for each failure: steps, data, screenshots and the build.
4. Spend a time-boxed session exploring beyond the scripts, following what looks odd, and record what was covered.
5. Report defects with clear steps and severity, and retest fixes against the original steps.
6. Summarize coverage of the criteria and the open defects.

Deliverables: test cases with results; defect reports with evidence; exploration notes; coverage summary against acceptance criteria

Acceptance: Every acceptance criterion has a case and a result Failures have reproducible steps and evidence An exploration session was recorded Fixes were retested

Validation: QA lead review.

- manual: count acceptance criteria and test cases that reference them expect: every criterion has at least one case
- manual: take three defect reports and reproduce them from the steps alone expect: all reproduce

Failure modes:
- Only happy paths tested | detect: Defects found by users | respond: Add boundary and negative cases
- Defect not reproducible | detect: Developer cannot repeat it | respond: Add steps, data and build
- Fix not retested | detect: Defect returns | respond: Retest with the original steps

ILLUSTRATIVE: Testing a discount feature from its criteria finds a correct result for a single code, then exploration with two codes applied in different order shows a different total; the defect is reported with the exact order and amounts.

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

- `npx --no-install playwright test --reporter=line   # example` expect: all journeys pass
- `npx --no-install playwright test --repeat-each=3` expect: no intermittent failures

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
**Sanity Testing** (complete). Purpose: decide quickly after a build or fix whether it is stable enough to deserve the full test effort.

Entry criteria: A new build or a fix is deployed; A short list of must-work checks exists; The tester has access to the environment

Inputs: new build and release notes; list of core checks; environment access; recent changes

Procedure:
1. Confirm the right build is deployed by checking its version identifier, before anything else.
2. Run the short list of core checks: start up, sign in, the main journey and the changed area, in minutes, not hours.
3. Check the changes named in the release notes, and one neighbouring area likely to be affected.
4. Stop at the first blocking failure and return the build with the failing step and evidence.
5. If all pass, record the result and release the build to the full test effort.
6. Keep the list short and review it when core functionality changes.

Deliverables: build version confirmation; sanity check result; return note when blocked; updated core check list

Acceptance: The build identifier was confirmed Checks finish within the agreed time A failure stops further testing with evidence The list is kept short and current

Validation: QA lead decision to accept the build.

- `curl -s https://test.example.com/version   # example` expect: returns the expected build id
- manual: run the core checks and time them expect: complete within the agreed time

Failure modes:
- Wrong build tested | detect: Version differs from the release note | respond: Redeploy and restart
- List grows into a full test | detect: Takes hours | respond: Cut back to blockers
- Blocked build still tested in full | detect: Wasted effort | respond: Stop and return the build

ILLUSTRATIVE: After a hotfix, the tester confirms the build id, signs in, completes a purchase and checks the fixed discount rule in eight minutes, then releases the build for the regression run.

Gate: 08-087. Approval: none required

## 88
**Cross-browser Testing** (complete). Purpose: make sure the product works for users on the browsers and versions that matter, based on who actually uses it.

Entry criteria: Analytics or customer data on browser use exist; Core journeys are defined; Access to the browsers or a cloud grid exists

Inputs: browser usage data; supported browser policy; core journeys; known rendering differences

Procedure:
1. Build the support matrix from real usage data and the support policy: browser, version range and operating system.
2. Rank the matrix by usage and risk, and decide which combinations get full tests and which get a smoke check.
3. Run the core journeys on each tier, using automation where it exists and manual checks for layout and input behavior.
4. Compare layout, fonts, forms, media and scripts, and note where features degrade without breaking the task.
5. Record each difference with browser, version, steps and a screenshot, and decide to fix, work around or document.
6. Review the matrix whenever usage shifts or a new browser release changes the picture.

Deliverables: support matrix with tiers; results per browser and version; differences log; decisions on fixes or documented limits

Acceptance: The matrix is based on usage data Core journeys passed on each top tier Differences have evidence and a decision The matrix has a review date

Validation: QA lead review.

- `npx --no-install playwright test --project=chromium --project=firefox --project=webkit   # example` expect: core journeys pass on all projects
- manual: open the checkout on the oldest supported version of each browser expect: task can be completed

Failure modes:
- Matrix based on guesses | detect: Users on untested browsers | respond: Use analytics data
- Cosmetic issue treated as blocker | detect: Time wasted | respond: Judge by task impact
- Matrix never updated | detect: New version breaks the page | respond: Schedule a review

ILLUSTRATIVE: Usage data places four browsers above 5 percent each; those get full journey runs, the others a smoke check. A date picker is found to behave differently in one version and gets a workaround.

Gate: 08-088. Approval: none required

## 89
**Mobile Compatibility Testing** (complete). Purpose: check that the product works on the phones and tablets users own, across sizes, operating systems, hardware and conditions.

Entry criteria: A mobile app or responsive web build exists; Device usage data exists; Real devices or a device farm are accessible

Inputs: device and operating system usage data; app or responsive build; core journeys; hardware features used

Procedure:
1. Select the device set from usage data: popular models, oldest supported OS, smallest and largest screens, low-memory devices.
2. Run the core journeys on each device, including rotation, text size changes, and dark mode.
3. Test hardware dependent features such as camera, location, biometrics, notifications and sensors with permission granted and denied.
4. Test interruptions and conditions: incoming calls, low battery, low storage, background and resume, and poor or lost connectivity.
5. Record issues with device, OS version, steps and a recording, and group them by cause.
6. Update the device set each quarter from fresh usage data.

Deliverables: device matrix from usage data; journey results per device; hardware and interruption test results; issue list grouped by cause

Acceptance: Devices were chosen from data Permission denied and interruption cases were tested Issues carry device and OS details The device set has a review date

Validation: QA lead review.

- manual: run checkout on the oldest supported OS and the smallest screen expect: task completes and nothing is cut off
- manual: deny camera permission and open the scan feature expect: clear message and an alternative

Failure modes:
- Only newest devices tested | detect: Crashes on older phones | respond: Add oldest supported OS and low memory
- Text clipped at large font size | detect: Buttons unreadable | respond: Fix layouts for scaled text
- Permission denial breaks the app | detect: Blank screen | respond: Handle denial with a message

ILLUSTRATIVE: Usage data selects eight devices. A low-memory phone restarts the app during photo upload, and a denied location permission produces a blank map; both are logged with device and OS version.

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

- `npx --no-install playwright test tests/a11y --reporter=line   # example: axe-based checks in the project's test runner` expect: no serious or critical violations on the key pages
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
**Stress Testing** (complete). Purpose: find where and how the system breaks when pushed beyond its design load, and check that it fails safely and recovers.

Entry criteria: Capacity limits and expected peaks are known; A production-like test environment exists; Monitoring is in place

Inputs: expected peak load; capacity limits; test environment with monitoring; dependency list

Procedure:
1. Define the stress goals: how far above peak to push, and which behaviors to observe.
2. Increase load in steps beyond the peak, recording latency, error rate and resource use at each step.
3. Record the point where service degrades and the first resource that saturates.
4. Check the failure behavior: whether errors are clear, protection such as rate limits and queues works, and nothing is corrupted.
5. Remove the load and measure how long recovery takes and whether manual action is needed.
6. Report the breaking point, the failure behavior and the fixes, and rerun after fixes.

Deliverables: stress test plan and load profile; breaking point with the first saturated resource; failure and recovery observations; fixes and retest results

Acceptance: The load exceeded the expected peak The first saturating resource is named Recovery time is measured Data integrity was checked after the test

Validation: Performance testing specialist report; service owner review.

- `k6 run --stage 5m:2x,5m:3x,5m:4x scripts/stress.js   # example; stages multiply expected peak` expect: results show where errors begin
- manual: after the test, compare record counts and run the data integrity query expect: no corruption or loss

Failure modes:
- System does not recover | detect: Errors continue after load stops | respond: Fix queues and connection handling
- Data corrupted under overload | detect: Integrity check fails | respond: Treat as a defect and fix
- Test environment smaller than production | detect: Results not comparable | respond: State the scale factor

ILLUSTRATIVE: Load is raised to four times peak. Errors begin at 2.5 times when the database connection pool is exhausted; after the load stops, the service takes 40 minutes to recover until the pool timeout is fixed.

Gate: 08-093. Approval: none required

## 94
**Soak Testing** (complete). Purpose: find problems that appear only when a system runs for a long time, such as leaks, drift and slow degradation.

Entry criteria: A stable build and a long-running environment exist; Monitoring of memory, handles and storage is in place; A realistic load profile exists

Inputs: realistic load profile; monitoring dashboards; baseline resource use; scheduled jobs and rotations

Procedure:
1. Define the duration and a steady realistic load that includes scheduled jobs, backups and log rotation.
2. Record baselines at the start: memory, open connections, file handles, disk, thread counts and latency.
3. Sample the same measures through the run, and watch for upward trends rather than for single peaks.
4. Investigate any steady growth with heap, handle or connection dumps, and find the source.
5. Check the effect of events during the run, such as certificate or token expiry, cache growth and clock changes.
6. Compare the end with the start, report the trends and fix leaks, then repeat the run.

Deliverables: soak plan with duration and load; baseline and time series; leak investigation; comparison of start and end

Acceptance: The duration covers scheduled jobs and rotations Trends are examined, not only peaks Leaks have a source identified Start and end measures are compared

Validation: Performance testing specialist report.

- manual: plot memory and open connections over the run and fit a trend line expect: slope near zero, or a leak recorded
- manual: compare p95 latency in the first and last hour expect: within the agreed margin

Failure modes:
- Run too short | detect: Leak not visible | respond: Extend to cover several cycles
- Memory rises steadily | detect: Out-of-memory after hours | respond: Find and fix the leak
- Disk fills with logs | detect: Space alarm during run | respond: Fix rotation and retention

ILLUSTRATIVE: A 24-hour run at average load shows memory rising 40 MB per hour. A heap dump finds an unbounded cache; after adding a size limit a repeat run stays flat and latency in the last hour matches the first.

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
**Defect Management** (complete). Purpose: track every defect from discovery to verified closure, so nothing is lost and the team can see quality trends.

Entry criteria: A defect tracking tool is available; Severity and priority definitions are agreed; Roles for triage are named

Inputs: defect reports; severity and priority definitions; release schedule; test results

Procedure:
1. Require each report to carry steps, expected and actual result, environment, build and evidence.
2. Triage on a schedule: confirm, remove duplicates, set severity by impact and priority by urgency, and assign an owner.
3. Track status through a defined flow, and see that no defect stays unowned or untouched beyond the agreed time.
4. Have the reporter or a tester verify the fix on a build before closing.
5. Analyze trends: where defects are found, where they were introduced and how long they stay open.
6. Use the analysis to change the process, for example adding a test where defects cluster.

Deliverables: defect records with required fields; triage decisions; verification records; trend report

Acceptance: Each defect has steps, evidence and an owner Severity follows the written definitions Fixes are verified before closure Trends feed process changes

Validation: QA lead review.

- manual: list open defects older than the agreed age or without an owner expect: each has a decision
- manual: sample five closed defects and check for a verification note expect: all have one

Failure modes:
- Duplicates multiply | detect: Same issue many times | respond: Merge during triage
- Severity inflation | detect: Everything marked critical | respond: Apply written definitions
- Closed without verification | detect: Reopened later | respond: Require verification

ILLUSTRATIVE: A weekly triage closes six duplicates, downgrades two inflated severities and assigns five unowned defects. The trend report shows most escaped defects came from the import module, which gets extra tests.

Gate: 08-096. Approval: none required

## 97
**Test Sign-off** (complete). Purpose: give the release decision-maker an honest, evidence-based statement of test status, with remaining risk stated in plain terms.

Entry criteria: Planned test execution is finished or cut off at a stated point; The test plan with exit criteria exists (stage 78); Defect data is current (stage 96)

Inputs: test plan and exit criteria; execution results and coverage; open defect list; risk register

Procedure:
1. Compare results with each exit criterion and mark it met, not met or waived, with the figure behind it.
2. List every open defect above the agreed severity, with impact, workaround and owner.
3. State what was not tested, and why, so absence of evidence is not read as evidence of absence.
4. Check that test results belong to the build proposed for release by comparing build identifiers and commit hashes.
5. Write the recommendation: release, release with conditions, or hold, with the residual risks.
6. Present it to the named release approver, record the decision and the waivers with their owners, and archive the evidence.

Deliverables: exit criteria scorecard; open defect and waiver list; not-tested list; sign-off record with the decision and approver

Acceptance: Each exit criterion has a figure and a status Results match the build proposed for release Untested areas are listed Waivers have a named owner

Validation: Named release approver decides; QA lead recommends.

- manual: compare the build id in the test report with the build id in the release candidate expect: identical
- manual: check every waived criterion has an owner, reason and expiry expect: none missing

Failure modes:
- Results from an older build | detect: Build ids differ | respond: Rerun the affected tests on the candidate
- Waivers without owners | detect: Criterion waived with no name | respond: Obtain a named decision
- Sign-off hides untested areas | detect: No not-tested list | respond: Add it before the meeting

ILLUSTRATIVE: The scorecard shows 7 of 8 exit criteria met; the load test ran at 1.2 times peak against a target of 1.5. The QA lead recommends release with a condition, the product owner accepts it with a retest date, and the waiver is recorded.

Gate: 08-097. Approval: none required
