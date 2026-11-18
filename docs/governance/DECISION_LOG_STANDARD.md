# Decision log standard

A decision log records choices that others will rely on: scope, design, risk acceptance, approvals, waivers, conflicts
and exceptions. It extends [`templates/decision-record.md`](../../templates/decision-record.md) (one decision per file)
with a running log, [`templates/decision-log.md`](../../templates/decision-log.md), for work that makes many small decisions
such as an incident or an orchestrated workflow.

## What to log

Log a decision when it (a) changes what will be built or run, (b) accepts a risk, (c) waives or overrides a gate,
(d) resolves a conflict between skills or people, or (e) was escalated to a human. Do not log routine steps.

## Fields

| Field | Rule |
|---|---|
| `id` | `DEC-<year>-<number>`; unique, never reused. |
| `time` | ISO 8601 with time zone. |
| `owner` | The named person or role who decided. An agent can propose; it cannot be the owner of an approval. |
| `question` | The decision in one sentence. |
| `options` | At least two, including do-nothing where it is real. |
| `decision` and `rationale` | What was chosen and why, in terms of evidence. |
| `risk_tier` | From [RISK_CLASSIFICATION.md](RISK_CLASSIFICATION.md). |
| `evidence` | References to evidence records with exact revisions. |
| `approval` | Approver and status, or "not required". |
| `reversal` | How and when the decision can be revisited, or its expiry. |
| `supersedes` | The id of an earlier decision this replaces, if any. |

## Rules

1. **Append only.** Never edit or delete an entry. To change a decision, add a new one that sets `supersedes`.
2. **One owner per decision.** Shared ownership means nobody owns it.
3. **Unknowns are written down.** If a fact is unverified, say "assumed" and who will check it by when.
4. **Link, do not copy.** Refer to evidence and other decisions by id.
5. **No secrets or personal data** in the log.
6. **Agents** record decisions they made or proposed with their role as the recorder; the human who decided is the owner.

## Using the log

- `master-orchestration` records routing choices and escalations.
- `incident-command` keeps the decision log during an incident and hands it to the post-incident review.
- `secure-change-control` links each approval to a decision id.
- `enterprise-governance` samples the log in audits to check that decisions have owners, evidence and expiry.
