---
name: incident-command
description: Coordinates live incidents: severity, roles, comms, timeline, recovery. Use when an incident is active. Do NOT use for routine support tickets.
metadata:
  author: kirubaharan181
  version: "1.1.0"
  tags: ["incident", "command", "communication", "recovery"]
---

# Incident command

## Purpose
Provides command and coordination during an active incident: it classifies severity, assigns roles, sets escalation and communication cadence, keeps a timeline and decision log, coordinates recovery and hands over to the post-incident review. It coordinates people and decisions; it does not perform the technical fix and it never claims an incident was handled when no incident was run.

## When to Use
- An incident is declared or a service is failing and impact is unclear.
- Several teams must coordinate, communicate and decide quickly.
- A timeline and decision log must be kept for later review.

## When NOT to Use
- Routine tickets: use maintenance-support.
- Designing monitoring or writing the postmortem analysis: use sre-observability.
- Fixing the bug: use software-implementation.

## Prerequisites and Requirements
- A way to reach the on-call people and stakeholders.
- Severity definitions and escalation paths.
- A shared place for the timeline and decision log.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- symptoms and affected users
- time of detection
- current owner

Optional inputs:
- recent changes
- dashboards
- previous similar incidents

Outputs and deliverables:
- severity classification with reason
- role assignments
- communication updates on a schedule
- timeline and decision log
- recovery confirmation and handover for review

## Procedure
1. Declare severity and assign commander, operations, communications and scribe roles.
2. Maintain timeline, customer impact, hypotheses, decisions and action owners.
3. Coordinate safe containment and recovery with change authority and evidence preservation.
4. Verify service health, communicate resolution and hand off blameless corrective actions.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Customer-visible outage or data risk | Classify as highest severity and page the incident roles. |
| Cause unknown after the agreed interval | Escalate to the next tier and widen the responder group. |
| Recent change plausibly related | Consider rollback first if safe and approved. |
| Fix needs a production change | Route through emergency change approval and record it. |
| Roles unfilled | Assign explicitly; one person is the incident commander. |
| Status uncertain | Say what is known, unknown and when the next update comes. |

## Quality Gates
- [ ] One incident commander and named role holders
- [ ] Updates sent at the agreed cadence
- [ ] Every decision logged with time and owner
- [ ] Recovery verified by evidence before closing

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Declare and classify
```text
Request: Checkout errors are rising; payments failing for some users.
Context: Error rate 8 percent, started 12 minutes ago after a release.
Agent behavior: Classify high severity, assign commander, communications and technical lead, and ask whether the release can be rolled back.
Output: Incident record with severity, roles, first update and next update time.
Acceptance: Roles are named and the first update is scheduled.
```

### Example 2: Log a decision
```text
Request: Decide whether to roll back.
Context: Rollback is tested; data impact is none.
Agent behavior: Record options, owner, decision, time and the approval route.
Output: Decision log entry with rollback approved by the on-call authority.
Acceptance: Entry has time, owner and rationale.
```

### Example 3: Close and hand over
```text
Request: Service recovered.
Context: Error rate normal for 30 minutes.
Agent behavior: Confirm recovery with metrics, send the final update, and open the review with timeline.
Output: Closure record and handover to the postmortem owner.
Acceptance: Recovery is shown by data, not by statement.
```

## Limitations
- Coordinates; it does not diagnose without telemetry or fix without access.
- Cannot confirm facts it was not told; it marks unknowns.
- Does not replace the humans who hold authority for emergency changes.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Too many responders talking | No single command | Name one commander and a communications lead. |
| No clear owner of the affected service | Ownership gaps | Escalate to the on-call manager and record the gap. |
| Conflicting information | Multiple sources | Record each source and time; verify with data. |

## Tools
- incident platform
- status communication
- telemetry and runbooks
- postmortem/action tracker

## Stages covered
None. This is a cross-cutting skill applied alongside stage skills.

## Handoffs
Hands to:
- `sre-observability`: timeline and decision log for root cause analysis
- `secure-change-control`: emergency change requests
- `maintenance-support`: customer communications and follow-up tickets

Receives from:
- `master-orchestration`: active incident declaration with severity
- `sre-observability`: severity and detection data when an incident is declared

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
