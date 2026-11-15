# Refactor progress

Branch: `refactor/dedupe-and-differentiate`. Updated after each phase. Resume by asking the agent to
"continue from docs/audit/PROGRESS.md".

| Phase | Status | Evidence |
|---|---|---|
| 0 Audit and safety net | done | `docs/audit/BASELINE.md`, `scripts/audit_duplication.py`, `scripts/check_references.py`, report-only CI steps |
| 1 Single source of truth and layout | done | registry renamed to `.json`; `registry_io.py` + defaults; JSON Schemas; `scripts/build.py` (+`--check`) and `Makefile`; derived files moved to `dist/`; dead auto-commit workflow removed |
| 2 Workflows | done | 23 distinct sources in `registry/workflows/*.json` (steps+owner+needs DAG, decisions, failure paths, handoffs); `render_workflows.py`; validator rules: distinct stage lists, owners are stage A/R, acyclic, targets resolve, every stage covered, NPD = 190 stages |
| 3 Roles | done | RACI on every stage; 0 unassigned roles; role contract fields derived from RACI, stage skills/approvers and workflow graph; `permission_tier` per role; shared policy in `docs/governance/COMMON_ROLE_POLICY.md`; `docs/audit/ROLE_DECISIONS.md` (all 74 kept, 0 merged/removed); fixed profile-regex bug (license-compliance got the audit contract); validator rejects role pairs >=0.85 similar, `master-orchestration` as role skill, unassigned roles |
| 4 Stage content | done (first tranche) | 25 Tier-1 stages authored in `registry/stage-content/*.json` (entry criteria, inputs, procedure, deliverables, acceptance, validation, failure modes, worked example), `status: complete`; 165 remain honest stubs; validator forbids `complete` without full content, missing scripts in commands, procedures >70% similar |
| 5 Skills | in progress | Skills moved to the Anthropic best-practice format: `name` = id, third-person `Use when` descriptions, <60-line `SKILL.md`, `reference/stages.md` per skill, `skills/_shared/CORE_PROCEDURE.md`; validator enforces it. Near-duplicate pairs >=0.80: 197 -> 7 (all role contracts). Remaining: labelled illustrative evidence examples, per-skill examples, similarity rule for skills |
| 6 Validation, tests, CI | not started | |
| 7 Adoption and community | not started | |

## Decisions
- `agents/*.md`, `workflows/*.md` and `SKILL.md` stay committed (platform adapters install them directly) but are generated; `build.py --check` fails CI on drift. CSV, coverage report and stage playbooks live only in `dist/`.
- Stage `status` defaults to `stub`; nothing is `complete` until Phase 4 content exists.

## Next action
Phase 5 remainder: labelled illustrative evidence examples per skill (`"example": true`), skill similarity rule. Then Phase 6 (pytest unit/golden/broken-fixture tests, scenario tests, flip report-only CI to blocking) and Phase 7 (adoption files, PR, v1.1.0 RC).
