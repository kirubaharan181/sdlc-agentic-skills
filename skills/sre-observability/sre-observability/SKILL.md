---
name: sre-observability
description: Designs monitoring, SLOs, alerts and incident analysis. Use when making a service observable or reliable. Do NOT use for command of live incidents.
metadata:
  author: kirubaharan181
  version: "1.1.0"
  tags: ["sre", "observability", "slo", "incident-analysis"]
---

# Reliability and observability

## Purpose
Makes service health visible and improves reliability: application and infrastructure monitoring, logs, metrics, traces, alerting, SLOs, capacity, incident detection and response practice, root cause analysis, postmortems and reliability improvement. It owns stages 153-166.

## When to Use
- A service needs monitoring, logging, tracing or alerts.
- SLOs and error budgets need defining or reviewing.
- A root cause analysis or postmortem is needed after an incident.

## When NOT to Use
- Commanding an active severe incident: use incident-command.
- Provisioning infrastructure: use cloud-hosting-operations.
- Fixing the bug: use maintenance-support or software-implementation.

## Prerequisites and Requirements
- Key user journeys and the service owner.
- Access to telemetry sources or a plan to add them.
- An on-call and escalation path.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- service and key journeys
- current telemetry

Optional inputs:
- incident history
- SLO targets
- traffic forecasts

Outputs and deliverables:
- indicators and objectives per journey
- dashboards and alerts linked to runbooks
- capacity plan
- root cause analysis and postmortem with actions

## Procedure
1. Define user-facing SLIs/SLOs, error budget and critical journeys.
2. Instrument golden signals, trace correlation, safe logs and actionable alerts.
3. Review capacity, toil, incident patterns and recovery objectives.
4. Run learning reviews and verify reliability improvement against baseline.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Alert needs no action | Remove or demote it to a ticket. |
| Metrics green but users report failures | Add synthetic and real-user checks. |
| Postmortem assigns blame to a person | Rewrite around causes and system fixes. |
| Telemetry contains sensitive data | Mask and fix the instrumentation. |

## Quality Gates
- [ ] Objectives exist for key journeys
- [ ] Pages map to user impact or fast budget burn
- [ ] Telemetry carries the release version
- [ ] Postmortem actions have owners and dates

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Define an SLO
```text
Request: Set an objective for checkout.
Context: Checkout success ratio is measured; no objective exists.
Agent behavior: Propose 99.5 percent success over 30 days, compute the error budget, and define burn-rate alerts.
Output: SLO document with indicator, objective, budget and alert rules.
Acceptance: Indicator is measurable from existing telemetry.
```

### Example 2: Write a postmortem
```text
Request: Write the postmortem for the 40-minute checkout outage.
Context: A release raised error rate; rollback restored service.
Agent behavior: Build the timeline from logs, identify contributing causes, and list owned actions.
Output: Blameless postmortem with timeline, causes, impact and four dated actions.
Acceptance: Each action has an owner and a date.
```

## Limitations
- Cannot see telemetry it is not given.
- Objectives need business agreement and are not set unilaterally.
- Root causes found from logs may be incomplete if data is missing.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Alert fatigue | Too many low-value pages | Review each alert monthly and remove or tune. |
| Traces break at a queue | Context not propagated | Propagate trace context in message headers. |
| Dashboards disagree | Different definitions | Standardize indicator definitions. |

## Tools
- OpenTelemetry or configured telemetry
- APM/log/metric/tracing platform
- incident tooling
- load/recovery testing

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 153 | Application Monitoring | complete | Observability Engineer |
| 154 | Infrastructure Monitoring | complete | Observability Engineer |
| 155 | Centralized Logging | complete | Observability Engineer |
| 156 | Metrics Monitoring | complete | Observability Engineer |
| 157 | Distributed Tracing | complete | Observability Engineer |
| 158 | Alert Management | complete | SRE |
| 159 | Uptime Monitoring | complete | Observability Engineer |
| 160 | SLA/SLO Management | complete | SRE |
| 161 | Capacity Planning | complete | SRE |
| 162 | Incident Detection | complete | Incident Manager |
| 163 | Incident Response | complete | Incident Manager |
| 164 | Root Cause Analysis | complete | SRE |
| 165 | Postmortem | complete | Incident Manager |
| 166 | Reliability Improvement | complete | SRE |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `incident-command`: severity and detection data when an incident is declared
- `maintenance-support`: reliability and fix backlog
- `enterprise-governance`: SLO and incident evidence for review

Receives from:
- `cloud-hosting-operations`: infrastructure telemetry and capacity data
- `incident-command`: timeline and decision log for root cause analysis
- `maintenance-support`: recurring issues as reliability work
- `release-deployment`: release markers and rollback criteria for monitoring

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: disaster-recovery, emergency-hotfix, incident-response, new-product-development, performance-optimization, rollback, root-cause-analysis.
- Roles: backend-engineer, incident-manager, infrastructure-engineer, observability-engineer, platform-engineer, process-improvement-specialist, production-support-engineer, sre.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
