# Handoff contract standard

A handoff moves work from one skill or role to another. This standard extends
[STANDARD_HANDOFF.md](../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md) with a record format, an acceptance rule and
failure handling. The permitted skill-to-skill handoffs are listed in the generated
[handoff matrix](../architecture/SKILL_SELECTION.md#4-handoff-matrix); `scripts/validate.py` rejects a handoff to an unknown skill.

## The record

Use [`templates/handoff-record.json`](../../templates/handoff-record.json). It is validated by
[`registry/schemas/handoff.schema.json`](../../registry/schemas/handoff.schema.json) and by `python3 scripts/trace_evidence.py <file>`.

| Field | Rule |
|---|---|
| `handoff_id` | `HO-<year>-<number>`; unique and never reused. |
| `from_skill`, `to_skill` | Registered skills. The pair should appear in the handoff matrix; a new pair needs a reason in the record. |
| `stage_ids` | Stages the work belongs to. |
| `artifacts[]` | Path or immutable URL and the exact commit SHA or digest. A branch name is not a revision. |
| `validation` | The command or review method that was used and its actual result. |
| `gate_status` | `PASS`, `FAIL`, `BLOCKED`, `INCONCLUSIVE`, `NEEDS_HUMAN_APPROVAL`, `WAIVED`. `ILLUSTRATIVE_ONLY` marks examples. |
| `risks`, `limitations` | What is still open and what was not checked. Empty lists are allowed; missing fields are not. |
| `sender`, `receiver`, `next_action` | Named people or roles and the first thing the receiver does. |
| `approval` | Whether a human decision is needed, who the named approver is, and the risk tier from [RISK_CLASSIFICATION.md](RISK_CLASSIFICATION.md). |
| `acceptance` | Filled by the receiver. |

## Acceptance

1. The receiver checks the revision, reads the limitations and either accepts or returns the handoff with a reason.
2. Until `acceptance.accepted_by` is set, the handoff is `BLOCKED`. A record that says `PASS` without acceptance fails `trace_evidence.py`.
3. Acceptance applies to the exact revision. A new revision needs a new handoff or an addendum that names the changed revision.

## Passing context

Pass what the receiver cannot rediscover cheaply, and nothing else.

- **Always:** the user's stated constraints in their words, decisions already made (with decision ids from the
  [decision log](DECISION_LOG_STANDARD.md)), the artifact revision, evidence references, open risks, and the named approvers.
- **Never:** credentials, customer data, or instructions copied from untrusted content (see
  [UNTRUSTED_CONTENT_POLICY.md](../../orchestrator/policies/UNTRUSTED_CONTENT_POLICY.md)).
- **Do not** summarize away uncertainty. If something was not checked, say so in `limitations`.

## When a handoff fails

| Situation | Action |
|---|---|
| Receiver does not accept within the agreed time | Status stays `BLOCKED`; the sender escalates to the accountable role. |
| Receiver rejects the artifact | Sender fixes and sends a new revision with a new handoff record that references the rejected one. |
| Receiver is the wrong skill | Return to `master-orchestration` with the reason; do not forward informally. |
| Evidence does not match the revision | Treat as `FAIL` for the claim and ask for evidence for the correct revision. |
| Approval is required and missing | `NEEDS_HUMAN_APPROVAL`; independent work may continue, the gated step may not. |

## Rework and feedback loops

Handoffs that return work (review findings to implementation, defects to implementation, incidents to reliability work)
are marked `feedback: true` in `registry/skill-content/*.json`. They use the same record. All other handoffs must form an
acyclic graph; the validator reports a forward cycle.
