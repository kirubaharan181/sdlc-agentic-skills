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
**Disaster Recovery** (stub). Purpose: restore critical services within approved recovery objectives.

Inputs: business impact analysis and service dependencies; approved RTO/RPO and recovery runbooks; isolated recovery credentials and backup inventory

Procedure:
1. Confirm business-approved RTO/RPO for each critical service and data set.
2. Prepare an isolated recovery environment with scoped credentials and network boundaries.
3. Restore or fail over in dependency order and capture actual recovery time and replication position.
4. Validate data integrity and user-facing journeys before reopening traffic; record gaps.

Deliverables: recovery plan; restore/failover execution log; integrity and application validation; RTO/RPO gap report

Acceptance: Actual recovery time and data loss are measured. Recovery environment is isolated and access audited. Business owners accept restored data and service state.

Validation: Run a timed recovery exercise and compare measured RTO/RPO with approved objectives.
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
**Auto Scaling** (stub). Purpose: assess dependency vulnerabilities and license obligations.

Inputs: resolved lockfiles and packaged artifact; SBOM and advisory feeds; license policy and runtime exposure

Procedure:
1. Generate inventory from resolved direct and transitive dependencies.
2. Match versions to advisories and assess reachability, exploitability and vendor support.
3. Review license compatibility, provenance and required notices.
4. Upgrade or replace affected components, rerun regression/security checks and compare SBOM.

Deliverables: SBOM; vulnerability and license disposition; dependency update diff; retest report

Acceptance: All shipped components have known versions and license status. Critical exposure is fixed or formally accepted. Packaged artifact matches scanned dependency tree.

Validation: Compare lockfile and packaged SBOM, then verify the resolved version and notices.
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
