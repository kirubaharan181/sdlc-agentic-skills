# Audit-ready documentation

What an auditor can reasonably ask of this library and where the answer is. This page does not claim compliance with any
standard. It describes how to produce evidence for a review.

## Questions and answers

| Question | Answer and command |
|---|---|
| Which stages exist, who owns them and who approves? | `python3 scripts/trace_evidence.py --matrix` |
| Which steps need a human decision, and why? | `approval_rationale` in the stage registry; [APPROVAL_POLICY.md](APPROVAL_POLICY.md) |
| How is risk classified and who decides? | [RISK_CLASSIFICATION.md](RISK_CLASSIFICATION.md), [APPROVAL_ESCALATION_MATRIX.md](APPROVAL_ESCALATION_MATRIX.md) |
| Is every claim of work backed by evidence for an exact revision? | [EVIDENCE_TRACEABILITY.md](EVIDENCE_TRACEABILITY.md); `python3 scripts/trace_evidence.py <records>` |
| Were decisions recorded with an owner? | [DECISION_LOG_STANDARD.md](DECISION_LOG_STANDARD.md) |
| Who owns which responsibility, and do skills overlap? | [Responsibility matrix](../architecture/SKILL_SELECTION.md#2-responsibility-matrix); the validator rejects duplicates |
| What changed in a skill and when? | `CHANGELOG.md`, the skill's `metadata.version` and `registry/skill-versions.lock.json` |
| What is the documentation quality, and has it regressed? | `python3 scripts/check_quality_regression.py --summary`; `reports/skill-quality/` |
| Is the generated documentation current? | `python3 scripts/build.py --check` |
| What is tested and what is only documented? | `adapters/COMPATIBILITY.md`; [README status line](../../README.md) |

## What to keep for an audit

1. The repository at the commit under review (a tag or SHA, not a branch).
2. Evidence records and handoff records for the work in scope, with raw outputs.
3. The decision log for the period.
4. Approval records naming a human and the exact revision.
5. Output of `make all` or the CI run for that commit.
6. Exceptions and waivers with owner and expiry.

## Limits

- The library validates structure, links and consistency. It does not prove that a procedure was followed in a real project.
- Stage content is authored but not yet proven on a real project; validation commands are examples.
- Quality scores come from a documentation checker; they do not measure correctness of the engineering advice.
- No security certification or compliance attestation is claimed.
