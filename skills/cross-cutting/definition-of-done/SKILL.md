---
name: definition-of-done
description: "Use when work is about to be called done: sets completion criteria and closes on evidence. Do NOT use to plan or do the work."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["completion", "acceptance", "quality-gates", "evidence"]
---

# Task-specific completion criteria

## Purpose
Makes completion mean accepted behavior with evidence, not finished activity. It selects the completion profile for the task (code, API, database, infrastructure, security fix, release, incident or documentation), checks the criteria, records exceptions with owners, and refuses to close work with unowned open risk.

## When to Use
- A task is about to be reported done.
- A new task needs its completion criteria agreed up front.
- Work is partly done and the remaining gap must be stated.

## When NOT to Use
- Planning or doing the work: use the stage skill.
- Judging the quality of evidence in depth: use evidence-quality-gates.
- Approving release: use release-deployment.

## Prerequisites and Requirements
- The task, its acceptance criteria and its owner.
- Access to the evidence the work produced.
- Templates in templates/definition-of-done/ for the profile.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- task description
- acceptance criteria
- evidence produced

Optional inputs:
- risk class
- waivers
- approver names

Outputs and deliverables:
- completion profile chosen with reason
- checklist result per criterion (PASS, FAIL, WAIVED, BLOCKED)
- list of open items with owners
- closure statement or a not-done statement

## Procedure
1. Select completion profile for code, API, data, infrastructure, security, release, incident or documentation.
2. Check acceptance, tests, security/privacy, operations, documentation and ownership appropriate to task.
3. Record evidence and limitations; verify unresolved risks have explicit owners and disposition.
4. Close only when required approvals and handoffs are complete.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Criterion has no evidence | Mark it BLOCKED, not PASS. |
| Criterion waived | Record reason, owner, expiry and approver. |
| Open risk without owner | Do not close; assign an owner or accept it explicitly. |
| Work is partly complete | Report what is done, what is not, and the next owner; do not call it done. |
| Task spans profiles (e.g. API and database) | Apply both profiles and merge their criteria. |

## Quality Gates
- [ ] Each acceptance criterion has a result and evidence reference
- [ ] Tests, security, operations and documentation are checked as the profile requires
- [ ] Waivers have owner and expiry
- [ ] Required approvals and handoffs are complete

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Close a bug fix
```text
Request: Is the discount bug fix done?
Context: Fix merged, regression test added, not yet released.
Agent behavior: Apply the bug-fix profile: test fails before and passes after, review done, release pending.
Output: Not done: release and verification in production are open; owner assigned.
Acceptance: Closure is withheld until verification evidence exists.
```

### Example 2: Select a profile
```text
Request: Define done for the new reporting API.
Context: New endpoint and a table.
Agent behavior: Combine the API and database-change profiles and list criteria for contract, tests, migration and rollback.
Output: Merged checklist with evidence required for each line.
Acceptance: No criterion is missing for either profile.
```

### Example 3: Handle a waiver
```text
Request: Accessibility check could not be run before launch.
Context: Launch date fixed.
Agent behavior: Record a WAIVED result with owner, reason and expiry, and add a follow-up.
Output: Waiver record and follow-up task.
Acceptance: Waiver has a named approver and an expiry date.
```

## Limitations
- Judges completeness against stated criteria; it cannot know criteria nobody wrote.
- Cannot verify evidence authenticity: that is evidence-quality-gates.
- A human closes the work; it only reports readiness.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Acceptance criteria missing | Task started without them | Draft criteria with the owner before judging completion. |
| Evidence is a claim only | No artifact or command output | Mark BLOCKED and request the record. |
| Profile unclear | Task type ambiguous | Ask the owner or apply the stricter profile. |

## Tools
- task acceptance checklist
- test/security evidence
- release/operational handoff
- risk and waiver register

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.

## Handoffs
Hands to:
- `evidence-quality-gates`: evidence sets that need deeper evaluation
- `release-deployment`: completion statement for release readiness

Receives from:
- `master-orchestration`: task completion check

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Selection and handoff guidance: the skill selection guide in the repository documentation.
