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
**Peer Code Review** (complete). Purpose: have an independent person judge whether a change is correct, safe and maintainable before it merges.

Entry criteria: Change is small enough to review (split otherwise) and linked to a work item; CI checks for the change have finished; Reviewer is not the author

Inputs: diff against the target branch; linked work item and acceptance criteria; CI results; coding and architecture standards

Procedure:
1. Read the description and acceptance criteria first, then the diff; confirm the change matches the stated intent.
2. Check behavior: edge cases, error paths, concurrency, data handling and backward compatibility.
3. Check tests: do they fail without the change, and do they assert behavior rather than implementation details.
4. Check security and privacy: input validation, authorization, secrets, logging of sensitive data.
5. Write findings with file and line, impact and a suggested fix; label each blocker or suggestion.
6. Re-review the author's fixes and approve only when all blockers are resolved.

Deliverables: review comments with severity labels; approval or change-request decision; list of deferred items with issue links

Acceptance: All blocker comments are resolved or explicitly deferred with an issue Reviewer ran or read the tests that cover the change Approval is on the final commit, not an earlier one Reviewer is independent of the author

Validation: Approval recorded against the exact head commit.

- `git diff --stat origin/main...HEAD` expect: diff size matches what the reviewer was asked to review
- `gh pr view --json reviewDecision,headRefOid` expect: reviewDecision is APPROVED and headRefOid equals the commit reviewed

Failure modes:
- Rubber-stamp approval | detect: Approval with no comments on a large risky diff | respond: Request a second reviewer for risky areas
- Approval on an earlier commit | detect: headRefOid differs from the approved commit | respond: Dismiss stale approval and re-review
- Author approves own change | detect: Reviewer equals author | respond: Reject; assign another reviewer

ILLUSTRATIVE: A change adds a discount code. Review finds the discount can be applied twice by retrying the request (blocker) and a missing test for negative totals (suggestion). The author adds an idempotency check and test; the reviewer approves the new commit.

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
**Dependency Review** (complete). Purpose: review each new or changed dependency for provenance, vulnerabilities and license fit before it is merged.

Entry criteria: A pull request adds or changes a dependency; License policy and approved-registry list exist; Lockfile diff is available

Inputs: dependency and lockfile diff; license policy; advisory data; the package's maintainer and release history

Procedure:
1. List each added or changed package, including transitive ones introduced by the lockfile diff.
2. Check provenance: official registry, maintainer activity, release age, download and repository signals, and typosquat look-alikes.
3. Check advisories and the license of each package against the policy; note copyleft or unknown licenses.
4. Check whether the dependency is needed or whether existing code or the standard library covers it.
5. Record approve, reject or approve-with-condition per package with the reason.
6. Require pinned versions and a lockfile change in the same pull request.

Deliverables: dependency review record; license findings; decision per package; lockfile diff reference

Acceptance: Every added package has a recorded decision No unknown or policy-forbidden license is approved Versions are pinned in the lockfile Reviewer is not the author of the change

Validation: Independent reviewer confirms findings and disposition.

- `git diff origin/main...HEAD -- package-lock.json requirements.txt   # example lockfiles` expect: every added or changed package appears in the review record
- `pip-audit -r requirements.txt   # example; use the ecosystem's audit tool` expect: no unresolved high or critical advisory

Failure modes:
- Look-alike package name approved | detect: Name differs by a character from a popular package | respond: Reject; use the intended package
- Transitive dependencies ignored | detect: Lockfile diff shows packages not in the record | respond: Review each new transitive package
- License unknown | detect: Metadata has no license | respond: Reject or ask legal for a written decision

ILLUSTRATIVE: A pull request adds a small date library. Review finds the same function already exists in the standard library, so the dependency is rejected and the author uses the standard function.

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
