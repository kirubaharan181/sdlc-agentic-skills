# Refactor progress

Branch: `refactor/dedupe-and-differentiate`. Updated after each phase. Resume by asking the agent to
"continue from docs/audit/PROGRESS.md".

| Phase | Status | Evidence |
|---|---|---|
| 0 Audit and safety net | done | `docs/audit/BASELINE.md`, `scripts/audit_duplication.py`, `scripts/check_references.py`, report-only CI steps |
| 1 Single source of truth and layout | done | registry renamed to `.json`; `registry_io.py` + defaults; JSON Schemas; `scripts/build.py` (+`--check`) and `Makefile`; derived files moved to `dist/`; dead auto-commit workflow removed |
| 2 Workflows | done | 23 distinct sources in `registry/workflows/*.json` (steps+owner+needs DAG, decisions, failure paths, handoffs); `render_workflows.py`; validator rules: distinct stage lists, owners are stage A/R, acyclic, targets resolve, every stage covered, NPD = 190 stages |
| 3 Roles | done | RACI on every stage; 0 unassigned roles; role contract fields derived from RACI, stage skills/approvers and workflow graph; `permission_tier` per role; shared policy in `docs/governance/COMMON_ROLE_POLICY.md`; `docs/audit/ROLE_DECISIONS.md` (all 74 kept, 0 merged/removed); fixed profile-regex bug (license-compliance got the audit contract); validator rejects role pairs >=0.85 similar, `master-orchestration` as role skill, unassigned roles |
| 4 Stage content | done: 190 of 190 authored (not run on a real project) | 25 Tier-1 stages plus batch 2 of 12 (102, 72, 90, 112, 120, 130, 150, 166, 170, 185, 34, 16) batch 3 of 12 (68, 75, 131, 85, 127, 139, 147, 168, 169, 172, 173, 152) batch 4 of 12 (27, 177, 178, 179, 162, 149, 86, 13, 67, 71, 81, 57) batch 5 of 12 (113, 114, 115, 116, 119, 124, 125, 171, 108, 142, 26, 58) batch 6 of 12 (84, 91, 92, 95, 103, 109, 118, 121, 123, 126, 134, 140) batch 7 of 12 (54, 55, 65, 70, 73, 76, 144, 155, 156, 157, 161, 167) batch 8 of 12 (1, 2, 4, 6, 7, 174, 175, 176, 180, 186, 188, 190) batch 9 of 12 (3, 8, 9, 10, 11, 12, 14, 15, 18, 19, 20, 21) batch 10 of 12 (23, 24, 29, 30, 32, 35, 36, 38, 39, 40, 41, 42) batch 11 of 12 (44, 45, 46, 47, 48, 52, 56, 59, 60, 61, 62, 63) batch 12 (64, 66, 74, 78, 82, 83, 87, 88, 89, 93, 94, 96), batch 13 (97, 104, 105, 106, 107, 122, 135, 136, 141, 143, 145) and batch 14 (146, 151, 153, 154, 159, 181, 182, 183, 187, 189) authored in `registry/stage-content/*.json` (entry criteria, inputs, procedure, deliverables, acceptance, validation, failure modes, worked example), `status: complete`; final batch (5, 17, 22, 25, 28, 31, 33, 37, 43, 49, 51, 53) authored; 0 stubs remain, but none of the content has been run on a real project; validator forbids `complete` without full content, missing scripts in commands, procedures >70% similar |
| 5 Skills | done | name=id, third-person `Use when` descriptions, short `SKILL.md`, `reference/stages.md`, shared `_shared/CORE_PROCEDURE.md`; per-skill generated evidence examples flagged `"example": true` / `ILLUSTRATIVE_ONLY`; validator: skills <0.70 similar, examples never PASS |
| 6 Validation, tests, CI | done | 32 pytest tests (unit, golden metrics, 6 scenarios, 7 broken-fixture); `check_links.py`; CI now blocks on duplicate audit (0.85), references + orphans, links, pytest; stage `status` complete\|stub validated |
| 7 Adoption and community | done (except owner-gated items) | `make demo`, quickstart, recorded demo + test, evals harness (no model results), CONTRIBUTING, CODE_OF_CONDUCT, templates, CODEOWNERS, 15 drafted issues, launch drafts, CHANGELOG, RC notes. Done: 15 good-first issues opened (#15-#29). Not done: tag/release (blocked for this session), posting, repo topics. Adapters remain documented, not tested |
| 8 Roadmap: quality and governance | done on branch `feat/roadmap-quality-governance`; after-scores not measured | `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md`, `reports/skill-quality/`, `docs/governance/`, `registry/skill-content/`, `tests/test_governance.py` |

## Decisions
- `agents/*.md`, `workflows/*.md` and `SKILL.md` stay committed (platform adapters install them directly) but are generated; `build.py --check` fails CI on drift. CSV, coverage report and stage playbooks live only in `dist/`.
- Stage `status` defaults to `stub`; nothing is `complete` until Phase 4 content exists.

## Next action
Open the PR (do not merge), then owner review. Owner decisions: tag v1.1.0-rc.1, open the drafted issues, repo topics, any launch posts.
