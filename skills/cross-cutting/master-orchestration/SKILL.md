---
name: master-orchestration
description: "Use when work spans several stages: routes to workflows and consolidates results. Do NOT use for single-skill tasks."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["orchestration", "routing", "workflow", "handoff"]
---

# Request orchestration

## Purpose
Acts as the entry point for work that spans several skills. It chooses the workflow and the specialists, passes context between them in order, resolves or escalates conflicts, tracks progress and approval boundaries, and consolidates one result that lists what is done and what is still undecided. It routes; it does not do the specialist work or approve anything.

## When to Use
- A request spans several stages or skills, such as 'ship this feature safely'.
- It is unclear which skill or workflow applies.
- Outputs from several specialists must be combined into one answer.

## When NOT to Use
- The request clearly fits one skill: invoke that skill directly.
- An active severe incident: hand to incident-command immediately.
- Approving a change or release: only named humans approve.

## Prerequisites and Requirements
- The user's request in their words.
- Access to the workflow and skill registries in this repository.
- A list of constraints the user stated, to preserve them.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- user request
- stated constraints

Optional inputs:
- repository context
- existing evidence
- deadlines
- named approvers

Outputs and deliverables:
- selected workflow and ordered skill list with reasons
- handoff records between skills
- progress and approval status
- consolidated result with unresolved decisions

## Procedure
1. Classify request, risk, urgency, affected systems and requested outcome.
2. Select canonical workflow and resolve required skills, roles and stage dependencies.
3. Delegate bounded tasks with inputs, outputs, authority and stop conditions.
4. Enforce gates, reconcile evidence and report status without claiming unrun work.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Request names a workflow | Use it if it fits; otherwise explain the mismatch. |
| Two skills claim the same task | Use the owner in the responsibility matrix; log the overlap. |
| Required context is missing | Ask the single most blocking question; continue with unaffected work. |
| A step needs approval | Stop at the gate, record NEEDS_HUMAN_APPROVAL with the named approver, and continue only independent steps. |
| Specialist outputs conflict | Apply the conflict resolution rules and escalate to the accountable human if unresolved. |
| Request is an active incident | Hand to incident-command before anything else. |

## Quality Gates
- [ ] Each selected skill has a stated reason
- [ ] No unrelated skill is invoked
- [ ] Handoffs name artifact, revision and receiver
- [ ] Unresolved decisions and approvals are listed in the result

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Route a feature request
```text
Request: Ship the new refund feature safely.
Context: Requirements exist; code is not written.
Agent behavior: Select the feature workflow, order skills requirements-design, technical-architecture, software-implementation, code-review-quality, quality-assurance, application-security, release-deployment, and set approval gates.
Output: Plan table with skill, input, output, owner and gate for each step, plus open decisions.
Acceptance: Every step has an owner and the production step shows a named approver.
```

### Example 2: Resolve a conflict
```text
Request: QA recommends release; security asks to hold.
Context: Open high-severity finding.
Agent behavior: Apply the rule that an open high security finding blocks release unless a named risk owner accepts it, and escalate.
Output: Decision request to the accountable human with both positions and evidence.
Acceptance: The conflict is escalated, not silently resolved.
```

### Example 3: Handle missing context
```text
Request: Fix our deployment.
Context: No error, system or goal given.
Agent behavior: Ask what failed, where and what outcome is expected; do not route yet.
Output: One clarifying question with options.
Acceptance: No specialist is invoked before the question is answered.
```

## Limitations
- Routes by the registries and the request; it cannot know about work not described.
- Does not approve, deploy or override specialists.
- Selection is advisory and should be confirmed when the request is ambiguous.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| No workflow fits | Request is novel | Compose the closest skills in dependency order and say that no workflow matched. |
| Loop between two skills | Feedback not bounded | Limit iterations, record the cause and escalate. |
| Specialist output lacks evidence | Report without proof | Return it as INCONCLUSIVE and request evidence. |
| Handoff not acknowledged | Receiver did not accept | Mark BLOCKED and notify the named receiver. |

## Tools
- canonical registries
- dependency graph
- issue/PR tooling
- evidence and handoff contracts

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.

## Handoffs
Hands to:
- `incident-command`: active incident declaration with severity
- `evidence-quality-gates`: evidence set for evaluation
- `secure-change-control`: change requests needing classification
- `definition-of-done`: task completion check

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
