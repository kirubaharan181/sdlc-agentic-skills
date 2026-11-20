# Quality reconciliation

| Run | Commit | Skill versions | Evaluator | Result | Recorded in history |
|---|---|---|---|---|---|
| Baseline (owner-supplied, 2026-11-17) | `a8be547` | unversioned | not recorded | 20 skills, average 87.3, none at 97+, 163 findings | yes (baseline rows) |
| Interim run (2026-11-18) | `79384e0` | 1.1.0 | skillevaluator 1.0.1 | 19 x 100.0; `secure-change-control` 96.2 (discoverability 85, "vague words") | no: superseded; `secure-change-control` reproduced on a checkout of `79384e0` |
| Run (2026-11-19) | `66e223e` | 1.1.1 | skillevaluator 1.0.1, skillspector 2.13.4 | 20 x 100.0, 0 quality findings; Tier 1 19 of 20 | yes (20 rows) |
| Final run (2026-11-20) | `b1b1739` | 1.1.1 | skillevaluator 1.0.1, skillspector 2.13.4 | 20 x 100.0, 0 quality findings; Tier 1 20 of 20 | yes (20 rows) |

Notes:

- The baseline and later runs may have used different evaluator versions or settings; the baseline's version was not recorded. The comparison shows direction, not a controlled experiment.
- "Findings resolved" means the quality-check no longer reports them in the final run. Findings from Tier 1 are tracked separately in `TIER1_RESULTS.csv`.
- README claims were updated to cite the final run only. No claim relies on the interim run.
- Reproduce: `skillevaluator quality-check skills/<group>/<skill> -r json -o <dir>` on commit `b1b1739` (or its squash-merged equivalent; scores depend on skill text, which the squash preserves).
