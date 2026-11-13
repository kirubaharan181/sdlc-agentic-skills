# Independent engineering review — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 68. Pull Request Creation

**Purpose:** prepare a reviewable and reproducible change proposal

**Procedure:**
- Check branch base and working-tree scope; separate unrelated changes.
- Write a PR summary linking issue, behavior change, risk and migration impact.
- Attach exact test commands/results, screenshots or reports and known limitations.
- Request required code owners and reviewers; ensure the PR is small enough to review.

**Inputs:** approved issue and acceptance criteria, working branch and target base, local test and review policy
**Artifact:** pull request description
**Verification:** PR checklist and diff review.
**Handoff:** Transfer pull request description with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 69. Peer Code Review

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 70. Architecture Review

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

## 71. Static Code Analysis

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 72. Dependency Review

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 73. Code Coverage Review

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 74. Coding Standards Validation

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 75. Merge Approval

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

## 76. Technical Debt Review

**Purpose:** independently inspect code quality and maintainability risks

**Procedure:**
- Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
- Inspect static findings and dependency provenance, severity, reachability and license obligations.
- Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
- Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

**Inputs:** diff and target branch, coding/architecture standards, test, dependency and static-analysis evidence
**Artifact:** review report
**Verification:** Independent reviewer confirms findings and disposition.
**Handoff:** Transfer review report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
