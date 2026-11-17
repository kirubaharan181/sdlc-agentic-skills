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
**Application Monitoring** (complete). Purpose: know whether the application is healthy and where it is hurting users, using signals from inside the application and from the user's side.

Entry criteria: The application is deployed with a version identifier; Logging, metrics and tracing foundations exist (stages 155-157); Key user journeys are known

Inputs: key journeys and business operations; service level objectives; application metrics and traces; release history

Procedure:
1. Define service level indicators for the key journeys, such as successful request ratio and latency under a threshold, and set objectives with error budgets.
2. Instrument application-level signals: request rate, errors by type, latency histograms, dependency calls, queue depth and business events like orders placed.
3. Alert on symptoms users feel and on fast error budget burn, with a page only when action is needed now and a ticket otherwise.
4. Tag telemetry with the release version, so a regression is tied to the change that caused it.
5. Add real user and synthetic journey monitoring to catch what server-side metrics miss.
6. Link each alert to a runbook and a dashboard, and review noisy alerts monthly to remove or tune them.

Deliverables: indicators and objectives per journey; dashboards and alerts; release-tagged telemetry; alert review record

Acceptance: Objectives exist for the key journeys Pages are tied to user impact or fast budget burn Telemetry carries the release version Each alert has a runbook

Validation: Observability owner review.

- manual: deploy a version with an injected error rate in staging and watch whether the burn-rate alert fires expect: alert fires within the configured window
- manual: sample five paging alerts from the last month and check each linked to a runbook and a real user impact expect: all do

Failure modes:
- Alert fatigue | detect: Pages that need no action | respond: Tune or demote to tickets
- Healthy metrics but unhappy users | detect: Complaints with green dashboards | respond: Add synthetic and real user checks
- Regression not tied to release | detect: Cause unclear | respond: Add version tags

ILLUSTRATIVE: Checkout has an objective of 99.5 percent success over 30 days. A fast-burn alert fires when a release raises errors, the version tag points to the culprit, and the runbook describes the rollback.

Gate: 13-153. Approval: none required

## 154
**Infrastructure Monitoring** (complete). Purpose: watch the servers, containers, clusters and cloud services under the applications, so saturation and failure are found early and tied to their cause.

Entry criteria: Infrastructure components are inventoried; Agents or exporters can be deployed; Capacity thresholds are defined (stage 161)

Inputs: infrastructure inventory; capacity thresholds; agent and exporter options; dependency map

Procedure:
1. Collect host and container metrics: CPU including steal and throttling, memory and swap, disk space, inode and I/O latency, network errors and saturation.
2. Collect orchestrator signals: pod restarts, pending pods, node conditions, resource requests and limits, and autoscaler activity.
3. Collect cloud service metrics and quota use for managed services, and alert before quotas are reached.
4. Alert on saturation trends and time-to-full forecasts, such as disks that will fill within a day, rather than only on current values.
5. Tag metrics with service, environment and owner, so alerts route to the right team and show affected applications.
6. Test that monitoring itself works: alert on missing data from the agents and on failure of the monitoring pipeline.

Deliverables: agent and exporter deployment; infrastructure dashboards; forecast-based alerts; monitoring health checks

Acceptance: Every host and cluster reports metrics Quota and time-to-full alerts exist Metrics carry owner tags Missing data raises an alert

Validation: Observability owner review.

- `promtool query instant http://prometheus:9090 'up == 0'   # example` expect: returns no unexpected targets
- manual: stop an exporter in staging expect: a missing-data alert fires

Failure modes:
- Silent agent failure | detect: Host disappears from dashboards | respond: Alert on absent metrics
- Disk full at night | detect: Alert only at 100 percent | respond: Alert on time-to-full forecast
- Container throttled | detect: Latency without high CPU | respond: Monitor throttling and limits

ILLUSTRATIVE: A forecast alert warns that a database volume fills in 18 hours at the current growth; the team expands it during working hours, and a test shows the absent-data alert fires when an exporter is stopped.

Gate: 13-154. Approval: none required

## 155
**Centralized Logging** (complete). Purpose: bring logs from every component into one place where they can be searched, correlated and kept for the right time.

Entry criteria: Services emit logs; A log platform and retention policy exist; Data protection requirements for logs are known

Inputs: services and their log formats; log platform; retention and access policy; data protection requirements

