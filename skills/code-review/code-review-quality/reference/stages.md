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
**Pull Request Creation** (complete). Purpose: package a finished change so a reviewer can understand it, verify it and merge it safely.

Entry criteria: The change builds and its tests pass locally; A work item with acceptance criteria exists; The branch is current with the target branch

Inputs: branch with the change; linked work item and acceptance criteria; test results; contribution guidelines

Procedure:
1. Keep the change to one purpose; split unrelated work into separate pull requests.
2. Write a title and description that state what changed, why, how it was tested and what could go wrong.
3. Link the work item and note any migration, configuration or rollout step the reviewer must know about.
4. Run the project's checks locally and confirm the CI checks start and pass.
5. Self-review the diff first and remove debug code, stray files and secrets.
6. Request reviewers who own the affected area and respond to comments promptly.

Deliverables: pull request with description; link to work item; test evidence; self-review notes

Acceptance: Description states purpose, testing and risk The diff contains only the intended change CI checks are running or green Work item is linked

Validation: Code review (stage 69) and merge approval (stage 75) follow.

- `git diff --stat origin/main...HEAD` expect: changed files match the stated purpose
- `gh pr checks` expect: required checks are pending or passing

Failure modes:
- Very large mixed change | detect: Diff touches unrelated areas | respond: Split into smaller pull requests
- Secret or debug output committed | detect: Scan or self-review finds it | respond: Remove, rotate if a secret, and force a clean history before review
- No description | detect: Body is empty | respond: Write the description before requesting review

ILLUSTRATIVE: A pull request adds an export endpoint. The description lists the new route, the test that covers pagination, and a note that a new index is created by migration 0042.

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
**Static Code Analysis** (complete). Purpose: enforce code quality, style and correctness rules automatically on every change so reviewers can spend time on design.

Entry criteria: Language and framework are known; Linter, formatter and type checker are chosen; Rules are agreed by the team

Inputs: source code; lint and type-check configuration; team coding standards; CI pipeline

Procedure:
1. Configure the formatter, linter and type checker in the repository with pinned versions.
2. Start with a rule set the team agrees on; record a baseline for existing violations so only new ones block.
3. Run the tools locally, in a pre-commit hook and in CI as a required check.
4. Fix new violations; allow a suppression only with a comment explaining why and a link to an issue.
5. Track the number of suppressions and the baseline over time and reduce them.
6. Review the rule set when the team finds a rule unhelpful, and change it by decision, not by silent suppression.

Deliverables: tool configuration; baseline of existing violations; CI check; suppression report

Acceptance: New violations fail the build Suppressions have explanations and issue links Tool versions are pinned Baseline is shrinking

Validation: Team review of rule changes.

- `ruff check . && ruff format --check . && mypy .   # example for Python` expect: exit 0
- `grep -rn 'noqa\|type: ignore' src | wc -l` expect: count does not grow without justification

Failure modes:
- Rules disabled to get green | detect: Config edited to relax rules in the same change | respond: Review the relaxation separately
- Suppressions without reason | detect: Comment lacks explanation | respond: Add reason and issue or remove
- Tools differ between machines | detect: Different results locally and in CI | respond: Pin versions

ILLUSTRATIVE: A pre-commit hook and a required CI check run the formatter, linter and type checker. A new unused-variable warning blocks a pull request until fixed; suppressions are limited to three, each with an issue link.

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
**Merge Approval** (complete). Purpose: confirm that a reviewed change meets the merge conditions and let it into the protected branch, by someone other than its author.

Entry criteria: Code review (stage 69) is approved on the current head commit; Required checks have passed; A merge steward or code owner is available

Inputs: pull request and head commit; review approvals; required check results; branch protection rules and code owners

Procedure:
1. Confirm the approvals are on the current head commit and from the required code owners.
2. Confirm every required check is green and no check was bypassed.
3. Confirm there are no unresolved blocking comments and no conflicts with the target branch.
4. Confirm the change fits the release plan or freeze status.
5. Merge using the agreed method and record who merged and when.
6. Confirm the target branch pipeline starts and passes after the merge.

Deliverables: merge record; approval and check summary; post-merge pipeline result

Acceptance: Approval is on the head commit being merged Required checks passed without bypass Merger is not the sole author and approver Post-merge pipeline is green

Validation: Code-owner approval.

- `gh pr view --json reviewDecision,headRefOid,mergeStateStatus` expect: reviewDecision APPROVED, mergeStateStatus CLEAN, headRefOid equals the reviewed commit
- `gh run list --branch main --limit 1 --json conclusion` expect: success after the merge

Failure modes:
- Stale approval | detect: Approved commit differs from head | respond: Dismiss and re-review
- Check bypassed by an admin | detect: Merge record shows an override | respond: Record the reason; review in the next retrospective
- Merge breaks the main branch | detect: Post-merge pipeline fails | respond: Revert quickly and investigate

ILLUSTRATIVE: The steward sees approval from the code owner on commit a1b2c3, all required checks green and no conflicts. The change merges and the main-branch pipeline passes.

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
