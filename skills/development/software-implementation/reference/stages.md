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
**Frontend Development** (stub). Purpose: implement accessible client behavior and resilient interface states.

Inputs: approved UI/UX specification; API contracts and browser support matrix; design tokens and accessibility criteria

Procedure:
1. Inspect routing, state management, component conventions and existing design system.
2. Implement semantic components, responsive layout, keyboard behavior and loading/empty/error states.
3. Integrate typed or validated API boundaries and handle cancellation/retry safely.
4. Add component and browser tests for critical interactions; verify accessibility and console/network errors.

Deliverables: component implementation; UI state model; component/browser tests; accessibility evidence

Acceptance: Critical flows work at supported viewports. Keyboard and screen-reader semantics are preserved. No unhandled errors or leaked async state.

Validation: UI peer review and browser test run.
Gate: 06-053. Approval: none required

## 54
**Backend Development** (stub). Purpose: implement service behavior with explicit contracts and operational controls.

Inputs: domain rules and API contract; data model and transaction constraints; security and performance requirements

Procedure:
1. Trace request handling through validation, domain logic, persistence and response mapping.
2. Enforce authentication/authorization at the service boundary and avoid trusting client fields.
3. Implement transaction, idempotency, timeout, retry and error semantics appropriate to side effects.
4. Add unit/integration tests, structured logs and metrics without sensitive payloads.

Deliverables: service change; API/error contract; migration if needed; backend test evidence

Acceptance: Authorization is server-side. Failure paths do not leak secrets or corrupt state. Tests cover boundaries and duplicate requests.

Validation: Code review and service integration tests.
Gate: 06-054. Approval: none required

## 55
**Full Stack Development** (stub). Purpose: deliver a coherent vertical slice across UI, service and persistence.

Inputs: user story and acceptance examples; frontend/backend/API contracts; data and deployment constraints

Procedure:
1. Trace the user journey across UI, API, domain service and persistence before editing.
2. Define compatible request/response and state transitions across layers.
3. Implement one end-to-end slice with validation, authorization, observability and failure handling.
4. Test the slice at component, API and integration levels; document deployment and migration impact.

Deliverables: vertical-slice change; contract and schema updates; cross-layer test evidence

Acceptance: UI and service behavior agree on contracts. Data changes are backward-compatible or migrated safely. Critical user journey has reproducible end-to-end evidence.

Validation: Cross-layer code review and E2E test.
Gate: 06-055. Approval: none required

## 56
**Mobile Development** (stub). Purpose: implement mobile behavior across device lifecycle and store constraints.

Inputs: platform targets and OS versions; design and API contracts; permissions, offline and store requirements

Procedure:
1. Inspect app lifecycle, navigation, state, networking and platform-specific conventions.
2. Implement permission prompts, secure local storage, offline/retry behavior and background lifecycle handling.
3. Test device sizes, OS versions, connectivity transitions and accessibility.
4. Validate signing/build configuration and store policy constraints without exposing signing secrets.

Deliverables: mobile feature; permission/data handling notes; device test matrix; build evidence

Acceptance: App resumes and recovers from network/lifecycle changes. Permissions are least-privilege and explained. Supported OS/device matrix passes.

Validation: Device testing and mobile release review.
Gate: 06-056. Approval: none required

## 57
**API Development** (stub). Purpose: implement a versioned and testable API contract.

Inputs: approved OpenAPI or interface contract; consumer and authorization requirements; data model and latency constraints

Procedure:
1. Implement route/resource semantics, schema validation and consistent error responses from the approved contract.
2. Enforce authentication, object-level authorization, rate limits and idempotency for side effects.
3. Handle pagination, filtering, version compatibility, timeouts and correlation IDs.
4. Run contract tests for success, invalid input, unauthorized access, boundary values and consumer compatibility.

Deliverables: API implementation; OpenAPI/schema update; contract test report; consumer migration note

Acceptance: Implementation matches the published contract. Auth and error cases are tested. Breaking changes require version and migration approval.