Procedure:
1. Use a structured format such as JSON with timestamp, level, service, version, environment and a correlation id on every line.
2. Ship logs from every service and infrastructure component to the central platform with the same fields.
3. Keep sensitive data out: no secrets, tokens or unnecessary personal data; mask what must appear.
4. Set retention and access by sensitivity, and keep security and audit logs longer and tamper-resistant.
5. Build saved searches for common questions and alerts for important error patterns.
6. Test that a real request can be followed across services by its correlation id.

Deliverables: log format standard; shipping configuration; retention and access rules; saved searches and a cross-service trace example

Acceptance: A request is traceable across services by one id Logs contain no secrets Retention and access follow the policy Every service ships logs with the standard fields

Validation: Observability owner and security review.

- manual: send one request and search the platform by its correlation id expect: log lines from every service on the path appear
- manual: search the platform for 'password=' and 'Authorization:' expect: no matches

Failure modes:
- Unstructured logs | detect: Searches need regular expressions | respond: Adopt a structured format
- Personal data logged | detect: Search finds email addresses | respond: Mask and shorten retention
- Logs lost under load | detect: Gaps in the timeline | respond: Add buffering and a delivery check

ILLUSTRATIVE: Each service logs JSON with a request id. Searching one request id in the platform shows the gateway, order service and payment adapter lines in order, with no card data in any line.

Gate: 13-155. Approval: none required

## 156
**Metrics Monitoring** (complete). Purpose: turn system behavior into numbers over time so trends, saturation and failure are visible before users complain.

Entry criteria: Services can expose metrics; A metrics platform exists; Service level objectives are known or being defined

Inputs: services and their key operations; metrics platform; SLOs and capacity concerns; dashboards in use

Procedure:
1. Instrument each service for the four golden signals: latency, traffic, errors and saturation.
2. Use consistent names and labels, and avoid labels with unbounded values such as user ids.
3. Collect infrastructure metrics (CPU, memory, disk, network) and dependency metrics (database, queues).
4. Build one overview dashboard per service answering 'is it healthy?' and drill-down dashboards for diagnosis.
5. Record business metrics for key flows so failures that technical metrics miss are visible.
6. Review dashboards after incidents and add the signals that would have helped.

Deliverables: instrumentation; dashboards per service; metric naming standard; post-incident improvements

Acceptance: Each service exposes the four golden signals Labels have bounded values An overview dashboard shows health at a glance Business-flow metrics exist for critical journeys

Validation: Observability owner review.

- `curl -s localhost:9100/metrics | grep -E 'http_requests_total|http_request_duration_seconds'   # example` expect: expected series are present
- manual: induce a small error rate in staging and watch the dashboard expect: the error panel shows it within the scrape interval

Failure modes:
- High-cardinality labels | detect: Metrics store grows rapidly | respond: Remove unbounded labels
- Dashboards nobody understands | detect: On-call cannot say if healthy | respond: Build a simple overview
- Only averages shown | detect: Tail latency invisible | respond: Use histograms and percentiles

ILLUSTRATIVE: The order service exposes request rate, error rate, latency histograms and queue depth. An induced error in staging appears on the overview dashboard within 30 seconds.

Gate: 13-156. Approval: none required

## 157
**Distributed Tracing** (complete). Purpose: follow a single request through many services to find where time is spent and where it fails.

Entry criteria: Services are instrumented or can be; A tracing backend exists; Context propagation standard is chosen

Inputs: service call graph; tracing backend; propagation standard; sampling policy

Procedure:
1. Adopt one propagation standard so the trace context passes through every call, including queues and background jobs.
2. Instrument inbound and outbound calls, database queries and key internal operations with meaningful span names.
3. Add useful attributes (route, status, tenant class) and keep sensitive data out of spans.
4. Set a sampling policy: always keep errors and slow requests, sample the rest, and state the cost.
5. Link traces with logs and metrics through the trace id.
6. Verify by tracing a real request across services and checking that no hop is missing.

Deliverables: instrumented services; propagation and sampling policy; trace-to-log linkage; verification trace

Acceptance: A request shows all hops, including asynchronous ones Errors and slow requests are always retained Spans contain no sensitive data Trace ids appear in logs

Validation: Observability owner review.

