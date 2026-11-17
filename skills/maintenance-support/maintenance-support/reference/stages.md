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
**L1 Support** (complete). Purpose: resolve common user problems on first contact and pass on what cannot be resolved, with everything the next team needs.

Entry criteria: Support channels and a ticket system exist; Runbooks and a knowledge base exist (stage 178); Escalation criteria are defined

Inputs: user report; knowledge base and runbooks; account and status information; escalation criteria

Procedure:
1. Record the user's problem in their words, the affected account, and the time and steps that led to it.
2. Check the status page and known issues first, then search the knowledge base for a matching article.
3. Apply the documented fix, confirm with the user that it worked, and record what was done.
4. If there is no fix or the criteria are met, escalate with the full record, identifiers and impact; do not ask the user to repeat themselves.
5. Keep the user informed at the agreed intervals in plain language.
6. Tag the ticket by cause so recurring problems show up and become knowledge base articles.

Deliverables: ticket with a complete record; resolution or escalation package; user updates; cause tag

Acceptance: Ticket has identifiers, steps and time Fixes follow runbooks and are confirmed with the user Escalations include the full record Cause tags are set

Validation: Support lead sampling review.

- manual: review five random closed tickets for identifiers, steps and confirmation expect: all complete
- manual: check the time to first response against the target expect: within target

Failure modes:
- User asked to repeat details | detect: Escalation lacks information | respond: Use the escalation template
- Fix not confirmed | detect: Ticket closed without user reply | respond: Confirm before closing
- Known issue handled as new | detect: Duplicate tickets | respond: Link to the known issue and update the user

ILLUSTRATIVE: A user cannot download an invoice. The agent finds a matching article, the fix works, the user confirms, and the ticket is tagged 'invoice download'; a second similar ticket the same week is escalated with the account id and error time.

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
**Patch Management** (complete). Purpose: keep running systems patched against known vulnerabilities within agreed timeframes, without breaking service.

Entry criteria: Inventory of systems and software versions exists; Patch policy sets timeframes by severity; Maintenance windows and rollback options exist

Inputs: system inventory; vulnerability and patch information; patch policy; maintenance windows

Procedure:
1. Match the inventory against advisories and rank by severity, exposure and exploit activity.
2. Test patches on a representative non-production system and record problems.
3. Schedule rollout in stages, starting with low-risk systems, with a rollback for each.
4. Apply patches by automation and verify the version and service health afterward.
5. Track compliance against the policy timeframes and report exceptions with owner and expiry.
6. Update the inventory and record what was patched.

Deliverables: patch plan with priorities; test results; rollout record; compliance report with exceptions

Acceptance: Critical patches are applied within the policy time or excepted Rollout was staged with verification Exceptions have owner and expiry Inventory is updated

Validation: System owner approval of the plan and exceptions.

- `apt list --upgradable 2>/dev/null | head   # example for Debian systems` expect: no pending security updates after rollout
- manual: compare patched versions with the advisory's fixed versions expect: versions equal or exceed the fix

Failure modes:
- Patch applied to production first | detect: No test record | respond: Test first, then roll out in stages
- Systems missing from inventory | detect: Unknown hosts found on scan | respond: Add them and patch
- Exceptions never expire | detect: Old exceptions without review | respond: Require expiry and review

ILLUSTRATIVE: A critical kernel advisory is tested on one staging node, rolled out to production nodes in three batches with health checks, and the compliance report shows all nodes patched within the 14-day policy.

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
**Performance Optimization** (complete). Purpose: improve the speed or resource use of a running system against a stated target, and keep the gain from regressing.

Entry criteria: A target exists, such as p95 latency or cost per request; The system is observable (stages 155-157); A repeatable load or benchmark exists

Inputs: performance target; production and test measurements; profiles and traces; change history of hot components

Procedure:
1. Reproduce the problem with a benchmark whose result you trust, and record the baseline with its spread.
2. Locate the bottleneck with profiles and traces; list the top three causes by time share.
3. Change one thing at a time, starting with the largest share, and re-measure after each change.
4. Keep only changes that improve the target beyond the noise; revert the rest.
5. Check that the gain holds on production-like data and does not move cost or errors elsewhere.
6. Add a performance check to CI or monitoring so a regression is caught, and record what was learned.

Deliverables: baseline and final measurements; list of kept and reverted changes; regression check; short write-up

Acceptance: Target met or the shortfall is explained Each kept change has measured benefit A regression check exists No functional test fails

Validation: Performance engineer and service owner review.

- manual: run the same benchmark three times before and after and compare the medians expect: improvement exceeds the run-to-run spread
- `pytest -q` expect: all functional tests pass after the changes

Failure modes:
- Gain within noise | detect: Before and after ranges overlap | respond: Revert or measure longer
- Fix shifts load elsewhere | detect: Another service slows | respond: Measure the whole path
- Regression returns | detect: Metric drifts back in weeks | respond: Add the CI or alert check

ILLUSTRATIVE: A search endpoint has p95 of 1.2 s against a 500 ms target. A profile shows 60 percent in one N+1 query; batching it brings p95 to 450 ms, and a latency alert is added at 600 ms.

