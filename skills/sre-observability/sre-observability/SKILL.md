---
name: sre-observability
description: Provides a specialist procedure to make service health measurable and incidents diagnosable. Use when the work involves Application Monitoring, Infrastructure Monitoring, Centralized Logging, Metrics Monitoring, Distributed Tracing, Alert Management, Uptime Monitoring, SLA/SLO Management and 6 more stages.
---

# Reliability and observability

Make service health measurable and incidents diagnosable.

## Procedure
1. Define user-facing SLIs/SLOs, error budget and critical journeys.
2. Instrument golden signals, trace correlation, safe logs and actionable alerts.
3. Review capacity, toil, incident patterns and recovery objectives.
4. Run learning reviews and verify reliability improvement against baseline.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

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

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: disaster-recovery, emergency-hotfix, incident-response, new-product-development, performance-optimization, rollback, root-cause-analysis.
- Roles: backend-engineer, incident-manager, infrastructure-engineer, observability-engineer, platform-engineer, process-improvement-specialist, production-support-engineer, sre.
