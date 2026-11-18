# Remaining findings

| # | Finding | Status | Next step |
|---|---|---|---|
| 1 | No post-change SkillEvaluator score for any skill | open: not measured | Run SkillEvaluator on the 20 skills; `python3 scripts/check_quality_regression.py --add ...` per skill |
| 2 | 97+ target unverified | open | Decide after measurement; fix whatever the evaluator reports |
| 3 | Baseline findings "addressed" but not re-measured | open | Same run; update `docs/quality/FINDINGS_TRACKER.md` |
| 4 | Skill examples are illustrative and have not been run in a real project | open | Dated runs by contributors (issues #27-#29) |
| 5 | Selection engine is lexical, not semantic | known limitation | Add cases to the golden tests when real misroutes are found; do not claim semantic routing |
| 6 | Codex and other adapters documented, not tested | open | Independent runner with a dated log |
| 7 | 190 stages authored, none run on a real project | open | Contributors: prove or correct a stage |
| 8 | GitHub private vulnerability reporting disabled | open, owner action | Enable in repository settings |
| 9 | `LICENSE` holder is the GitHub handle | open, owner action | Confirm or replace with a legal name |
| 10 | Release tag `v1.1.0-rc.1` not created | open, owner action | Create tag and release |