Validation: Consumer contract review and automated API tests.
Gate: 06-057. Approval: none required

## 58
**Database Development** (stub). Purpose: implement data access and schema evolution without integrity loss.

Inputs: logical data model and query requirements; transaction and concurrency model; migration and recovery policy

Procedure:
1. Implement constraints, indexes and parameterized queries based on observed access patterns.
2. Define transaction boundaries, isolation, concurrency and retry behavior.
3. Write forward and rollback/forward-fix migration scripts with pre/post checks.
4. Test data integrity, query plans and migration on representative volume.

Deliverables: schema/query change; migration scripts; integrity assertions; query plan evidence

Acceptance: Constraints protect invariants. Migration is repeatable and rehearsed. Performance is measured against a representative workload.

Validation: DBA review and migration rehearsal.
Gate: 06-058. Approval: none required

## 59
**Authentication Development** (stub). Purpose: implement identity proof and credential lifecycle securely.

Inputs: identity provider and protocol requirements; session/token lifecycle; threat model and user experience

Procedure:
1. Choose supported OIDC/OAuth/SAML flow based on client type and trust boundaries.
2. Validate issuer, audience, signature, expiry, nonce/state and redirect URI as applicable.
3. Protect refresh tokens, cookies, secrets and recovery flows; implement rotation and revocation.
4. Test replay, CSRF, redirect abuse, expiry and account recovery scenarios.

Deliverables: authentication flow design; secure configuration; auth test evidence

Acceptance: No credential is stored or logged insecurely. Token/session validation is complete. Recovery and revocation paths are tested.

Validation: Independent security review.
Gate: 06-059. Approval: none required

## 60
**Authorization Development** (stub). Purpose: enforce resource and action permissions at trusted boundaries.

Inputs: roles/attributes and resource ownership model; sensitive actions and data classification; policy and audit requirements

Procedure:
1. Define policy semantics for subject, action, resource and context.
2. Enforce authorization server-side at every relevant endpoint and background job.
3. Test horizontal/vertical privilege escalation, tenant isolation and default-deny behavior.
4. Emit auditable decision metadata without leaking sensitive data.

Deliverables: authorization policy; permission matrix; negative security tests; audit event spec

Acceptance: Unauthenticated and unauthorized paths deny by default. Tenant/object ownership checks are enforced. Negative tests cover privilege boundaries.

Validation: Security review and access-control test.
Gate: 06-060. Approval: none required

## 61
**Third-party Integration** (stub). Purpose: integrate an external system with explicit contract and failure isolation.

Inputs: partner API/contract and credentials via approved secret store; rate limits and service objectives; data mapping and privacy constraints

Procedure:
1. Validate partner contract, authentication, version and sandbox availability.
2. Map external schemas to internal domain types with validation and provenance.
3. Implement timeouts, bounded retries, idempotency, circuit breaking and dead-letter/reconciliation where appropriate.
4. Test partner errors, throttling, duplicate delivery, schema drift and outage recovery.

Deliverables: integration adapter; mapping specification; contract tests; operational runbook

Acceptance: External failures are isolated and observable. Retries cannot create unsafe duplicate effects. Credentials and personal data are protected.

Validation: Contract test and integration owner review.
Gate: 06-061. Approval: none required

## 62
**Real-time Development** (stub). Purpose: deliver ordered, recoverable real-time updates.

Inputs: event/message contract; ordering and delivery guarantees; connection and scale profile

Procedure:
1. Define event schema, partition/key strategy, ordering scope and delivery semantics.
2. Implement reconnect, replay, backpressure, deduplication and client state reconciliation.
3. Secure channels and authorize subscriptions at resource level.
4. Test burst load, dropped connections, duplicate/out-of-order events and consumer lag.

Deliverables: event contract; stream implementation; recovery behavior; load/reconnect tests

Acceptance: Ordering guarantee is explicit. Clients recover without missing or duplicating state. Backpressure and resource limits are enforced.

