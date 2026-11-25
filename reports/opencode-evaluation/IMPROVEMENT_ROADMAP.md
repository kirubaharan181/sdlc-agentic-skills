# Improvement Roadmap

**Evaluation date:** 2026-11-24
**Scope:** Recommended changes identified during this read-only evaluation.
**Status:** Not implemented (initial evaluation is read-only; no changes made to skill definitions).

---

## P0 — Immediate blockers

None. No CRITICAL or HIGH-severity library defects were found. All skills respect human-approval boundaries and none perform destructive or unsafe actions.

## P1 — High-priority fixes

| # | Affected files | Recommended change | Expected benefit | Complexity | Validation criteria |
|---|---|---|---|---|---|
| P1-1 | `skills/cloud-hosting-operations/`, `skills/devops-platform/`, `skills/enterprise-governance/`, `skills/sre-observability/` (and test harness) | Provide simulated provider/test backends or document required live infrastructure; execute each skill in a provisioned environment and record transcripts. | Completes execution coverage for 4/20 skills currently BLOCKED; raises confidence in production readiness. | Medium | Transcripts for all 4 skills with PASS/PARTIAL PASS statuses; `--check` still passes. |
| P1-2 | `docs/agent-guide/OPENCODE_USAGE.md`, `scripts/install.py` | Make the OpenCode restart-after-install requirement explicit and prominent; test a fresh OpenCode process start after install to confirm detection. | Removes ambiguity about when skills become available; avoids false "discovery works" claims. | Low | Fresh-process install + detection test passes; documentation updated. |

## P2 — Quality improvements

| # | Affected files | Recommended change | Expected benefit | Complexity | Validation criteria |
|---|---|---|---|---|---|
| P2-1 | `tests/scenarios/` | Add executable scenario fixtures mapped to each skill (illustrative examples made runnable where safe). | Turns illustrative examples into reproducible verification; strengthens evidence-over-assertion. | Medium | `python3 -m pytest -q` passes; each scenario has a recorded result. |
| P2-2 | `skills/*/*/SKILL.md` | Add per-skill "tested in OpenCode: yes/no + test ID" pointer to the execution transcript index. | Makes evidence traceability immediate for consumers of the library. | Low | TRANSCRIPT_INDEX.md references every skill; cross-links present. |
| P2-3 | `skills/engineering-governance/` | Add branching-policy document and CI-enforced lint/format config (if the repo is to serve as a production template); otherwise document governance enforcement as out of scope. | Clarifies whether governance gaps are intentional or omissions. | Low/Medium | engineering-governance re-test shows governance artifacts present or explicitly out of scope. |
| P2-4 | `reports/skill-quality/SCORE_HISTORY.csv` | Note that SkillEvaluator quality scores (recorded 100.0 for all 20 skills at commits 66e223e / b1b1739) are documentation-quality snapshots, not execution evidence. | Prevents conflating documentation scores with OpenCode execution results. | Low | Report clarifies distinction. |

## P3 — Future enhancements

| # | Affected files | Recommended change | Expected benefit | Complexity | Validation criteria |
|---|---|---|---|---|---|
| P3-1 | OpenCode integration | Request/implement OpenCode skill-activation telemetry so skill invocation is observable rather than inferred. | Direct, auditable evidence of skill activation. | High (platform-level) | OpenCode exposes per-skill invocation events. |
| P3-2 | `scripts/select_skill.py` | Run the keyword skill-selector against each executed test scenario and confirm it selects the same skill the test used. | Validates the skill-selection engine against real usage. | Low | `select_skill.py "<scenario>"` returns the expected skill for each test scenario. |
| P3-3 | CI workflow | Add an OpenCode compatibility job that installs skills and runs a subset of safe execution tests on PRs. | Continuous compatibility assurance. | Medium | CI job passes on main; new skills are tested before merge. |
| P3-4 | `adapters/COMPATIBILITY.md` | Expand to a per-platform capability matrix (OpenCode / Codex / Claude Code) noting discovery, loading, restart, and telemetry support. | Clear cross-platform expectations. | Low | Matrix published and matches observed behavior. |

---

## Implementation note

All P0–P3 items are recommendations only. Per AGENTS.md and the evaluation rules, no changes were made to the original skill definitions during this initial evaluation, and no commits/pushes/releases were created. A named human approver is required before any production-relevant change (see `docs/governance/APPROVAL_POLICY.md`).
