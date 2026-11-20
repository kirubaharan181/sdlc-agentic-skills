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
**Solution Architecture** (complete). Purpose: define how a business solution fits together across systems, teams and vendors, so the parts can be built and the whole works.

Entry criteria: Business goals and requirements are agreed; The existing landscape is documented at least roughly; Constraints on cost, time and compliance are known

Inputs: requirements and goals; current systems landscape; constraints; feasibility results

Procedure:
1. Describe the business capabilities the solution must provide and the systems and people involved.
2. Draw the context view: what is inside the solution, what is outside, and every external connection.
3. Choose the main building blocks and say which are reused, bought or built, with reasons.
4. Define the interfaces and data ownership between the blocks and with existing systems.
5. Check the design against the key requirements and constraints, and list risks and open decisions.
6. Record the main decisions with options considered, and review the design with stakeholders.

Deliverables: solution context diagram; building block and interface list; decision records; risk and open-issue list

Acceptance: Every external connection is shown Build, buy or reuse is decided with reasons Data ownership is stated per block Key requirements are traced to blocks

Validation: Architecture board review.

- manual: trace five key requirements to the building blocks that satisfy them expect: all traced
- manual: check each interface names an owner and a data owner expect: none missing

Failure modes:
- Boundary unclear | detect: Teams assume others own a function | respond: Redraw context and assign
- Reuse assumed without checking | detect: Existing system lacks the capability | respond: Verify before committing
- Decisions unrecorded | detect: Reasons lost | respond: Write decision records

ILLUSTRATIVE: A customer portal is split into identity (bought), account data (existing core system) and a new notification service (built). The context diagram shows the payment provider as an external connection with a named owner.

Gate: 03-023. Approval: none required

## 24
**System Architecture** (complete). Purpose: design the internal structure of one system so that it meets its quality targets and can be changed safely.

Entry criteria: The solution architecture and quality targets exist (stages 14, 23); Technology choices are known or being made; The team who will build it is known

Inputs: solution architecture; quality requirements; technology choices; team skills

Procedure:
1. Select an architectural style that fits the quality targets and team, such as modular monolith or services, and state why.
2. Divide the system into components with one clear responsibility each and rules for who may depend on whom.
3. Design data flow, state, and failure handling: timeouts, retries, idempotency and degradation.
4. Describe how the design meets each quality target, for example scaling, recovery and observability.
5. Define the deployment shape and the environments, and how configuration is handled.
6. Write decision records, and turn the dependency rules into automated checks.

Deliverables: component and dependency design; failure handling design; quality attribute mapping; decision records and dependency rules

Acceptance: Each quality target maps to a design element Dependency rules are written and checkable Failure behavior is designed, not left to defaults The style choice has a stated reason

Validation: Architect peer review.

- manual: list each quality target and the design element that meets it expect: no target left without an element
- manual: check the dependency rules can be expressed in a tool and run in CI expect: rules listed with the tool

Failure modes:
- Style chosen by fashion | detect: No link to targets | respond: Justify against targets
- Shared database between components | detect: Changes break neighbours | respond: Assign data to one owner
- Failure paths missing | detect: Outage cascades | respond: Design timeouts and degradation

ILLUSTRATIVE: A modular monolith is chosen for a team of six; modules own their tables and may call each other only through interfaces, and a dependency rule in CI rejects direct table access across modules.

Gate: 03-024. Approval: none required

## 25
**Application Architecture** (complete). Purpose: design how one application is organized internally, so features can be added and fixed without the whole thing being affected.

Entry criteria: Quality targets and the solution context exist (stages 14, 23); Technology stack is chosen (stage 32); The team size and skills are known

Inputs: quality targets; solution context; technology choices; domain model

Procedure:
1. Identify the business domains and their boundaries from the domain model, and align modules to them rather than to technical layers alone.
2. Define each module's public interface and rules for dependencies, keeping the business logic independent of frameworks and storage.
3. Choose how modules communicate: direct calls inside a process, events for loose coupling, and state the consistency each needs.
4. Define cross-cutting design: configuration, error handling, logging, authentication context and transaction boundaries.
5. Check the design against the quality targets with a scenario for each, such as a change to one module or a dependency failure.
6. Record decisions, create a skeleton that already enforces the dependency rules, and review it with the developers.

