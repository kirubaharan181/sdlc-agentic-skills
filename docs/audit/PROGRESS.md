# Refactor progress

Branch: `refactor/dedupe-and-differentiate`. Updated after each phase. Resume by asking the agent to
"continue from docs/audit/PROGRESS.md".

| Phase | Status | Evidence |
|---|---|---|
| 0 Audit and safety net | done | `docs/audit/BASELINE.md`, `scripts/audit_duplication.py`, `scripts/check_references.py`, report-only CI steps |
| 1 Single source of truth and layout | done | registry renamed to `.json`; `registry_io.py` + defaults; JSON Schemas; `scripts/build.py` (+`--check`) and `Makefile`; derived files moved to `dist/`; dead auto-commit workflow removed |
| 2 Workflows | not started | |
| 3 Roles | not started | |
| 4 Stage content | not started | |
| 5 Skills | not started | |
| 6 Validation, tests, CI | not started | |
| 7 Adoption and community | not started | |

## Decisions
- `agents/*.md`, `workflows/*.md` and `SKILL.md` stay committed (platform adapters install them directly) but are generated; `build.py --check` fails CI on drift. CSV, coverage report and stage playbooks live only in `dist/`.
- Stage `status` defaults to `stub`; nothing is `complete` until Phase 4 content exists.

## Next action
Phase 2: give each workflow its own stages, roles, approvals, inputs, outputs, failure paths; restore `new-product-development` to all 190 stages; add the distinct-stage-list validator rule.
