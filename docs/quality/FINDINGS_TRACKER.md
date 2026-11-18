# Documentation findings tracker

Findings reported by SkillEvaluator for the 20 skills before the roadmap work (source: the repository owner's run, 2026-11-17;
raw data in `reports/skill-quality/BASELINE_FINDINGS.csv`). "Addressed" means the repository now contains the content the
finding asked for. It does not mean the evaluator confirmed it: **the evaluator has not been rerun on the new documentation.**

| Finding (evaluator wording) | Skills affected | Severity | Change made | Status |
|---|---:|---|---|---|
| No examples provided | 20 | LOW | 2-3 skill-specific examples per skill in a code block | Addressed, not re-measured |
| SKILL_SPEC recommended field missing: `metadata.author` | 20 | MEDIUM | `metadata.author` in frontmatter | Addressed, not re-measured |
| SKILL_SPEC recommended field missing: `metadata.tags` | 20 | MEDIUM | `metadata.tags` (4 per skill) in frontmatter | Addressed, not re-measured |
| No `## Purpose` section | 20 | LOW | `## Purpose` added | Addressed, not re-measured |
| No prerequisites/requirements documented | 20 | LOW | `## Prerequisites and Requirements` added | Addressed, not re-measured |
| No limitations documented | 20 | LOW | `## Limitations` added | Addressed, not re-measured |
| No troubleshooting section documented | 20 | LOW | `## Troubleshooting` with Error, Cause, Resolution added | Addressed, not re-measured |
| Guide-only skill has very little content (19 lines) | 5 | MEDIUM | Cross-cutting skills expanded with decision rules, quality gates and 3+ examples each | Addressed, not re-measured |
| Description very long (289-353 chars, recommend 50-150) | 15 | LOW | Descriptions rewritten to 50-150 characters, validated | Addressed, not re-measured |
| Broad description without negative triggers | 3 | LOW | Every description states "Do NOT use ..." | Addressed, not re-measured |

## Open

| Item | Why open | Next step |
|---|---|---|
| Re-run SkillEvaluator on all 20 skills | Needs the evaluator installed | Run it, append rows to `SCORE_HISTORY.csv`, update this table |
| 97+ target | Not measured | Judge after the rerun; address remaining findings by reading the evaluator's criteria |
| "Publication eligibility: Incomplete" | Reported by the evaluator for Tier 1; the criteria were not part of the supplied output | Read the evaluator's publication criteria and record the gaps |