Deliverables: module and dependency design; communication and consistency rules; cross-cutting design; skeleton with enforced rules

Acceptance: Modules align to domains with stated interfaces Dependency rules are enforced by a tool Each quality target has a checked scenario Decisions are recorded

Validation: Software architect and team lead review.

- `npx --no-install depcruise --validate .dependency-cruiser.js src   # example; use the language's equivalent` expect: no rule violations in the skeleton
- manual: walk through a change to one module and list the other modules touched expect: none beyond the declared interface

Failure modes:
- Modules by technical layer only | detect: A feature touches every layer's code in many places | respond: Reorganize around domains
- Shared mutable state | detect: Changes in one module break another | respond: Make ownership explicit
- Rules only on paper | detect: Violations appear | respond: Enforce in CI

ILLUSTRATIVE: An ordering application is split into catalogue, basket, orders and payments modules. Payments may be called only through its interface, and the CI rule fails a change that imports its internals.

Gate: 03-025. Approval: none required

## 26
**Database Architecture** (complete). Purpose: design how data is structured, stored, protected and evolved so it stays correct and performs as the system grows.

Entry criteria: Domain model and requirements for data are known; Volume, access patterns and consistency needs are estimated; Compliance requirements for data are known

Inputs: domain model; access patterns and volumes; consistency, availability and retention requirements; data protection requirements

Procedure:
1. Choose the data store type from access patterns and consistency needs, and record the alternatives considered.
2. Design schemas with explicit keys, constraints and relationships; define ownership of each dataset.
3. Plan indexes from the main queries and estimate size and growth.
4. Design for evolution: how schema changes are made without downtime and how data is migrated.
5. Define protection: encryption, access roles, masking of sensitive fields, retention and deletion.
6. Review with the engineers who will use it and record decisions.

Deliverables: data architecture document; schema design; decision records; retention and protection rules

Acceptance: Each dataset has an owner and constraints Main queries have supporting indexes A schema evolution approach exists Sensitive fields have protection rules

Validation: Architecture review.

- manual: run the top five queries on a production-sized sample with EXPLAIN expect: plans use the intended indexes
- manual: check each sensitive field against the protection rules expect: all covered

Failure modes:
- Schema chosen before access patterns | detect: Queries need full scans | respond: Revisit with real patterns
- No retention rule | detect: Data kept forever | respond: Define retention and deletion
- Two services write one table | detect: Shared ownership | respond: Assign one owner

ILLUSTRATIVE: Orders use a relational store because of transactional consistency. The design defines the order and line tables with foreign keys, an index on customer and date, and a rule to archive orders after seven years.

Gate: 03-026. Approval: none required

## 27
**API Architecture** (complete). Purpose: define how the system's APIs are shaped, versioned and secured so clients and services can rely on them.

Entry criteria: Requirements and consumers of the API are identified; Domain model or data ownership is drafted; An API style guide or standard exists or will be agreed

Inputs: functional requirements and consumer list; domain model and data ownership; security and compliance requirements; API style guide

Procedure:
1. List the consumers and the use cases each API must serve; separate public, partner and internal APIs.
2. Design resources and operations around the domain, with consistent naming, pagination, filtering and error format.
3. Define authentication, authorization scopes, rate limits and idempotency for each operation.
4. Define the versioning and deprecation policy, including how breaking changes are announced.
5. Write the contract in a machine-readable specification and review it with consumers.
6. Record the decisions and their alternatives as architecture decision records.

Deliverables: API specification (for example OpenAPI); API design decisions; versioning and deprecation policy; security model for the API

Acceptance: Each use case maps to an operation in the specification Errors, pagination and idempotency are defined Breaking-change policy is written At least one consumer reviewed the contract

Validation: Architecture review and consumer review of the specification.

- `npx --no-install @stoplight/spectral-cli lint openapi.yaml   # example linter; use the project's` expect: no errors against the style rules
- manual: ask a consumer team to implement one call from the specification alone expect: they succeed or the gaps are logged

Failure modes:
- API mirrors the database | detect: Operations expose tables not use cases | respond: Redesign around domain operations
- No versioning policy | detect: Breaking change shipped without notice | respond: Define policy before release
- Inconsistent errors | detect: Different formats across endpoints | respond: Adopt one error format

