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
**Engineering Governance** (complete). Purpose: set and enforce the engineering rules that apply across all teams, with measurable compliance and a route for exceptions.

Entry criteria: Engineering policies are agreed with leadership; Compliance can be measured from tooling; A decision forum exists

Inputs: policy set; tooling data on repositories, pipelines and environments; exception requests; audit findings

Procedure:
1. Express each policy as a testable control, for example 'main branches require review and passing checks', with the data source that proves it.
2. Measure compliance by querying the tools (repositories, CI, cloud accounts) on a schedule, and publish results by team.
3. Enforce where possible by guardrails (branch protection, policy as code in the pipeline, organization policies) and not by reminders.
4. Handle exceptions through a record with reason, compensating control, approver and expiry date, and report open exceptions.
5. Review each policy at least yearly for effect and cost, and remove or revise policies that do not reduce real risk.
6. Report trends and the largest gaps to leadership with owners for each gap.

Deliverables: control catalogue with data sources; compliance dashboard by team; exception register with expiry; policy review notes

Acceptance: Each policy is a testable control with a data source Compliance is measured automatically Exceptions expire Gaps have owners

Validation: Engineering leadership approval.

- `gh api orgs/<org>/repos --paginate --jq '.[].name' | head   # example input to a compliance script` expect: all repositories are in the compliance data
- manual: sample five repositories and compare the dashboard value with a direct settings check expect: values agree

Failure modes:
- Policy cannot be measured | detect: No data source | respond: Rewrite as a testable control or drop it
- Exceptions never expire | detect: Old exceptions stay | respond: Add expiry and review
- Dashboard out of date | detect: Data not refreshed | respond: Schedule and alert on staleness

ILLUSTRATIVE: The control 'secret scanning enabled' is checked nightly across 240 repositories; 12 are non-compliant, owners are notified, and two have approved exceptions expiring in 60 days.

Gate: 15-181. Approval: none required

## 182
**Quality Governance** (complete). Purpose: set targets for quality, check that teams meet them with evidence, and use the results to improve how work is done.

Entry criteria: Quality measures can be collected; A definition of done exists; Teams accept shared measures

Inputs: quality measures; defect and incident data; test and review data; customer feedback

Procedure:
1. Define a small set of quality indicators with owners, such as escaped defects, change failure rate, test reliability and customer-reported issues.
2. Set targets and thresholds per indicator, based on current performance and the business need, and publish the definitions to avoid arguments about numbers.
3. Check adherence to the definition of done by sampling completed work for tests, reviews, documentation and acceptance, with findings recorded.
4. Investigate indicators outside thresholds with the team, find causes by examples, and agree an improvement with an owner.
5. Guard against gaming: review how numbers are produced, and look at several indicators together.
6. Review results quarterly, adjust targets and retire indicators that no longer drive decisions.

Deliverables: indicator definitions and targets; sampling reports; improvement actions with owners; quarterly quality review

Acceptance: Indicators are defined and owned Sampling checks the definition of done on real work Out-of-threshold results have causes and actions Gaming risks are reviewed

Validation: Quality governance lead review.

- manual: sample ten completed items and check each for tests, review and acceptance evidence expect: pass rate recorded
- manual: recompute one indicator from raw data expect: matches the reported value

Failure modes:
- Indicators gamed | detect: Numbers improve, quality does not | respond: Combine indicators and sample real work
- Targets arbitrary | detect: No link to need | respond: Base on baseline and customer impact
- Actions not done | detect: Same issue recurs | respond: Track actions to done

ILLUSTRATIVE: Escaped defects rise in one team. A sample of ten stories shows four without a test for the error path; the team adds the check to its definition of done, and the indicator is reviewed next quarter.

Gate: 15-182. Approval: none required

## 183
**Security Governance** (complete). Purpose: check, independently of the teams, that security controls are in place and working, and that gaps are tracked to closure.

Entry criteria: A security control framework is chosen; The auditor has read access to evidence; The scope of review is agreed

Inputs: security policies and control framework; system configurations and logs; vulnerability and incident records; previous findings

Procedure:
1. Map the policies to testable controls, such as access reviews, vulnerability patch times, encryption, logging and incident response.
2. Collect evidence directly from the systems (configuration exports, access lists, scanner results, logs) rather than from interviews alone.
3. Test operation over a period by sampling, for example the time between disclosure and patch for a sample of critical vulnerabilities.
4. Rate findings by risk, and require the control owner to respond with a plan, an owner and a date.
5. Verify closure by reviewing new evidence, not by accepting a statement that it was done.
6. Report trends to security leadership, including repeated findings and areas not yet reviewed.

