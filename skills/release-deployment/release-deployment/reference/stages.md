# Release and deployment control: stage reference

## Contents
- [126 Release Planning](#126)
- [127 Release Notes](#127)
- [128 Release Readiness](#128)
- [129 Change Approval](#129)
- [130 Staging Deployment](#130)
- [131 Staging Validation](#131)
- [132 Database Migration](#132)
- [133 Production Deployment](#133)
- [134 Domain & DNS](#134)
- [135 SSL/TLS Setup](#135)
- [136 Load Balancer Setup](#136)
- [137 Rollback Planning](#137)
- [138 Production Smoke Test](#138)
- [139 Deployment Sign-off](#139)

## 126
**Release Planning** (stub). Purpose: prepare and execute a controlled release or migration.

Inputs: release candidate digest and scope; change approvals and readiness evidence; rollback/recovery and communication plan

Procedure:
1. Confirm immutable candidate, included changes, compatibility and outstanding risk.
2. Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
3. Obtain change authority and communicate schedule, impact, owners and stop conditions.
4. Deploy progressively, verify health and business signals, then confirm or execute recovery.

Deliverables: release manifest; readiness checklist; deployment and migration evidence; post-deploy verification

Acceptance: Deployed digest matches approved candidate. Migration and recovery are rehearsed. Stop/rollback thresholds and authority are explicit.

Validation: Change authority approval and post-deploy verification.

Gate: 11-126. Approval: none required

## 127
**Release Notes** (stub). Purpose: communicate the exact behavior and operational impact of a release.

Inputs: approved change list and issue links; target audience and supported version; known issues and rollout schedule

Procedure:
1. Group changes by user-visible capability, fixes, security and operational impact.
2. Describe behavior changes, compatibility/deprecation and required customer actions accurately.
3. Include known issues, upgrade notes and links to support guidance.
4. Verify every statement against the approved candidate and obtain product/support review.

Deliverables: versioned release notes; upgrade and known-issue notes; review approval

Acceptance: Notes match the actual candidate contents. Breaking changes and user actions are explicit. No unverified capability claim is published.

Validation: Compare release notes with the merged change list and candidate digest.

Gate: 11-127. Approval: none required

## 128
**Release Readiness** (complete). Purpose: decide whether a specific build is ready to go to production, using recorded evidence rather than opinion.

Entry criteria: Release candidate build exists with an immutable id; Test, security and migration stages for the scope have results; Release manager is not the sole implementer

Inputs: release candidate id and scope; test and security evidence; open defect list; rollback and monitoring plans

Procedure:
1. List every change in the release and link to its evidence.
2. Check each required gate has a PASS with a commit and command, or an approved waiver.
3. Review open defects and exceptions; each must be accepted by its owner.
4. Confirm rollback plan, monitoring and on-call coverage exist for the release window.
5. Confirm communications and support readiness.
6. Record GO, NO-GO or CONDITIONAL with reasons and send to change approval (stage 129).

Deliverables: release readiness checklist; evidence index; go/no-go record; open risk list

Acceptance: Every required gate has evidence or an approved waiver No critical defect is open Rollback and monitoring are confirmed Decision is recorded with its reasons

Validation: Go/no-go reviewed in the change approval step.

- `python3 scripts/check_references.py && python3 scripts/validate.py   # repository integrity if the release includes registry changes` expect: both exit 0
- manual: open each evidence link and confirm it names the release candidate id expect: all links resolve and match the candidate id

Failure modes:
- Evidence belongs to a different build | detect: Commit in evidence differs from candidate | respond: Treat as missing evidence; NO-GO until rerun
- Waivers without owner | detect: Waiver lacks owner or expiry | respond: Reject the waiver
- Readiness decided in a meeting without a record | detect: No go/no-go record | respond: Write the record before proceeding

ILLUSTRATIVE: All gates pass except a medium accessibility defect with an owner and fix date. The decision is CONDITIONAL: ship, with the fix tracked in the next release.

Gate: 11-128. Approval: none required

## 129
**Change Approval** (complete). Purpose: have the named change authority approve or reject a production change after seeing its risk, evidence and rollback.

Entry criteria: Release readiness has a GO or CONDITIONAL record; Change window is proposed; Change-board members are available

Inputs: change request; readiness record and evidence index; risk assessment; rollback plan and window

Procedure:
1. Submit the change request with scope, risk, window, rollback and monitoring owner.
2. Check for conflicts with other changes or freezes in the window.
3. Change board reviews the evidence; asks for missing items rather than assuming them.
4. Board decides approve, reject or approve with conditions; the decision is recorded with names and time.
5. Approval is bound to the specific release id and window; a different build needs a new approval.
6. Notify implementers, support and stakeholders of the decision.

Deliverables: change request record; board decision with conditions; conflict check; notification

Acceptance: Decision is made by the named approver, not the requester Approval names the release id and window Conditions are written and tracked Conflicts were checked

Validation: Change-board decision.

- manual: compare release id in the approval with the build to be deployed expect: identical
- manual: confirm approver is not the requester or implementer expect: different people

Failure modes:
- Approval reused for a different build | detect: Release id differs | respond: Approval void; resubmit
- Requester approves own change | detect: Requester equals approver | respond: Reject; route to the board
- Window conflicts with a freeze | detect: Calendar overlap | respond: Reschedule

ILLUSTRATIVE: A config change to payment retries is approved for Tuesday 02:00 with the condition that the on-call SRE watches error rate for one hour afterwards.

Gate: 11-129. Approval: change-board (always)

## 130
**Staging Deployment** (stub). Purpose: prepare and execute a controlled release or migration.

Inputs: release candidate digest and scope; change approvals and readiness evidence; rollback/recovery and communication plan

Procedure:
1. Confirm immutable candidate, included changes, compatibility and outstanding risk.
2. Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
3. Obtain change authority and communicate schedule, impact, owners and stop conditions.
4. Deploy progressively, verify health and business signals, then confirm or execute recovery.

Deliverables: release manifest; readiness checklist; deployment and migration evidence; post-deploy verification

Acceptance: Deployed digest matches approved candidate. Migration and recovery are rehearsed. Stop/rollback thresholds and authority are explicit.

Validation: Change authority approval and post-deploy verification.

Gate: 11-130. Approval: none required

## 131
**Staging Validation** (stub). Purpose: prepare and execute a controlled release or migration.

Inputs: release candidate digest and scope; change approvals and readiness evidence; rollback/recovery and communication plan

Procedure:
1. Confirm immutable candidate, included changes, compatibility and outstanding risk.
2. Validate staging environment, migrations, monitoring, backup and rollback/forward-fix rehearsal.
3. Obtain change authority and communicate schedule, impact, owners and stop conditions.
4. Deploy progressively, verify health and business signals, then confirm or execute recovery.

Deliverables: release manifest; readiness checklist; deployment and migration evidence; post-deploy verification

Acceptance: Deployed digest matches approved candidate. Migration and recovery are rehearsed. Stop/rollback thresholds and authority are explicit.

Validation: Change authority approval and post-deploy verification.

Gate: 11-131. Approval: none required

## 132
**Database Migration** (complete). Purpose: change the production database schema or data safely, with verified backups and a path back.

Entry criteria: Migration script is reviewed and tested on a production-like copy; Backup or snapshot plan exists; DBA owner is named

Inputs: migration scripts; test results on a copy; backup and restore procedure; expected duration and locking impact

Procedure:
1. Review the script for locks, long transactions and irreversible steps; prefer additive, expand-then-contract changes.
2. Run on a production-sized copy; record duration and locking.
3. Take and verify a backup or snapshot; prove restore works.
4. Obtain DBA-owner approval for the window.
5. Run the migration with monitoring; stop on error thresholds.
6. Verify schema and data checks after; keep the rollback or forward-fix ready until the observation window ends.

Deliverables: migration plan; copy-run report; verified backup record; post-migration verification

Acceptance: Restore from backup was tested Duration and locking are within the window Verification queries pass DBA owner approved

Validation: DBA-owner approval before running in production.

- `psql -f migrations/0042_add_index.sql --single-transaction -v ON_ERROR_STOP=1   # example on the copy` expect: exit 0; duration recorded
- `psql -c "SELECT count(*) FROM orders WHERE new_col IS NULL"   # example check` expect: expected count after the migration

Failure modes:
- Migration locks a hot table | detect: Copy run shows long locks | respond: Redesign (online or batched) before approval
- Backup not restorable | detect: Restore test fails | respond: BLOCKED until a restorable backup exists
- Irreversible change without plan | detect: No rollback or forward-fix | respond: Reject

ILLUSTRATIVE: Adding a column with a default is done in two steps: add nullable, backfill in batches, then add the constraint. Copy run shows no long locks; restore of last night's snapshot is verified.

Gate: 11-132. Approval: dba-owner (always)

## 133
**Production Deployment** (complete). Purpose: put the approved build into production by an authorized, repeatable path with health checks and stop conditions.

Entry criteria: Change approval exists for this release id and window; Artifact digest matches the approved release; Rollback plan is ready and monitoring is watched

Inputs: approved release id and artifact digest; deployment runbook; health checks and stop thresholds; rollback plan

Procedure:
1. Verify the artifact digest equals the approved one and that the window is open.
2. Deploy with the pipeline using the approved strategy (rolling, canary or blue-green).
3. Watch error rate, latency and saturation against the stop thresholds during rollout.
4. Proceed in steps; stop and roll back if a threshold is crossed.
5. Record start and end times, versions and who deployed.
6. Hand over to the smoke test (stage 138).

Deliverables: deployment record; health metrics during rollout; version inventory; handover to smoke test

Acceptance: Deployed digest equals the approved digest Thresholds stayed within limits or rollback occurred Deployment is recorded Production approver authorized the deployment

Validation: Production-approver authorization before start.

- `kubectl rollout status deployment/app --timeout=10m   # example` expect: successfully rolled out
- `kubectl get deployment app -o jsonpath='{.spec.template.spec.containers[0].image}'` expect: image digest equals the approved digest

Failure modes:
- Wrong artifact deployed | detect: Digest mismatch | respond: Roll back and redeploy the approved artifact
- Error rate climbs during rollout | detect: Alert or threshold breach | respond: Stop and roll back per plan
- Deployment outside the window | detect: Timestamp outside the approved window | respond: Stop; get new approval

ILLUSTRATIVE: A canary receives 5 percent of traffic for ten minutes with stable error rate and latency, then proceeds to 100 percent; the digest check matches the approved release.

Gate: 11-133. Approval: production-approver (always)

## 134
**Domain & DNS** (stub). Purpose: configure secure and resilient network edge routing.

Inputs: domain ownership and target topology; certificate and trust requirements; traffic and health-check profile

Procedure:
1. Verify domain/account ownership and change window.
2. Configure records, certificates, ciphers, health checks, routing and origin restrictions.
3. Validate propagation, certificate chain/expiry, redirects and failover behavior.
4. Document TTL, renewal, rollback and monitoring.

Deliverables: DNS/TLS/routing configuration; validation output; renewal and rollback runbook

Acceptance: No unexpected public exposure. Certificate chain and hostname validation pass. Failover and rollback are tested.

Validation: Network/security review.

Gate: 11-134. Approval: none required

## 135
**SSL/TLS Setup** (stub). Purpose: configure secure and resilient network edge routing.

Inputs: domain ownership and target topology; certificate and trust requirements; traffic and health-check profile

Procedure:
1. Verify domain/account ownership and change window.
2. Configure records, certificates, ciphers, health checks, routing and origin restrictions.
3. Validate propagation, certificate chain/expiry, redirects and failover behavior.
4. Document TTL, renewal, rollback and monitoring.

Deliverables: DNS/TLS/routing configuration; validation output; renewal and rollback runbook

Acceptance: No unexpected public exposure. Certificate chain and hostname validation pass. Failover and rollback are tested.

Validation: Network/security review.

Gate: 11-135. Approval: none required

## 136
**Load Balancer Setup** (stub). Purpose: configure secure and resilient network edge routing.

Inputs: domain ownership and target topology; certificate and trust requirements; traffic and health-check profile

Procedure:
1. Verify domain/account ownership and change window.
2. Configure records, certificates, ciphers, health checks, routing and origin restrictions.
3. Validate propagation, certificate chain/expiry, redirects and failover behavior.
4. Document TTL, renewal, rollback and monitoring.

Deliverables: DNS/TLS/routing configuration; validation output; renewal and rollback runbook

Acceptance: No unexpected public exposure. Certificate chain and hostname validation pass. Failover and rollback are tested.

Validation: Network/security review.

Gate: 11-136. Approval: none required

## 137
**Rollback Planning** (complete). Purpose: decide in advance how to undo a release and prove the undo works.

Entry criteria: Release scope and deployment method are known; Data and schema changes in the release are identified; Previous version is available

Inputs: release scope; deployment method; schema and data change list; previous version artifact

Procedure:
1. For each component, state the rollback action and its time limit.
2. Mark changes that cannot be rolled back (data migrations, external side effects) and define a forward-fix instead.
3. Define the trigger conditions and who decides.
4. Test the rollback in a non-production environment and record the time taken.
5. Confirm the previous version, config and secrets are still available.
6. Add the plan to the readiness record.

Deliverables: rollback plan; trigger conditions and decision owner; rollback test record; forward-fix notes

Acceptance: Every component has a rollback or forward-fix Rollback test succeeded and time is recorded Triggers and decision owner are named Irreversible steps are called out

Validation: Rollback rehearsal in a non-production environment.

- `kubectl rollout undo deployment/app && kubectl rollout status deployment/app   # example rehearsal in staging` expect: previous version running; time recorded
- manual: confirm the previous artifact digest is still pullable expect: pull succeeds

Failure modes:
- Plan untested | detect: No rehearsal record | respond: Rehearse before approval
- Schema change blocks rollback | detect: Old version fails on new schema | respond: Use expand-then-contract or define a forward-fix
- Nobody owns the decision | detect: No named owner | respond: Assign owner

ILLUSTRATIVE: Rollback of the service takes four minutes in staging. The additive schema change is left in place because the old version ignores the new column.

Gate: 11-137. Approval: none required

## 138
**Production Smoke Test** (complete). Purpose: confirm right after deployment that the critical user journeys work in production.

Entry criteria: Deployment finished; Smoke checks are defined and safe to run in production; Test accounts exist

Inputs: list of critical journeys; production test accounts; health dashboards; rollback trigger conditions

Procedure:
1. Run read-only or safely reversible checks for each critical journey with test accounts.
2. Compare key metrics with the pre-deployment baseline.
3. Check logs for new error types.
4. Record result per journey as PASS or FAIL with evidence.
5. On any critical failure trigger rollback per plan.
6. Report outcome to the release manager and keep watch through the observation window.

Deliverables: smoke test results; metric comparison; log check; outcome report

Acceptance: All critical journeys pass or rollback was triggered Metrics are within baseline limits No new error class in logs Results are recorded with times

Validation: Rerun of the failed check after any fix.

- `curl -fsS https://app.example.com/healthz   # example; replace with the real health URL` expect: HTTP 200 and expected body
- manual: complete login and one read-only purchase-history view with the test account expect: page loads with expected data

Failure modes:
- Smoke test creates real data | detect: Test leaves records | respond: Use dedicated test accounts and cleanup
- Checks run too early | detect: Pods not ready | respond: Wait for readiness then rerun
- Failure ignored | detect: FAIL without rollback or decision | respond: Escalate to release manager

ILLUSTRATIVE: After release, login, search and order history each respond within normal latency; the error rate matches the baseline for fifteen minutes.

Gate: 11-138. Approval: none required

## 139
**Deployment Sign-off** (stub). Purpose: prepare a controlled decision with sufficient evidence and independent authority.

Inputs: decision request and accountable sponsor; impact/risk assessment; supporting evidence and alternatives

Procedure:
1. Check the decision request is complete, in scope and owned by an authorized requester.
2. Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
3. Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
4. Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

Deliverables: decision record; evidence index; conditions and waiver log

Acceptance: Decision authority is verified. Conditions are measurable, owned and time-bound. No missing or failed critical evidence is silently waived.

Validation: Independent approval record and audit trail.

Gate: 11-139. Approval: none required
