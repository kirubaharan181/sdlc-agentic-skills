# Risk classification framework

Every change, approval and handoff carries a risk tier from `R0` to `R4`. The tiers, their criteria and the stage
assignments are data in [`registry/risk-tiers.json`](../../registry/risk-tiers.json); this page explains how to use them.
The tiers are defaults to adapt to your organization. They are a framework, not a certification.

## Tiers

| Tier | Name | Typical examples | Approval | Rollback | Evidence |
|---|---|---|---|---|---|
| R0 | Informational | Documents, analysis, code on a branch | None | Not applicable | Self-check recorded |
| R1 | Low | Reversible change in non-production | Peer review | Documented | Tests or checks recorded |
| R2 | Moderate | Reversible, tested production-reaching change; merge approval; UAT | Named owner of the service or decision | Tested | Test evidence for the exact build |
| R3 | High | Production schema or data, IAM, secrets, network policy, security controls, funding, legal obligation | Named accountable human plus an independent verifier | Tested and rehearsed | Independently verified evidence |
| R4 | Critical | Irreversible or destructive action, active attack testing, full failover, product retirement, risk acceptance for the organization | Named executive risk owner plus the security or compliance owner | Rehearsed, or a written statement that none is possible | Independent evidence and a written risk acceptance |

## How to classify

1. Start at R0. Move up one tier for each question answered yes, taking the highest tier that applies.
2. Does it reach production? (R2 at least.)
3. Does it change production data, access, secrets, network policy or a security control, or commit money or legal obligation? (R3 at least.)
4. Is it irreversible, destructive, an active attack test, a full failover, a retirement, or an acceptance of risk for the organization? (R4.)
5. If unsure between two tiers, choose the higher one and ask the governance owner to clarify the criterion.
6. A change that matches a pre-approved standard change keeps its tier but may follow the standard procedure.

## Rules

- The tier is recorded in the change request, handoff record or decision record with the reason.
- A tier is never lowered to avoid approval. Lowering needs a recorded reason and the approver of the higher tier.
- Approvers are named humans. An agent prepares the pack and never approves (see [APPROVAL_POLICY.md](APPROVAL_POLICY.md)).
- Every approval-gated stage has exactly one tier in `registry/risk-tiers.json`; `tests/test_governance.py` fails if one is missing.
- See [APPROVAL_ESCALATION_MATRIX.md](APPROVAL_ESCALATION_MATRIX.md) for who decides and when to escalate.

## Stage tiers

The stage-to-tier table is generated on demand: `python3 scripts/trace_evidence.py --matrix` prints stage, gate, approver and tier as CSV.
