# Reliability and observability: stage reference

## Contents
- [153 Application Monitoring](#153)
- [154 Infrastructure Monitoring](#154)
- [155 Centralized Logging](#155)
- [156 Metrics Monitoring](#156)
- [157 Distributed Tracing](#157)
- [158 Alert Management](#158)
- [159 Uptime Monitoring](#159)
- [160 SLA/SLO Management](#160)
- [161 Capacity Planning](#161)
- [162 Incident Detection](#162)
- [163 Incident Response](#163)
- [164 Root Cause Analysis](#164)
- [165 Postmortem](#165)
- [166 Reliability Improvement](#166)

## 153
**Application Monitoring** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-153. Approval: none required

## 154
**Infrastructure Monitoring** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-154. Approval: none required

## 155
**Centralized Logging** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-155. Approval: none required

## 156
**Metrics Monitoring** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-156. Approval: none required

## 157
**Distributed Tracing** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-157. Approval: none required

## 158
**Alert Management** (complete). Purpose: page the right person for conditions that need action, and nobody for anything else.

Entry criteria: Service level objectives or critical symptoms are defined; On-call rota and escalation path exist; Metrics and logs are available to alert on

Inputs: SLOs and critical user symptoms; metrics and log sources; on-call rota; runbooks

Procedure:
1. Choose alerts that reflect user-visible symptoms or SLO burn, not every internal metric.
2. For each alert write severity, threshold, evaluation window, owner and a runbook link stating the first action.
3. Route by severity: page for urgent user impact, ticket for non-urgent.
4. Test each alert by triggering or replaying the condition in a safe environment.
5. Review alert volume weekly; remove or retune alerts that fire without action.
6. Record every change to alert rules in version control.

Deliverables: alert rule definitions; runbook per alert; routing configuration; alert quality review

Acceptance: Every page has an owner and a runbook with a first action Each alert was tested at least once Pages that required no action are tracked and reduced Rules are versioned

Validation: Test fire of each alert reaches the on-call person.

- `promtool check rules alerts/*.yml   # example for Prometheus rules` expect: SUCCESS for every file
- manual: trigger the test alert and confirm the on-call device receives it within the target time expect: receipt time recorded

Failure modes:
- Alert fatigue | detect: More than half of pages need no action | respond: Retune or delete the alert
- Alert without runbook | detect: Runbook link empty | respond: Block merge of the rule
- Routing sends to a team that no longer exists | detect: Test page not received | respond: Fix routing; retest

ILLUSTRATIVE: A page for 'error budget burn above 10x over one hour' links to a runbook that starts with checking the latest deployment. A test replay of last week's incident metrics fires the alert.

Gate: 13-158. Approval: none required

## 159
**Uptime Monitoring** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-159. Approval: none required

## 160
**SLA/SLO Management** (complete). Purpose: set measurable reliability targets with users in mind and use the remaining error budget to steer work.

Entry criteria: Critical user journeys are identified; Measurement data exists or can be collected; Service owner and product owner are available

Inputs: critical journeys; historical reliability data; dependency list; support and incident history

Procedure:
1. Choose SLIs that measure what users experience (availability, latency, correctness) for each critical journey.
2. Set SLO targets and windows from historical data and user expectations, not from aspiration alone.
3. Compute the error budget and define the policy: what happens when it is spent (for example pause risky releases).
4. Implement measurement and a dashboard; verify the SLI matches real user experience.
5. Review SLO attainment and budget burn on a fixed cadence.
6. Adjust targets with owners when evidence shows they are wrong.

Deliverables: SLO specification; error-budget policy; SLI dashboard; review notes

Acceptance: Each SLO has a clear SLI, window and target Error-budget policy is agreed by service and product owners SLI measurement was verified against a known event Review cadence is scheduled

Validation: Service owner and product owner agree the policy.

- manual: replay a known past outage against the SLI query and confirm it registers expect: SLI dips during the outage window
- `promtool query instant http://prometheus:9090 'sum(rate(http_requests_total{code!~"5.."}[30d]))/sum(rate(http_requests_total[30d]))'   # example` expect: returns a ratio matching the dashboard

Failure modes:
- SLI does not reflect user pain | detect: Outage did not move the SLI | respond: Redefine the SLI
- Budget policy never enforced | detect: Budget spent with no action | respond: Escalate to the owners
- Target set above what the dependencies allow | detect: SLO exceeds dependency SLO | respond: Lower the target or fix the dependency

ILLUSTRATIVE: A checkout journey gets an SLO of 99.9 percent success over 30 days, a budget of about 43 minutes, and a policy to freeze risky releases when 75 percent of the budget is spent.

Gate: 13-160. Approval: none required

## 161
**Capacity Planning** (stub). Purpose: provide actionable observability and service-level control.

Inputs: service map and critical user journeys; SLO and alert thresholds; telemetry and privacy requirements

Procedure:
1. Instrument golden signals and key business transactions with stable service/environment labels.
2. Correlate logs, metrics and traces using request IDs while excluding secrets and sensitive payloads.
3. Define SLI/SLO windows, burn-rate alerts, ownership, runbooks and paging policy.
4. Test alert routing and diagnostic usefulness; remove noisy or unactionable alerts.

Deliverables: telemetry specification; dashboards and alerts; SLO/error-budget report; runbook links

Acceptance: Signals support diagnosis and customer impact assessment. Alerts have owner and action. SLOs are measurable and privacy-safe.

Validation: SRE review and alert simulation.

Gate: 13-161. Approval: none required

## 162
**Incident Detection** (complete). Purpose: notice that something is wrong in production quickly and reliably, and route it to the right responder with enough context.

Entry criteria: Monitoring, alerts and logs exist for the service; On-call and escalation paths are defined; Severity definitions are agreed

Inputs: alerts and monitoring signals; user reports and support tickets; on-call rota; severity definitions

Procedure:
1. Collect detection signals from alerts, synthetic checks, logs and user reports into one view.
2. Decide whether a signal indicates user impact; check the dashboards and recent changes.
3. Declare an incident when the impact threshold is met and assign severity.
4. Page the owner by the rota with the context: symptoms, start time, affected users, recent changes.
5. Record detection time and how it was detected; note if users noticed before monitoring did.
6. Hand over to incident response (stage 163).

Deliverables: incident declaration; detection timeline; page with context; detection-gap note

Acceptance: Detection time and source are recorded The responder received symptoms and recent changes Severity is set Cases detected by users are listed as monitoring gaps

Validation: Incident manager review of detection performance.

- manual: compare incident start time with first alert time expect: gap within the target, or gap recorded as an action
- manual: confirm the page contained symptoms, time and recent changes expect: all present

Failure modes:
- Users report before alerts fire | detect: First report earlier than first alert | respond: Add or tune detection for that symptom
- Page lacks context | detect: Responder had to ask what was wrong | respond: Improve the alert text and links
- Severity wrong | detect: Later raised or lowered | respond: Review criteria

ILLUSTRATIVE: A synthetic checkout check fails twice in a row and pages the on-call engineer with the failing step and the deployment from ten minutes earlier. The incident is declared as severity 2.

Gate: 13-162. Approval: none required

## 163
**Incident Response** (complete). Purpose: restore service quickly and safely when something is broken, with clear command and communication.

Entry criteria: An alert or report indicates user impact; On-call responder is reachable; Severity levels and roles are defined

Inputs: alert or report; runbooks and dashboards; severity definitions; recent change list

Procedure:
1. Acknowledge, assign an incident commander and open a single incident channel and record.
2. Classify severity by user impact and blast radius; escalate per severity.
3. Check recent changes and dashboards; choose the safest mitigation (rollback, feature flag, failover) before searching for root cause.
4. Communicate status at a fixed interval to stakeholders and affected users.
5. Verify recovery with user-facing checks and metrics, then close or downgrade.
6. Hand off timeline and artifacts to the postmortem (stage 165).

Deliverables: incident record with timeline; status updates; mitigation actions list; recovery verification

Acceptance: Single commander and channel were named Customer-impact communications were sent on schedule Recovery was verified by metrics, not by absence of alerts Timeline is complete enough for a postmortem

Validation: Recovery verified by an independent check.

- manual: compare error rate and latency to pre-incident baseline for 30 minutes expect: within baseline
- `git log --since='6 hours ago' --oneline` expect: changes before the incident are listed in the record

Failure modes:
- Investigating while users are impacted | detect: Mitigation delayed for diagnosis | respond: Mitigate first (rollback or flag)
- No communication | detect: No status update inside the interval | respond: Commander assigns a communicator
- Multiple people changing production | detect: Conflicting actions in the timeline | respond: Commander approves all changes

ILLUSTRATIVE: Error rate jumps right after a release. The commander rolls back within ten minutes, confirms the error rate returns to baseline, and keeps the incident open for thirty minutes of observation.

Gate: 13-163. Approval: none required

## 164
**Root Cause Analysis** (complete). Purpose: find the conditions that caused an incident and prove them, so the fix addresses the cause and not the symptom.

Entry criteria: Incident is mitigated; Timeline and artifacts are preserved; People who responded are available

Inputs: incident timeline; logs, metrics and traces; change history; configuration at the time

Procedure:
1. Build a precise timeline from logs, metrics and change history.
2. List contributing factors across code, config, process and detection.
3. Ask why repeatedly for each factor until you reach something the team can change.
4. Test each hypothesis against evidence or reproduce it; mark unproven hypotheses as such.
5. State the most likely cause with its confidence and what evidence supports it.
6. Propose corrective and preventive actions with owners and dates.

Deliverables: root-cause analysis document; evidence references; hypothesis log with status; action list

Acceptance: Causes are supported by evidence or marked unproven No cause is a person's name; causes are conditions Actions have owners and dates Detection and response gaps are included

Validation: Reproduction or evidence check by someone outside the responding team.

- manual: reproduce the failure in a test environment or replay the logs expect: failure reproduced or the document states it was not
- manual: check each action has an owner and due date expect: none missing

Failure modes:
- Blame assigned to an individual | detect: Cause text names a person | respond: Rewrite as a condition
- Cause not verified | detect: Hypothesis has no evidence | respond: Mark INCONCLUSIVE and list tests to run
- Only the trigger is addressed | detect: Actions fix the symptom only | respond: Add actions for the underlying condition

ILLUSTRATIVE: A connection pool exhausted because a new feature held connections during a slow external call. Contributing factors: no timeout, no pool alert, load test missed the path. Actions: add timeout, alert, and a load test.

Gate: 13-164. Approval: none required

## 165
**Postmortem** (complete). Purpose: learn from an incident in writing, blamelessly, and make sure the lessons become tracked work.

Entry criteria: Incident is resolved; Timeline and RCA draft exist; Participants are available for review

Inputs: incident record; RCA document; customer impact data; action candidates

Procedure:
1. Summarize impact, duration, detection time and recovery time with numbers.
2. Write the timeline and what went well, what went badly and where luck helped.
3. Link the RCA findings; agree actions with owners and dates.
4. Review in a blameless meeting; capture disagreements.
5. Publish to the engineering organization.
6. Track actions to completion and report overdue ones.

Deliverables: postmortem document; action items in the tracker; published summary; follow-up report

Acceptance: Impact numbers are stated Language is blameless Every action is in the tracker with owner and date Postmortem is published within the agreed time

Validation: Review meeting and published record.

- manual: compare action list in the document with tracker items expect: every action has an issue id
- manual: check postmortem publish date against incident close date expect: within the agreed number of days

Failure modes:
- Actions never completed | detect: Overdue items in tracker | respond: Report to engineering leadership
- Postmortem skipped for minor incidents | detect: No document for a sev-2 | respond: Create a short one
- Blame language | detect: Names attached to errors | respond: Edit to focus on conditions

ILLUSTRATIVE: A forty-minute checkout outage produces a two-page postmortem with six actions, each in the tracker; the follow-up report shows five complete after a month.

Gate: 13-165. Approval: none required

## 166
**Reliability Improvement** (complete). Purpose: turn recurring reliability problems into prioritized, owned improvements and confirm they worked.

Entry criteria: Incident, postmortem and SLO data exist for the service; Error budget status is known; Service owner is available to prioritize

Inputs: incident and postmortem actions; SLO and error-budget reports; toil and on-call load data; dependency failure history

Procedure:
1. Group incidents and alerts by cause to find the largest sources of lost reliability.
2. Estimate the budget or toil each cause consumes and the cost of fixing it.
3. Prioritize improvements with the service owner and put them in the delivery backlog with owners and dates.
4. Implement each change with a measurable target (for example fewer pages or lower failure rate).
5. After release, measure the effect against the target over a stated period.
6. Report results and drop or rework improvements that did not help.

Deliverables: reliability improvement backlog; impact estimates; before and after measurements; review report

Acceptance: Each improvement has an owner, date and measurable target Effect was measured against the target Improvements follow evidence from incidents and SLO data Ineffective changes are reviewed

Validation: Incident commander and service owner review.

- manual: compare error-budget burn for the 30 days before and after the change expect: burn decreased by the stated target or the report says it did not
- manual: confirm each improvement item has an issue id, owner and date expect: none missing

Failure modes:
- Improvements chosen by opinion | detect: No incident or SLO data cited | respond: Add the evidence or drop the item
- No measurement after release | detect: No before and after numbers | respond: Measure now; mark INCONCLUSIVE until done
- Backlog never scheduled | detect: Items older than a quarter with no owner | respond: Escalate to the service owner

ILLUSTRATIVE: Three of five last-quarter incidents came from slow retries to one dependency. The team adds a timeout and circuit breaker, and the following month's pages from that cause drop to zero.

Gate: 13-166. Approval: none required