Gate: 14-174. Approval: none required

## 175
**Technical Debt Reduction** (complete). Purpose: reduce a chosen piece of debt safely, in small steps that keep behavior unchanged and leave the code easier to change.

Entry criteria: The debt item is chosen and has an owner (stage 76); Tests cover the area or can be added first; The change can ship in small steps

Inputs: debt register entry; code and its tests; change and incident history; agreed done definition

Procedure:
1. State the outcome that proves the debt is paid, such as a removed module or a lower defect rate.
2. Add characterization tests around current behavior before touching the code.
3. Refactor in small commits that each keep the tests green; do not mix in new features.
4. Release behind a flag or in stages when the area is critical, and watch the metrics after each release.
5. Delete the old code and unused configuration once nothing uses them.
6. Close the register entry with the evidence and note anything new discovered.

Deliverables: characterization tests; small refactoring commits; removed old code; closed register entry with evidence

Acceptance: Behavior is unchanged by the characterization tests The stated outcome is met Old code is actually removed No unrelated features are in the change

Validation: Code review and owner confirmation.

- `pytest -q` expect: characterization and existing tests pass at every commit
- `git grep -n 'old_module_name' -- src | wc -l` expect: 0 references to removed code

Failure modes:
- Refactor changes behavior | detect: Characterization test fails | respond: Revert the step and make it smaller
- Scope grows | detect: Pull request mixes features | respond: Split it
- Old code stays | detect: Dead modules after release | respond: Delete in a follow-up

ILLUSTRATIVE: A hand-written date parser causes repeated bugs. Tests pin its current outputs, calls are moved to the standard library in five small commits, and the parser file is deleted.

Gate: 14-175. Approval: none required

## 176
**Feature Enhancement** (complete). Purpose: decide and deliver an improvement to an existing feature based on evidence of how users actually use it.

Entry criteria: The feature is live and used; Usage data and feedback exist; A product owner owns the backlog

Inputs: usage analytics; user feedback and support tickets; feature goals; delivery capacity

Procedure:
1. Gather evidence: how often and how the feature is used, where users stop, and what they ask for.
2. Write the problem as a user outcome and the metric that should move.
3. List options including doing nothing, estimate effort and risk, and pick one with a reason.
4. Define acceptance criteria and a rollout plan, with a flag for staged release when useful.
5. Ship, then compare the metric with the baseline after a fixed period.
6. Record the result and decide to keep, adjust or roll back.

Deliverables: problem statement with evidence; chosen option and reasoning; acceptance criteria; post-release result

Acceptance: The change targets a stated outcome and metric Alternatives were considered The result is compared with a baseline A keep or rollback decision is recorded

Validation: Product owner decision with stakeholder input.

- manual: compare the metric for the period before release with the period after expect: change reported with the dates used
- manual: confirm each acceptance criterion in staging expect: all pass

Failure modes:
- Request from one loud user | detect: No wider usage evidence | respond: Check data before committing
- No baseline | detect: Cannot tell if it worked | respond: Record the baseline before release
- Feature creep | detect: Scope keeps growing | respond: Hold to the stated outcome

ILLUSTRATIVE: Analytics show 40 percent of users abandon the export dialog at the format choice. Defaulting to the last-used format is shipped behind a flag, and completion is compared two weeks later.

Gate: 14-176. Approval: none required

## 177
**Customer Feedback** (complete). Purpose: collect, understand and act on what customers tell us, so product decisions rest on evidence.

Entry criteria: Feedback channels are identified (support, surveys, reviews, interviews); An owner for feedback triage exists; A backlog or roadmap exists to receive insights

Inputs: feedback from each channel; customer segments and usage data; support ticket themes; current roadmap

Procedure:
1. Gather feedback from every channel into one place with its source and customer segment.
2. Tag each item by theme and severity; merge duplicates and keep counts.
3. Separate what customers asked for from the problem they are trying to solve.
4. Compare themes with usage data to check that loud feedback matches real behavior.
5. Decide per theme: act, investigate, defer or decline, with a reason, and link to backlog items.
6. Tell customers what was decided where practical, and review the outcomes later.

Deliverables: feedback log with themes and counts; insight summary; decisions linked to backlog items; customer follow-up record

Acceptance: Every theme has a decision and a reason Counts and segments are shown Insights are checked against usage data Decisions link to backlog items

Validation: Product owner review of the decisions.

- manual: sample five feedback items and trace each to a theme and decision expect: all traced
- manual: compare the top theme with product usage data expect: data agrees or the disagreement is explained

Failure modes:
- Only the loudest voice is heard | detect: One account dominates the themes | respond: Weight by segment and count
- Feedback never reaches the backlog | detect: No backlog links | respond: Link or decline with a reason
- Requests taken literally | detect: Solutions recorded without the underlying problem | respond: Capture the problem

ILLUSTRATIVE: Forty tickets and two interviews mention slow report exports. Usage data confirms exports over a minute for large accounts. The theme is acted on and linked to a backlog item for background exports.

Gate: 14-177. Approval: none required

