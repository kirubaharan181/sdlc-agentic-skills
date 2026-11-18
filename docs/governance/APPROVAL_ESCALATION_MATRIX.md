# Approval and escalation matrix

Who decides, who verifies, and when to escalate, by risk tier ([RISK_CLASSIFICATION.md](RISK_CLASSIFICATION.md)). The named
approver per stage is `approver` in `registry/SDLC_STAGE_REGISTRY.json`. Times are defaults to adapt, not promises.

## Matrix

| Tier | Decides | Independent verifier | Escalate if no decision after | Escalate to | If the approver is unavailable |
|---|---|---|---|---|---|
| R0 | Author | None | Not applicable | Not applicable | Not applicable |
| R1 | Peer reviewer | Reviewer is the verifier | 48 hours | Engineering lead | Another peer |
| R2 | Named service or decision owner | Reviewer or tester who did not build it | 24 hours | Owner's manager | Documented delegate only |
| R3 | Named accountable human for the stage approver role | Independent verifier of the evidence | 8 hours | Head of the function | Documented delegate; never the implementer |
| R4 | Named executive risk owner and the security or compliance owner | Independent verifier | 4 hours | Executive sponsor | No delegate; the action waits |

## Approver roles in the registry

| Approver role | Used by stages |
|---|---|
| business-sponsor | 9, 180 |
| legal-owner | 10 |
| change-board | 44, 129 |
| secrets-owner | 50 |
| code-owner | 75 |
| uat-acceptor | 95 |
| security-lead | 104, 110 |
| compliance-owner | 108 |
| infra-owner | 117, 121 |
| dba-owner | 132, 173 |
| production-approver | 133 |
| dr-owner | 148 |
| finops-owner | 151 |
| access-owner | 184 |

`tests/test_governance.py` keeps this table in step with the registry.

## Escalation triggers

Escalate immediately, whatever the tier, when:

- the approver, the executor and the verifier would be the same person;
- a gate is `FAIL`, `BLOCKED` or `INCONCLUSIVE` and the work is due to proceed;
- a security control would be disabled, or an irreversible action is proposed;
- the user's stated constraint conflicts with a specialist's advice (see [CONFLICT_RESOLUTION.md](CONFLICT_RESOLUTION.md));
- an incident is active (hand to `incident-command`).

## Emergency changes

An emergency change may start after recorded approval from the on-call authority for its tier, with a review within one
business day. The review confirms the emergency was real, the change was minimal and the record is complete. Missing the review is itself a finding.

## Records

Each decision is a row in the [decision log](DECISION_LOG_STANDARD.md) and an evidence record bound to the exact revision.
