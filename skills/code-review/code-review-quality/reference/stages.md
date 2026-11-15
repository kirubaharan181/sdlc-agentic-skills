# Independent engineering review: stage reference

## Contents
- [68 Pull Request Creation](#68)
- [69 Peer Code Review](#69)
- [70 Architecture Review](#70)
- [71 Static Code Analysis](#71)
- [72 Dependency Review](#72)
- [73 Code Coverage Review](#73)
- [74 Coding Standards Validation](#74)
- [75 Merge Approval](#75)
- [76 Technical Debt Review](#76)

## 68
**Pull Request Creation** (stub). Purpose: prepare a reviewable and reproducible change proposal.

Inputs: approved issue and acceptance criteria; working branch and target base; local test and review policy

Procedure:
1. Check branch base and working-tree scope; separate unrelated changes.
2. Write a PR summary linking issue, behavior change, risk and migration impact.
3. Attach exact test commands/results, screenshots or reports and known limitations.
4. Request required code owners and reviewers; ensure the PR is small enough to review.

Deliverables: pull request description; linked issue; test evidence; risk and migration note

Acceptance: Diff contains only intended changes. Evidence is from the PR head commit. Required reviewers and checks are requested.

Validation: PR checklist and diff review.
Gate: 07-068. Approval: none required

## 69
**Peer Code Review** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-069. Approval: none required

## 70
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
Gate: 07-070. Approval: none required

## 71
**Static Code Analysis** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-071. Approval: none required

## 72
**Dependency Review** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-072. Approval: none required

## 73
**Code Coverage Review** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-073. Approval: none required

## 74
**Coding Standards Validation** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-074. Approval: none required

## 75
**Merge Approval** (stub). Purpose: prepare a controlled decision with sufficient evidence and independent authority.

Inputs: decision request and accountable sponsor; impact/risk assessment; supporting evidence and alternatives

Procedure:
1. Check the decision request is complete, in scope and owned by an authorized requester.
2. Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
3. Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
4. Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

Deliverables: decision record; evidence index; conditions and waiver log

Acceptance: Decision authority is verified. Conditions are measurable, owned and time-bound. No missing or failed critical evidence is silently waived.

Validation: Independent approval record and audit trail.
Gate: 07-075. Approval: code-owner (always)

## 76
**Technical Debt Review** (stub). Purpose: independently inspect code quality and maintainability risks.

Inputs: diff and target branch; coding/architecture standards; test, dependency and static-analysis evidence

Procedure:
1. Review control flow, edge cases, data handling, concurrency and compatibility in the changed code.
2. Inspect static findings and dependency provenance, severity, reachability and license obligations.
3. Assess test coverage quality and identify untested critical branches rather than relying only on percentage.
4. Record actionable findings with location, impact, severity and remediation; separate blockers from suggestions.

Deliverables: review report; static/dependency findings; coverage interpretation; technical debt actions

Acceptance: Findings are reproducible and tied to exact commit. False positives and accepted debt have rationale and owner. Critical paths have meaningful assertions.

Validation: Independent reviewer confirms findings and disposition.
Gate: 07-076. Approval: none required
