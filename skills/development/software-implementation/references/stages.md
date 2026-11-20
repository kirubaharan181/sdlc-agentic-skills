# Product implementation: stage reference

## Contents
- [53 Frontend Development](#53)
- [54 Backend Development](#54)
- [55 Full Stack Development](#55)
- [56 Mobile Development](#56)
- [57 API Development](#57)
- [58 Database Development](#58)
- [59 Authentication Development](#59)
- [60 Authorization Development](#60)
- [61 Third-party Integration](#61)
- [62 Real-time Development](#62)
- [63 Data Engineering](#63)
- [64 AI/ML Development](#64)
- [65 Caching & Optimization](#65)
- [66 Error Handling](#66)
- [67 Developer Testing](#67)

## 53
**Frontend Development** (complete). Purpose: build the user-facing part of the application so it is correct, fast, accessible and maintainable, using the agreed designs and API contracts.

Entry criteria: Approved designs and an API contract exist; A design system or component library is in place; The browser and device support policy is known

Inputs: designs and design system; API contract; accessibility and performance requirements; supported browser policy

Procedure:
1. Build from the design system components, and extend them rather than writing page-specific copies; use semantic HTML and correct roles so accessibility starts from structure.
2. Handle all states: loading, empty, error and success, plus validation messages and disabled states, against the real API contract using mocks until the backend exists.
3. Manage state deliberately: keep server data in a data-fetching layer with caching, local state local, and avoid duplicating the same data in several stores.
4. Meet performance budgets: control bundle size with code splitting, optimize images, defer non-critical scripts and measure Core Web Vitals.
5. Protect against common web risks: escape output, avoid unsafe HTML insertion, use content security policy and keep tokens out of local storage where the design allows.
6. Test with unit and component tests, accessibility checks and a few end-to-end journeys, and run them in CI.

Deliverables: components and pages built from the design system; state and data fetching layer; performance measurements; component, accessibility and end-to-end tests

Acceptance: All states are implemented Semantic HTML and keyboard use are verified Performance budgets are measured and met Untrusted data is never inserted as HTML

Validation: Frontend lead review.

- `npx --no-install vitest run && npx --no-install playwright test --grep @a11y   # example; use the project's tools` expect: tests pass, including accessibility checks
- `npx --no-install lighthouse http://localhost:3000 --only-categories=performance,accessibility --quiet --chrome-flags='--headless'   # example` expect: scores meet the agreed budgets

Failure modes:
- Only the happy state built | detect: Blank screen on error | respond: Implement every state
- Bundle grows unchecked | detect: Slow first load | respond: Add a size budget in CI
- Unescaped user content | detect: Script runs from input | respond: Escape and add a content security policy

ILLUSTRATIVE: A product list page uses the design system table, shows skeleton, empty and error states, fetches through a cached data layer, and a CI budget fails the build if the main bundle grows by more than 10 percent.

Gate: 06-053. Approval: none required

## 54
**Backend Development** (complete). Purpose: implement server-side behavior that is correct, secure, observable and easy to change.

Entry criteria: Requirements and API contract are agreed; Data model exists or is being built (stage 58); Development environment runs locally

Inputs: requirements and acceptance criteria; API contract; data access layer; architecture and coding standards

Procedure:
1. Break the work into small vertical slices, each with a test, so the system always builds and passes.
2. Keep business rules in one layer that does not depend on the web framework or database, so they can be tested alone.
3. Validate every input at the boundary, check authorization on every operation and return errors in the agreed format.
4. Handle failure explicitly: timeouts and retries with limits, idempotent writes, and clear errors instead of silent failure.
5. Add structured logs with correlation ids, and metrics for the main operations, without logging sensitive data.
6. Open small pull requests with tests and note any behavior or configuration the reviewer must check.

Deliverables: working backend code; unit and integration tests; logging and metrics hooks; pull requests with notes

Acceptance: Each acceptance criterion has a passing test Inputs are validated and authorization is checked per operation External calls have timeouts and bounded retries Logs carry correlation ids and no secrets

Validation: Code review (stage 69) and CI results.

- `pytest -q --cov=app --cov-fail-under=80   # example threshold; use the project's` expect: passes and meets the agreed coverage
- `grep -rniE 'password|secret|token' app/ --include=*.py | grep -i 'log'` expect: no secret values reach log calls

Failure modes:
- Business rules inside controllers | detect: Tests need a running server | respond: Move rules into a plain layer
- Unbounded retries | detect: Retry storm during an outage | respond: Add limits, backoff and jitter
- Sensitive data in logs | detect: Review finds values | respond: Remove and rotate if secrets

ILLUSTRATIVE: A refund endpoint validates the amount against the original payment, checks the caller owns the order, uses an idempotency key to ignore duplicate requests, and logs the correlation id and outcome without card data.

Gate: 06-054. Approval: none required

## 55
**Full Stack Development** (complete). Purpose: deliver a feature across interface, service and data in one coherent change, without leaving the seams untested.

Entry criteria: The feature is described end to end with acceptance criteria; Front-end and back-end contracts are defined; The whole stack runs locally or in an ephemeral environment

Inputs: feature description and acceptance criteria; API and UI designs; existing front-end and back-end code; test environment

Procedure:
1. Agree the contract between interface and service first; use it to build both sides in parallel against stubs.
2. Implement the thinnest working path from interface to data, then add cases and error handling.
3. Keep state and validation consistent on both sides; the server stays the authority.
4. Test across the seam with at least one end-to-end test of the main path plus unit tests on each side.
5. Check the user experience for loading, empty, error and slow states, and accessibility basics.
6. Release behind a feature flag when the change is risky, with a documented way to turn it off.

Deliverables: working feature across layers; contract and tests on both sides; one end-to-end test; feature flag and removal note

Acceptance: The main path works end to end Error, empty and loading states are handled The server validates everything the client validates A switch-off path exists for risky features

Validation: Code review and product owner demonstration.

- `pytest -q tests/api && npx --no-install playwright test tests/e2e/feature.spec.ts   # example` expect: both pass
- manual: switch the feature flag off and confirm the old behavior returns expect: no errors

Failure modes:
- Client and server rules diverge | detect: Server rejects what the client allowed | respond: Make the server the authority and share the schema
- Only the happy path built | detect: No error-state test | respond: Add the states
- No way to turn off | detect: Flag missing for a risky change | respond: Add the flag before release

ILLUSTRATIVE: A saved-search feature adds a save button, an API endpoint and a table. The contract is agreed first; one end-to-end test saves and reloads a search, and a flag allows hiding the button without a deployment.

Gate: 06-055. Approval: none required

## 56
**Mobile Development** (complete). Purpose: build a mobile app that works on real devices, handles poor networks and respects each platform's rules.

Entry criteria: Requirements and designs are approved; Target platforms and versions are chosen; Test devices or a device farm are available

Inputs: designs and requirements; API contract; target platform versions; store policies

Procedure:
1. Pick the approach (native, cross-platform) based on the needs and the team's skills, and record the reason.
2. Build features in small slices and test each on real devices as well as simulators.
3. Design for poor connectivity: cache sensible data, queue writes, retry with limits and show clear status.
4. Handle the app lifecycle: backgrounding, interruptions, permission refusal and low memory.
5. Store sensitive data in the platform's secure storage, request only needed permissions and explain them to the user.
6. Check the store policies, app size, startup time and battery use before release, and plan staged rollout.

Deliverables: working app builds; device test results; offline and lifecycle tests; store submission checklist

Acceptance: Features work on the supported OS versions and real devices Behavior without a network is defined and tested Permissions are minimal and explained Sensitive data uses secure storage

Validation: Mobile lead review.

- manual: run the main flows on one low-end and one current device with airplane mode toggled expect: flows complete or fail with a clear message
- manual: review the requested permissions against the features that use them expect: each permission is needed

Failure modes:
- Works only on the simulator | detect: Crashes on real devices | respond: Test on real devices
- Data lost when offline | detect: Write fails silently | respond: Queue and retry
- Excess permissions | detect: Store review questions | respond: Remove unneeded ones

ILLUSTRATIVE: A delivery app queues status updates while offline and retries when the network returns; location permission is requested only when the user opens the map, with a message explaining why.

Gate: 06-056. Approval: none required

## 57
**API Development** (complete). Purpose: build the API as specified so that clients get consistent, secure and well-behaved interfaces.

Entry criteria: API specification is approved (stage 27); Data and business logic services are available; Test environment exists

Inputs: approved API specification; business logic and data layer; security requirements; test environment

Procedure:
1. Generate or write the route and schema skeleton from the specification.
2. Implement handlers that validate every input against the schema and return the specified errors.
3. Enforce authentication and per-object authorization in one place and keep it out of handlers.
4. Add pagination, idempotency keys, rate limiting and request logging with correlation ids; never log secrets.
5. Write contract tests that run against the implementation and keep the specification and code in sync.
6. Document known differences from the specification and raise them for decision.

Deliverables: API implementation; contract tests; authorization enforcement; difference notes

Acceptance: Implementation conforms to the specification Authorization is enforced centrally and tested Inputs are validated against schemas Logs have correlation ids and no secrets

Validation: Code review (stage 69) and API test results (stage 81).

- `pytest -q tests/contract` expect: all contract tests pass
- `grep -rniE 'password|secret|token' app/logging.py` expect: no secret values are logged

Failure modes:
- Handler trusts client input | detect: Missing validation on a field | respond: Validate against the schema
- Authorization inside handlers | detect: Inconsistent checks across routes | respond: Centralize
- Implementation drifts from the specification | detect: Contract test fails | respond: Fix code or update the contract by decision

ILLUSTRATIVE: The orders API handlers reject bodies that fail schema validation with the specified 422 format, check object ownership through a shared dependency, and log a correlation id on each request.

Gate: 06-057. Approval: none required

## 58
**Database Development** (complete). Purpose: build the database objects and data access layer that the application needs, safely and testably.

Entry criteria: Database design is approved (stage 26); Development database and migration tooling exist; Naming and migration standards exist

Inputs: approved data design; migration tooling and standards; application data access requirements; test data

Procedure:
1. Write schema changes as versioned, repeatable migrations in source control; never edit the database by hand.
2. Prefer additive, backward-compatible changes so old and new code run against the same schema.
3. Implement queries with parameters, explicit columns and tested access paths; avoid building SQL from strings.
4. Test migrations on a copy with realistic data, forward and where possible backward, and record the duration.
5. Check query plans for the main queries and add indexes where needed.
6. Review with the database administrator before the change goes toward production (stage 132).

Deliverables: migration scripts; data access code; migration test results; query plan evidence

Acceptance: Every change is a versioned migration Queries use parameters Migration ran on realistic data with duration recorded Main queries have reviewed plans

Validation: Database administrator review.

- `alembic upgrade head && alembic downgrade -1 && alembic upgrade head   # example migration tool` expect: all three succeed on a fresh database
- `grep -rnE "execute\(f?\"[^\"]*(%s|\{)" app/` expect: no SQL built by string formatting

Failure modes:
- Manual change in a shared database | detect: Schema differs from migrations | respond: Recreate through migration
- Migration slow on production-size data | detect: Copy run exceeds the window | respond: Batch or redesign
- SQL injection risk | detect: Query built from strings | respond: Use parameters

ILLUSTRATIVE: A migration adds a nullable column and an index concurrently. It runs up, down and up again on a fresh database, takes two minutes on a production-size copy, and the main query plan uses the new index.

Gate: 06-058. Approval: none required

## 59
**Authentication Development** (complete). Purpose: implement login and session handling that proves who the user is without weakening the system.

Entry criteria: Authentication requirements and the identity provider are decided; A threat model covers sign-in (stage 29); Test accounts exist

Inputs: security requirements; identity provider documentation; threat model; session policy

Procedure:
1. Use the chosen identity provider and a maintained library; do not write cryptography or token handling yourself.
2. Store passwords only as salted slow hashes if you manage them, and prefer federated or passwordless sign-in where allowed.
3. Add multi-factor authentication for privileged and sensitive actions, and secure account recovery.
4. Issue sessions or tokens with a short life, secure cookie flags, rotation on privilege change and logout that invalidates them.
5. Limit repeated attempts, and respond the same way for unknown users and wrong passwords.
6. Log sign-in events and failures without logging passwords or tokens, and test the flows including the failures.

Deliverables: authentication code using the provider; session configuration; recovery flow; tests for failure paths

Acceptance: No home-made cryptography Sessions expire and are invalidated on logout Repeated failures are limited Logs contain no credentials

Validation: Security review.

- `pytest -q tests/auth` expect: sign-in, lockout, expiry and logout tests pass
- `grep -rniE 'md5|sha1\(|password.*log' src | head` expect: no weak hashing or password logging found

Failure modes:
- Tokens never expire | detect: Old token still works | respond: Set lifetime and revoke on logout
- Different messages for unknown user and wrong password | detect: Account enumeration possible | respond: Use one message
- Recovery link reusable | detect: Link works twice | respond: Make it single use and short lived

ILLUSTRATIVE: Sign-in uses the company's identity provider with a maintained library; sessions last 30 minutes of inactivity, are invalidated on logout, and five failed attempts trigger a delay and an alert.

Gate: 06-059. Approval: none required

## 60
**Authorization Development** (complete). Purpose: make the system allow each action only to those entitled to take it, checked on the server every time.

Entry criteria: Roles, permissions and data ownership rules are defined; Authentication works (stage 59); Test users with different roles exist

Inputs: permission model; data ownership rules; list of operations and resources; authentication context

Procedure:
1. Define roles and permissions from the business rules, using least privilege and separate duties for risky actions.
2. Check authorization on the server for every operation and every object, not only in the user interface.
3. Check that the user owns or may access the specific record, not only that they have the role.
4. Deny by default: new routes and operations have no access until a rule is added.
5. Log access decisions for sensitive actions, and provide a way to review who can do what.
6. Test with a matrix of roles against operations, including attempts to reach another user's records.

Deliverables: permission model implemented; server-side checks; role-by-operation tests; access review report

Acceptance: Every operation is checked on the server Object-level access is tested Default is deny Sensitive access is logged

Validation: Security review.

- `pytest -q tests/authz   # example matrix of role against operation` expect: all expected allows and denies pass
- manual: as user A request user B's record by changing the id in the URL expect: denied, with no data returned

Failure modes:
- Only the interface hides buttons | detect: Direct request succeeds | respond: Add server checks
- Role check without object check | detect: User reads another's record | respond: Check ownership
- New route unprotected | detect: Access allowed by default | respond: Switch to deny by default

ILLUSTRATIVE: A test matrix tries each role against each operation. It finds that a support role can export all invoices, which should be limited to the customer in the open ticket; the check is added and the test recorded.

Gate: 06-060. Approval: none required

## 61
**Third-party Integration** (complete). Purpose: connect to an outside service in a way that keeps working when the service is slow, changes or fails.

Entry criteria: The integration need and the provider are chosen; The provider's documentation and terms are available; Credentials for a test environment exist

Inputs: provider API documentation; terms and rate limits; data to be exchanged; test environment

Procedure:
1. Read the provider's terms, limits and data handling rules, and confirm the data you send is allowed.
2. Wrap the provider behind an interface of your own, so the rest of the system does not depend on its details.
3. Set timeouts, bounded retries with backoff, and a circuit breaker so failures do not spread.
4. Verify incoming webhooks by signature, and handle repeated or out-of-order messages.
5. Keep credentials in secrets storage, rotate them, and give them the least access offered.
6. Test against the provider's sandbox, simulate failures, and monitor errors and quota use.

Deliverables: integration module behind an interface; failure handling and tests; credential handling; monitoring of errors and quota

Acceptance: The provider is behind an interface Timeouts and retries are bounded Webhooks are verified and idempotent Quota and errors are monitored

Validation: Integration architect review.

- `pytest -q tests/integration/test_provider_failures.py   # example` expect: timeout, error and repeated message cases pass
- manual: send a webhook with a wrong signature to staging expect: rejected

Failure modes:
- Provider outage stops the whole system | detect: Requests pile up | respond: Add timeout and breaker
- Duplicate webhook processed twice | detect: Double effect | respond: Make handling idempotent
- Quota exceeded | detect: Provider blocks calls | respond: Throttle and alert before the limit

ILLUSTRATIVE: A shipping-rate provider sits behind a small interface; calls time out at two seconds, retry twice with backoff, and fall back to a flat rate with a warning if the provider is down.

Gate: 06-061. Approval: none required

## 62
**Real-time Development** (complete). Purpose: deliver updates to users as they happen, while keeping connections, ordering and load under control.

Entry criteria: The need for live updates is justified; Expected concurrent connections are estimated; A transport is chosen (WebSocket, server-sent events or similar)

Inputs: use cases needing live updates; expected connection counts; message volume; authentication model

Procedure:
1. Confirm that live updates are needed; polling is simpler when delay of a few seconds is acceptable.
2. Authenticate each connection and authorize each channel or subscription on the server.
3. Design messages with identifiers and sequence numbers, so clients can detect gaps and request a resync.
4. Handle reconnection: backoff with jitter on the client, and resume from the last sequence number.
5. Limit per-connection message size and rate, and apply back pressure for slow clients.
6. Load test at the expected connection count, and monitor connections, latency and dropped messages.

Deliverables: real-time service; message format with sequence numbers; reconnect and resync logic; load test results

Acceptance: Every subscription is authorized on the server Clients can detect and repair gaps Reconnection uses backoff with jitter Load test reached the expected connection count

Validation: Backend lead review.

- manual: connect a client, kill the network for 30 seconds, restore it expect: client resumes without missing or duplicated messages
- manual: subscribe to another user's channel with a valid token expect: refused

Failure modes:
- Reconnect storm after an outage | detect: Spike of connections | respond: Add jitter and limits
- Missed messages | detect: Client state differs | respond: Add sequence numbers and resync
- Slow client holds memory | detect: Server memory grows | respond: Add limits and drop slow consumers

ILLUSTRATIVE: A live order-status feed numbers each message; after a dropped connection the client asks for everything after its last number, and a load test holds 20,000 connections with p95 delivery under 300 ms.

Gate: 06-062. Approval: none required

## 63
**Data Engineering** (complete). Purpose: build reliable pipelines that move and prepare data, so analysis and products can trust it.

Entry criteria: Sources, targets and ownership are identified; Data quality expectations exist; Data classification is known (stage 30)

Inputs: source systems and schemas; target data model; quality and freshness requirements; privacy rules

Procedure:
1. Define each dataset's owner, schema, freshness target and quality rules before building.
2. Build pipelines to be rerunnable and idempotent, so a repeat run gives the same result.
3. Validate data at entry and at each stage: types, ranges, uniqueness and referential checks, with bad records set aside.
4. Apply privacy rules in the pipeline: masking, minimization and retention.
5. Record lineage and run metadata, and alert on failures, late data and volume anomalies.
6. Test with sample and edge-case data, including late and duplicate records, and document recovery steps.

Deliverables: pipeline code; data quality checks; lineage and run metadata; recovery runbook

Acceptance: Rerunning does not duplicate data Bad records are set aside and counted Privacy rules are applied in the pipeline Late, failed and anomalous runs raise alerts

Validation: Data owner and data engineering lead review.

- `python -m pipelines.run --date 2026-01-01 && python -m pipelines.run --date 2026-01-01 && python -m pipelines.check_counts   # example` expect: row counts equal after the second run
- manual: inject a record with an invalid value and a duplicate expect: the invalid one lands in the quarantine, the duplicate is dropped

Failure modes:
- Rerun duplicates rows | detect: Count doubles | respond: Use keys or replace the partition
- Silent bad data | detect: Nulls reach reports | respond: Add checks and quarantine
- Late data missed | detect: Daily numbers change afterwards | respond: Reprocess a window

ILLUSTRATIVE: A daily orders pipeline replaces its date partition on every run, quarantines rows with negative quantities, masks email addresses before the warehouse load, and alerts when the volume falls 30 percent below the weekly norm.

Gate: 06-063. Approval: none required

## 64
**AI/ML Development** (complete). Purpose: build a model-based feature whose quality is measured, whose limits are known and whose failures are handled.

Entry criteria: The problem is defined with a success measure; Data with a known source and permitted use exists; Evaluation data is held apart from training data

Inputs: problem definition and success measure; datasets and their permitted use; baseline solution; compute and cost limits

Procedure:
1. Start with a simple baseline, such as rules or a basic model, and record its score on the success measure.
2. Split the data before any tuning, keeping a test set that nobody uses for decisions until the end.
3. Train and compare candidates, recording data version, code version, parameters and scores for each run.
4. Evaluate on slices that matter, such as user groups and rare cases, not only the overall average, and examine the worst errors.
5. Define behavior when the model is unsure or wrong: confidence thresholds, human review and a non-model fallback.
6. Package the model with its version, data lineage and a monitoring plan for drift and quality after release.

Deliverables: baseline and candidate comparison; evaluation report with slices; fallback design; versioned model package with monitoring plan

Acceptance: The model beats the baseline on the success measure The test set was used once at the end Slice results and worst errors are reported A fallback exists for low confidence and failure

Validation: AI/ML lead review.

- `python -m ml.evaluate --model models/current --data data/test --by-slice   # example` expect: metrics per slice are printed and meet the thresholds
- manual: check the run record contains data version, code version and parameters expect: all present

Failure modes:
- Leakage between train and test | detect: Scores too good to be true | respond: Re-split by entity or time and rerun
- Average hides weak groups | detect: A slice scores far lower | respond: Fix or limit use for that slice
- No fallback | detect: Failure blocks the user | respond: Add a non-model path

ILLUSTRATIVE: A ticket-routing model beats the keyword baseline overall, but scores lower on short messages; those below the confidence threshold go to a human queue, and weekly monitoring compares accuracy on a labelled sample.

Gate: 06-064. Approval: none required

## 65
**Caching & Optimization** (complete). Purpose: make frequently used paths faster by measuring first, caching where it is safe, and proving the gain.

Entry criteria: A measured performance problem or objective exists; Profiling or tracing is available; Cache invalidation owners are known

Inputs: performance measurements and profiles; hot paths and data access patterns; freshness requirements for data; cache infrastructure

Procedure:
1. Measure the hot path and find where time goes before changing anything.
2. Fix the cheapest cause first: queries, indexes, repeated work and payload size; add caching only for what remains.
3. Decide freshness per item: what can be stale, for how long, and what invalidates it.
4. Design the cache key to include everything that changes the answer, including user or tenant, so one user never sees another's data.
5. Handle misses and failures: the system must still work correctly when the cache is empty or down.
6. Measure again under the same conditions and record the gain and the cost (memory, complexity).

Deliverables: before and after measurements; cache design with freshness rules; invalidation logic and tests; failure-mode test

Acceptance: The gain is measured under the same conditions as the baseline Cache keys include tenant or user where data differs The system is correct with the cache empty or unavailable Staleness limits are documented

Validation: Performance engineer review of the measurements.

- manual: run the same load test before and after and compare p95 expect: improvement matches the report
- manual: stop the cache service and run the functional tests expect: tests pass, possibly slower

Failure modes:
- Stale data shown | detect: Users see old values past the limit | respond: Fix invalidation or shorten the lifetime
- Cache key omits the tenant | detect: One tenant sees another's data | respond: Add the tenant to the key and purge; treat as a security incident
- Optimized without measuring | detect: No baseline recorded | respond: Measure first

ILLUSTRATIVE: Profiling shows 70 percent of a product page's time is one repeated query. An index removes most of it; a 60-second cache keyed by product and locale handles the rest, lowering p95 from 900 ms to 240 ms, and the page still works with the cache down.

Gate: 06-065. Approval: none required

## 66
**Error Handling** (complete). Purpose: make failures visible, contained and recoverable, so a fault in one place does not become an outage or a silent wrong answer.

Entry criteria: The system's main operations and dependencies are known; A logging and error reporting approach exists; An error format for clients is agreed

Inputs: operations and dependencies; error format and codes; logging standard; recovery requirements

Procedure:
1. List how each operation can fail and decide for each whether to retry, fail fast, degrade or stop.
2. Never swallow errors: handle them where there is something useful to do, otherwise pass them up with context.
3. Return errors in the agreed format, with a stable code and a safe message that exposes no internals.
4. Log the full detail with the correlation id on the server, and keep sensitive data out.
5. Keep operations safe to repeat, and leave data consistent when a step fails halfway.
6. Test the failure paths by injecting faults, and check the alerts they cause.

Deliverables: failure decision table; error handling code and format; fault injection tests; alert checks

Acceptance: No error is silently swallowed Client errors expose no internals A failed step leaves data consistent Fault injection tests pass

Validation: Code review.

- `grep -rnE 'except:\s*pass|catch\s*\([^)]*\)\s*\{\s*\}' src | head` expect: no empty handlers found
- `pytest -q tests/failure_paths` expect: injected timeout and error tests pass

Failure modes:
- Stack trace shown to the client | detect: Response includes internals | respond: Return a safe message and log the detail
- Half-completed update | detect: Inconsistent records after failure | respond: Use a transaction or compensating step
- Retries without limit | detect: Repeated load on a failing service | respond: Bound retries and back off

ILLUSTRATIVE: A failed payment call returns a stable code and a short message to the user, logs the provider response with the correlation id, leaves the order marked pending, and a retry job picks it up at most three times.

Gate: 06-066. Approval: none required

## 67
**Developer Testing** (complete). Purpose: let the developer find and fix defects early by testing their own change before it is handed on.

Entry criteria: The change is implemented locally; The test suite runs locally; Acceptance criteria are understood

Inputs: the change; acceptance criteria; test suite and tools; local or ephemeral environment

Procedure:
1. Re-read the acceptance criteria and list the behaviors to check, including error cases.
2. Run the unit tests and add tests for new behavior and for edge cases found.
3. Run the application locally and exercise each criterion by hand, including one unhappy path.
4. Check logs for new warnings or errors and verify data created by the change.
5. Run the project's checks (format, lint, type check) and fix problems.
6. Note what was and was not tested in the pull request.

Deliverables: tests for the change; manual test notes; check results; pull request testing note

Acceptance: Every acceptance criterion was exercised At least one error path was tried Local checks pass Testing note lists gaps

Validation: Reviewer reads the testing note and reruns key tests.

- `pytest -q && ruff check . && mypy .   # example toolchain` expect: all pass
- manual: exercise each acceptance criterion locally and note the result expect: each criterion verified or gap noted

Failure modes:
- Only the happy path tested | detect: No error-case test | respond: Add one
- Tests not run before pushing | detect: CI fails on basic checks | respond: Run checks locally first
- Testing note empty | detect: Reviewer cannot tell what was verified | respond: Write it

ILLUSTRATIVE: A developer adds an export limit. They test 9,999, 10,000 and 10,001 orders locally, see the expected error at 10,001, add a unit test for the boundary and note that large exports were not load tested.

Gate: 06-067. Approval: none required
