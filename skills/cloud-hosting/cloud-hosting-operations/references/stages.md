# Cloud and infrastructure operations: stage reference

## Contents
- [140 Cloud Hosting](#140)
- [141 Compute Management](#141)
- [142 Database Hosting](#142)
- [143 Storage Management](#143)
- [144 DNS Management](#144)
- [145 SSL Certificate Management](#145)
- [146 Network Operations](#146)
- [147 Backup Management](#147)
- [148 Disaster Recovery](#148)
- [149 High Availability](#149)
- [150 Auto Scaling](#150)
- [151 Cost Optimization](#151)
- [152 Infrastructure Maintenance](#152)

## 140
**Cloud Hosting** (complete). Purpose: run workloads on cloud accounts and services that are organized, secured and cost-aware from the start.

Entry criteria: Cloud provider and account structure decisions exist; Workload requirements and environments are known; Identity provider and billing ownership are defined

Inputs: workload requirements; environment list; organization and identity design; budget

Procedure:
1. Separate accounts or projects by environment and by risk; production is isolated from the others.
2. Federate identity, use roles with least privilege, and disable long-lived user keys.
3. Set guardrails: allowed regions and services, mandatory encryption, logging to a separate account, and budget alerts.
4. Provision the hosting resources from code, tagged with owner, environment and cost center.
5. Enable audit logging and threat-detection services and route alerts to the on-call team.
6. Review cost and access monthly and remove unused resources.

Deliverables: account structure; guardrail policies; provisioning code with tags; cost and access review

Acceptance: Production is isolated from other environments No long-lived access keys for people Audit logging is on and centralized Budget alerts exist and resources carry owner tags

Validation: Cloud owner and security review.

- `aws iam list-users --query 'Users[].UserName'   # example; expect no routine human IAM users` expect: empty or only break-glass accounts
- manual: list resources without an owner tag expect: none

Failure modes:
- Shared account for all environments | detect: Test and production resources together | respond: Split accounts
- Unused resources keep billing | detect: Cost report shows idle resources | respond: Remove or schedule shutdown
- Logging disabled | detect: No audit trail for a change | respond: Enable and centralize

ILLUSTRATIVE: Production runs in its own account reached only by federated roles, audit logs flow to a security account, and a monthly review removes two idle databases.

Gate: 12-140. Approval: none required

## 141
**Compute Management** (complete). Purpose: manage virtual machines, containers and functions so capacity matches demand, patches are applied, and every resource has an owner and a purpose.

Entry criteria: Cloud accounts and an inventory source exist; Tagging standard exists; Patch and image policies are defined

Inputs: resource inventory; tagging and ownership standard; utilization metrics; patch and image policy

Procedure:
1. Create compute only from code (infrastructure as code) and from approved, patched base images, with required tags for owner, environment and cost centre.
2. Right-size using measured CPU, memory and network utilization over at least two weeks, and choose scaling policies with tested limits.
3. Patch by replacing instances with new images through the pipeline rather than patching in place, and track images older than the policy.
4. Harden: no public administrative ports, instance roles with least privilege, and no long-lived credentials on instances.
5. Find and remove idle, orphaned and untagged resources through a scheduled report and an owner confirmation step.
6. Test scaling and replacement under load, and record the time to replace a failed instance.

Deliverables: compute defined as code; image and patch status report; right-sizing and idle resource report; scaling and replacement test results

Acceptance: Compute comes from code and approved images Every resource has an owner tag Images are within the patch policy Idle resources are reviewed

Validation: Cloud engineer review.

- `aws ec2 describe-instances --query 'Reservations[].Instances[?!not_null(Tags[?Key==`owner`])].InstanceId' --output text   # example` expect: no untagged instances
- manual: list instances launched from images older than the policy age expect: none, or each has an exception

Failure modes:
- Manual instance changes | detect: Drift from code | respond: Detect drift and reapply code
- Over-provisioned fleet | detect: CPU under 10 percent for weeks | respond: Right-size
- Old images in use | detect: Patch policy exceeded | respond: Rebuild and roll

ILLUSTRATIVE: An inventory report finds 14 untagged instances; owners claim nine, and five idle ones are stopped after confirmation. The fleet moves to a new base image through a rolling replacement, and the old image is retired.

Gate: 12-141. Approval: none required

## 142
**Database Hosting** (complete). Purpose: run production databases on infrastructure that meets availability, performance, security and recovery needs.

Entry criteria: Database engine, size and recovery objectives are decided; Network and access design exists; Backup approach is agreed (stage 147)

Inputs: recovery and availability objectives; workload profile; network and security requirements; cost limits

Procedure:
1. Choose managed or self-managed hosting from objectives, skills and cost; write the reasons down.
2. Provision from code with encryption at rest and in transit, private networking and least-privilege access.
3. Configure high availability and replicas to meet the objective and test a failover.
4. Configure monitoring for capacity, replication lag, connections and slow queries, with alerts.
5. Set up patching and maintenance windows and confirm backups restore.
6. Document the connection method, limits and runbooks.

Deliverables: hosting design and rationale; provisioning code; failover test results; monitoring and runbooks

Acceptance: Encryption and private networking are in place Failover was tested against the objective Monitoring and alerts cover capacity and replication Restore from backup was verified

Validation: Database administrator and security review.

- `terraform plan -detailed-exitcode   # example; exit 0 after apply` expect: no drift
- manual: trigger a failover in a non-production copy and time it expect: within the recovery time objective

Failure modes:
- Database reachable from the internet | detect: Public endpoint enabled | respond: Move to private networking
- HA configured but never tested | detect: No failover record | respond: Test it
- Capacity alert missing | detect: Disk fills unnoticed | respond: Add alerts with headroom

ILLUSTRATIVE: A managed PostgreSQL cluster with one replica in another zone is provisioned from code, reachable only from the application subnet, with alerts for replication lag; a failover test completes in 40 seconds.

Gate: 12-142. Approval: none required

## 143
**Storage Management** (complete). Purpose: manage storage so data is durable, access is controlled, cost matches use, and capacity never surprises anyone.

Entry criteria: Storage services and data owners are inventoried; Data classification exists; Retention rules exist

Inputs: storage inventory; classification and retention rules; usage and growth data; access policies

Procedure:
1. Match storage type to need (block, file, object) and class to access pattern, with lifecycle rules that move or expire data.
2. Block public access by default, use policies tied to roles, and review access on a schedule.
3. Enable encryption at rest with managed keys, and versioning or object lock where recovery or immutability is needed.
4. Set backup or replication for important data, and test restoring a sample.
5. Monitor capacity growth and set alerts with enough lead time to act, and forecast from the trend.
6. Report cost per data owner, and remove abandoned volumes, snapshots and buckets after owner confirmation.

Deliverables: storage inventory with owners and classes; lifecycle and access policies; restore test record; capacity forecast and cost report

Acceptance: No storage is publicly accessible unless approved Lifecycle rules exist for data with retention limits Restores were tested Growth alerts give action lead time

Validation: Cloud engineer and data owner review.

- `aws s3api get-public-access-block --bucket <bucket>   # example` expect: all four blocks are true
- manual: restore ten objects or one volume snapshot from backup and compare checksums expect: identical

Failure modes:
- Public bucket | detect: Anonymous access found | respond: Block and review the cause
- Orphan snapshots accumulate | detect: Cost rises without owner | respond: Report and delete with confirmation
- Disk fills unexpectedly | detect: Alert fires late | respond: Alert on growth rate and forecast

ILLUSTRATIVE: A lifecycle rule moves log objects to a colder class after 30 days and deletes them at 400 days per policy; a monthly report lists 22 orphaned snapshots, 19 deleted after confirmation, and a restore of a sample volume matches checksums.

Gate: 12-143. Approval: none required

## 144
**DNS Management** (complete). Purpose: keep name resolution reliable and secure through controlled day-to-day changes and monitoring.

Entry criteria: DNS zones and records are inventoried (stage 134); Change process and access controls exist; Monitoring of resolution is available

Inputs: DNS zone files and inventory; change requests; resolution monitoring; provider and registrar access controls

Procedure:
1. Handle each record change as a reviewed change in code with the requester, reason and ticket recorded.
2. Check the impact before the change: who depends on the name, TTL and propagation, and rollback.
3. Apply the change and verify from several networks and resolvers, not only from the office.
4. Monitor resolution time and failures, and alert when the authoritative servers or records misbehave.
5. Audit records regularly for stale, duplicate and dangling entries and remove them.
6. Test the recovery path: restoring zones from version control or backup.

Deliverables: change records; verification results; monitoring and alerts; audit findings and cleanup

Acceptance: Every change is traceable to a request and reviewed Verification was done from multiple resolvers Stale and dangling records are removed Zone restore was tested

Validation: Network owner review of changes.

- `for r in one.one.one.one dns.google dns9.quad9.net; do dig @$r +short app.example.com; done   # example` expect: all resolvers return the intended answer
- manual: restore the zone from version control into a test zone and compare expect: records identical

Failure modes:
- Change breaks resolution | detect: Failure in monitoring after change | respond: Roll back from version control
- Stale record points to released infrastructure | detect: Audit finds dangling entry | respond: Remove it
- One resolver tested only | detect: Different answers elsewhere | respond: Verify from several resolvers

ILLUSTRATIVE: A request to move a service to a new address is applied through a reviewed change, the TTL is lowered a day before, and three public resolvers return the new address within the TTL; the old record is removed after a week.

Gate: 12-144. Approval: none required

## 145
**SSL Certificate Management** (complete). Purpose: keep every certificate valid, inventoried and renewed on time, so no outage is caused by an expiry.

Entry criteria: TLS is in use on several endpoints (stage 135); A certificate inventory source exists or can be built; Owners for endpoints are known

Inputs: certificate inventory; issuance and renewal automation; monitoring and alerting; endpoint owners

Procedure:
1. Discover certificates from the authorities, load balancers, clusters and by scanning your address ranges, and record issuer, names, expiry, owner and where installed.
2. Automate renewal wherever possible, and track the exceptions that need manual steps with an owner and a calendar date.
3. Monitor expiry from outside, and alert at several stages (for example 30, 14 and 7 days) to different recipients with escalation.
4. Check the renewal result by confirming the new certificate is served, not only that issuance succeeded.
5. Revoke and replace when a key is exposed or a name is retired, and remove retired certificates from the inventory.
6. Practise the emergency replacement of an expired certificate and record the time it takes.

Deliverables: certificate inventory with owners; renewal automation and exceptions list; expiry monitoring and alerts; emergency replacement drill record

Acceptance: Every certificate has an owner and an expiry date in the inventory Alerts run at several stages with escalation Renewal is verified by what is served Manual exceptions have calendar dates

Validation: Cloud engineer review.

- `echo | openssl s_client -connect app.example.com:443 -servername app.example.com 2>/dev/null | openssl x509 -noout -enddate   # example` expect: expiry is later than the alert threshold
- manual: compare the inventory with a scan of the address ranges expect: no certificate found that is not in the inventory

Failure modes:
- Certificate expires unnoticed | detect: Clients receive errors | respond: Replace now and add the alert
- Renewal succeeded but old certificate is served | detect: Expiry date unchanged | respond: Reload the service and add a verification step
- Unknown certificate found | detect: Scan finds one not in inventory | respond: Find owner and register or remove

ILLUSTRATIVE: A weekly scan finds a certificate on a forgotten admin host with 19 days left; the owner is identified, it is moved to automated issuance, and a monitor now alerts at 30, 14 and 7 days.

Gate: 12-145. Approval: none required

## 146
**Network Operations** (complete). Purpose: operate the network day to day so it stays available, capacity is known, changes are safe and faults are found before users report them.

Entry criteria: Network devices and links are inventoried; Monitoring covers devices and links; A change process exists (stage 44)

Inputs: network inventory and diagrams; device and link telemetry; configuration backups; change calendar

Procedure:
1. Collect link utilization, errors, discards, latency, packet loss and device health, and alert on sustained thresholds and on loss of redundancy, not only on total failure.
2. Back up device configurations automatically after each change, and compare running with the approved configuration to detect drift.
3. Make changes through reviewed configuration as code or templates, test in a lab or with a dry run, and prepare a rollback.
4. Verify redundancy by testing failover of links and devices in a window, and measure convergence time.
5. Review capacity monthly against growth, and plan upgrades before utilization passes the planning threshold.
6. Run a security hygiene check: management access limited and logged, unused ports disabled, firmware within support, and access lists reviewed.

Deliverables: monitoring and alert configuration; configuration backups and drift reports; failover test results; capacity and hygiene reports

Acceptance: Configuration drift is detected Failover was tested and timed Capacity is reviewed with a plan Management access is restricted and logged

Validation: Network owner review.

- manual: diff each device's running configuration with its approved version expect: no unexplained difference
- manual: disable one uplink in a window and measure time to reconverge expect: within the agreed time with no lasting loss

Failure modes:
- Redundant link down unnoticed | detect: Single point of failure for weeks | respond: Alert on lost redundancy
- Config change not backed up | detect: Cannot restore after failure | respond: Automate backup on change
- Errors rising on an interface | detect: Rising discard counter | respond: Investigate cable, optics or duplex mismatch

ILLUSTRATIVE: Drift detection finds one switch with a manual change to a VLAN; it is reverted from the approved template. A failover test of the primary uplink reconverges in 3 seconds with no lasting loss.

Gate: 12-146. Approval: none required

## 147
**Backup Management** (complete). Purpose: make sure data can be restored when needed, by taking backups on schedule and proving they restore.

Entry criteria: Data stores and their recovery objectives are listed; Backup tooling and storage are available; Retention and encryption requirements are known

Inputs: list of data stores and criticality; recovery point and time objectives; backup configuration; retention and encryption policy

Procedure:
1. Configure backups per data store to meet the recovery point objective; encrypt them and store a copy in a separate failure domain.
2. Monitor each backup job and alert on failure or missing runs.
3. Restore a recent backup into an isolated environment on a schedule and verify the data.
4. Record restore time and compare it with the recovery time objective.
5. Enforce retention and deletion rules, including legal and privacy requirements.
6. Report failures and restore-test results to the data owner.

Deliverables: backup configuration; job monitoring and alerts; restore test reports; retention evidence

Acceptance: Every critical store has a backup that meets the recovery point objective A restore test succeeded within the recovery time objective Backups are encrypted and stored in a separate failure domain Failures alert someone

Validation: Database administrator and data owner review of restore results.

- manual: restore last night's backup into an isolated environment and run row-count and integrity checks expect: restore succeeded; time recorded; checks pass
- manual: list backup jobs that did not run in the last 7 days expect: none, or each has a ticket

Failure modes:
- Backups never restored | detect: No restore test record | respond: Run a restore test now
- Backup job silently failing | detect: Missing runs without an alert | respond: Add monitoring and alert
- Backups in the same failure domain | detect: Copy only in the primary region or account | respond: Add a separate copy

ILLUSTRATIVE: A monthly restore of the orders database into a sandbox takes 22 minutes against a 60-minute objective, and checksums of key tables match production at the backup time.

Gate: 12-147. Approval: none required

## 148
**Disaster Recovery** (complete). Purpose: make sure the service can be restored after a major loss, within agreed recovery time and data-loss limits, and prove it.

Entry criteria: Recovery time objective and recovery point objective are agreed for the service; Backups or replicas exist; DR owner is named

Inputs: RTO and RPO targets; architecture and dependencies; backup and replication configuration; recovery runbook

Procedure:
1. Identify critical components and their dependencies; define recovery order.
2. Document and automate recovery steps where possible; keep the runbook current.
3. Run a recovery exercise in an isolated environment or a controlled production test; record recovery time and data-loss window.
4. Compare measured RTO and RPO with the targets; list gaps.
5. Fix gaps or get the DR owner to accept the risk with an expiry.
6. Schedule the next exercise and record results.

Deliverables: DR plan and runbook; exercise report with measured RTO and RPO; gap list; risk acceptance

Acceptance: Measured RTO and RPO meet targets or gaps are accepted Runbook worked as written or was corrected Backup restore was verified DR owner approved the result

Validation: DR-owner approval after a recorded exercise.

- manual: restore the latest backup into an isolated environment and time it expect: restore time recorded; data validated
- manual: compare newest restored record timestamp with the failure time expect: difference is within the RPO

Failure modes:
- Backups never restored | detect: No restore test record | respond: Run a restore test before approval
- Runbook outdated | detect: Steps fail during exercise | respond: Update and rerun
- RTO exceeded | detect: Measured time above target | respond: Improve or formally accept the gap

ILLUSTRATIVE: A regional failover exercise restores the database in 18 minutes with 40 seconds of data loss against targets of 30 minutes and 5 minutes; one runbook step is corrected.

Gate: 12-148. Approval: dr-owner (always)

## 149
**High Availability** (complete). Purpose: keep the service available through the failure of a component, zone or dependency, by design.

Entry criteria: Availability objective is stated; Architecture and dependency map exist; Failure domains (zones, regions, accounts) are known

Inputs: availability objective; architecture and dependency map; failure domains; traffic and data characteristics

Procedure:
1. Identify single points of failure across compute, data, network and dependencies.
2. Remove them with redundancy across failure domains, health checks and automatic failover where the objective needs it.
3. Design state handling: replication mode, consistency and the data-loss window on failover.
4. Test failover by removing a component or zone in a safe environment and measure the user impact and time.
5. Document degraded modes and what the service does when a dependency is down.
6. Review the design when dependencies or load change.

Deliverables: high-availability design; failover test results; degraded-mode description; single-point-of-failure list with status

Acceptance: No unmitigated single point of failure remains or each is accepted Failover was tested and timed Degraded behavior is documented Design meets the availability objective

Validation: Cloud architect and service owner review.

- manual: terminate one instance in a non-production zone and watch the service expect: traffic continues; failover time recorded
- manual: list components with a single instance or a single zone expect: each has mitigation or accepted risk

Failure modes:
- Redundancy exists but failover untested | detect: No failover test record | respond: Test before relying on it
- Hidden single dependency | detect: Outage in one shared service takes everything down | respond: Add it to the map and mitigate
- Replication loses data on failover | detect: Data gap after a test | respond: Change replication mode or accept the window explicitly

ILLUSTRATIVE: A service runs in three zones behind health-checked load balancing. Removing one zone in a test keeps error rate under one percent and p95 latency stays within the objective.

Gate: 12-149. Approval: none required

## 150
**Auto Scaling** (complete). Purpose: make capacity follow demand automatically within limits, so users keep their performance and cost stays bounded.

Entry criteria: Load profile and performance objectives are known; Metrics for utilization and latency are available; Minimum and maximum capacity limits are agreed with the owner

Inputs: traffic and load profile; performance objectives; utilization and latency metrics; cost limits

Procedure:
1. Choose scaling signals that track user demand (requests, queue depth, latency) rather than only CPU.
2. Set minimum, maximum and scaling step values from load-test results, and record why each was chosen.
3. Set cooldowns and scale-in protection so capacity does not oscillate or drop sessions.
4. Load test with a rising and a spiking pattern; record time to add capacity and user-facing impact.
5. Alert on hitting the maximum, on scaling failures and on cost against budget.
6. Review scaling events monthly and adjust limits.

Deliverables: autoscaling configuration with rationale; load test results; alerts for limits and failures; scaling review notes

Acceptance: Latency objective holds during the tested ramp and spike Minimum and maximum limits are justified Alerts exist for max reached and scaling failure Cost is within the agreed bound

Validation: Service owner and performance engineer review of load-test results.

- `k6 run --vus 200 --duration 10m loadtest/ramp.js   # example` expect: latency and error thresholds pass; instance count rises as expected
- `kubectl get hpa app -o wide   # example` expect: current replicas between configured minimum and maximum

Failure modes:
- Scaling is too slow for a spike | detect: Latency exceeds objective during the spike | respond: Raise minimum, scale on an earlier signal or pre-warm
- Oscillation | detect: Replica count repeatedly goes up and down | respond: Lengthen cooldown and widen thresholds
- Runaway cost | detect: Capacity stays at maximum with no demand | respond: Investigate the signal and cap with an alert

ILLUSTRATIVE: A service scales on queue depth with a minimum of 3 and a maximum of 20 replicas. A spike test adds capacity within two minutes and keeps p95 latency under the objective.

Gate: 12-150. Approval: none required

## 151
**Cost Optimization** (complete). Purpose: keep cloud spend aligned with value by finding waste, committing where it is safe and making each team accountable for what it spends.

Entry criteria: Cost and usage data with tags is available; Resource owners are known; A budget or target exists

Inputs: billing and usage data; resource tags and owners; utilization metrics; budgets and forecasts

Procedure:
1. Allocate cost to teams and products using tags and account structure, and fix untagged spend first because it cannot be managed.
2. Find waste: idle and orphaned resources, over-sized instances, unattached storage, excessive data transfer and over-retained logs and snapshots.
3. Right-size and schedule non-production resources off outside working hours, based on measured utilization and with owner confirmation.
4. Consider commitments (reserved or savings plans) only for steady baseline usage, and size them from observed minimum usage, not peak.
5. Estimate savings per action with the assumptions, and rank by saving and effort; changes with risk to availability need the service owner's approval.
6. Track realized savings against estimates monthly, and report unit cost (cost per transaction or customer), not only total cost.

Deliverables: cost allocation report; optimization actions with estimates and owners; commitment analysis; realized savings report and unit cost

Acceptance: Untagged spend is reported and shrinking Commitments are sized from baseline usage Each action has an owner and an estimate Realized savings are compared with estimates

Validation: Named budget owner approves commitments and risky changes.

- manual: compare the sum of allocated cost with the invoice total expect: difference under the agreed tolerance
- manual: after each action, compare spend for the affected resources for 30 days before and after expect: saving reported with the dates

Failure modes:
- Commitment too large | detect: Unused commitment each month | respond: Size to the baseline and review quarterly
- Right-sizing causes slowdowns | detect: Latency alerts after change | respond: Roll back and size with peak data
- Savings never verified | detect: Estimates not compared with bills | respond: Track realized savings

ILLUSTRATIVE: Non-production environments are scheduled off at night and weekends, saving an estimated 40 percent of their cost; a savings plan is bought for the minimum steady compute observed over three months, and the bill is compared 30 days later.

Gate: 12-151. Approval: finops-owner (when resizing, deleting or committing spend on billing-sensitive resources)

## 152
**Infrastructure Maintenance** (complete). Purpose: keep servers, networks and platform components patched, supported and healthy through planned changes.

Entry criteria: Inventory of infrastructure and versions exists; Maintenance windows and owners are defined; Rollback or replacement approach is known

Inputs: infrastructure inventory with versions; vendor advisories and end-of-support dates; maintenance windows; monitoring

Procedure:
1. Review the inventory for items with security patches due, nearing end of support or showing health problems.
2. Plan the change: scope, order, window, communication and rollback; roll out to non-production first.
3. Apply changes in small batches using automation, with health checks between batches.
4. Verify service health and capacity afterward and compare with the baseline.
5. Update the inventory and retire items that are out of support.
6. Record the work, exceptions and the next planned maintenance.

Deliverables: maintenance plan; change execution log; post-change verification; updated inventory

Acceptance: Security patches are applied within the agreed time or excepted Rollout was staged with health checks Inventory reflects the new versions Exceptions have an owner and an expiry

Validation: Platform owner review of the results.

- `kubectl get nodes -o wide   # example; use the platform's inventory command` expect: all nodes at the target version and Ready
- manual: list inventory items past end of support expect: none without an exception or retirement plan

Failure modes:
- Batch patch breaks service | detect: Health checks fail mid-rollout | respond: Stop, roll back the batch, and fix before continuing
- Unsupported systems ignored | detect: Items past end of support without plan | respond: Schedule retirement or accept risk with expiry
- Inventory out of date | detect: Versions differ from reality | respond: Reconcile from automation output

ILLUSTRATIVE: Nodes are upgraded in batches of two with a health check between batches; one node fails its check and is replaced, and the inventory is updated to the new versions.

Gate: 12-152. Approval: none required
