# Refactor progress

Branch: `refactor/dedupe-and-differentiate`. Updated after each phase. Resume by asking the agent to
"continue from docs/audit/PROGRESS.md".

| Phase | Status | Evidence |
|---|---|---|
| 0 Audit and safety net | done | `docs/audit/BASELINE.md`, `scripts/audit_duplication.py`, `scripts/check_references.py`, report-only CI steps |
| 1 Single source of truth and layout | done | registry renamed to `.json`; `registry_io.py` + defaults; JSON Schemas; `scripts/build.py` (+`--check`) and `Makefile`; derived files moved to `dist/`; dead auto-commit workflow removed |
| 2 Workflows | done | 23 distinct sources in `registry/workflows/*.json` (steps+owner+needs DAG, decisions, failure paths, handoffs); `render_workflows.py`; validator rules: distinct stage lists, owners are stage A/R, acyclic, targets resolve, every stage covered, NPD = 190 stages |
| 3 Roles | in progress | RACI on every stage; 0 orphan roles; approvers named. Remaining: derive role contract fields from RACI, ROLE_DECISIONS.md, role similarity rule |
| 4 Stage content | not started | |
| 5 Skills | not started | |
| 6 Validation, tests, CI | not started | |
| 7 Adoption and community | not started | |

## Decisions
- `agents/*.md`, `workflows/*.md` and `SKILL.md` stay committed (platform adapters install them directly) but are generated; `build.py --check` fails CI on drift. CSV, coverage report and stage playbooks live only in `dist/`.
- Stage `status` defaults to `stub`; nothing is `complete` until Phase 4 content exists.

## Next action
Phase 3 remainder: derive role contract fields from RACI/stages, drop `master-orchestration` as default skill, write `docs/audit/ROLE_DECISIONS.md`, add role-similarity (>85%) validator rule.
