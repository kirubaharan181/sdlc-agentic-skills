# Baseline audit

Repository `kirubaharan181/sdlc-agentic-skills`, `main` at `79384e0` (after PR #40). Findings use the evidence listed; see `BASELINE_FINDINGS.csv` for the full table with status.

## What was inspected

| Area | Method | Result |
|---|---|---|
| Canonical registries (190 stages, 74 roles, 20 skills, 23 workflows) | `scripts/validate.py` | pass |
| Stage workflow references | script comparing every `workflow_ids` entry to the 23 workflow IDs | all resolve; README's mismatch note was stale (F-001) |
| Generated-file drift | `scripts/build.py --check` | no drift |
| Skill frontmatter | parse every `SKILL.md` frontmatter as YAML | 2 of 20 invalid (F-003) |
| Skill documentation quality | SkillEvaluator 1.0.1 `quality-check` | 19 x 100.0, `secure-change-control` 96.2 (F-004); reproduced at `79384e0` |
| Skill static checks | SkillEvaluator 1.0.1 `tier1 --no-llm` | 5 pass, 15 incomplete or failed (F-005 to F-008) |
| Score history | read `SCORE_HISTORY.csv` | no commit, skill version or evaluator version (F-015) |
| GitHub About | `gh api repos/...` | no description or topics (F-014) |

## Not inspected or not run

Application behavior, deployments, external services, agent platforms (Codex, Claude Code), Tier 2 and Tier 3 evaluation, LLM-based checks.
No real project was used to test any skill.

## Existing capabilities preserved

Registry sources of truth, generated outputs, selection engine (lexical), dependency graph, handoff and evidence contracts, risk tiers, version lock, regression tracking, templates. None were rebuilt.