## 178
**Knowledge Base** (complete). Purpose: keep accurate, findable answers to recurring questions so users and support solve problems without escalation.

Entry criteria: Recurring questions and incidents are identified from tickets; A knowledge base tool and owners exist; Review process for accuracy exists

Inputs: ticket and incident themes; runbooks and product documentation; release notes; search queries from users

Procedure:
1. Pick the questions that recur most from tickets and search queries.
2. Write each article for a named audience: problem as the user states it, steps, expected result, and when to escalate.
3. Have a subject-matter expert check accuracy and test the steps on a current build.
4. Tag and title articles with the words users actually search for; link related articles.
5. Review articles when the product changes and retire outdated ones.
6. Measure whether articles reduce tickets and fix those that do not.

Deliverables: knowledge base articles; accuracy review record; review schedule; usage and deflection measures

Acceptance: Steps were tested on the current build Each article has an owner and review date Outdated articles are retired Searches for top questions find an article

Validation: Subject-matter expert review of each new article.

- manual: follow each new article's steps on a current build expect: steps work as written
- manual: search the knowledge base for the top five ticket topics expect: each returns the right article first

Failure modes:
- Article describes an old version | detect: Steps fail on current build | respond: Update or retire
- Cannot be found | detect: Search for the user's wording returns nothing | respond: Retitle and retag
- No owner | detect: Owner field empty | respond: Assign owner and review date

ILLUSTRATIVE: The most common ticket is password reset failing for SSO users. An article explains that SSO users reset in their identity provider, with steps and a link, and ticket volume for that topic falls the next month.

Gate: 14-178. Approval: none required

## 179
**Maintenance Release** (complete). Purpose: ship a small, planned release of fixes and low-risk changes with the same controls as any production change.

Entry criteria: Scope is limited to fixes and low-risk changes; Changes are merged, tested and linked to work items; Release manager is assigned

Inputs: list of merged changes; regression and smoke results; release calendar and freeze rules; rollback plan

Procedure:
1. Confirm each change is in scope for a maintenance release and has passed review and tests.
2. Cut the release candidate and run regression and smoke tests against it.
3. Check migration and configuration changes and the rollback plan for the release.
4. Obtain change approval and schedule the window outside freezes.
5. Deploy using the standard path, verify with smoke tests and watch the metrics.
6. Publish release notes and record the outcome.

Deliverables: maintenance release record; test results; change approval; release notes

Acceptance: Only in-scope changes are included Regression and smoke tests passed on the candidate Approval and rollback plan exist Release notes are published

Validation: Release manager decision with change approval where required.

- `git log --oneline v2.3.0..release/2.3.1` expect: every commit maps to an in-scope work item
- `gh run list --branch release/2.3.1 --limit 1 --json conclusion` expect: success

Failure modes:
- A feature slips in | detect: Commit for new functionality in the list | respond: Remove it or move to a feature release
- Skipped testing because the release is small | detect: No regression record | respond: Run it; small releases break too
- No rollback plan | detect: Plan missing | respond: Prepare before approval

ILLUSTRATIVE: Release 2.3.1 contains seven fixes. Regression and smoke tests pass on the candidate, the change board approves a Tuesday window, and the release notes list each fix.

Gate: 14-179. Approval: none required

## 180
**Product Lifecycle Management** (complete). Purpose: manage a product from launch to retirement with decisions made on evidence and communicated to those affected.

Entry criteria: The product is released or planned for release; Usage, revenue or cost data exists; A sponsor accepts decisions on investment and retirement

Inputs: usage and business data; support and maintenance cost; roadmap and strategy; customer commitments

Procedure:
1. Define the lifecycle stages in use (introduce, grow, mature, decline, retire) and the signals for each.
2. Review each product on a regular schedule using the same measures: users, revenue, cost, risk and strategic fit.
3. Decide per product to invest, maintain, simplify or retire, and record the reason with the sponsor.
4. For retirement, plan the notice period, migration path, data handling and support end date.
5. Communicate to customers and internal teams in advance and track who has moved.
6. Shut down in stages, confirm nothing depends on it, and archive records required by policy.

Deliverables: lifecycle review; decision record with sponsor; retirement plan and notices; archive confirmation

Acceptance: Every product has a stage and a decision Retirement has notice, migration and data handling Dependents are identified before shutdown The sponsor approved investment and retirement

Validation: Business sponsor approval.

- manual: check each product in scope has a recorded stage and decision with date expect: no gaps
- manual: confirm for each retirement that no active customers or internal consumers remain expect: none, or exceptions approved

Failure modes:
- Products linger unreviewed | detect: No review in over a year | respond: Schedule reviews with an owner
- Retirement surprises customers | detect: Complaints after shutdown | respond: Extend notice and support
- Hidden dependency | detect: Another system breaks on shutdown | respond: Inventory dependents first

ILLUSTRATIVE: A reporting add-on has 3 percent of users and 15 percent of support load. The sponsor approves retirement with six months notice and a migration guide; usage is tracked until it reaches zero.

Gate: 14-180. Approval: business-sponsor (always)
