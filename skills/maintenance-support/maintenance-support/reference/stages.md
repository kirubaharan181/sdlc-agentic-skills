# Service maintenance and customer support: stage reference

## Contents
- [167 L1 Support](#167)
- [168 L2 Support](#168)
- [169 L3 Support](#169)
- [170 Bug Fixing](#170)
- [171 Patch Management](#171)
- [172 Dependency Updates](#172)
- [173 Database Maintenance](#173)
- [174 Performance Optimization](#174)
- [175 Technical Debt Reduction](#175)
- [176 Feature Enhancement](#176)
- [177 Customer Feedback](#177)
- [178 Knowledge Base](#178)
- [179 Maintenance Release](#179)
- [180 Product Lifecycle Management](#180)

## 167
**L1 Support** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-167. Approval: none required

## 168
**L2 Support** (complete). Purpose: resolve user-reported problems that first-line support cannot, using logs, runbooks and safe diagnosis, and escalate correctly.

Entry criteria: A ticket is escalated from first-line support with steps and impact; Runbooks and read access to logs and dashboards exist; Escalation path to engineering is defined

Inputs: escalated ticket; logs, metrics and dashboards; runbooks and known-issue list; recent changes

Procedure:
1. Confirm the impact, the affected users and the severity; raise severity if many users are affected.
2. Reproduce or find the failing request in logs using the ticket's identifiers.
3. Check the known-issue list and recent changes for a match and apply the runbook fix if one exists.
4. If there is no known fix, collect the evidence engineering needs and escalate to L3 with it.
5. Update the customer at the agreed intervals in plain language.
6. Record the cause and fix, and add or improve the runbook entry.

Deliverables: diagnosis notes; customer updates; escalation package or resolution record; runbook update

Acceptance: Severity and impact are recorded Escalation includes identifiers, logs and reproduction steps Customer was updated at the agreed intervals Runbook was updated for new fixes

Validation: Support lead review of the resolution record.

- manual: confirm the escalation ticket contains request identifiers, timestamps and log excerpts expect: all present
- manual: check the time between updates to the customer against the target expect: within target

Failure modes:
- Escalation without evidence | detect: L3 asks for basic details | respond: Return and gather evidence first
- Customer left without updates | detect: Gap longer than target | respond: Send an update now
- Fix applied without recording | detect: No runbook change | respond: Document it

ILLUSTRATIVE: A customer's invoices fail to download. Logs show a timeout on one large account. The runbook step to regenerate the file works; the cause is escalated to L3 with the request id, and the customer is updated.

Gate: 14-168. Approval: none required

## 169
**L3 Support** (complete). Purpose: fix or workaround production problems that need code-level investigation, with evidence and a safe change.

Entry criteria: The issue is escalated from L2 with evidence; Access to code, logs and a test environment exists; Severity and owner are set

Inputs: escalation package with evidence; source code and recent changes; logs and traces; test environment

Procedure:
1. Reproduce the problem in a test environment or isolate it precisely in logs and traces.
2. Find the root cause; if a quick safe workaround exists, give support a workaround first.
3. Write a failing test, then the smallest fix; hand off to the bug-fix procedure (stage 170) for delivery.
4. Review with an independent engineer and check data impact; plan any data repair separately and carefully.
5. Release through the normal or emergency path according to severity.
6. Return the resolution and the cause to L2 and the reporter, and update the runbook.

Deliverables: root-cause note; workaround for support; failing test and fix; resolution communication

Acceptance: The cause is established with evidence A workaround was offered when the fix could not be immediate Any data repair was planned and approved separately Support has the resolution and runbook update

Validation: Service owner acceptance of the resolution.

- `pytest -q tests/regression/test_issue_5678.py   # example failing test then passing` expect: fails before, passes after the fix
- manual: check data affected by the defect and confirm repair or a decision not to repair expect: decision recorded

Failure modes:
- Fix deployed without a test | detect: No regression test in the change | respond: Add the test
- Data damage not assessed | detect: No statement on affected data | respond: Assess and plan repair
- Support not informed | detect: L2 has no resolution note | respond: Send resolution and workaround details

ILLUSTRATIVE: An escalation shows duplicate shipments for retried orders. Engineers reproduce it, add an idempotency check with a regression test, release the fix, and support receives the list of affected orders to correct.

Gate: 14-169. Approval: none required

## 170
**Bug Fixing** (complete). Purpose: fix a confirmed defect with the smallest safe change and prove it with a test that failed before.

Entry criteria: Defect is reproduced and has a ticket with steps and expected behavior; The affected version and area of code are known; Owner and priority are set

Inputs: defect report with reproduction steps; affected code and version; existing tests; acceptance expectation

Procedure:
1. Write a failing test that reproduces the defect before touching the code.
2. Find the root cause; fix the cause rather than the symptom, with the smallest change.
3. Confirm the new test passes and the surrounding tests still pass.
4. Check related code paths for the same mistake and note or fix them.
5. Describe cause, fix and risk in the pull request and link the ticket.
6. After release, confirm with the reporter or monitoring that the defect no longer occurs.

Deliverables: regression test; minimal fix; pull request with cause and risk; post-release confirmation

Acceptance: The regression test fails without the fix and passes with it The change is limited to the defect Related paths were checked Reporter or monitoring confirms the fix

Validation: Service owner acceptance and customer-facing closure check.

- `git stash && pytest -q tests/regression/test_bug_1234.py; git stash pop && pytest -q tests/regression/test_bug_1234.py   # example` expect: fails before the fix, passes after
- `pytest -q` expect: full suite passes

Failure modes:
- Test passes without the fix | detect: Test does not fail on the old code | respond: Rewrite the test to reproduce the defect
- Fix changes unrelated behavior | detect: Diff touches unrelated files | respond: Split the change
- Symptom hidden, cause remains | detect: Same defect appears elsewhere | respond: Fix the root cause

ILLUSTRATIVE: Totals are off by one cent for certain discounts. A test with that discount fails; the rounding is moved to the end of the calculation; the test and suite pass; the finance team confirms next day.

Gate: 14-170. Approval: none required

## 171
**Patch Management** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-171. Approval: none required

## 172
**Dependency Updates** (complete). Purpose: keep dependencies current and safe through small, tested updates on a regular schedule.

Entry criteria: Lockfiles exist and the test suite is reliable enough to detect breakage; A schedule and an owner for updates exist; Advisory feed or audit tool is available

Inputs: dependency list and lockfiles; advisory and release information; test suite; update policy

Procedure:
1. List outdated and vulnerable dependencies, with security fixes first.
2. Group low-risk updates; update high-risk or major-version dependencies one at a time.
3. Read the changelog for breaking changes and deprecations before updating.
4. Run the full test suite and any relevant scans after each update.
5. Merge through the normal review (stage 72 for new dependencies), with rollback by reverting the commit.
6. Record versions changed and any deferred updates with a reason and a date.

Deliverables: update pull requests; test results; deferred update list; version change record

Acceptance: Security updates are applied within the agreed time Each update was tested Deferred updates have a reason and a date Updates are reversible by revert

Validation: Review of the update pull request.

- `pip list --outdated   # example; use the ecosystem's tool` expect: list recorded; security-relevant items addressed
- `pytest -q && pip-audit` expect: tests pass and no unresolved high or critical advisory

Failure modes:
- Big-bang update breaks many things | detect: Many failures after a batch update | respond: Split and update one at a time
- Update skipped for months | detect: Outdated list grows | respond: Schedule and enforce a cadence
- Changelog ignored | detect: Behavior change in production | respond: Read changelogs; add a test for the changed behavior

ILLUSTRATIVE: A monthly run updates six minor versions in one pull request after the tests pass, and moves one major-version upgrade into its own tracked change with a migration test.

Gate: 14-172. Approval: none required

## 173
**Database Maintenance** (complete). Purpose: maintain the health of production databases through planned, safe, reversible maintenance.

Entry criteria: Maintenance needs are identified from monitoring (bloat, fragmentation, growth, statistics); A maintenance window is agreed; Backup and restore are verified

Inputs: database health metrics; maintenance plan and window; verified backup; rollback or stop conditions

Procedure:
1. Identify the work from metrics: index maintenance, statistics, vacuum or compaction, storage growth, version patches.
2. Rehearse on a copy and record duration and locking effects.
3. Confirm a verified backup exists and obtain the DBA owner's approval for the window.
4. Run the maintenance with monitoring and stop conditions; stop if thresholds are crossed.
5. Verify health metrics and query performance afterward against the baseline.
6. Record what was done and schedule the next review.

Deliverables: maintenance plan and rehearsal results; approval for the window; execution log; before and after metrics

Acceptance: Backup was verified before starting Rehearsal showed acceptable impact Metrics improved or stayed within limits DBA owner approved the window

Validation: DBA-owner approval.

- `psql -c "SELECT relname, n_dead_tup FROM pg_stat_user_tables ORDER BY n_dead_tup DESC LIMIT 10"   # example for PostgreSQL` expect: dead tuples fall after maintenance
- manual: compare p95 query latency before and after the window expect: no regression

Failure modes:
- Maintenance locks a busy table | detect: Rehearsal or run shows long locks | respond: Use online methods or schedule later
- No backup before starting | detect: No verified backup record | respond: Stop until one exists
- Performance worsens | detect: Latency above baseline after | respond: Roll back where possible or apply the prepared fix

ILLUSTRATIVE: A weekend window rebuilds three bloated indexes online. Rehearsal showed no long locks; afterward the table's dead tuples drop and p95 latency is unchanged.

Gate: 14-173. Approval: dba-owner (for destructive or locking maintenance on production data)

## 174
**Performance Optimization** (stub). Purpose: improve measured performance without violating correctness.

Inputs: baseline workload and latency profile; consistency/freshness requirements; resource and cost limits

Procedure:
1. Profile before changing code; identify dominant cost and reproducible baseline.
2. Choose cache key, TTL, invalidation and consistency behavior based on data semantics.
3. Bound memory, stampede, stale data and eviction behavior.
4. Compare before/after p50/p95/p99, throughput, error rate and cost under equivalent load.

Deliverables: profile report; optimization change; cache policy; before/after benchmark

Acceptance: Improvement is measured against baseline. Correctness and freshness invariants hold. No unbounded memory or stale-data risk is introduced.

Validation: Performance and correctness regression review.

Gate: 14-174. Approval: none required

## 175
**Technical Debt Reduction** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-175. Approval: none required

## 176
**Feature Enhancement** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-176. Approval: none required

## 177
**Customer Feedback** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-177. Approval: none required

## 178
**Knowledge Base** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-178. Approval: none required

## 179
**Maintenance Release** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-179. Approval: none required

## 180
**Product Lifecycle Management** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-180. Approval: business-sponsor (always)
