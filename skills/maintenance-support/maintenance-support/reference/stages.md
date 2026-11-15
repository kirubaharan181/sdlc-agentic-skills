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
**L2 Support** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-168. Approval: none required

## 169
**L3 Support** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

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
**Dependency Updates** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

Gate: 14-172. Approval: none required

## 173
**Database Maintenance** (stub). Purpose: maintain a live service safely and preserve customer continuity.

Inputs: support case or maintenance request; affected versions and customer impact; service ownership and change policy

Procedure:
1. Classify severity, affected customers, workaround and escalation path using support policy.
2. Reproduce against the affected version; correlate logs, metrics and recent changes without exposing customer data.
3. Implement the smallest safe correction or maintenance action with regression and compatibility coverage.
4. Communicate workaround/fix version, verify closure and update runbook or knowledge base.

Deliverables: support/maintenance record; reproduction and diagnosis; fix or patch evidence; customer communication and knowledge update

Acceptance: Customer impact and affected versions are explicit. Fix is verified on supported versions. Operational knowledge is updated and owned.

Validation: Service owner acceptance and customer-facing closure check.

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
