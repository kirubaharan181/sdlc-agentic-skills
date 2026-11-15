# Refactor progress

Branch: `refactor/dedupe-and-differentiate`. Updated after each phase. Resume by asking the agent to
"continue from docs/audit/PROGRESS.md".

| Phase | Status | Evidence |
|---|---|---|
| 0 Audit and safety net | done | `docs/audit/BASELINE.md`, `scripts/audit_duplication.py`, `scripts/check_references.py`, report-only CI steps |
| 1 Single source of truth and layout | done | registry renamed to `.json`; `registry_io.py` + defaults; JSON Schemas; `scripts/build.py` (+`--check`) and `Makefile`; derived files moved to `dist/`; dead auto-commit workflow removed |
| 2 Workflows | done | 23 distinct sources in `registry/workflows/*.json` (steps+owner+needs DAG, decisions, failure paths, handoffs); `render_workflows.py`; validator rules: distinct stage lists, owners are stage A/R, acyclic, targets resolve, every stage covered, NPD = 190 stages |
| 3 Roles | done | RACI on every stage; 0 unassigned roles; role contract fields derived from RACI, stage skills/approvers and workflow graph; `permission_tier` per role; shared policy in `docs/governance/COMMON_ROLE_POLICY.md`; `docs/audit/ROLE_DECISIONS.md` (all 74 kept, 0 merged/removed); fixed profile-regex bug (license-compliance got the audit contract); validator rejects role pairs >=0.85 similar, `master-orchestration` as role skill, unassigned roles |
| 4 Stage content | in progress (37 of 190 complete) | 25 Tier-1 stages plus a second batch of 12 (102, 72, 90, 112, 120, 130, 150, 166, 170, 185, 34, 16) authored in `registry/stage-content/*.json` (entry criteria, inputs, procedure, deliverables, acceptance, validation, failure modes, worked example), `status: complete`; 165 remain honest stubs; validator forbids `complete` without full content, missing scripts in commands, procedures >70% similar |
| 5 Skills | done | name=id, third-person `Use when` descriptions, short `SKILL.md`, `reference/stages.md`, shared `_shared/CORE_PROCEDURE.md`; per-skill generated evidence examples flagged `"example": true` / `ILLUSTRATIVE_ONLY`; validator: skills <0.70 similar, examples never PASS |
| 6 Validation, tests, CI | done | 32 pytest tests (unit, golden metrics, 6 scenarios, 7 broken-fixture); `check_links.py`; CI now blocks on duplicate audit (0.85), references + orphans, links, pytest; stage `status` complete\|stub validated |
| 7 Adoption and community | done (except owner-gated items) | `make demo`, quickstart, recorded demo + test, evals harness (no model results), CONTRIBUTING, CODE_OF_CONDUCT, templates, CODEOWNERS, 15 drafted issues, launch drafts, CHANGELOG, RC notes. Not done, owner-gated: tag/release, opening issues, posting, repo topics. Adapters remain documented, not tested |

## Decisions
- `agents/*.md`, `workflows/*.md` and `SKILL.md` stay committed (platform adapters install them directly) but are generated; `build.py --check` fails CI on drift. CSV, coverage report and stage playbooks live only in `dist/`.
- Stage `status` defaults to `stub`; nothing is `complete` until Phase 4 content exists.

## Next action
Open the PR (do not merge), then owner review. Owner decisions: tag v1.1.0-rc.1, open the drafted issues, repo topics, any launch posts.
