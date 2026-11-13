# Evidence Gate Policy

## State machine

`NOT_STARTED → IN_PROGRESS → PASS | FAIL | BLOCKED | INCONCLUSIVE | NEEDS_HUMAN_APPROVAL | WAIVED`

Only new evidence can move `FAIL`, `BLOCKED`, or `INCONCLUSIVE` to `PASS`. A waiver never changes the underlying finding; it records the authorized risk decision and expiry/review condition.

## Required evidence minimum

Every gate references a stage ID, owner, exact revision/digest, command or review method, timestamp, artifact path, result, limitations, and approver when relevant. High-risk release/security/compliance evidence is verified by someone independent of implementation.
