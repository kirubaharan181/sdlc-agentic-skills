# Architecture and technical decision-making — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 23. Solution Architecture

**Purpose:** define the system structure and component boundaries for the target quality attributes

**Procedure:**
- Define system context, actors, external systems and trust boundaries.
- Decompose capabilities into components and assign ownership, interfaces and dependency direction.
- Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
- Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

**Inputs:** business capabilities and system context, runtime/deployment constraints, quality attribute scenarios
**Artifact:** system context and container diagrams
**Verification:** Architecture review against documented quality attribute scenarios.
**Handoff:** Transfer system context and container diagrams with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 24. System Architecture

**Purpose:** define the system structure and component boundaries for the target quality attributes

**Procedure:**
- Define system context, actors, external systems and trust boundaries.
- Decompose capabilities into components and assign ownership, interfaces and dependency direction.
- Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
- Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

**Inputs:** business capabilities and system context, runtime/deployment constraints, quality attribute scenarios
**Artifact:** system context and container diagrams
**Verification:** Architecture review against documented quality attribute scenarios.
**Handoff:** Transfer system context and container diagrams with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 25. Application Architecture

**Purpose:** define the system structure and component boundaries for the target quality attributes

**Procedure:**
- Define system context, actors, external systems and trust boundaries.
- Decompose capabilities into components and assign ownership, interfaces and dependency direction.
- Evaluate synchronous/asynchronous boundaries, data ownership, failure isolation and deployment topology.
- Compare architecture options against latency, availability, scalability, security, operability and cost scenarios.

**Inputs:** business capabilities and system context, runtime/deployment constraints, quality attribute scenarios
**Artifact:** system context and container diagrams
**Verification:** Architecture review against documented quality attribute scenarios.
**Handoff:** Transfer system context and container diagrams with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 26. Database Architecture

**Purpose:** design durable data structures and safe evolution strategy

**Procedure:**
- Model entities, keys, constraints, cardinality and transactional boundaries.
- Evaluate indexes, query patterns, partitioning, consistency and growth assumptions.
- Define retention, encryption, access boundaries, backup and recovery strategy.
- Plan additive migration, backfill, compatibility window and rollback/forward-fix path.

**Inputs:** data ownership and lifecycle, query and workload profile, retention, privacy and recovery requirements
**Artifact:** logical/physical data model
**Verification:** DBA, security and application owner review.
**Handoff:** Transfer logical/physical data model with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 27. API Architecture

**Purpose:** design stable API resources, contracts and compatibility policy

**Procedure:**
- Model resources, identifiers, relationships, pagination, filtering and lifecycle semantics.
- Define OpenAPI schemas, required/optional fields, validation, error envelope and idempotency behavior.
- Specify authentication, authorization, rate limits, versioning and deprecation policy.
- Assess consumer migration and generate contract compatibility checks.

**Inputs:** consumer journeys and use cases, data ownership and security classification, latency/throughput and compatibility needs
**Artifact:** API decision record
**Verification:** API consumer and security architecture review.
**Handoff:** Transfer API decision record with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 28. Cloud Architecture

**Purpose:** design a secure, resilient and supportable cloud landing pattern

**Procedure:**
- Choose regions, network zones, identity boundaries and managed services against requirements.
- Model failure domains, autoscaling, backup, observability and deployment topology.
- Define policy-as-code, encryption, key ownership and secret integration.
- Estimate lifecycle cost and document portability/vendor lock-in trade-offs.

**Inputs:** availability and recovery objectives, workload sizing and data classification, provider constraints and cost ceiling
**Artifact:** cloud architecture diagram
**Verification:** Cloud security and operations design review.
**Handoff:** Transfer cloud architecture diagram with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 29. Security Architecture

**Purpose:** define trust boundaries and security controls before implementation

**Procedure:**
- Identify assets, entry points, identities, trust boundaries and privileged operations.
- Model abuse cases and threats using a documented method such as STRIDE where suitable.
- Map preventive, detective and recovery controls to threats and owners.
- Record residual risk, security assumptions and verification requirements.

**Inputs:** data flows and assets, threat actors and trust boundaries, regulatory and risk appetite
**Artifact:** data-flow diagram
**Verification:** Independent security architecture review.
**Handoff:** Transfer data-flow diagram with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 30. Data Architecture

**Purpose:** govern data domains, semantics, lineage and lifecycle

**Procedure:**
- Define domain entities, canonical terms, identifiers and system-of-record ownership.
- Map ingestion, transformation, sharing, lineage and quality responsibility.
- Set classification, access, retention, deletion and residency rules.
- Review interoperability and schema evolution with producers and consumers.

**Inputs:** business data domains and owners, source/consumer inventory, classification and retention obligations
**Artifact:** domain model
**Verification:** Data governance council review.
**Handoff:** Transfer domain model with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 31. Integration Architecture

**Purpose:** design reliable boundaries between independently operated systems

**Procedure:**
- Select synchronous or asynchronous interaction based on coupling and latency needs.
- Define schema, correlation IDs, idempotency, retries, ordering and dead-letter behavior.
- Specify authentication, secrets, rate limits, observability and contract evolution.
- Test timeout, duplicate, partial failure and partner outage scenarios.

**Inputs:** producer/consumer contracts, protocol, volume and latency constraints, failure and ownership model
**Artifact:** context/container diagram
**Verification:** Producer, consumer and operations review.
**Handoff:** Transfer context/container diagram with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 32. Technology Selection

**Purpose:** choose technology through evidence-based trade-off analysis

**Procedure:**
- Define decision criteria and weights before scoring candidates.
- Evaluate functional fit, integration, maturity, security, licensing, operability and exit cost.
- Prototype only uncertain high-impact capabilities and record measured results.
- Publish decision, rejected alternatives, assumptions and review trigger.

**Inputs:** capability requirements and constraints, candidate options and lifecycle costs, security, skills and support requirements
**Artifact:** technology scorecard
**Verification:** Architecture governance review.
**Handoff:** Transfer technology scorecard with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 33. Architecture Documentation

**Purpose:** publish architecture decisions and models for future operators

**Procedure:**
- Document context, scope, constraints, component boundaries and data/control flows.
- Link ADRs, interfaces, deployment topology, quality attributes and known limitations.
- Keep diagrams source-controlled and validate rendering and links.
- Assign owners and review triggers for decisions that can become stale.

**Inputs:** approved architecture decisions, audience and repository conventions, system context and change history
**Artifact:** architecture overview
**Verification:** Architecture peer review.
**Handoff:** Transfer architecture overview with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 34. Architecture Review

**Purpose:** independently evaluate architecture against quality attributes and constraints

**Procedure:**
- Check component boundaries, coupling, data ownership, failure domains and dependency direction.
- Evaluate security, resilience, scalability, operability, accessibility and cost against scenarios.
- Record evidence, deviations, trade-offs and remediation priority.
- Issue accept, conditional accept or reject recommendation without implementing the reviewed change.

**Inputs:** architecture baseline and ADRs, quality attribute scenarios, risk and change context
**Artifact:** architecture review report
**Verification:** Independent architecture board decision.
**Handoff:** Transfer architecture review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
