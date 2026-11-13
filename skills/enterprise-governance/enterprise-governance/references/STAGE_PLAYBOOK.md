# Enterprise engineering governance — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 181. Engineering Governance

**Purpose:** govern repository controls, engineering standards and exception lifecycle

**Procedure:**
- Map branch protections, code owners, required checks and contribution policy to each repository.
- Sample actual repository settings and verify enforcement rather than relying on documentation.
- Review onboarding, toolchain support, secrets and change exceptions.
- Track drift and verify corrective actions across repositories.

**Inputs:** repository inventory and ownership, engineering policy and required checks, team onboarding and exception records
**Artifact:** repository control inventory
**Verification:** Repository policy sample audit.
**Handoff:** Transfer repository control inventory with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 182. Quality Governance

**Purpose:** govern quality policy, evidence and corrective action across teams

**Procedure:**
- Define measurable quality objectives, required evidence and ownership.
- Sample delivery records and verify controls operate as documented.
- Analyze defects, escaped issues, test gaps and corrective-action trends.
- Assign systemic improvements and verify effectiveness over a review period.

**Inputs:** quality policy and objectives, process/product quality data, control owners and audit period
**Artifact:** quality policy and control map
**Verification:** Quality governance review and sample audit.
**Handoff:** Transfer quality policy and control map with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 183. Security Governance

**Purpose:** govern security policy, risk acceptance and control effectiveness

**Procedure:**
- Map security obligations to preventive, detective and recovery controls.
- Review control operation, access, vulnerabilities and incident trends.
- Approve or route exceptions with compensating controls, owner and expiry.
- Report material risk and verify remediation closure.

**Inputs:** security policy and risk appetite, asset/control ownership, risk and exception register
**Artifact:** security control matrix
**Verification:** Security governance council review.
**Handoff:** Transfer security control matrix with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 184. Access Governance

**Purpose:** govern identity lifecycle and privileged access

**Procedure:**
- Review role definitions, segregation conflicts and least-privilege mappings.
- Sample access grants, changes, recertifications and removals against approvals.
- Identify dormant, orphaned, excessive and shared privileged accounts.
- Track remediation and verify timely revocation and periodic recertification.

**Inputs:** identity inventory and role model, joiner/mover/leaver events, privileged access policy
**Artifact:** role/access matrix
**Verification:** Independent access recertification audit.
**Handoff:** Transfer role/access matrix with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 185. Compliance Auditing

**Purpose:** review contractual and regulatory obligations before commitment

**Procedure:**
- Identify service, data, security, availability, audit, retention, subcontracting and exit obligations.
- Map each obligation to an internal control owner and evidence source.
- Flag ambiguous liability, data processing, IP, jurisdiction, renewal and termination terms.
- Record legal review questions and do not provide legal approval outside delegated authority.

**Inputs:** contract version and counterparties, applicable policy/control obligations, legal/compliance owner
**Artifact:** obligation matrix
**Verification:** Legal and compliance owner sign-off.
**Handoff:** Transfer obligation matrix with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 186. Documentation Governance

**Purpose:** control documentation accuracy, ownership and lifecycle

**Procedure:**
- Inventory authoritative documents, audience, version and source of truth.
- Check accuracy against current implementation, policy and approved decisions.
- Review access, retention, link integrity and stale/duplicate content.
- Assign owner and review date; archive superseded material according to policy.

**Inputs:** document inventory and classification, owners and review cadence, retention and publication policy
**Artifact:** document register
**Verification:** Documentation governance sample review.
**Handoff:** Transfer document register with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 187. Change Governance

**Purpose:** govern the portfolio of material engineering changes

**Procedure:**
- Classify normal, standard and emergency changes under policy.
- Review impact, approvals, segregation, schedule and recovery readiness.
- Sample completed changes for evidence, unauthorized drift and failed outcomes.
- Analyze change failure rate and assign systemic control improvements.

**Inputs:** change policy and decision authority, change requests and risk classifications, release and incident history
**Artifact:** change control matrix
**Verification:** Change advisory or governance review.
**Handoff:** Transfer change control matrix with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 188. Vendor Management

**Purpose:** govern supplier performance, obligations and exit readiness

**Procedure:**
- Map supplier service, data access, subprocessors, criticality and business dependency.
- Review SLA performance, incidents, security attestations, financial/operational health and open obligations.
- Track corrective actions, renewal decisions, concentration risk and exit/portability plan.
- Escalate material breaches and record authorized risk acceptance.

**Inputs:** supplier contract and service inventory, performance/security evidence, renewal and exit dates
**Artifact:** supplier scorecard
**Verification:** Procurement, legal, security and service-owner review.
**Handoff:** Transfer supplier scorecard with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 189. FinOps Governance

**Purpose:** optimize cloud and platform economics without degrading service outcomes

**Procedure:**
- Allocate spend to accountable services and normalize by meaningful workload/unit.
- Identify idle, oversized, uncommitted and architecture-driven cost drivers.
- Model savings, engineering effort, risk and commitment trade-offs.
- Implement controlled optimization and compare realized savings with baseline and SLO impact.

**Inputs:** tagged spend and usage data, service ownership and unit metrics, budget and SLO constraints
**Artifact:** cost allocation report
**Verification:** Finance and service-owner review.
**Handoff:** Transfer cost allocation report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 190. Process Improvement

**Purpose:** improve a measured process through controlled experimentation

**Procedure:**
- Map current flow, queues, handoffs, rework and failure demand using observed data.
- Identify root causes and distinguish symptoms from constraints.
- Design a small experiment with hypothesis, guardrail metric and rollback.
- Compare results with baseline, retain or revert the change and assign ongoing ownership.

**Inputs:** process baseline and outcome metric, stakeholder pain points, change constraints
**Artifact:** process map
**Verification:** Process owner and affected team review.
**Handoff:** Transfer process map with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