ILLUSTRATIVE: An orders API defines create, get and cancel operations with an idempotency key on create, cursor pagination on list, and a policy that breaking changes get a new major version and a six-month deprecation window.

Gate: 03-027. Approval: none required

## 28
**Cloud Architecture** (complete). Purpose: design how the system uses cloud services so it is secure, resilient across failures, cost-aware and operable from code.

Entry criteria: Requirements, quality targets and data classification exist; A cloud provider and account strategy is chosen; Recovery objectives are defined

Inputs: quality and recovery targets; data classification; provider capabilities and quotas; compliance obligations

Procedure:
1. Design the account or subscription structure: separate environments and workloads, central logging and guardrails with organization-level policies.
2. Design networking: private subnets for workloads, controlled ingress and egress, private connectivity to managed services and segmentation by trust.
3. Design resilience to the failure level required: multi-zone by default, and multi-region only where the recovery objectives justify the cost and complexity.
4. Choose managed services where they reduce operational load, noting lock-in, limits and failure modes of each.
5. Design identity: roles with least privilege, no long-lived keys, and separate admin paths with strong authentication.
6. Define everything as code with environments created from the same definitions, and estimate the run cost with the assumptions.

Deliverables: account and network design; resilience design with recovery mapping; identity and access design; infrastructure as code layout and cost estimate

Acceptance: Resilience level matches the recovery objectives Workloads sit in private networks with controlled egress No long-lived keys Cost estimate states its assumptions

Validation: Cloud architect and security review.

- `terraform validate && terraform plan -out=plan.out   # example; use the project's IaC tool` expect: plan shows only expected resources
- manual: map each recovery objective to the design element that meets it expect: none unmapped

Failure modes:
- Multi-region without need | detect: Complexity and cost without benefit | respond: Match the design to objectives
- Public access by default | detect: Workloads exposed | respond: Use private subnets and explicit ingress
- Manual console changes | detect: Drift from code | respond: Detect drift and enforce IaC

ILLUSTRATIVE: A service runs across three zones in one region because the recovery objective is a 30-minute RTO for zone loss; workloads are in private subnets, access uses roles, and the whole stack is created from code.

Gate: 03-028. Approval: none required

## 29
**Security Architecture** (complete). Purpose: design the controls that protect the system and its data, based on the threats it faces and the obligations it carries.

Entry criteria: Architecture and data flows are described; Data classification exists; Compliance obligations are listed (stage 10)

Inputs: architecture and data flows; data classification; threat model; compliance obligations

Procedure:
1. List the assets to protect and the trust boundaries in the design.
2. Identify threats at each boundary with a structured method, and rank them by impact and likelihood.
3. Design controls for the highest-ranked threats: identity and access, encryption, network separation, input handling and secrets management.
4. Apply least privilege and separation of duties, and design how access is granted, reviewed and removed.
5. Design logging and detection for security events, and the response path.
6. Map controls to obligations and record accepted residual risk with an owner.

Deliverables: threat model; control design; access model; residual risk register with owners

Acceptance: Each high-ranked threat has a control or an accepted risk Trust boundaries are drawn Access has a grant, review and removal path Residual risk has a named owner

Validation: Security architect and risk owner approval.

- manual: trace the five highest threats to a control or an accepted-risk entry expect: all traced
- manual: check that logging covers authentication, access changes and data export expect: covered

Failure modes:
- Controls without threats | detect: Effort on low risk | respond: Rank and refocus
- Shared admin accounts | detect: No individual accountability | respond: Use named accounts
- Risk accepted by no one | detect: Residual row has no owner | respond: Assign or reduce

ILLUSTRATIVE: A threat model of an upload feature ranks malicious files highest. Controls: type and size limits, scanning, storage outside the web root, and an alert on repeated rejected uploads; residual risk is accepted by the service owner.

Gate: 03-029. Approval: none required

## 30
**Data Architecture** (complete). Purpose: design how data is stored, owned, moved and protected, so it stays correct, available and compliant.

Entry criteria: Requirements and data needs are known; Data classification is available; Integration points are listed

Inputs: data requirements; data classification; integration needs; retention and privacy obligations

