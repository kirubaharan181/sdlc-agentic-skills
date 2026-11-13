# Product implementation — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 53. Frontend Development

**Purpose:** implement accessible client behavior and resilient interface states

**Procedure:**
- Inspect routing, state management, component conventions and existing design system.
- Implement semantic components, responsive layout, keyboard behavior and loading/empty/error states.
- Integrate typed or validated API boundaries and handle cancellation/retry safely.
- Add component and browser tests for critical interactions; verify accessibility and console/network errors.

**Inputs:** approved UI/UX specification, API contracts and browser support matrix, design tokens and accessibility criteria
**Artifact:** component implementation
**Verification:** UI peer review and browser test run.
**Handoff:** Transfer component implementation with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 54. Backend Development

**Purpose:** implement service behavior with explicit contracts and operational controls

**Procedure:**
- Trace request handling through validation, domain logic, persistence and response mapping.
- Enforce authentication/authorization at the service boundary and avoid trusting client fields.
- Implement transaction, idempotency, timeout, retry and error semantics appropriate to side effects.
- Add unit/integration tests, structured logs and metrics without sensitive payloads.

**Inputs:** domain rules and API contract, data model and transaction constraints, security and performance requirements
**Artifact:** service change
**Verification:** Code review and service integration tests.
**Handoff:** Transfer service change with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 55. Full Stack Development

**Purpose:** deliver a coherent vertical slice across UI, service and persistence

**Procedure:**
- Trace the user journey across UI, API, domain service and persistence before editing.
- Define compatible request/response and state transitions across layers.
- Implement one end-to-end slice with validation, authorization, observability and failure handling.
- Test the slice at component, API and integration levels; document deployment and migration impact.

**Inputs:** user story and acceptance examples, frontend/backend/API contracts, data and deployment constraints
**Artifact:** vertical-slice change
**Verification:** Cross-layer code review and E2E test.
**Handoff:** Transfer vertical-slice change with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 56. Mobile Development

**Purpose:** implement mobile behavior across device lifecycle and store constraints

**Procedure:**
- Inspect app lifecycle, navigation, state, networking and platform-specific conventions.
- Implement permission prompts, secure local storage, offline/retry behavior and background lifecycle handling.
- Test device sizes, OS versions, connectivity transitions and accessibility.
- Validate signing/build configuration and store policy constraints without exposing signing secrets.

**Inputs:** platform targets and OS versions, design and API contracts, permissions, offline and store requirements
**Artifact:** mobile feature
**Verification:** Device testing and mobile release review.
**Handoff:** Transfer mobile feature with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 57. API Development

**Purpose:** implement a versioned and testable API contract

**Procedure:**
- Implement route/resource semantics, schema validation and consistent error responses from the approved contract.
- Enforce authentication, object-level authorization, rate limits and idempotency for side effects.
- Handle pagination, filtering, version compatibility, timeouts and correlation IDs.
- Run contract tests for success, invalid input, unauthorized access, boundary values and consumer compatibility.

**Inputs:** approved OpenAPI or interface contract, consumer and authorization requirements, data model and latency constraints
**Artifact:** API implementation
**Verification:** Consumer contract review and automated API tests.
**Handoff:** Transfer API implementation with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 58. Database Development

**Purpose:** implement data access and schema evolution without integrity loss

**Procedure:**
- Implement constraints, indexes and parameterized queries based on observed access patterns.
- Define transaction boundaries, isolation, concurrency and retry behavior.
- Write forward and rollback/forward-fix migration scripts with pre/post checks.
- Test data integrity, query plans and migration on representative volume.

**Inputs:** logical data model and query requirements, transaction and concurrency model, migration and recovery policy
**Artifact:** schema/query change
**Verification:** DBA review and migration rehearsal.
**Handoff:** Transfer schema/query change with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 59. Authentication Development

**Purpose:** implement identity proof and credential lifecycle securely

**Procedure:**
- Choose supported OIDC/OAuth/SAML flow based on client type and trust boundaries.
- Validate issuer, audience, signature, expiry, nonce/state and redirect URI as applicable.
- Protect refresh tokens, cookies, secrets and recovery flows; implement rotation and revocation.
- Test replay, CSRF, redirect abuse, expiry and account recovery scenarios.

**Inputs:** identity provider and protocol requirements, session/token lifecycle, threat model and user experience
**Artifact:** authentication flow design
**Verification:** Independent security review.
**Handoff:** Transfer authentication flow design with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 60. Authorization Development