Deliverables: control test matrix; evidence references; findings with owners and dates; closure verification and trend report

Acceptance: Evidence comes from systems Findings have owners and dates Closure is verified with new evidence Repeated findings are reported

Validation: Security auditor report; security leadership decision on risk acceptance.

- manual: sample ten critical vulnerabilities and compute days from disclosure to fix expect: median and worst case reported against the policy
- manual: take five closed findings and check each has fresh evidence expect: all do

Failure modes:
- Findings closed on a statement | detect: No evidence attached | respond: Reopen and require evidence
- Same finding every audit | detect: Repeat in the trend report | respond: Escalate for a structural fix
- Auditor lacks access | detect: Scope not covered | respond: Grant read-only access or reduce the scope formally

ILLUSTRATIVE: A sample shows critical patches take a median of 9 days against a 7-day policy, with two over 30. Findings go to the platform owner with a plan, and closure is verified from the next scan.

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
**Change Governance** (complete). Purpose: make sure changes to important systems are controlled consistently across teams, with proportionate approval and complete records.

Entry criteria: A change policy exists (stage 44); Deployment tooling records changes; Risk classes are defined

Inputs: change policy and risk classes; deployment and change records; incident records linked to changes; exception log

Procedure:
1. Define risk classes with examples and the approval needed for each, favoring pre-approved standard changes for low risk and tested automation.
2. Link change records to deployments automatically, so a deployment without a record is detected.
3. Measure change failure rate, rollbacks, emergency change share and incidents caused by changes, by team and service.
4. Review a sample of changes for correct classification, evidence and approval by a named human where required.
5. Review emergency changes within a set time to confirm they were justified and fix the cause.
6. Adjust the classes and standard changes using the data, so process effort goes where risk is.

Deliverables: risk class catalogue; deployment-to-change reconciliation; change metrics; sample review findings

Acceptance: Every production deployment maps to a change record Approval follows the class Emergency changes are reviewed Classes are tuned with data

Validation: Engineering governance owner review.

- manual: reconcile last month's production deployments with change records expect: no deployment without a record, or each listed as an incident
- manual: sample ten changes and check class, evidence and named approver expect: all consistent

Failure modes:
- Deployments without records | detect: Reconciliation shows gaps | respond: Block deploys without a change id
- Everything treated as high risk | detect: Approvals queue | respond: Introduce standard changes
- Emergency path overused | detect: Large share of changes | respond: Review causes and fix planning

ILLUSTRATIVE: Reconciliation finds 6 of 410 deployments with no record; the pipeline now requires a change id, and configuration-only updates move to a pre-approved standard change.

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
**FinOps Governance** (complete). Purpose: keep cloud and engineering spending governed by shared rules, budgets and accountability, so cost surprises are rare and spending decisions are traceable.

Entry criteria: Cloud cost data is available with allocation by team; Budgets exist or are being set; A finance partner is named

Inputs: cost and usage data; budgets and forecasts; tagging and account standards; finance calendar

Procedure:
1. Set budgets per team and product with owners, and alerts at several thresholds of actual and forecast spend.
2. Enforce tagging and account rules through policy so new resources without owner or cost centre are refused or flagged.
3. Hold a regular review with team leads and finance: variance to budget, anomalies, upcoming launches and commitments.
4. Detect anomalies automatically and require an owner to explain each one within a set time.
5. Require a cost estimate for large changes before approval, and compare to actual after launch.
6. Report unit economics and trends to leadership, and record decisions on budget changes and commitments.

Deliverables: budgets and alerts; tag and account policies; review minutes and decisions; anomaly explanations and unit cost report

Acceptance: Every budget has an owner and alerts Untagged resources are blocked or flagged Anomalies are explained within the set time Large changes carry a cost estimate

Validation: Finance partner and budget owner review.

- manual: list anomalies from the last month and check each has an explanation and an owner expect: none unexplained beyond the set time
- manual: compare the budget report totals with the invoice expect: agree within tolerance

Failure modes:
- Budget alert ignored | detect: Overspend with no response | respond: Define the responder and escalation
- Untagged spend grows | detect: Cost with no owner | respond: Enforce tags by policy
- Estimate never checked | detect: Launch costs more than planned | respond: Compare after launch and learn

ILLUSTRATIVE: An anomaly alert shows a doubling of data transfer cost; the owner finds a misconfigured job within a day, it is fixed, and the budget review minutes record the explanation and a new alert threshold.

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
