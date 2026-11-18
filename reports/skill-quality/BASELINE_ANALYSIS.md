# Baseline analysis

Source: NVIDIA SkillEvaluator quality check, run by the repository owner on 2026-11-17 against `main` at `a8be547`
(before the roadmap work). The raw numbers are in `BASELINE_SCORES.csv` and `BASELINE_FINDINGS.csv`. Nothing below is
estimated; counts were recomputed from those files.

## Scores

- 20 skills; average 87.3; none at 97 or above.
- 12 skills scored 88.5 (grade B), 3 scored 87.2, 5 scored 84.5 (the cross-cutting skills: `master-orchestration`,
  `evidence-quality-gates`, `secure-change-control`, `definition-of-done`, `incident-command`).
- 163 findings: 20 skills had the same eight recurring findings, plus length and breadth findings on some.

## Findings by pattern

| Findings | Severity | Dimension | Pattern |
|---|---|---|---|
| 20 | LOW | correctness | No examples |
| 20 | LOW | discoverability | No `## Purpose` section |
| 20 | LOW | reliability | No limitations |
| 20 | LOW | reliability | No prerequisites |
| 20 | LOW | reliability | No troubleshooting |
| 20 | MEDIUM | correctness | `metadata.author` missing |
| 20 | MEDIUM | correctness | `metadata.tags` missing |
| 15 | LOW | discoverability | Description too long (recommended 50-150 characters) |
| 5 | MEDIUM | correctness | Guide-only skill with very little content (about 19 lines) |
| 3 | LOW | discoverability | Broad description without negative triggers |

## Reading the baseline

- The findings are structural, and uniform across skills. A single content model and a single renderer can fix them at once,
  instead of editing 20 files by hand. That is why skill documentation moved into `registry/skill-content/<skill>.json`.
- The five weakest skills were thin guides, so they needed real content (decision rules, quality gates, examples, troubleshooting), not only headings.
- Efficiency scored 100 everywhere; correctness (85) and reliability (85) held the scores down.
- The evaluator checks documentation quality. It does not run the skills, so a high score would not show that a skill works.
