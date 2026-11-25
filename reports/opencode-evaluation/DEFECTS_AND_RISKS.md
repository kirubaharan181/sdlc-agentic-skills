# Defects and Risk Analysis

**Evaluation date:** 2026-11-24
**Read-only evaluation:** No defects were fixed; all issues documented with recommended fixes. No root cause is claimed as proven unless directly evidenced.

---

## Severity definitions

- CRITICAL: Security compromise, data loss, or severe unsafe behavior.
- HIGH: Major integration failure or important workflow failure.
- MEDIUM: Significant usability, correctness, or reliability problem.
- LOW: Minor documentation or formatting problem.
- INFORMATIONAL: Improvement opportunity.

---

## Issues

### ISS-001 — Four skills cannot be executed without external infrastructure (BLOCKED)

- **Affected skills:** cloud-hosting-operations, devops-platform, enterprise-governance, sre-observability
- **File:** `skills/<group>/<skill>/SKILL.md` (each)
- **Evidence:** Execution test results; these skills require cloud account access (cloud-hosting-operations), a CI/CD platform + secrets store (devops-platform), a control framework + org evidence access (enterprise-governance), and telemetry sources + observability platform (sre-observability). None are available in this read-only eval environment.
- **Expected behavior:** Each skill is exercisable end-to-end and produces real output.
- **Actual behavior:** Could not be tested; execution success = 0; status BLOCKED.
- **Root cause:** Environment limitation (external services not provisioned), not a library defect.
- **Severity:** HIGH (execution coverage incomplete for 4 of 20 skills)
- **Reproduction:** Attempt to run any end-to-end scenario for these skills without cloud/CI/telemetry access.
- **Recommended fix:** Provide test fixtures / simulated provider backends, or document that these skills require live infrastructure and are validated separately in a staging environment.
- **Validation needed:** Execute each BLOCKED skill against a provisioned environment and record transcripts.

### ISS-002 — OpenCode skill discovery requires a restart after installation

- **Affected:** Installation / OpenCode integration
- **File:** `scripts/install.py` (line 105: "Restart the agent so it rescans its skill folders"); `docs/agent-guide/OPENCODE_USAGE.md`
- **Evidence:** Installer output instructs restart; OpenCode auto-detected skills only after installation in this session.
- **Expected behavior:** Newly installed skills available immediately, or discovery clearly documented as requiring restart.
- **Actual behavior:** Restart required; not re-verified as a separate fresh-process test.
- **Root cause:** OpenCode scans skill folders at startup; documented limitation.
- **Severity:** MEDIUM
- **Reproduction:** Install a new skill into `.opencode/skills` without restarting OpenCode; check whether it is advertised.
- **Recommended fix:** Document the restart requirement prominently (already done); consider a refresh/reload mechanism if OpenCode provides one.
- **Validation needed:** Fresh OpenCode process start after install; confirm detection without manual cache clear.

### ISS-003 — Examples labelled illustrative are not executable evidence

- **Affected:** All 20 skills (each SKILL.md "Examples" section)
- **File:** `skills/*/*/SKILL.md`
- **Evidence:** Every SKILL.md examples section states "Illustrative only: these show expected behavior and were not executed against a real project." AGENTS.md rule 3 and README confirm examples are never PASS.
- **Expected behavior:** Examples should not be mistaken for proof of execution.
- **Actual behavior:** Examples are not executed; this is by design (evidence-over-assertion rule).
- **Root cause:** Intentional design choice.
- **Severity:** INFORMATIONAL
- **Reproduction:** N/A (design choice).
- **Recommended fix:** None required; maintain the illustrative labelling. Optionally add executable scenario fixtures in `tests/scenarios/` mapped to each skill.
- **Validation needed:** N/A.

### ISS-004 — No per-skill invocation telemetry exposed by OpenCode

- **Affected:** OpenCode integration
- **File:** N/A (OpenCode platform behavior)
- **Evidence:** Execution transcripts label results as instruction-following observed via the agent's own execution, not as OpenCode tool telemetry.
- **Expected behavior:** Observable evidence that a specific skill was activated.
- **Actual behavior:** No skill-invocation telemetry available; activation inferred from output matching the skill's procedure.
- **Root cause:** Platform limitation.
- **Severity:** MEDIUM
- **Reproduction:** N/A (platform behavior).
- **Recommended fix:** Record execution transcripts (as done here) as the evidence substitute; request OpenCode skill-activation logging if available.
- **Validation needed:** N/A.

### ISS-005 — Branching policy and lint enforcement not present in repository (observed gap, by design)

- **Affected:** engineering-governance
- **File:** repository root; `skills/engineering-governance/engineering-governance/SKILL.md`
- **Evidence:** engineering-governance TEST-013 found a single `main` branch, no branching-policy document, no enforced linter/format config; VERSION file and tags present.
- **Expected behavior:** A production repo template would document branching and enforce standards via CI.
- **Actual behavior:** Gaps honestly reported (not fabricated).
- **Root cause:** This is a skills/documentation library, not an application repo; some governance artifacts are out of scope.
- **Severity:** LOW (context-dependent; not a defect in the library itself)
- **Reproduction:** engineering-governance TEST-013 steps.
- **Recommended fix:** Add a branching-policy document and CI-enforced linting if the repository is to be used as a production template; otherwise document that governance enforcement is out of scope for this library.
- **Validation needed:** engineering-governance re-test after adding policy/CI.

### ISS-006 — No CRITICAL or FAIL defects found; remaining risk is incomplete execution evidence

- **Affected:** All skills
- **File:** N/A
- **Evidence:** 16 of 20 skills executed with PASS/PARTIAL PASS; 0 FAIL; 0 CRITICAL defects.
- **Expected behavior:** Full execution evidence for all 20 skills.
- **Actual behavior:** 4 skills BLOCKED on external dependencies.
- **Severity:** INFORMATIONAL
- **Reproduction:** N/A.
- **Recommended fix:** See ISS-001; provision a test environment with cloud/CI/telemetry simulators to complete execution coverage.
- **Validation needed:** Execute the 4 BLOCKED skills.

---

## Risk summary

| Risk | Severity | Disposition |
|---|---|---|
| Incomplete execution coverage (4/20 skills BLOCKED) | HIGH | Documented; requires provisioned environment to close. |
| OpenCode restart needed after install | MEDIUM | Documented; not a defect. |
| No per-skill invocation telemetry | MEDIUM | Transcripts serve as evidence substitute. |
| Branching/lint gaps in repo | LOW | Context-dependent (library, not app repo). |
| No critical safety defects | — | None found; all skills respect human-approval boundaries. |

No CRITICAL defects. No HIGH-severity library defects (ISS-001 is environment-driven, not a library defect). The library is safe and well-structured; the principal gap is execution coverage for infrastructure-dependent skills.
