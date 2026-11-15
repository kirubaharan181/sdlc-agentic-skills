# Human approval policy

A stage sets `approval_required: true` in `registry/SDLC_STAGE_REGISTRY.json` when a human with authority must
decide before the agent proceeds. The one-line reason for each stage is its `approval_rationale` field; this page
explains the rules used to decide, so the registry has one statement per stage and this page has the criteria.

## Test for requiring approval

A stage needs a human approver if **any** of these is true:

1. **Irreversible or hard to reverse** — data deletion, schema change in production, secret rotation, deleting infrastructure.
2. **Changes who can do what** — IAM, privileged access, break-glass access, firewall and network policy.
3. **Accepts risk or obligation on the organization's behalf** — residual security risk, license exceptions, retiring a product.
4. **Touches customers or money directly** — production deployment, billing-sensitive resource changes.
5. **Needs legal authorization** — active security testing against a target.

Stages that only produce documents, analysis, code on a branch, or test results do **not** need approval; they are
controlled by evidence gates and independent review instead.

## Rules that always apply

- The approver must not be the agent (or person) that implemented or verified the change.
- Approval is recorded as evidence against an exact artifact version or commit, not as a free-text "ok".
- An approval for one artifact version does not carry over to the next.
- A waiver of a failed gate is not an approval; it needs reason, risk, approver, date and expiry.

## Stages considered and left ungated

| Stage | Why no separate approval |
|---|---|
| 171 Patch Management, 172 Dependency Updates | Reach production only through stages 129 and 133, which are gated. |
| 137 Rollback Planning | Planning only; executing a rollback is a production deployment (133) or incident action. |
| 134 Domain & DNS, 135 SSL/TLS Setup | Covered by 117/121 when performed as infrastructure change; revisit if DNS is changed outside IaC. |
| 147 Backup Management | Creating backups is non-destructive; restore is covered by 148. |

## Reviewing this policy

Revisit when a new stage is added, after any incident caused by an ungated change, and at each minor release.
`scripts/validate.py` fails if a stage has `approval_required: true` without an `approval_rationale`.
