# Conflict resolution rules

Conflicts happen between skills, between a skill and a user constraint, between evidence sources and between people. Resolve
them in this order and record the outcome in the [decision log](DECISION_LOG_STANDARD.md). Do not resolve a conflict by silence or by averaging.

## Precedence

1. **Safety, law and explicit prohibitions** (security model, [APPROVAL_POLICY.md](APPROVAL_POLICY.md), licence and legal obligations).
2. **The user's explicit constraints and scope**, unless they would break rule 1.
3. **Approval and gate outcomes** for the exact artifact revision.
4. **Evidence over opinion.** Reproducible evidence closer to the system beats a summary or an estimate.
5. **The owning skill.** Use the owner in the [responsibility matrix](../architecture/SKILL_SELECTION.md#2-responsibility-matrix). A skill advising on another skill's responsibility is input, not a decision.
6. **The more conservative option** when two options are otherwise equal and one is easier to reverse.

## Common conflicts

| Conflict | Rule |
|---|---|
| QA recommends release; security reports an open high finding | Open high security findings block release unless a named risk owner accepts the risk. Escalate with both positions. |
| Two skills claim the same task | The owner in the responsibility matrix does it; log the overlap so it can be fixed. |
| User wants to skip a gate | Record the request as a waiver with owner, reason, risk and expiry; the gate result is unchanged. Skipping needs the approver of the tier. |
| Two evidence sources disagree | Compare scope, time and method; prefer reproducible, system-near evidence; record the conflict; request more evidence if still unresolved. |
| Speed against safety | Use the tier rules; an emergency change follows the emergency path and is reviewed afterwards. |
| Standards disagree (team against organization) | The organization standard wins unless an exception with owner and expiry exists. |
| Specialist advice contradicts the registry | The registry is canonical; raise a change to the registry rather than working around it. |

## Escalation

Escalate to the accountable human for the stage when the rules above do not decide the matter, when the conflict involves
risk acceptance, or when two named owners disagree. State both positions, the evidence and what decision is needed by when.
`master-orchestration` presents the conflict; it does not choose between humans.