**Purpose:** enforce resource and action permissions at trusted boundaries

**Procedure:**
- Define policy semantics for subject, action, resource and context.
- Enforce authorization server-side at every relevant endpoint and background job.
- Test horizontal/vertical privilege escalation, tenant isolation and default-deny behavior.
- Emit auditable decision metadata without leaking sensitive data.

**Inputs:** roles/attributes and resource ownership model, sensitive actions and data classification, policy and audit requirements
**Artifact:** authorization policy
**Verification:** Security review and access-control test.
**Handoff:** Transfer authorization policy with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 61. Third-party Integration

**Purpose:** integrate an external system with explicit contract and failure isolation

**Procedure:**
- Validate partner contract, authentication, version and sandbox availability.
- Map external schemas to internal domain types with validation and provenance.
- Implement timeouts, bounded retries, idempotency, circuit breaking and dead-letter/reconciliation where appropriate.
- Test partner errors, throttling, duplicate delivery, schema drift and outage recovery.

**Inputs:** partner API/contract and credentials via approved secret store, rate limits and service objectives, data mapping and privacy constraints
**Artifact:** integration adapter
**Verification:** Contract test and integration owner review.
**Handoff:** Transfer integration adapter with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 62. Real-time Development

**Purpose:** deliver ordered, recoverable real-time updates

**Procedure:**
- Define event schema, partition/key strategy, ordering scope and delivery semantics.
- Implement reconnect, replay, backpressure, deduplication and client state reconciliation.
- Secure channels and authorize subscriptions at resource level.
- Test burst load, dropped connections, duplicate/out-of-order events and consumer lag.

**Inputs:** event/message contract, ordering and delivery guarantees, connection and scale profile
**Artifact:** event contract
**Verification:** Load and failure-injection review.
**Handoff:** Transfer event contract with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 63. Data Engineering

**Purpose:** build reproducible and governed data pipelines

**Procedure:**
- Define ingestion mode, watermark, schema evolution and replay boundary.
- Implement idempotent transforms, validation rules, quarantine and dead-letter handling.
- Capture lineage, quality metrics, access controls and retention behavior.
- Test late, duplicate, malformed and backfilled data at representative scale.

**Inputs:** source contracts and data classification, target model and freshness objective, volume, quality and lineage expectations
**Artifact:** pipeline DAG
**Verification:** Data owner acceptance and pipeline replay test.
**Handoff:** Transfer pipeline DAG with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 64. AI/ML Development

**Purpose:** deliver an evaluated and monitored ML capability

**Procedure:**
- Define task, users, prohibited use, baseline and failure costs before model choice.
- Inspect data provenance, representativeness, leakage, label quality and split strategy.
- Train or integrate the model with reproducible configuration; evaluate task metrics and subgroup failure modes.
- Add safety guardrails, human fallback, latency/cost monitoring and model/data version traceability.

**Inputs:** problem framing and intended use, approved dataset and privacy basis, baseline and evaluation criteria
**Artifact:** model/data card
**Verification:** Independent model risk and product review.
**Handoff:** Transfer model/data card with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 65. Caching & Optimization

**Purpose:** improve measured performance without violating correctness

**Procedure:**
- Profile before changing code; identify dominant cost and reproducible baseline.
- Choose cache key, TTL, invalidation and consistency behavior based on data semantics.
- Bound memory, stampede, stale data and eviction behavior.
- Compare before/after p50/p95/p99, throughput, error rate and cost under equivalent load.

**Inputs:** baseline workload and latency profile, consistency/freshness requirements, resource and cost limits
**Artifact:** profile report
**Verification:** Performance and correctness regression review.
**Handoff:** Transfer profile report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 66. Error Handling

**Purpose:** make failures predictable, diagnosable and safe to retry

**Procedure:**
- Classify validation, dependency, timeout, authorization and internal failures.
- Map errors to stable codes and safe user-facing messages.
- Apply retries only to transient idempotent operations; define timeout and cancellation behavior.
- Test fault injection and ensure logs include correlation context but exclude secrets and sensitive payloads.

**Inputs:** failure taxonomy and API contract, retry/idempotency constraints, logging and alert requirements
**Artifact:** error taxonomy
**Verification:** Failure-path test and security review.
**Handoff:** Transfer error taxonomy with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 67. Developer Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Run focused unit, lint, type, build and local integration checks before requesting review.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Capture command, exit status and output for each required check.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