- manual: send one request and open its trace expect: spans for gateway, services and database appear in order
- manual: search a log line by the trace id from that request expect: matching log lines found

Failure modes:
- Broken trace at a queue | detect: Spans end at the producer | respond: Propagate context in message headers
- Sampling drops the failures | detect: Errors missing from traces | respond: Always sample errors
- Sensitive values in spans | detect: Attributes contain tokens | respond: Remove and review the instrumentation

ILLUSTRATIVE: A checkout request traces through the gateway, order service, payment adapter and database. The trace shows 800 of 950 ms spent waiting on the payment provider, and the trace id links to the log lines of each service.

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
**Uptime Monitoring** (complete). Purpose: detect outages from outside the system as a user would, and notify the right people with a trustworthy status.

Entry criteria: Public and critical endpoints are listed; A monitoring service reaching from outside exists; An on-call and status process exists

Inputs: endpoint list with expected behavior; regions of users; on-call schedule; status page

Procedure:
1. Probe each critical endpoint from several regions outside your network, checking status code, response content and latency, not only that the port is open.
2. Add checks for the full journey where possible, such as sign-in and a read operation, using a dedicated test account.
3. Require several consecutive failures from more than one location before alerting, to avoid false alarms from single probe faults.
4. Page the on-call person with the endpoint, region and first failing time, and update the status page from a verified fault.
5. Also monitor the monitor: a second independent checker or a heartbeat that fires when probes stop reporting.
6. Calculate uptime from probe data with a stated method, and review misses and false alarms monthly.

Deliverables: probe configuration and journeys; alert rules with confirmation logic; status page process; uptime reports with method

Acceptance: Probes run from several outside locations Alerts need confirmation across probes Monitoring has its own heartbeat Uptime states how it is calculated

Validation: Observability owner review.

- `curl -s -o /dev/null -w '%{http_code} %{time_total}\n' https://app.example.com/health   # example from outside the network` expect: expected code within the latency target
- manual: block the endpoint in staging for five minutes expect: alert fires after the confirmation count and the status process is followed

Failure modes:
- False alarms from one probe | detect: Pages with no outage | respond: Require multi-location confirmation
- Port open but app broken | detect: Probe is green during outage | respond: Check content and journey
- Monitor fails silently | detect: No alert during outage | respond: Add heartbeat and second checker

ILLUSTRATIVE: Three regions probe the sign-in journey every minute; two consecutive failures from two regions page on-call, and a dead-man heartbeat from the probe service alerts if reports stop for five minutes.

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
**Capacity Planning** (complete). Purpose: make sure the system has the capacity it will need before demand arrives, at a cost the business accepts.

Entry criteria: Demand forecasts or growth data exist; Current utilization and performance data exist; Capacity limits of the system are known (stage 92)

Inputs: demand history and forecast; utilization and performance data; known capacity limits; lead times and budgets

Procedure:
1. Collect demand and utilization trends and the business events that will change them (launches, campaigns, seasons).
2. Convert forecast demand into resource needs using measured capacity per unit, with a stated safety margin.
3. Find the first resource to run out for each scenario and the lead time to add more.
4. Decide actions with owners and dates: scale, optimize, order, or accept risk; compare cost options.
5. Alert when utilization approaches the planning threshold, with enough warning for the lead time.
6. Review forecast against actuals each period and correct the model.

Deliverables: capacity plan with scenarios; first-limit analysis; actions with owners and dates; forecast accuracy review

Acceptance: Each scenario names the first resource to run out Safety margin and lead times are stated Actions have owners and dates Forecast accuracy is reviewed

Validation: Service owner and finance review of the plan.

- manual: compare last quarter's forecast with actual peak load expect: difference recorded with its cause
- manual: check each alert threshold leaves time for the lead time to add capacity expect: yes for every resource

Failure modes:
- Forecast ignores planned events | detect: Campaign doubles traffic unexpectedly | respond: Add events to the model
- Lead time overlooked | detect: Capacity arrives after the peak | respond: Alert earlier or reserve in advance
- Over-provisioning | detect: Utilization far below plan | respond: Right-size and set review

ILLUSTRATIVE: Peak traffic is forecast to rise 40 percent for the holiday season. Load tests show the database saturates first; the plan adds a read replica two weeks before and sets an alert at 70 percent database CPU.

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
