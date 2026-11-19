---
name: evidence-quality-gates
description: "Use when a gate needs proof: classifies, checks, accepts or rejects evidence. Do NOT use to produce the evidence itself."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["evidence", "traceability", "quality-gates", "audit"]
---

# Evidence and gate evaluation

## Purpose
Decides whether the evidence offered for a claim is good enough to pass a gate. It classifies the evidence, checks provenance and reliability, ties it to the claim and revision, assigns a confidence level, handles conflicting or missing evidence, and returns PASS, FAIL, BLOCKED, INCONCLUSIVE, NEEDS_HUMAN_APPROVAL or WAIVED with reasons.

## When to Use
- A gate, sign-off or approval depends on evidence.
- Evidence from different sources disagrees.
- A report claims work was done and the proof must be checked.

## When NOT to Use
- Producing the evidence: use the specialist skill.
- Checking task completion overall: use definition-of-done.
- Auditing controls across teams: use enterprise-governance.

## Prerequisites and Requirements
- The claim being gated and its gate id.
- The evidence artifacts or immutable links.
- templates/evidence-record.json as the record shape.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- claim and gate
- evidence records or artifacts
- revision or build identifier

Optional inputs:
- previous results
- tool versions
- reviewer identity

Outputs and deliverables:
- evidence classification and provenance check
- confidence level with reasons
- traceability from claim to evidence to revision
- gate decision with status and limitations

## Procedure
1. Define gate criteria and required evidence before execution.
2. Pin evidence to commit, artifact digest, environment, command, executor and timestamp.
3. Distinguish PASS, FAIL, BLOCKED, INCONCLUSIVE and approved waiver.
4. Reject stale, incomplete or self-approved evidence; retain decision and follow-up.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Evidence has no revision or timestamp | Treat as INCONCLUSIVE. |
| Evidence is for a different build | FAIL for this claim; request the correct evidence. |
| Two sources conflict | Prefer the one closer to the system and reproducible; record the conflict; do not average. |
| Evidence is an example or illustration | Never count it; examples are marked example true. |
| Only the producer vouches for the work | Request independent confirmation for high-risk gates. |
| Critical evidence missing | BLOCKED; list exactly what is needed. |

## Quality Gates
- [ ] Each claim links to evidence with revision, method, executor and time
- [ ] Confidence level is stated with reasons
- [ ] Conflicts and gaps are listed
- [ ] Rejection reasons are specific and fixable

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Accept test evidence
```text
Request: Gate: all unit tests pass for build 2.8.0.
Context: A CI log and report are attached.
Agent behavior: Check build id, command, executor, time and result in the log, then confirm that raw output matches the summary.
Output: PASS with confidence high; limitation: unit tests only.
Acceptance: Record lists artifact link, revision and limitations.
```

### Example 2: Reject a claim
```text
Request: Security scan passed.
Context: Only a screenshot without date or revision.
Agent behavior: Mark INCONCLUSIVE because provenance is missing and request the scan output.
Output: INCONCLUSIVE with the exact missing items.
Acceptance: Reason is specific and fixable.
```

### Example 3: Conflicting evidence
```text
Request: Load test shows pass; monitoring shows errors at the same time.
Context: Both from the last release.
Agent behavior: Compare timestamps and environment, record the conflict, and prefer production-measured data for production claims.
Output: Conflict record with decision rationale and escalation if unresolved.
Acceptance: Conflict is recorded, not averaged away.
```

## Limitations
- Judges the evidence offered; it cannot discover evidence that does not exist.
- Cannot prove authenticity beyond provenance fields it can check.
- Gate decisions that need approval go to a named human.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Evidence link expired | Mutable or temporary URL | Request an immutable copy or hash. |
| Evidence is redacted | Sensitive data removed | Accept with a stated limitation or request a safer form. |
| Conflicting sources | Different scope or time | Normalize scope and time, then compare. |

## Tools
- CI/test reports
- artifact provenance
- evidence schema validator
- approval and waiver log

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.

## Handoffs
Hands to:
- `enterprise-governance`: evidence assessments for audits
- `release-deployment`: gate decisions for release readiness

Receives from:
- `definition-of-done`: evidence sets that need deeper evaluation
- `enterprise-governance`: evidence sets for quality evaluation
- `master-orchestration`: evidence set for evaluation

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