Validation: Load and failure-injection review.
Gate: 06-062. Approval: none required

## 63
**Data Engineering** (stub). Purpose: build reproducible and governed data pipelines.

Inputs: source contracts and data classification; target model and freshness objective; volume, quality and lineage expectations

Procedure:
1. Define ingestion mode, watermark, schema evolution and replay boundary.
2. Implement idempotent transforms, validation rules, quarantine and dead-letter handling.
3. Capture lineage, quality metrics, access controls and retention behavior.
4. Test late, duplicate, malformed and backfilled data at representative scale.

Deliverables: pipeline DAG; schema contract; quality report; lineage and replay runbook

Acceptance: Reprocessing is deterministic or explicitly reconciled. Quality failures are visible and bounded. Lineage and ownership are complete.

Validation: Data owner acceptance and pipeline replay test.
Gate: 06-063. Approval: none required

## 64
**AI/ML Development** (stub). Purpose: deliver an evaluated and monitored ML capability.

Inputs: problem framing and intended use; approved dataset and privacy basis; baseline and evaluation criteria

Procedure:
1. Define task, users, prohibited use, baseline and failure costs before model choice.
2. Inspect data provenance, representativeness, leakage, label quality and split strategy.
3. Train or integrate the model with reproducible configuration; evaluate task metrics and subgroup failure modes.
4. Add safety guardrails, human fallback, latency/cost monitoring and model/data version traceability.

Deliverables: model/data card; reproducible experiment; evaluation report; deployment and monitoring plan

Acceptance: Evaluation matches intended use and baseline. Data leakage and subgroup failures are assessed. Fallback and monitoring are operationally defined.

Validation: Independent model risk and product review.
Gate: 06-064. Approval: none required

## 65
**Caching & Optimization** (stub). Purpose: improve measured performance without violating correctness.

Inputs: baseline workload and latency profile; consistency/freshness requirements; resource and cost limits

Procedure:
1. Profile before changing code; identify dominant cost and reproducible baseline.
2. Choose cache key, TTL, invalidation and consistency behavior based on data semantics.
3. Bound memory, stampede, stale data and eviction behavior.
4. Compare before/after p50/p95/p99, throughput, error rate and cost under equivalent load.

Deliverables: profile report; optimization change; cache policy; before/after benchmark

Acceptance: Improvement is measured against baseline. Correctness and freshness invariants hold. No unbounded memory or stale-data risk is introduced.

Validation: Performance and correctness regression review.
Gate: 06-065. Approval: none required

## 66
**Error Handling** (stub). Purpose: make failures predictable, diagnosable and safe to retry.

Inputs: failure taxonomy and API contract; retry/idempotency constraints; logging and alert requirements

Procedure:
1. Classify validation, dependency, timeout, authorization and internal failures.
2. Map errors to stable codes and safe user-facing messages.
3. Apply retries only to transient idempotent operations; define timeout and cancellation behavior.
4. Test fault injection and ensure logs include correlation context but exclude secrets and sensitive payloads.

Deliverables: error taxonomy; response mapping; fault-injection tests; runbook updates

Acceptance: No stack trace or secret leaks to users. Retry policy cannot multiply side effects. Errors are observable and actionable.

Validation: Failure-path test and security review.
Gate: 06-066. Approval: none required

## 67
**Developer Testing** (stub). Purpose: verify software behavior using risk-based and reproducible tests.

Inputs: testable acceptance criteria and risk profile; test environment and data; supported platform/workload matrix

Procedure:
1. Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
2. Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
3. Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
4. Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
5. Run focused unit, lint, type, build and local integration checks before requesting review.

Deliverables: test strategy or plan; version-pinned test report; defect records; coverage and limitation summary; developer verification transcript

Acceptance: Critical risks have test coverage. Evidence identifies build, environment, data and result. Flaky or blocked tests are not reported as PASS. All required local checks pass on the exact working-tree revision.

Validation: Independent QA review and acceptance decision. Capture command, exit status and output for each required check.
Gate: 06-067. Approval: none required
