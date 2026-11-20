# Application security engineering: stage reference (part 4 of 4)

## Contents
- [110 Security Sign-off](#110)

## 110
**Security Sign-off** (complete). Purpose: give a person independent of the implementation the evidence needed to accept the remaining security risk of a release.

Entry criteria: Security stages in scope (threat model, SAST, DAST, SCA, secrets) have recorded results; Open findings and exceptions are listed with owners; Auditor did not implement the controls being reviewed

Inputs: evidence records for security stages; open findings and exception register; threat model residual risks; release scope

Procedure:
1. Collect the evidence record of each security stage and check it names a real commit, command and result.
2. Re-run a sample of the recorded checks independently and compare results.
3. List every open finding, exception and residual risk with owner and expiry; flag any without one.
4. Decide per finding: accept, require fix, or require compensating control; state reasoning.
5. Write the sign-off record: scope, evidence reviewed, sample re-runs, decision, conditions.
6. Submit to the security-lead for the human decision; do not self-approve.

Deliverables: sign-off record; sample re-run results; open risk register; conditions list

Acceptance: Every security stage in scope has evidence or an explicit waiver Sample re-runs agree with recorded results No critical or high finding is open without a security-lead exception Decision and conditions are written and dated

Validation: Security-lead approval of the sign-off record.

- `python3 scripts/check_references.py && python3 scripts/validate.py   # repository integrity before review` expect: both exit 0
- manual: open each stage evidence record and confirm commit, command, result and that it is not flagged example expect: none missing; none flagged example

Failure modes:
- Evidence is illustrative or unrun | detect: Record flagged example or lacks a command and revision | respond: Treat as FAIL for that stage; do not sign off
- Auditor reviewed own work | detect: Auditor appears as implementer in the record | respond: Reassign review to an independent person
- Pressure to ship with open critical findings | detect: Exception without owner or expiry | respond: Decline; escalate to the security-lead

ILLUSTRATIVE: Evidence is complete except one DAST high finding with a fix merged but not retested. The auditor requires the retest as a condition; sign-off is conditional on that passing before release.

Gate: 09-110. Approval: security-lead (always)
