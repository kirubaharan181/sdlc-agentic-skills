# Requirements and experience design: stage reference

## Contents
- [11 Requirement Elicitation](#11)
- [12 Requirement Documentation](#12)
- [13 Functional Requirements](#13)
- [14 Non-Functional Requirements](#14)
- [15 User Research](#15)
- [16 User Journey Mapping](#16)
- [17 Wireframing](#17)
- [18 UI Design](#18)
- [19 UX Design](#19)
- [20 Prototype Development](#20)
- [21 Accessibility Review](#21)
- [22 Requirement Validation](#22)

## 11
**Requirement Elicitation** (stub). Purpose: discover complete and testable stakeholder needs.

Inputs: stakeholder map and interview plan; business goals and known constraints; elicitation sources

Procedure:
1. Select interviews, workshops, observation or document analysis appropriate to each stakeholder.
2. Ask for goals, tasks, exceptions, pain points, constraints and examples of successful outcomes.
3. Resolve conflicting statements by recording source, authority and decision owner.
4. Convert findings into candidate requirements and confirm them with the source stakeholder.

Deliverables: elicitation notes; stakeholder needs catalogue; open-question log

Acceptance: Needs are attributed to a source and context. Conflicts and assumptions remain visible. Coverage includes exceptions and operational users.

Validation: Stakeholder playback and confirmation.

Gate: 02-011. Approval: none required

## 12
**Requirement Documentation** (stub). Purpose: create a navigable, versioned and traceable specification.

Inputs: validated needs and decisions; document template and audience; source-of-truth repository

Procedure:
1. Organize scope, actors, terminology, requirements, constraints, dependencies and exclusions.
2. Assign stable IDs and link each requirement to source, owner and downstream tests.
3. Document diagrams, examples, exceptions and unresolved decisions in the repository convention.
4. Review clarity, consistency, links, version and change history.

Deliverables: versioned specification; traceability matrix; glossary and decision links

Acceptance: No ambiguous pronouns or unbounded terms remain in normative requirements. IDs are stable and traceable. Links, diagrams and examples render.

Validation: Peer review by product, engineering and QA.

Gate: 02-012. Approval: none required

## 13
**Functional Requirements** (stub). Purpose: specify observable system behavior and business rules.

Inputs: user and system scenarios; business rules and data definitions; external interface constraints

Procedure:
1. Write behavior using actor, trigger, precondition, main flow, alternate flow and postcondition.
2. Define validation, state transitions, error responses and idempotency where applicable.
3. Derive positive, negative, boundary and authorization acceptance cases.
4. Trace each behavior to a requirement ID and owner.

Deliverables: functional requirement catalogue; state/sequence diagrams; acceptance scenarios

Acceptance: Each requirement has observable expected behavior. Boundary and failure cases are covered. No implementation detail is mistaken for a user outcome.

Validation: Scenario walkthrough with developer and tester.

Gate: 02-013. Approval: none required

## 14
**Non-Functional Requirements** (stub). Purpose: quantify reliability, performance, security and operability expectations.

Inputs: workload profile and business criticality; service objectives and compliance constraints; measurement and verification environment

Procedure:
1. Select relevant quality attributes such as latency, throughput, availability, recovery, scalability, privacy and accessibility.
2. Set thresholds with percentile, workload, duration, measurement point and acceptable error rate.
3. Define telemetry and test conditions needed to verify each target.
4. Resolve trade-offs among quality attributes and obtain product/operations owner acceptance.

Deliverables: quality attribute scenarios; measurable NFR matrix; verification plan

Acceptance: Every NFR has a threshold, workload condition and verification method. Targets are measurable and tied to business criticality. Trade-offs and owners are explicit.

Validation: Review each NFR for measurable thresholds and verify test plans can produce the required evidence.

Gate: 02-014. Approval: none required

## 15
**User Research** (stub). Purpose: collect ethical and representative evidence about user behavior.

Inputs: research question and participant criteria; consent/privacy plan; interview or usability protocol

Procedure:
1. Recruit participants against explicit inclusion criteria and record sampling limitations.
2. Obtain consent; avoid collecting unnecessary personal or sensitive data.
3. Run neutral interviews or observations with consistent prompts and session notes.
4. Code findings into themes, counterexamples and confidence levels; distinguish participant statements from researcher inference.

Deliverables: research protocol; consented notes; coded themes; insight report

Acceptance: Research question maps to evidence. Sampling bias and limitations are disclosed. Recommendations do not overgeneralize beyond the sample.

Validation: Research peer review and stakeholder playback.

Gate: 02-015. Approval: none required

## 16
**User Journey Mapping** (stub). Purpose: map user goals, touchpoints, decisions and friction across a complete journey.

Inputs: validated personas or user segments; research observations; journey scope and start/end events

Procedure:
1. Define journey boundary, user goal and success event.
2. Map stages, actions, touchpoints, emotions, questions, failures and backstage dependencies.
3. Annotate evidence source and pain-point severity at each step.
4. Prioritize opportunities and define measurable experience improvements.

Deliverables: journey map; pain-point evidence; opportunity backlog

Acceptance: Journey reflects observed behavior, not assumed ideal flow. Frontstage and backstage dependencies are visible. Each opportunity has an owner and measure.

Validation: Walkthrough with users and service owners.

Gate: 02-016. Approval: none required

## 17
**Wireframing** (stub). Purpose: explore information hierarchy and interaction structure before visual polish.

Inputs: validated task flows; content requirements; target viewport/device constraints

Procedure:
1. Identify primary tasks and content hierarchy for each screen.
2. Create low-fidelity layouts with navigation, states, responsive behavior and annotations.
3. Review task completion paths, empty/error/loading states and keyboard flow.
4. Record design decisions and unresolved usability questions.

Deliverables: annotated wireframes; screen inventory; interaction flow

Acceptance: Wireframes cover all critical states and target viewports. Labels and navigation support user goals. No decorative styling hides missing behavior.

Validation: Product/design review and quick usability walkthrough.

Gate: 02-017. Approval: none required

## 18
**UI Design** (stub). Purpose: define a consistent and accessible visual interface.

Inputs: approved wireframes and design tokens; brand and component standards; accessibility requirements

Procedure:
1. Apply typography, color, spacing, hierarchy and component states using the design system.
2. Specify responsive behavior, focus/hover/disabled/error states and asset usage.
3. Check color contrast, text scaling and semantic component intent.
4. Document deviations and reusable component decisions.

Deliverables: high-fidelity screens; component specifications; design token usage

Acceptance: Visual states and responsive breakpoints are specified. Contrast and text scaling meet agreed standards. Components reuse approved tokens or record justified exceptions.

Validation: Design-system review and accessibility check.

Gate: 02-018. Approval: none required

## 19
**UX Design** (stub). Purpose: optimize task completion, comprehension and error recovery.

Inputs: user goals and journey evidence; wireframes and interaction constraints; usability criteria

Procedure:
1. Design navigation, information scent, feedback, affordances and error recovery around user tasks.
2. Cover first-use, repeat-use, empty, loading, failure and recovery states.
3. Prototype critical paths and observe representative users.
4. Revise based on task success, time, error and qualitative feedback.

Deliverables: interaction specification; task flow; usability findings

Acceptance: Critical tasks have clear entry, progress and recovery. Usability issues are prioritized by impact. Design changes are linked to research evidence.

Validation: Moderated usability review.

Gate: 02-019. Approval: none required

## 20
**Prototype Development** (stub). Purpose: validate a risky interaction or concept before production implementation.

Inputs: hypothesis and target user task; prototype fidelity decision; success and failure thresholds

Procedure:
1. Choose fidelity that answers the question without implying production readiness.
2. Build only the critical path and realistic states needed for the experiment.
3. Run task-based sessions and capture observations, failures and time-on-task.
4. Decide iterate, validate further or discard; label simulated behavior and data.

Deliverables: prototype artifact; experiment protocol; test observations; decision log

Acceptance: Prototype limitations are explicit. Success criteria are measured. No prototype-only behavior is represented as production capability.

Validation: Product/design decision review.

Gate: 02-020. Approval: none required

## 21
**Accessibility Review** (stub). Purpose: verify inclusive access against applicable WCAG criteria.

Inputs: target standard and conformance level; supported browsers/devices and assistive tech; critical user journeys

Procedure:
1. Inspect semantic structure, accessible names, headings, landmarks, labels and error associations.
2. Test keyboard-only operation, focus order/visibility, dialogs and escape behavior.
3. Check contrast, zoom/reflow, reduced motion and screen-reader announcements.
4. Combine automated scans with manual assistive-technology testing; log criterion-level failures.

Deliverables: accessibility audit; manual test evidence; defect and remediation list

Acceptance: Automated scans are not treated as full conformance proof. Critical journeys work without pointer input. Findings cite criterion, impact and reproduction.

Validation: Independent accessibility specialist review.

Gate: 02-021. Approval: none required

## 22
**Requirement Validation** (stub). Purpose: prove requirements are complete, consistent, feasible and testable.

Inputs: draft requirements and traceability; stakeholder authority; acceptance and quality criteria

Procedure:
1. Check each requirement for atomicity, necessity, clarity, feasibility and verifiability.
2. Trace business goals to requirements, design elements and test cases.
3. Run ambiguity, conflict, duplication and orphan checks.
4. Resolve or explicitly defer findings with owners before baseline approval.

Deliverables: validated baseline; traceability matrix; review issue log

Acceptance: No critical orphan, conflict or untestable requirement remains. Stakeholders approve the baseline version. Deferred items have owner and impact.

Validation: Cross-functional requirements review.

Gate: 02-022. Approval: none required
