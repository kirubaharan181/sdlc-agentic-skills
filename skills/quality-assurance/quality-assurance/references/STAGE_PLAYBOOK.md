# Risk-based verification — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 77. Test Strategy

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Select risk-based test levels and map each critical product risk to an oracle and accountable test owner.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Review coverage against top user and failure scenarios.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 78. Test Planning

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Sequence test cases by dependency, environment readiness and risk; define fixtures, entry criteria and execution windows.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Review plan completeness and fixture reproducibility.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 79. Unit Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Isolate pure logic with deterministic fixtures and cover boundaries, invariants and failure results.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run focused unit suite and inspect assertion quality.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 80. Integration Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Verify service, database, queue and adapter contracts with isolated dependencies.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run integration suite with dependency health and cleanup evidence.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 81. API Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Exercise OpenAPI success, validation, authorization, pagination, idempotency and error cases.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run contract and negative-case suite against the exact build.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 82. UI Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Verify component states, keyboard interaction, validation feedback and responsive layout.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run browser tests and inspect captured screenshots/traces.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 83. Functional Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Trace each business requirement to positive, negative, alternate and exception scenarios.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Review traceability and execute critical business paths.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 84. End-to-End Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Exercise complete user journeys across UI, APIs, persistence and external side effects with synthetic data.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run critical journeys and reconcile resulting state across services.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 85. Regression Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Select impacted behavior using code dependencies, API/data changes and historical defect evidence.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Compare targeted suite results with the baseline candidate.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 86. Smoke Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Check release-blocking startup, health, authentication and critical transaction paths after deployment.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run smoke suite against the deployed artifact.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 87. Sanity Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Verify the narrow changed area and immediate dependencies after a small patch.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Execute the bounded checklist on the exact patch.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 88. Cross-browser Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Run identical critical journeys across the supported browser/OS matrix and compare rendering and interaction.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run matrix tests and attach browser/version evidence.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 89. Mobile Compatibility Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Verify responsive layout, touch targets, orientation, OS permissions and network transitions on supported devices.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run emulator and representative physical-device tests.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 90. Accessibility Testing

**Purpose:** verify inclusive access against applicable WCAG criteria

**Procedure:**
- Inspect semantic structure, accessible names, headings, landmarks, labels and error associations.
- Test keyboard-only operation, focus order/visibility, dialogs and escape behavior.
- Check contrast, zoom/reflow, reduced motion and screen-reader announcements.
- Combine automated scans with manual assistive-technology testing; log criterion-level failures.
- Check semantic names, keyboard-only operation, focus management, contrast, zoom and screen-reader announcements.

**Inputs:** target standard and conformance level, supported browsers/devices and assistive tech, critical user journeys
**Artifact:** accessibility audit
**Verification:** Independent accessibility specialist review. Run automated scans plus keyboard and screen-reader verification.
**Handoff:** Transfer accessibility audit with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 91. Performance Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Measure representative workload latency, throughput, saturation and error rate against service objectives.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Compare equivalent before/after runs with workload pinned.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 92. Load Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Ramp concurrency and request mix to expected peak and observe throughput, queue depth and latency percentiles.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run controlled load ramp and retain telemetry.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 93. Stress Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Increase load beyond expected capacity to identify saturation point and failure mode.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Run approved stress profile in an isolated environment.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 94. Soak Testing

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Sustain representative load long enough to expose leaks, queue growth and resource drift.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Review time-series trends and post-run resource recovery.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 95. UAT

**Purpose:** verify software behavior using risk-based and reproducible tests

**Procedure:**
- Derive scenarios from requirements, risks, boundaries and prior defects; identify test level and oracle.
- Prepare deterministic fixtures, environment, cleanup and sensitive-data controls.
- Execute positive, negative, boundary and failure scenarios; preserve raw reports and exact build identity.
- Triage failures as product defect, test defect, environment issue or inconclusive evidence; rerun only with recorded reason.
- Validate real business workflows with authorized users against agreed acceptance examples.

**Inputs:** testable acceptance criteria and risk profile, test environment and data, supported platform/workload matrix
**Artifact:** test strategy or plan
**Verification:** Independent QA review and acceptance decision. Capture user execution evidence and explicit acceptance decision.
**Handoff:** Transfer test strategy or plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 96. Defect Management

**Purpose:** control defects from reproduction through verified closure

**Procedure:**
- Reproduce on a named build and capture minimal steps, expected/actual behavior and logs.
- Assess impact, exploitability, affected users and workaround; assign severity separately from priority.
- Link root cause and fix commit to regression coverage.
- Verify fix on the target build and close only with reproducible evidence.

**Inputs:** defect report and affected build, severity/priority policy, reproduction environment
**Artifact:** defect ticket
**Verification:** QA owner verifies closure.
**Handoff:** Transfer defect ticket with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 97. Test Sign-off

**Purpose:** prepare a controlled decision with sufficient evidence and independent authority

**Procedure:**
- Check the decision request is complete, in scope and owned by an authorized requester.
- Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
- Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
- Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

**Inputs:** decision request and accountable sponsor, impact/risk assessment, supporting evidence and alternatives
**Artifact:** decision record
**Verification:** Independent approval record and audit trail.
**Handoff:** Transfer decision record with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
