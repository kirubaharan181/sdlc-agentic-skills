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
**Cloud Hosting** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**Database Hosting** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**Backup Management** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**High Availability** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

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
**Infrastructure Maintenance** (stub). Purpose: operate cloud infrastructure within reliability and cost objectives.

Inputs: service inventory and ownership; SLO/RTO/RPO and capacity profile; access, backup and cost policies

Procedure:
1. Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
2. Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
3. Measure health, capacity, utilization, recovery readiness and cost allocation.
4. Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

Deliverables: infrastructure inventory; change record; health/capacity/cost evidence; operator runbook

Acceptance: Changes are scoped and reversible. Backup/recovery meets stated objectives. Cost and reliability effects are measured.

Validation: Cloud operations and security review.

Gate: 12-152. Approval: none required
