# Documentation findings tracker

Findings reported by SkillEvaluator for the 20 skills before the roadmap work (source: the repository owner's run, 2026-11-17;
raw data in `reports/skill-quality/BASELINE_FINDINGS.csv`). "Resolved" means the quality check was re-run
(skillevaluator 1.0.1, 2026-11-19, commit `66e223e`, skills 1.1.1) and reported 0 findings for all 20 skills (`reports/skill-quality/SCORE_HISTORY.csv`).
Tier 1 static findings are tracked separately in `reports/skill-quality/TIER1_RESULTS.csv` and `reports/enhancement/BASELINE_FINDINGS.csv`.

| Finding (evaluator wording) | Skills affected | Severity | Change made | Status |
|---|---:|---|---|---|
| No examples provided | 20 | LOW | 2-3 skill-specific examples per skill in a code block | Resolved (re-measured) |
| SKILL_SPEC recommended field missing: `metadata.author` | 20 | MEDIUM | `metadata.author` in frontmatter | Resolved (re-measured) |
| SKILL_SPEC recommended field missing: `metadata.tags` | 20 | MEDIUM | `metadata.tags` (4 per skill) in frontmatter | Resolved (re-measured) |
| No `## Purpose` section | 20 | LOW | `## Purpose` added | Resolved (re-measured) |
| No prerequisites/requirements documented | 20 | LOW | `## Prerequisites and Requirements` added | Resolved (re-measured) |
| No limitations documented | 20 | LOW | `## Limitations` added | Resolved (re-measured) |
| No troubleshooting section documented | 20 | LOW | `## Troubleshooting` with Error, Cause, Resolution added | Resolved (re-measured) |
| Guide-only skill has very little content (19 lines) | 5 | MEDIUM | Cross-cutting skills expanded with decision rules, quality gates and 3+ examples each | Resolved (re-measured) |
| Description very long (289-353 chars, recommend 50-150) | 15 | LOW | Descriptions rewritten to 50-150 characters, validated | Resolved (re-measured) |
| Broad description without negative triggers | 3 | LOW | Every description states "Do NOT use ..." | Resolved (re-measured) |

## Open

| Item | Why open | Next step |
|---|---|---|
| Re-run SkillEvaluator on all 20 skills | Done 2026-11-20 at `b1b1739`: 20 x 100.0, 0 findings; Tier 1 (no LLM) passes for all 20 | Repeat after any skill change |
| 97+ target | Met by measurement (100.0) for the quality check only; not publication approval | See `reports/enhancement/PUBLICATION_REQUIREMENTS.md` |
| "Publication eligibility: Incomplete" | Criteria read from the evaluator source: needs complete Tier 1, Tier 2, Tier 3 and LLM evidence; Tier 2 (needs an embedding provider API key), Tier 3 and LLM checks not run | `reports/enhancement/PUBLICATION_REQUIREMENTS.md` |
