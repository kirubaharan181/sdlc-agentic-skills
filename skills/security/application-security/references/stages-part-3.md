# Application security engineering: stage reference (part 3 of 4)

## Contents
- [106 Data Protection](#106)
- [107 Compliance Review](#107)
- [108 License Compliance](#108)
- [109 Vulnerability Remediation](#109)

## 106
**Data Protection** (complete). Purpose: check that data is protected at rest, in transit and in use according to its classification, and that exposure paths are closed.

Entry criteria: Data classification and flows exist (stage 30); Encryption and key management are designed; Test environment holds representative data

Inputs: data inventory and classification; data flow diagrams; encryption and key configuration; privacy and retention rules

Procedure:
1. Trace each classified data element through its flow, and confirm encryption in transit with a modern protocol version on every hop, including internal ones.
2. Check encryption at rest for databases, object stores, backups and logs, and see who can use or export the keys.
3. Look for exposure paths: verbose errors, logs, analytics payloads, URLs, caches, debug endpoints and misconfigured public storage.
4. Check access to the data against least privilege, and that access to sensitive tables and exports is logged.
5. Check masking or synthetic data outside production, and that retention and deletion jobs actually remove data, including from backups after their cycle.
6. Report gaps with the data element, the path and the fix, and retest.

Deliverables: data protection test report; exposure path findings; key and access review; retention verification

Acceptance: Every classified element has a traced flow Encryption in transit and at rest was verified, not assumed Non-production data is masked Deletion was proven by a test

Validation: Application security engineer and data owner review.

- `nmap --script ssl-enum-ciphers -p 443 test.example.com   # example` expect: only supported protocol versions and strong ciphers
- manual: create a test record, delete it through the product, and query the database and the search index expect: record absent from both

Failure modes:
- Sensitive field in logs | detect: Search of logs finds personal data | respond: Mask and purge
- Public storage bucket | detect: Anonymous listing succeeds | respond: Block public access and review
- Deleted data persists in a cache or index | detect: Record still found | respond: Add invalidation to the deletion job

ILLUSTRATIVE: A trace of customer email finds it in application logs and an analytics event; both are masked, a search for the address in logs afterwards returns nothing, and the deletion test confirms removal from the search index.

Gate: 09-106. Approval: none required

## 107
**Compliance Review** (complete). Purpose: check, against named rules, that the system and the way it is built and run meet legal, regulatory and contractual obligations, and keep the evidence.

Entry criteria: Applicable obligations are listed (stage 10); Controls exist and are in operation; Evidence is accessible to the reviewer

Inputs: obligations register; control descriptions; system evidence such as configurations, logs and records; previous audit findings

Procedure:
1. Select the obligations in scope and break each into testable control statements.
2. Gather evidence for each control from the system itself (configurations, access lists, logs, tickets) rather than from descriptions alone.
3. Test a sample for operation over the period, not only the design: for example, a sample of changes for approval records.
4. Classify results: compliant, partly compliant, non-compliant or not applicable, with the evidence reference.
5. Raise each gap with an owner, a remediation and a date, and record accepted risks with an approver.
6. Report to the compliance owner, and retest remediations before closing.

Deliverables: control test matrix with evidence references; gap register with owners; accepted risk records; review report

Acceptance: Each in-scope obligation has a control and a result Evidence comes from the system, not only from descriptions Samples cover the review period Gaps have owners and dates

Validation: Compliance owner accepts the report; named executive accepts residual risk.

- manual: sample 10 changes from the period and check each for approval and test records expect: all present, or exceptions listed
- manual: check each non-compliant row has an owner and a date expect: none missing

Failure modes:
- Control described but not operating | detect: Sample fails | respond: Record as non-compliant and fix
- Evidence outdated | detect: Evidence dated outside the period | respond: Collect current evidence
- Risk accepted by a team member | detect: No executive approval | respond: Escalate for proper acceptance

ILLUSTRATIVE: A review of an access-review obligation samples four quarters and finds one missing; it is raised as a gap with an owner, completed within 30 days, and the new record is added to the evidence.

Gate: 09-107. Approval: none required

## 108
**License Compliance** (complete). Purpose: check that third-party licenses allow how we use and distribute the software, and keep proof.

Entry criteria: Dependency inventory or SBOM exists; License policy lists allowed, review-required and forbidden licenses; Legal or compliance contact exists

Inputs: SBOM and dependency list; license policy; distribution model (internal, SaaS, shipped); license texts

Procedure:
1. List every dependency with its license from the SBOM, including transitive and vendored code.
2. Classify each license against the policy and the way the software is distributed; copyleft obligations depend on distribution.
3. Flag unknown, missing and conflicting licenses for review by compliance.
4. Resolve flagged items: replace the component, obtain permission, or document the accepted obligation.
5. Prepare required notices and attributions and include them in the release.
6. Record the decision for each flagged license with the person who made it.

Deliverables: license inventory; flagged items and decisions; notices and attribution file; compliance-owner approval

Acceptance: Every component has a recorded license No forbidden license remains Each review-required license has a decision Notices are included in the release

Validation: Compliance-owner approval.

- `pip-licenses --format=csv > reports/licenses.csv   # example; use the ecosystem's tool` expect: every dependency has a license entry
- manual: compare licenses in the report against the forbidden list expect: no matches or each has a decision

Failure modes:
- License unknown | detect: Entry says UNKNOWN | respond: Check the source; ask legal or replace
- Copyleft in a shipped product | detect: Strong copyleft licence in distributed code | respond: Replace or obtain legal approval
- Notices missing | detect: Release lacks attribution file | respond: Generate and ship it

ILLUSTRATIVE: The inventory shows one dependency with an unknown license. Compliance contacts the maintainer, receives a permissive license statement, and records the decision before release.

Gate: 09-108. Approval: compliance-owner (when a license exception is requested)

## 109
**Vulnerability Remediation** (complete). Purpose: fix confirmed vulnerabilities within agreed deadlines and prove they are closed.

Entry criteria: Vulnerability findings are triaged and confirmed (stages 99-101); Remediation deadlines by severity exist; An owner for each finding can be named

Inputs: triaged findings with severity; remediation deadline policy; affected code, dependency or configuration; exception process

Procedure:
1. Order findings by severity, exposure and exploit activity, and assign an owner and a due date to each.
2. Choose the remedy: patch or upgrade, code fix, configuration change, or compensating control when no fix exists.
3. Apply the fix on a branch with a test that fails on the vulnerable behavior where practical.
4. Run the same scan or test that found the issue and confirm it no longer reports it.
5. Release through the normal path; use the emergency path only for actively exploited issues.
6. Close the finding with evidence, or record an exception with owner, reason and expiry.

Deliverables: remediation plan with owners and due dates; fix and regression test; rescan evidence; exception register entries

Acceptance: Every critical and high finding is fixed within policy or has an approved exception Closure is shown by rerunning the original check Exceptions have owner and expiry Fixes shipped through reviewed changes

Validation: Independent rescan by security, not by the fixing engineer.

- `semgrep scan --config auto --error reports-src/   # example; rerun the scanner that found it` expect: the finding no longer appears
- manual: compare open findings with their due dates expect: none overdue without an exception

Failure modes:
- Fix closes the finding in the tracker but not in the scan | detect: Rescan still reports it | respond: Reopen the finding
- Deadline missed silently | detect: Overdue finding with no exception | respond: Escalate to the security lead
- Fix introduces a regression | detect: Tests fail after patching | respond: Revert and redesign the fix

ILLUSTRATIVE: A high-severity injection finding is assigned with a seven-day due date. The fix uses a parameterized query with a regression test; the SAST rescan no longer reports the finding and security closes it.

Gate: 09-109. Approval: none required
