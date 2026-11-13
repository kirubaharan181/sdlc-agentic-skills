# Requirements and experience design — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 11. Requirement Elicitation

**Purpose:** discover complete and testable stakeholder needs

**Procedure:**
- Select interviews, workshops, observation or document analysis appropriate to each stakeholder.
- Ask for goals, tasks, exceptions, pain points, constraints and examples of successful outcomes.
- Resolve conflicting statements by recording source, authority and decision owner.
- Convert findings into candidate requirements and confirm them with the source stakeholder.

**Inputs:** stakeholder map and interview plan, business goals and known constraints, elicitation sources
**Artifact:** elicitation notes
**Verification:** Stakeholder playback and confirmation.
**Handoff:** Transfer elicitation notes with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 12. Requirement Documentation

**Purpose:** create a navigable, versioned and traceable specification

**Procedure:**
- Organize scope, actors, terminology, requirements, constraints, dependencies and exclusions.
- Assign stable IDs and link each requirement to source, owner and downstream tests.
- Document diagrams, examples, exceptions and unresolved decisions in the repository convention.
- Review clarity, consistency, links, version and change history.

**Inputs:** validated needs and decisions, document template and audience, source-of-truth repository
**Artifact:** versioned specification
**Verification:** Peer review by product, engineering and QA.
**Handoff:** Transfer versioned specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 13. Functional Requirements

**Purpose:** specify observable system behavior and business rules

**Procedure:**
- Write behavior using actor, trigger, precondition, main flow, alternate flow and postcondition.
- Define validation, state transitions, error responses and idempotency where applicable.
- Derive positive, negative, boundary and authorization acceptance cases.
- Trace each behavior to a requirement ID and owner.

**Inputs:** user and system scenarios, business rules and data definitions, external interface constraints
**Artifact:** functional requirement catalogue
**Verification:** Scenario walkthrough with developer and tester.
**Handoff:** Transfer functional requirement catalogue with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 14. Non-Functional Requirements

**Purpose:** quantify reliability, performance, security and operability expectations

**Procedure:**
- Select relevant quality attributes such as latency, throughput, availability, recovery, scalability, privacy and accessibility.
- Set thresholds with percentile, workload, duration, measurement point and acceptable error rate.
- Define telemetry and test conditions needed to verify each target.
- Resolve trade-offs among quality attributes and obtain product/operations owner acceptance.

**Inputs:** workload profile and business criticality, service objectives and compliance constraints, measurement and verification environment
**Artifact:** quality attribute scenarios
**Verification:** Review each NFR for measurable thresholds and verify test plans can produce the required evidence.
**Handoff:** Transfer quality attribute scenarios with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 15. User Research

**Purpose:** collect ethical and representative evidence about user behavior

**Procedure:**
- Recruit participants against explicit inclusion criteria and record sampling limitations.
- Obtain consent; avoid collecting unnecessary personal or sensitive data.
- Run neutral interviews or observations with consistent prompts and session notes.
- Code findings into themes, counterexamples and confidence levels; distinguish participant statements from researcher inference.

**Inputs:** research question and participant criteria, consent/privacy plan, interview or usability protocol
**Artifact:** research protocol
**Verification:** Research peer review and stakeholder playback.
**Handoff:** Transfer research protocol with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 16. User Journey Mapping

**Purpose:** map user goals, touchpoints, decisions and friction across a complete journey

**Procedure:**
- Define journey boundary, user goal and success event.
- Map stages, actions, touchpoints, emotions, questions, failures and backstage dependencies.
- Annotate evidence source and pain-point severity at each step.
- Prioritize opportunities and define measurable experience improvements.

**Inputs:** validated personas or user segments, research observations, journey scope and start/end events
**Artifact:** journey map
**Verification:** Walkthrough with users and service owners.
**Handoff:** Transfer journey map with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 17. Wireframing

**Purpose:** explore information hierarchy and interaction structure before visual polish

**Procedure:**
- Identify primary tasks and content hierarchy for each screen.
- Create low-fidelity layouts with navigation, states, responsive behavior and annotations.
- Review task completion paths, empty/error/loading states and keyboard flow.
- Record design decisions and unresolved usability questions.

**Inputs:** validated task flows, content requirements, target viewport/device constraints
**Artifact:** annotated wireframes
**Verification:** Product/design review and quick usability walkthrough.
**Handoff:** Transfer annotated wireframes with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 18. UI Design

**Purpose:** define a consistent and accessible visual interface

**Procedure:**
- Apply typography, color, spacing, hierarchy and component states using the design system.
- Specify responsive behavior, focus/hover/disabled/error states and asset usage.
- Check color contrast, text scaling and semantic component intent.
- Document deviations and reusable component decisions.

**Inputs:** approved wireframes and design tokens, brand and component standards, accessibility requirements
**Artifact:** high-fidelity screens
**Verification:** Design-system review and accessibility check.
**Handoff:** Transfer high-fidelity screens with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 19. UX Design

**Purpose:** optimize task completion, comprehension and error recovery

**Procedure:**
- Design navigation, information scent, feedback, affordances and error recovery around user tasks.
- Cover first-use, repeat-use, empty, loading, failure and recovery states.
- Prototype critical paths and observe representative users.
- Revise based on task success, time, error and qualitative feedback.

**Inputs:** user goals and journey evidence, wireframes and interaction constraints, usability criteria
**Artifact:** interaction specification
**Verification:** Moderated usability review.
**Handoff:** Transfer interaction specification with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 20. Prototype Development

**Purpose:** validate a risky interaction or concept before production implementation

**Procedure:**
- Choose fidelity that answers the question without implying production readiness.
- Build only the critical path and realistic states needed for the experiment.
- Run task-based sessions and capture observations, failures and time-on-task.
- Decide iterate, validate further or discard; label simulated behavior and data.

**Inputs:** hypothesis and target user task, prototype fidelity decision, success and failure thresholds
**Artifact:** prototype artifact
**Verification:** Product/design decision review.
**Handoff:** Transfer prototype artifact with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 21. Accessibility Review

**Purpose:** verify inclusive access against applicable WCAG criteria

**Procedure:**
- Inspect semantic structure, accessible names, headings, landmarks, labels and error associations.
- Test keyboard-only operation, focus order/visibility, dialogs and escape behavior.
- Check contrast, zoom/reflow, reduced motion and screen-reader announcements.
- Combine automated scans with manual assistive-technology testing; log criterion-level failures.

**Inputs:** target standard and conformance level, supported browsers/devices and assistive tech, critical user journeys
**Artifact:** accessibility audit
**Verification:** Independent accessibility specialist review.
**Handoff:** Transfer accessibility audit with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 22. Requirement Validation

**Purpose:** prove requirements are complete, consistent, feasible and testable

**Procedure:**
- Check each requirement for atomicity, necessity, clarity, feasibility and verifiability.
- Trace business goals to requirements, design elements and test cases.
- Run ambiguity, conflict, duplication and orphan checks.
- Resolve or explicitly defer findings with owners before baseline approval.

**Inputs:** draft requirements and traceability, stakeholder authority, acceptance and quality criteria
**Artifact:** validated baseline
**Verification:** Cross-functional requirements review.
**Handoff:** Transfer validated baseline with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
