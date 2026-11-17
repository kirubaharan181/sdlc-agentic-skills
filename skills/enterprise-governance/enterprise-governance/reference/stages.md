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
**Documentation Governance** (complete). Purpose: keep documentation accurate, findable and owned over time, so people can trust it.

Entry criteria: Documentation exists in known places; A way to assign owners exists; A review cadence can be agreed

Inputs: documentation inventory; usage and search data; recent product and process changes; style and structure standards

Procedure:
1. Inventory the documents, assign an owner to each and record the last review date.
2. Define standards for structure, naming, status labels and where each type of content lives.
3. Link documentation changes to code or process changes so they are reviewed together.
4. Review on a schedule by type, and archive or delete outdated pages instead of leaving them.
5. Check for broken links and orphaned pages automatically.
6. Track search failures and reader feedback, and fix the most common gaps first.

Deliverables: documentation inventory with owners; standards; review schedule and results; archive log

Acceptance: Every document has an owner and a review date No broken links in published docs Outdated pages are archived Changes to behavior include documentation updates

Validation: Documentation owner approval of standards.

- `python3 scripts/check_links.py` expect: no broken relative links
- manual: list documents past their review date expect: each has an owner and a planned action

Failure modes:
- Documents without owners | detect: Inventory blanks | respond: Assign or archive
- Docs drift from the code | detect: Readers report wrong steps | respond: Tie docs to the change review
- Duplicate pages | detect: Different answers to one question | respond: Merge and redirect

ILLUSTRATIVE: An inventory finds 12 pages with no owner. Eight are archived, four are assigned, and a link check runs in CI so a renamed page fails the build instead of leaving dead links.

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
**Vendor Management** (complete). Purpose: choose, contract and oversee outside suppliers so the organization gets the service it pays for and carries known risk.

Entry criteria: A need that may be met by a vendor exists; Procurement and legal contacts are known; Security and compliance requirements are defined

Inputs: requirements; vendor proposals; security and compliance requirements; budget

Procedure:
1. Write requirements and evaluation criteria, with weights, before talking to vendors.
2. Assess each candidate on the criteria, including security, data handling, financial stability and exit options.
3. Negotiate service levels, data ownership, breach notice, audit rights and termination terms with legal.
4. After onboarding, track delivery against service levels and review on a schedule with the vendor.
5. Keep a register of vendors with owner, data accessed, contract end and renewal notice date.
6. Plan the exit: data return, transition support and replacement options.

Deliverables: evaluation record; contract terms summary; vendor register; review notes and exit plan

Acceptance: Selection used criteria written before the vendor talks Security and data terms were reviewed The register shows owner and renewal date An exit path is documented

Validation: Procurement and security approval.

- manual: compare the contract terms with the requirements list expect: gaps noted and accepted or closed
- manual: list contracts with renewal notice due within 90 days expect: each has an owner decision

Failure modes:
- Auto-renewal missed | detect: Contract renews unnoticed | respond: Track notice dates
- Vendor holds data without terms | detect: No data clause | respond: Add before access is given
- Lock-in | detect: No export route | respond: Require export and test it

ILLUSTRATIVE: Three monitoring vendors are scored on weighted criteria. The chosen one agrees to 72-hour breach notice and full data export, and the register notes a renewal notice date of 90 days before term end.

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
**Process Improvement** (complete). Purpose: find, test and embed process changes that reduce delay, rework or risk, and show whether they worked.

Entry criteria: A process with measurable pain exists; Process data or the means to collect it exists; A process owner agrees to change

Inputs: process descriptions; cycle time, rework and defect data; feedback from people who do the work; retrospective actions

Procedure:
1. Pick one process and measure it first: cycle time, waiting time, rework and defects.
2. Map the actual process with the people who do it and mark where work waits or loops back.
3. Choose the largest cause and design a small change with an expected effect on a named measure.
4. Trial it for a fixed period with a few teams, comparing with the baseline.
5. Adopt, adjust or drop based on the result; update the documented process if adopted.
6. Share what was learned and revisit the measure after several months.

Deliverables: baseline measures; process map; trial design and results; updated process document

Acceptance: A baseline exists before the change The trial has a period and a measure The decision follows the results Adopted changes are documented

Validation: Process owner decision.

- manual: compare cycle time for the trial period with the baseline period expect: difference and sample size reported
- manual: check the process document reflects the adopted change expect: updated and dated

Failure modes:
- Change without a baseline | detect: Cannot show improvement | respond: Measure first
- Change imposed without the team | detect: Workarounds appear | respond: Involve the people who do the work
- Gains fade | detect: Measure returns to baseline | respond: Review later and embed the change in tooling

ILLUSTRATIVE: Pull requests wait a median of 30 hours for review. Two trial teams adopt a daily review slot and the median falls to 12 hours over four weeks; the process page is updated and the slot adopted by other teams.

Gate: 15-190. Approval: none required
