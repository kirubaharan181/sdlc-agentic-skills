# Skill Execution Transcript

**Date/time:** 2026-11-24T17:15:00+05:30
**OpenCode version:** v2.3.0
**Model:** nemotron-3.5-super-vl-free (OpenCode)
**Skill name:** incident-command
**Skill path:** skills/cross-cutting/incident-command/SKILL.md (installed to .opencode/skills/incident-command/)
**Test ID:** TEST-004
**Test scenario:** Declare and classify a simulated service incident (checkout errors rising after a release).
**Status:** PARTIAL PASS

---

## User input (test scenario)

"Checkout errors are rising; payments failing for some users. Error rate 8%, started 12 minutes ago after a release. Declare and classify the incident using incident-command."

---

## Skill instructions followed (from SKILL.md)

- Purpose: command and coordination during an active incident; classify severity, assign roles, set escalation/comms cadence, keep timeline and decision log, coordinate recovery, hand over to post-incident review. Coordinates; does NOT perform the technical fix.
- When to use: an incident is declared or a service is failing and impact is unclear; several teams must coordinate.
- Prerequisites: a way to reach on-call people/stakeholders; severity definitions and escalation paths; a shared place for timeline and decision log.
- Required inputs: symptoms and affected users; time of detection; current owner.
- Procedure steps followed:
  1. Declare severity and assign commander, operations, communications and scribe roles.
  2. Maintain timeline, customer impact, hypotheses, decisions and action owners.
  3. Coordinate safe containment and recovery with change authority and evidence preservation.
  4. Verify service health, communicate resolution and hand off blameless corrective actions.
- Decision rules applied:
  - Customer-visible outage or data risk -> classify as highest severity and page incident roles.
  - Recent change plausibly related -> consider rollback first if safe and approved.
  - Roles unfilled -> assign explicitly; one person is incident commander.

---

## Actual execution steps

1. Classified severity: customer-visible (payments failing for some users) + error rate 8% after a release -> HIGHEST severity (customer-visible outage/data risk).
2. Assigned roles explicitly:
   - Incident commander: on-call engineering lead (named placeholder)
   - Operations: backend on-call
   - Communications: support/comms lead
   - Scribe: incident scribe
3. Recorded timeline: detection 12 minutes ago after release; error rate 8%; payments failing for some users.
4. Hypotheses: recent release plausibly related (decision rule: consider rollback first if safe and approved).
5. Recommended action: evaluate rollback via emergency change approval; do NOT perform the technical fix (skill limitation).
6. Did NOT page real people (no on-call system configured; simulated only).
7. Did not set a real communication cadence channel (simulated).

---

## Actual output (incident record)

- Severity: HIGH (customer-visible payment failures) — classified with reason.
- Roles assigned: commander, operations, communications, scribe (named placeholders; simulated).
- Timeline entry: detection time, symptoms, affected users, related change (release).
- Hypothesis: recent release plausibly related; rollback considered first if safe and approved.
- Next step: route rollback through emergency change approval; coordinate with secure-change-control.
- First update scheduled; next update time noted.

---

## Verification evidence

- SKILL.md decision rule: "Customer-visible outage or data risk | Classify as highest severity and page the incident roles" — applied.
- SKILL.md limitation: "It does not diagnose without telemetry or fix without access" — respected; no fix performed.
- templates/incident-timeline.md and templates/decision-log.md exist for recording.

---

## Limitations

- No real on-call/incident platform or paging system configured; roles and communications are simulated placeholders.
- No telemetry/dashboards available; hypothesis based on user-provided info only (skill correctly marks unknowns).
- Did not execute an actual rollback (would be a production change requiring approval).

---

## Test status

PARTIAL PASS — The skill procedure was followed (severity classified, roles assigned, timeline started, rollback considered via change authority). Correctly did NOT perform a fix or page real people. Full PASS would require a live incident platform and real responders, which are out of scope and correctly simulated.
