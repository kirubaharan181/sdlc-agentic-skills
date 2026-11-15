---
name: evidence-quality-gates
description: Provides a specialist procedure to make every quality/security/release decision reproducible and auditable. Use when a request calls for this capability across stages.
---

# Evidence and gate evaluation

Make every quality/security/release decision reproducible and auditable.

## Procedure
1. Define gate criteria and required evidence before execution.
2. Pin evidence to commit, artifact digest, environment, command, executor and timestamp.
3. Distinguish PASS, FAIL, BLOCKED, INCONCLUSIVE and approved waiver.
4. Reject stale, incomplete or self-approved evidence; retain decision and follow-up.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- CI/test reports
- artifact provenance
- evidence schema validator
- approval and waiver log

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.