Procedure:
1. Identify the main data entities, who owns each, and where the system of record is.
2. Choose storage types per need (transactional, analytical, search, cache) and justify each.
3. Design how data moves between systems, how often, and how consistency is kept.
4. Define retention, archiving, deletion and backup rules for each class of data.
5. Design access control and protection by classification, including masking in non-production.
6. Document lineage for key data and the quality checks that guard it.

Deliverables: entity ownership map; storage and flow design; retention and deletion rules; lineage and quality checks

Acceptance: Each entity has one system of record and an owner Retention and deletion rules exist per class Non-production data is masked or synthetic Key data has lineage

Validation: Data architect and data owner approval.

- manual: check every entity in the model lists a system of record and an owner expect: none missing
- manual: check each personal-data field has a retention rule expect: none missing

Failure modes:
- Two systems of record | detect: Values disagree | respond: Choose one and sync from it
- No deletion rule | detect: Data kept indefinitely | respond: Add retention and deletion
- Production data in test | detect: Copies found in non-production | respond: Mask or replace

ILLUSTRATIVE: Customer data is owned by the account service; the warehouse receives a nightly copy with email masked, and personal fields are deleted 24 months after account closure.

Gate: 03-030. Approval: none required

## 31
**Integration Architecture** (complete). Purpose: design how systems exchange data and trigger each other, with contracts, failure handling and ownership that keep the connections reliable and changeable.

Entry criteria: The systems to connect and the data to exchange are listed; Ownership of each system and its data is known; Latency and volume needs are estimated

Inputs: system inventory; data and event inventory; latency, volume and consistency needs; security requirements

Procedure:
1. Choose the interaction style per need: synchronous request-response, asynchronous messaging or events, or batch transfer, and justify each.
2. Define contracts with versioned schemas for every interface, with rules for compatible change and a compatibility check in CI.
3. Design for failure: timeouts, retries with backoff, idempotency keys, dead-letter handling and replay, and what happens on partial failure.
4. Decide the consistency model and ordering needs, and avoid distributed transactions unless unavoidable, using sagas or reconciliation instead.
5. Define security and access for each interface: authentication between systems, authorization, encryption and data minimization.
6. Document each integration with owner, contract, volume, failure behavior and monitoring, and keep the catalogue current.

Deliverables: integration catalogue with owners; versioned contracts and compatibility checks; failure and replay design; security design per interface

Acceptance: Every interface has an owner and a versioned contract Compatibility is checked automatically Failure, replay and idempotency are designed Each interface has monitoring

Validation: Integration architect review.

- `npx --no-install @stoplight/spectral-cli lint openapi.yaml && oasdiff breaking base.yaml openapi.yaml   # example` expect: no lint errors and no breaking changes
- manual: send the same message twice to a consumer in staging expect: effect occurs once

Failure modes:
- Breaking change released | detect: Consumer fails after deploy | respond: Add contract compatibility check
- Duplicate messages double-apply | detect: Repeated effect | respond: Use idempotency keys
- Poison message blocks a queue | detect: Consumer stuck | respond: Add dead-letter queue and alert

ILLUSTRATIVE: An order event is published with a versioned schema; consumers use the event id for idempotency, failed messages move to a dead-letter queue after five attempts with an alert, and CI rejects a schema change that removes a field.

Gate: 03-031. Approval: none required

## 32
**Technology Selection** (complete). Purpose: choose technology on evidence and fit, so the team gets tools it can run and change for the life of the product.

Entry criteria: Requirements and constraints are known; Candidate technologies are identified; Team skills and operating model are known

Inputs: requirements and quality targets; constraints; candidate options; team skills and licensing terms

Procedure:
1. Write the criteria first: fit to requirements, team skill, maturity, security record, cost, licence, vendor risk and exit cost.
2. Weight the criteria with the stakeholders before scoring any option.
3. Test the top candidates with a short proof of concept on the riskiest requirement.
4. Score each option with evidence, and check licences and the support and release history.
5. Choose, and record the decision with rejected options and the conditions that would reopen it.
6. Add the choice to the approved technology list with an owner and review date.

Deliverables: criteria and weights; proof of concept results; scored comparison; decision record and technology list entry

Acceptance: Criteria and weights were set before scoring A proof of concept tested the riskiest requirement Licence and exit cost were checked Reopen conditions are recorded

