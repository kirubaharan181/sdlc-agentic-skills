# Evidence traceability

Every claim of work done must be traceable, in both directions, along this chain:

```
requirement or decision  ->  stage  ->  gate  ->  evidence record (exact revision)  ->  approver
```

| Link | Where it lives |
|---|---|
| Requirement | `REQ-` ids in the project's requirements (see stage 12, Requirement Documentation) |
| Decision | `DEC-` ids in the [decision log](DECISION_LOG_STANDARD.md) |
| Stage and gate | `stage_id` and `quality_gate` in `registry/SDLC_STAGE_REGISTRY.json` (for example gate `11-133`) |
| Evidence record | [`templates/evidence-record.json`](../../templates/evidence-record.json): gate, revision, executor, method, result, limitations |
| Approver | `approver` on the stage and `approved_by` on the record; a named human, never an agent |
| Handoff | [handoff record](HANDOFF_CONTRACT_STANDARD.md) carrying the same revision |

## Rules

1. **Exact revision.** A record names a commit SHA or artifact digest. Evidence for another revision is not evidence for this one.
2. **Raw output is kept.** The record points to the unedited log or report, not only to a summary.
3. **Status is honest.** `PASS` needs a real revision, executor, timestamp, at least one real evidence item and stated limitations.
   Anything not run is `BLOCKED` or `INCONCLUSIVE`. Examples say `"example": true` and never `PASS`.
4. **Independent approval.** The approver is not the executor. Stages with `approval_required` need `approved_by`.
5. **Conflicts are recorded**, not averaged (see [CONFLICT_RESOLUTION.md](CONFLICT_RESOLUTION.md)).
6. **Retention.** Keep records for as long as the claim they support is relied upon, and at least as long as the organization's audit retention rule.

## Checking

```
python3 scripts/trace_evidence.py records/*.json    # evidence and handoff records
python3 scripts/trace_evidence.py --templates       # the shipped templates keep their shape
python3 scripts/trace_evidence.py --matrix > matrix.csv   # stage, gate, approver, risk tier for all 190 stages
```

The checker verifies that the stage exists, the gate matches the stage, a `PASS` has real values, approvers are human and
independent, and a handoff without acceptance is not `PASS`. It checks structure and links. It cannot prove that a command was
really run; that remains the job of the independent verifier ([evidence-quality-gates](../../skills/cross-cutting/evidence-quality-gates/SKILL.md)).
