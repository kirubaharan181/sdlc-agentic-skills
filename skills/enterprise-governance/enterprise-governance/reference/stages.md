# Enterprise engineering governance: stage reference

## Contents
- [181 Engineering Governance](#181)
- [182 Quality Governance](#182)
- [183 Security Governance](#183)
- [184 Access Governance](#184)
- [185 Compliance Auditing](#185)
- [186 Documentation Governance](#186)
- [187 Change Governance](#187)
- [188 Vendor Management](#188)
- [189 FinOps Governance](#189)
- [190 Process Improvement](#190)

## 181
**Engineering Governance** (stub). Purpose: govern repository controls, engineering standards and exception lifecycle.

Inputs: repository inventory and ownership; engineering policy and required checks; team onboarding and exception records

Procedure:
1. Map branch protections, code owners, required checks and contribution policy to each repository.
2. Sample actual repository settings and verify enforcement rather than relying on documentation.
3. Review onboarding, toolchain support, secrets and change exceptions.
4. Track drift and verify corrective actions across repositories.

Deliverables: repository control inventory; policy compliance report; exception register; onboarding standard

Acceptance: Repository controls are verified in the platform. Exceptions have owner, expiry and compensating control. Clean-checkout onboarding is reproducible.

Validation: Repository policy sample audit.

Gate: 15-181. Approval: none required

## 182
**Quality Governance** (stub). Purpose: govern quality policy, evidence and corrective action across teams.

Inputs: quality policy and objectives; process/product quality data; control owners and audit period

Procedure:
1. Define measurable quality objectives, required evidence and ownership.
2. Sample delivery records and verify controls operate as documented.
3. Analyze defects, escaped issues, test gaps and corrective-action trends.
4. Assign systemic improvements and verify effectiveness over a review period.

Deliverables: quality policy and control map; quality scorecard; audit samples; corrective action register

Acceptance: Metrics have definitions and owners. Evidence samples are reproducible. Corrective actions are verified for effectiveness.

Validation: Quality governance review and sample audit.

Gate: 15-182. Approval: none required

## 183
**Security Governance** (stub). Purpose: govern security policy, risk acceptance and control effectiveness.

Inputs: security policy and risk appetite; asset/control ownership; risk and exception register

Procedure:
1. Map security obligations to preventive, detective and recovery controls.
2. Review control operation, access, vulnerabilities and incident trends.
3. Approve or route exceptions with compensating controls, owner and expiry.
4. Report material risk and verify remediation closure.

Deliverables: security control matrix; risk/exception register; control effectiveness report

Acceptance: Risk acceptance is authorized and time-bound. Controls have evidence and accountable owners. Material exceptions are escalated.

Validation: Security governance council review.

Gate: 15-183. Approval: none required

## 184
**Access Governance** (complete). Purpose: make sure each person and system has only the access it needs, and that access is reviewed and removable.

Entry criteria: Systems in scope and their access owners are listed; Current access export can be obtained from each system; Access policy defines roles and review cadence

Inputs: access export per system; role and entitlement definitions; joiner-mover-leaver records; access policy

Procedure:
1. Export current entitlements per system and map each account to a named person or service owner.
2. Compare entitlements with the role definitions; flag excess, dormant and orphaned accounts.
3. Send each access owner their list for confirm or revoke; set a deadline.
4. Apply revocations through the normal change path; keep the ticket id for each.
5. Verify by re-export that revoked access is gone.
6. Record completion, exceptions with expiry, and the next review date; access-owner approves.

Deliverables: access review report; revocation tickets; exception register; post-review export

Acceptance: Every account has an owner and a role justification Dormant and orphaned accounts are removed or excepted Re-export confirms revocations Next review is scheduled

Validation: Access-owner approval plus re-export comparison.

- `diff <(sort before.csv) <(sort after.csv)` expect: only the requested revocations appear as removed lines; no additions
- `grep -c ',dormant,' reports/access-review.csv   # example` expect: zero without an exception id

Failure modes:
- Owner confirms everything without looking | detect: Zero changes across a large population | respond: Sample-check entitlements against role definitions
- Revocation requested but not applied | detect: Re-export still lists the access | respond: Reopen ticket; BLOCK completion
- Service accounts have no owner | detect: Owner column empty | respond: Assign an owner or disable the account

ILLUSTRATIVE: A quarterly review of the deployment tool finds two departed contractors with admin rights and one service account with no owner. Admin rights are revoked, the service account is assigned to the platform team, and re-export confirms it.

Gate: 15-184. Approval: access-owner (when granting or widening privileged or break-glass access, or revoking access in bulk)

## 185
**Compliance Auditing** (complete). Purpose: provide independent, evidenced assurance that controls operate as claimed, and track findings to closure.

Entry criteria: Audit scope, criteria (policy or standard) and period are agreed; Auditor is independent of the controls being audited; Evidence sources and owners are named

Inputs: audit scope and criteria; control descriptions and owners; evidence from the audit period; previous audit findings

Procedure:
1. Agree scope, criteria, period and sampling approach in writing.
2. Request evidence for a risk-based sample of controls and test both design and operation over the period.
3. Re-perform the control or verify the evidence independently; do not rely only on assertions.
4. Rate each finding with criteria, condition, cause and effect; agree corrective actions and dates with owners.
5. Issue the report with scope limits stated, then verify closure of each action independently.
6. Report overdue findings to the compliance owner.

Deliverables: audit plan; workpapers with evidence references; findings report; closure verification

Acceptance: Each finding cites criteria and evidence Sampling basis is documented Auditor is independent of the audited control Closure is independently verified

Validation: Legal and compliance owner sign-off.

- manual: re-perform two sampled controls from raw evidence expect: results match the control owner's assertions or differences are logged
- manual: confirm each corrective action has an owner and date expect: none missing

Failure modes:
- Auditor reviews own work | detect: Auditor appears as control implementer | respond: Reassign the audit
- Evidence accepted without testing | detect: Workpapers contain only screenshots of assertions | respond: Re-perform tests
- Findings never closed | detect: Overdue actions | respond: Escalate to the compliance owner

ILLUSTRATIVE: A sample of ten access removals is tested. Two departed users kept access for 45 days against a 7-day policy. The finding is rated medium and closed after a re-extract shows the access removed.

Gate: 15-185. Approval: none required

## 186
**Documentation Governance** (stub). Purpose: control documentation accuracy, ownership and lifecycle.

Inputs: document inventory and classification; owners and review cadence; retention and publication policy

Procedure:
1. Inventory authoritative documents, audience, version and source of truth.
2. Check accuracy against current implementation, policy and approved decisions.
3. Review access, retention, link integrity and stale/duplicate content.
4. Assign owner and review date; archive superseded material according to policy.

Deliverables: document register; accuracy/review report; retention and archive log

Acceptance: Each authoritative document has owner and review date. Published guidance matches current behavior. Superseded documents are clearly marked or archived.

Validation: Documentation governance sample review.

Gate: 15-186. Approval: none required

## 187
**Change Governance** (stub). Purpose: govern the portfolio of material engineering changes.

Inputs: change policy and decision authority; change requests and risk classifications; release and incident history

Procedure:
1. Classify normal, standard and emergency changes under policy.
2. Review impact, approvals, segregation, schedule and recovery readiness.
3. Sample completed changes for evidence, unauthorized drift and failed outcomes.
4. Analyze change failure rate and assign systemic control improvements.

Deliverables: change control matrix; change approval records; audit sample report; change performance metrics

Acceptance: Emergency path is controlled and retrospectively reviewed. Approval precedes implementation where required. Change outcomes and incidents are linked.

Validation: Change advisory or governance review.

Gate: 15-187. Approval: none required

## 188
**Vendor Management** (stub). Purpose: govern supplier performance, obligations and exit readiness.

Inputs: supplier contract and service inventory; performance/security evidence; renewal and exit dates

Procedure:
1. Map supplier service, data access, subprocessors, criticality and business dependency.
2. Review SLA performance, incidents, security attestations, financial/operational health and open obligations.
3. Track corrective actions, renewal decisions, concentration risk and exit/portability plan.
4. Escalate material breaches and record authorized risk acceptance.

Deliverables: supplier scorecard; obligation and risk register; renewal/exit recommendation

Acceptance: Critical supplier risks have owners and contingency. Contract obligations are evidenced. Exit strategy is practical and tested where critical.

Validation: Procurement, legal, security and service-owner review.

Gate: 15-188. Approval: none required

## 189
**FinOps Governance** (stub). Purpose: optimize cloud and platform economics without degrading service outcomes.

Inputs: tagged spend and usage data; service ownership and unit metrics; budget and SLO constraints

Procedure:
1. Allocate spend to accountable services and normalize by meaningful workload/unit.
2. Identify idle, oversized, uncommitted and architecture-driven cost drivers.
3. Model savings, engineering effort, risk and commitment trade-offs.
4. Implement controlled optimization and compare realized savings with baseline and SLO impact.

Deliverables: cost allocation report; optimization backlog; forecast and variance; realized savings evidence

Acceptance: Savings are measured against a comparable baseline. Ownership and allocation coverage are visible. Reliability and security are not traded away silently.

Validation: Finance and service-owner review.

Gate: 15-189. Approval: none required

## 190
**Process Improvement** (stub). Purpose: improve a measured process through controlled experimentation.

Inputs: process baseline and outcome metric; stakeholder pain points; change constraints

Procedure:
1. Map current flow, queues, handoffs, rework and failure demand using observed data.
2. Identify root causes and distinguish symptoms from constraints.
3. Design a small experiment with hypothesis, guardrail metric and rollback.
4. Compare results with baseline, retain or revert the change and assign ongoing ownership.

Deliverables: process map; baseline and experiment plan; result report; standardized improvement

Acceptance: Change is evidence-backed. Guardrails prevent local optimization harm. Adopted process has an owner and review date.

Validation: Process owner and affected team review.

Gate: 15-190. Approval: none required
