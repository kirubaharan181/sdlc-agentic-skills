# Architecture and technical decision-making: stage reference

## Contents
- [23 Solution Architecture](#23)
- [24 System Architecture](#24)
- [25 Application Architecture](#25)
- [26 Database Architecture](#26)
- [27 API Architecture](#27)
- [28 Cloud Architecture](#28)
- [29 Security Architecture](#29)
- [30 Data Architecture](#30)
- [31 Integration Architecture](#31)
- [32 Technology Selection](#32)
- [33 Architecture Documentation](#33)
- [34 Architecture Review](#34)

## 23
**Solution Architecture** (stub). Purpose: define the system structure and component boundaries for the target quality attributes.

Inputs: business capabilities and system context; runtime/deployment constraints; quality attribute scenarios

Procedure:
1. Define system context, actors, external systems and trust boundaries.
2. Decompose capabilities into components and assign ownership, interfaces and dependency direction.
3. Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
4. Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

Deliverables: system context and container diagrams; component/interface catalogue; architecture decision records

Acceptance: Every component has responsibility and owner. Dependencies and failure domains are explicit. Trade-offs are tied to measurable quality scenarios.

Validation: Architecture review against documented quality attribute scenarios.
Gate: 03-023. Approval: none required

## 24
**System Architecture** (stub). Purpose: define the system structure and component boundaries for the target quality attributes.

Inputs: business capabilities and system context; runtime/deployment constraints; quality attribute scenarios

Procedure:
1. Define system context, actors, external systems and trust boundaries.
2. Decompose capabilities into components and assign ownership, interfaces and dependency direction.
3. Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
4. Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

Deliverables: system context and container diagrams; component/interface catalogue; architecture decision records

Acceptance: Every component has responsibility and owner. Dependencies and failure domains are explicit. Trade-offs are tied to measurable quality scenarios.

Validation: Architecture review against documented quality attribute scenarios.
Gate: 03-024. Approval: none required

## 25
**Application Architecture** (stub). Purpose: define the system structure and component boundaries for the target quality attributes.

Inputs: business capabilities and system context; runtime/deployment constraints; quality attribute scenarios

Procedure:
1. Define system context, actors, external systems and trust boundaries.
2. Decompose capabilities into components and assign ownership, interfaces and dependency direction.
3. Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
4. Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

Deliverables: system context and container diagrams; component/interface catalogue; architecture decision records

Acceptance: Every component has responsibility and owner. Dependencies and failure domains are explicit. Trade-offs are tied to measurable quality scenarios.

Validation: Architecture review against documented quality attribute scenarios.
Gate: 03-025. Approval: none required

## 26
**Database Architecture** (stub). Purpose: design durable data structures and safe evolution strategy.

Inputs: data ownership and lifecycle; query and workload profile; retention, privacy and recovery requirements

Procedure:
1. Model entities, keys, constraints, cardinality and transactional boundaries.
2. Evaluate indexes, query patterns, partitioning, consistency and growth assumptions.
3. Define retention, encryption, access boundaries, backup and recovery strategy.
4. Plan additive migration, backfill, compatibility window and rollback/forward-fix path.

Deliverables: logical/physical data model; index and workload rationale; migration strategy; data control matrix

Acceptance: Integrity constraints are enforceable. Performance decisions are workload-backed. Migration and restore path are rehearsable.

Validation: DBA, security and application owner review.
Gate: 03-026. Approval: none required

## 27
**API Architecture** (stub). Purpose: design stable API resources, contracts and compatibility policy.

Inputs: consumer journeys and use cases; data ownership and security classification; latency/throughput and compatibility needs

Procedure:
1. Model resources, identifiers, relationships, pagination, filtering and lifecycle semantics.
2. Define OpenAPI schemas, required/optional fields, validation, error envelope and idempotency behavior.
3. Specify authentication, authorization, rate limits, versioning and deprecation policy.
4. Assess consumer migration and generate contract compatibility checks.

Deliverables: API decision record; OpenAPI contract; versioning and migration plan

Acceptance: Contract is machine-valid and has representative examples. Breaking changes and consumer impact are identified. Auth/error/idempotency behavior is explicit.

Validation: API consumer and security architecture review.
Gate: 03-027. Approval: none required

## 28
**Cloud Architecture** (stub). Purpose: design a secure, resilient and supportable cloud landing pattern.

Inputs: availability and recovery objectives; workload sizing and data classification; provider constraints and cost ceiling

Procedure:
1. Choose regions, network zones, identity boundaries and managed services against requirements.
2. Model failure domains, autoscaling, backup, observability and deployment topology.
3. Define policy-as-code, encryption, key ownership and secret integration.
4. Estimate lifecycle cost and document portability/vendor lock-in trade-offs.

Deliverables: cloud architecture diagram; landing-zone decisions; resilience model; cost estimate

Acceptance: Failure domains align with RTO/RPO. IAM and network boundaries are least privilege. Cost assumptions and service quotas are explicit.

Validation: Cloud security and operations design review.
Gate: 03-028. Approval: none required

## 29
**Security Architecture** (stub). Purpose: define trust boundaries and security controls before implementation.

Inputs: data flows and assets; threat actors and trust boundaries; regulatory and risk appetite

Procedure:
1. Identify assets, entry points, identities, trust boundaries and privileged operations.
2. Model abuse cases and threats using a documented method such as STRIDE where suitable.
3. Map preventive, detective and recovery controls to threats and owners.
4. Record residual risk, security assumptions and verification requirements.

Deliverables: data-flow diagram; threat model; control matrix; residual risk record

Acceptance: High-impact threats have treatment and owner. Trust boundaries and data flows are complete. Controls have testable verification evidence.

Validation: Independent security architecture review.
Gate: 03-029. Approval: none required

## 30
**Data Architecture** (stub). Purpose: govern data domains, semantics, lineage and lifecycle.

Inputs: business data domains and owners; source/consumer inventory; classification and retention obligations

Procedure:
1. Define domain entities, canonical terms, identifiers and system-of-record ownership.
2. Map ingestion, transformation, sharing, lineage and quality responsibility.
3. Set classification, access, retention, deletion and residency rules.
4. Review interoperability and schema evolution with producers and consumers.

Deliverables: domain model; data catalogue; lineage map; classification/retention policy

Acceptance: Critical elements have owners and definitions. Lineage covers source-to-consumer flow. Privacy and retention controls are enforceable.

Validation: Data governance council review.
Gate: 03-030. Approval: none required

## 31
**Integration Architecture** (stub). Purpose: design reliable boundaries between independently operated systems.

Inputs: producer/consumer contracts; protocol, volume and latency constraints; failure and ownership model

Procedure:
1. Select synchronous or asynchronous interaction based on coupling and latency needs.
2. Define schema, correlation IDs, idempotency, retries, ordering and dead-letter behavior.
3. Specify authentication, secrets, rate limits, observability and contract evolution.
4. Test timeout, duplicate, partial failure and partner outage scenarios.

Deliverables: context/container diagram; interface contract; failure-mode table; operational ownership

Acceptance: Every interface has owner and version policy. Retries cannot create unsafe duplicate side effects. Failure handling and telemetry are specified.

Validation: Producer, consumer and operations review.
Gate: 03-031. Approval: none required

## 32
**Technology Selection** (stub). Purpose: choose technology through evidence-based trade-off analysis.

Inputs: capability requirements and constraints; candidate options and lifecycle costs; security, skills and support requirements

Procedure:
1. Define decision criteria and weights before scoring candidates.
2. Evaluate functional fit, integration, maturity, security, licensing, operability and exit cost.
3. Prototype only uncertain high-impact capabilities and record measured results.
4. Publish decision, rejected alternatives, assumptions and review trigger.

Deliverables: technology scorecard; proof evidence; architecture decision record

Acceptance: Scoring criteria are transparent. Total cost and exit strategy are included. Decision is reproducible from evidence.

Validation: Architecture governance review.
Gate: 03-032. Approval: none required

## 33
**Architecture Documentation** (stub). Purpose: publish architecture decisions and models for future operators.

Inputs: approved architecture decisions; audience and repository conventions; system context and change history

Procedure:
1. Document context, scope, constraints, component boundaries and data/control flows.
2. Link ADRs, interfaces, deployment topology, quality attributes and known limitations.
3. Keep diagrams source-controlled and validate rendering and links.
4. Assign owners and review triggers for decisions that can become stale.

Deliverables: architecture overview; ADRs; versioned diagrams; review schedule

Acceptance: Documentation matches deployed reality. Every key decision has rationale and alternatives. Owners and freshness triggers are defined.

Validation: Architecture peer review.
Gate: 03-033. Approval: none required

## 34
**Architecture Review** (stub). Purpose: independently evaluate architecture against quality attributes and constraints.

Inputs: architecture baseline and ADRs; quality attribute scenarios; risk and change context

Procedure:
1. Check component boundaries, coupling, data ownership, failure domains and dependency direction.
2. Evaluate security, resilience, scalability, operability, accessibility and cost against scenarios.
3. Record evidence, deviations, trade-offs and remediation priority.
4. Issue accept, conditional accept or reject recommendation without implementing the reviewed change.

Deliverables: architecture review report; decision and exception log; remediation actions

Acceptance: Findings cite model element and impact. Reviewer independence is preserved. Exceptions have owner and expiry.

Validation: Independent architecture board decision.
Gate: 03-034. Approval: none required
