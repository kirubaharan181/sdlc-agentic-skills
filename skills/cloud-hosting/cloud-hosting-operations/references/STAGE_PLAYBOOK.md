# Cloud and infrastructure operations — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 140. Cloud Hosting

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 141. Compute Management

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 142. Database Hosting

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 143. Storage Management

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 144. DNS Management

**Purpose:** configure secure and resilient network edge routing

**Procedure:**
- Verify domain/account ownership and change window.
- Configure records, certificates, ciphers, health checks, routing and origin restrictions.
- Validate propagation, certificate chain/expiry, redirects and failover behavior.
- Document TTL, renewal, rollback and monitoring.

**Inputs:** domain ownership and target topology, certificate and trust requirements, traffic and health-check profile
**Artifact:** DNS/TLS/routing configuration
**Verification:** Network/security review.
**Handoff:** Transfer DNS/TLS/routing configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 145. SSL Certificate Management

**Purpose:** configure secure and resilient network edge routing

**Procedure:**
- Verify domain/account ownership and change window.
- Configure records, certificates, ciphers, health checks, routing and origin restrictions.
- Validate propagation, certificate chain/expiry, redirects and failover behavior.
- Document TTL, renewal, rollback and monitoring.

**Inputs:** domain ownership and target topology, certificate and trust requirements, traffic and health-check profile
**Artifact:** DNS/TLS/routing configuration
**Verification:** Network/security review.
**Handoff:** Transfer DNS/TLS/routing configuration with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 146. Network Operations

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 147. Backup Management

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 148. Disaster Recovery

**Purpose:** restore critical services within approved recovery objectives

**Procedure:**
- Confirm business-approved RTO/RPO for each critical service and data set.
- Prepare an isolated recovery environment with scoped credentials and network boundaries.
- Restore or fail over in dependency order and capture actual recovery time and replication position.
- Validate data integrity and user-facing journeys before reopening traffic; record gaps.

**Inputs:** business impact analysis and service dependencies, approved RTO/RPO and recovery runbooks, isolated recovery credentials and backup inventory
**Artifact:** recovery plan
**Verification:** Run a timed recovery exercise and compare measured RTO/RPO with approved objectives.
**Handoff:** Transfer recovery plan with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 149. High Availability

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 150. Auto Scaling

**Purpose:** assess dependency vulnerabilities and license obligations

**Procedure:**
- Generate inventory from resolved direct and transitive dependencies.
- Match versions to advisories and assess reachability, exploitability and vendor support.
- Review license compatibility, provenance and required notices.
- Upgrade or replace affected components, rerun regression/security checks and compare SBOM.

**Inputs:** resolved lockfiles and packaged artifact, SBOM and advisory feeds, license policy and runtime exposure
**Artifact:** SBOM
**Verification:** Compare lockfile and packaged SBOM, then verify the resolved version and notices.
**Handoff:** Transfer SBOM with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 151. Cost Optimization

**Purpose:** improve measured performance without violating correctness

**Procedure:**
- Profile before changing code; identify dominant cost and reproducible baseline.
- Choose cache key, TTL, invalidation and consistency behavior based on data semantics.
- Bound memory, stampede, stale data and eviction behavior.
- Compare before/after p50/p95/p99, throughput, error rate and cost under equivalent load.

**Inputs:** baseline workload and latency profile, consistency/freshness requirements, resource and cost limits
**Artifact:** profile report
**Verification:** Performance and correctness regression review.
**Handoff:** Transfer profile report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 152. Infrastructure Maintenance

**Purpose:** operate cloud infrastructure within reliability and cost objectives

**Procedure:**
- Inspect actual resource configuration, dependencies, quotas and recent changes before modifying.
- Verify identity boundaries, encryption, network exposure, patch state and backup coverage.
- Measure health, capacity, utilization, recovery readiness and cost allocation.
- Apply a reviewed, reversible change and verify telemetry, drift and customer impact.

**Inputs:** service inventory and ownership, SLO/RTO/RPO and capacity profile, access, backup and cost policies
**Artifact:** infrastructure inventory
**Verification:** Cloud operations and security review.
**Handoff:** Transfer infrastructure inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
