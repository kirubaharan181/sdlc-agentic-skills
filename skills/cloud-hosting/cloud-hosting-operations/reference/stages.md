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
**Compute Management** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**Storage Management** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

Gate: 12-143. Approval: none required

## 144
**DNS Management** (stub). Purpose: configure secure and resilient network edge routing.

Inputs: domain ownership and target topology; certificate and trust requirements; traffic and health-check profile

Procedure:
1. Verify domain/account ownership and change window.
2. Configure records, certificates, ciphers, health checks, routing and origin restrictions.
3. Validate propagation, certificate chain/expiry, redirects and failover behavior.
4. Document TTL, renewal, rollback and monitoring.

Deliverables: DNS/TLS/routing configuration; validation output; renewal and rollback runbook

Acceptance: No unexpected public exposure. Certificate chain and hostname validation pass. Failover and rollback are tested.

Validation: Network/security review.

Gate: 12-144. Approval: none required

## 145
**SSL Certificate Management** (stub). Purpose: configure secure and resilient network edge routing.

Inputs: domain ownership and target topology; certificate and trust requirements; traffic and health-check profile

Procedure:
1. Verify domain/account ownership and change window.
2. Configure records, certificates, ciphers, health checks, routing and origin restrictions.
3. Validate propagation, certificate chain/expiry, redirects and failover behavior.
4. Document TTL, renewal, rollback and monitoring.

Deliverables: DNS/TLS/routing configuration; validation output; renewal and rollback runbook

Acceptance: No unexpected public exposure. Certificate chain and hostname validation pass. Failover and rollback are tested.

Validation: Network/security review.

Gate: 12-145. Approval: none required

## 146
**Network Operations** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**Cost Optimization** (stub). Purpose: improve measured performance without violating correctness.

Inputs: baseline workload and latency profile; consistency/freshness requirements; resource and cost limits

Procedure:
1. Profile before changing code; identify dominant cost and reproducible baseline.
2. Choose cache key, TTL, invalidation and consistency behavior based on data semantics.
3. Bound memory, stampede, stale data and eviction behavior.
4. Compare before/after p50/p95/p99, throughput, error rate and cost under equivalent load.

Deliverables: profile report; optimization change; cache policy; before/after benchmark

Acceptance: Improvement is measured against baseline. Correctness and freshness invariants hold. No unbounded memory or stale-data risk is introduced.

Validation: Performance and correctness regression review.

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
