# Role Operating Model

## Accountability model

The primary role owns delivery of the stage artifact; supporting roles contribute evidence; a separate verifier confirms high-risk controls. The release manager coordinates release readiness but cannot substitute for the named business, security, or production approver. The implementer does not approve their own security, architecture, or production gate.

## Handoff acceptance

Receivers verify scope, version/digest, evidence readability, known risks, and their authority to accept ownership. A rejected or unacknowledged handoff is `BLOCKED`. The orchestrator may route remediation but cannot silently redefine acceptance criteria.

## Permission tiers

| Tier | Default capability | Examples |
|---|---|---|
| Observe | Read-only evidence and telemetry | reviewers, analysts |
| Change non-production | Scoped repository/environment write | engineers, QA |
| Propose sensitive action | Prepare plan only | deployer, DBA, security engineer |
| Authorize sensitive action | Explicit human decision | designated business/security/release authority |

No role is granted a tier simply because it has a title; permissions must be configured by the host platform.