Validation: Enterprise architect decision.

- manual: check the criteria file is dated before the scoring file expect: dates in the right order
- manual: read the licence of the chosen technology against the intended use expect: compatible, or exception recorded

Failure modes:
- Resume-driven choice | detect: Fit evidence missing | respond: Score against criteria
- Licence conflict | detect: Use not permitted | respond: Choose another or negotiate
- Proof of concept skipped | detect: Surprises at build time | respond: Test the riskiest part first

ILLUSTRATIVE: Two message brokers are compared. A one-day proof of concept at the expected peak rate shows one cannot keep ordering; the other is chosen, with a note to reopen the decision if volume exceeds ten times the test.

Gate: 03-032. Approval: none required

## 33
**Architecture Documentation** (complete). Purpose: write the architecture down so that others can understand it, check it and change it, and keep it in step with the system.

Entry criteria: Architecture decisions exist; Audiences are identified; A place for documentation under version control exists

Inputs: architecture designs and decision records; audiences and their questions; existing diagrams; the codebase

Procedure:
1. List the audiences (developers, operators, security, management) and the questions each asks, and organize the documentation around those questions.
2. Use a few consistent views, for example a context diagram, a container or component view and key runtime scenarios, with a legend and a stated scope for each.
3. Record significant decisions as short records with context, options, decision and consequences, and link them from the views.
4. Keep documentation as text and diagrams in code in the repository, reviewed with the code it describes.
5. Add a check that detects drift, for example a link check and a script that compares documented components with the code layout.
6. Review the documentation with a new team member by asking them to answer onboarding questions from it, and fix what they cannot answer.

Deliverables: architecture documentation set with views; decision records; automated documentation checks; review result by a newcomer

Acceptance: Each view states its scope and legend Decisions are recorded with options Documentation lives with the code A newcomer could answer onboarding questions

Validation: Architect review.

- `python3 scripts/check_links.py` expect: no broken links
- manual: ask a new team member to find where the payment module is called from using only the documentation expect: found without help

Failure modes:
- Diagram no longer matches reality | detect: Component named in diagram is gone | respond: Update with the change and add a drift check
- One huge diagram | detect: Nobody can read it | respond: Split into views with scope
- Decisions lost | detect: No one knows why | respond: Write decision records

ILLUSTRATIVE: Documentation keeps a context diagram, a component view and a decision record for choosing a message broker. A new engineer follows it to find the order flow in under ten minutes, and a CI check fails on broken links.

Gate: 03-033. Approval: none required

## 34
**Architecture Review** (complete). Purpose: have a person independent of the design judge whether it meets the requirements, quality attributes and standards, and record the decision.

Entry criteria: Design document and architecture decision records exist; Requirements and quality-attribute targets are available; Reviewer did not design the system

Inputs: architecture description and diagrams; architecture decision records; quality-attribute requirements; standards and constraints

Procedure:
1. Read the requirements and quality-attribute targets first; then review the design against them.
2. Examine boundaries, coupling, data ownership, failure modes, scalability and security assumptions.
3. Check each significant decision has a record with alternatives and consequences.
4. Record findings as blocker, risk or suggestion with the affected requirement.
5. Decide approve, approve with conditions or reject, and record the reasoning.
6. Track conditions to completion and re-review changes that affect a decision.

Deliverables: review report with severity-labelled findings; decision record; conditions list; updated decision records

Acceptance: Each finding names the requirement or attribute at risk Every significant decision has a record with alternatives The decision and its reasons are recorded Reviewer is independent of the designer

Validation: Independent architecture board decision.

- manual: trace each quality-attribute target to the part of the design that satisfies it expect: every target maps to a design element or a recorded risk
- manual: check each blocker finding has an owner and a resolution date expect: none missing

Failure modes:
- Design approved without the requirements | detect: Review record cites no requirement | respond: Redo the review against the requirements
- Blockers deferred silently | detect: Conditions without owners | respond: Assign owners or reject
- Reviewer is the designer | detect: Same person on both records | respond: Assign an independent reviewer

ILLUSTRATIVE: Review of a new order service finds one shared database table written by two services. It is rated a blocker for data ownership; the design is changed so one service owns the table and the other reads through an API.

Gate: 03-034. Approval: none required
