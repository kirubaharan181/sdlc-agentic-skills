# Continuous quality management

How documentation quality of the 20 skills is measured, recorded, protected against regression and owned.

## What is measured, and what is not

NVIDIA SkillEvaluator's quality check scores each `SKILL.md` for correctness (35%), discoverability (25%), reliability (25%)
and efficiency (15%). It measures documentation structure and clarity. It does not run the skills, test engineering
correctness, or certify security. Scores come only from a real evaluator run; nothing in this repository computes or estimates them.

## Records

| Record | Location | Purpose |
|---|---|---|
| Score history | [`reports/skill-quality/SCORE_HISTORY.csv`](../../reports/skill-quality/SCORE_HISTORY.csv) | One row per skill per evaluator run, with date, source, who ran it and the library version |
| Baseline scores and findings | `reports/skill-quality/BASELINE_SCORES.csv`, `BASELINE_FINDINGS.csv` | The measured state before the roadmap work (20 skills, average 87.3, 163 findings) |
| Findings tracker | [FINDINGS_TRACKER.md](FINDINGS_TRACKER.md) | Each finding type, its status and the change that addresses it |
| Change log | `CHANGELOG.md` and skill versions | What changed in which skill and why |
| Version lock | `registry/skill-versions.lock.json` | Released version and content hash per skill |

## Running the evaluator and recording the result

1. Run the SkillEvaluator quality check on each skill path in `registry/SKILL_REGISTRY.json` on a machine where it is installed.
2. For each skill, append one row:
   `python3 scripts/check_quality_regression.py --add <skill> <score> <grade> <C> <D> <R> <E> <findings> --date YYYY-MM-DD --source "SkillEvaluator <version>" --run-by "<name>" --library-version "<git sha>"`
3. Update [FINDINGS_TRACKER.md](FINDINGS_TRACKER.md) from the findings the evaluator printed.
4. Commit the rows with the change that produced them.

The coding agent that edits the documentation can not run the evaluator unless it is installed in its environment. In that case the rows stay unrecorded and
the tracker says "not measured", never an estimate.

## Regression tracking

`python3 scripts/check_quality_regression.py` compares each skill's latest run with its previous run and fails when the
overall score falls by more than 0.5, any dimension falls by more than 5, or the finding count rises. CI runs it, so a
regression recorded in the history blocks a merge. `--summary` prints the latest scores, the average, the lowest, the highest and how many skills are at or above 97.

## Targets

The aim is 97 or higher for every skill. It is a target, not a result. Report actual scores and the remaining findings; if a skill
plateaus, read the evaluator's criteria instead of adding content to chase the number.

## Ownership

| Area | Owner | Path |
|---|---|---|
| Skill content | Repository owner (`CODEOWNERS`) | `registry/skill-content/` |
| Skill renderer and validator | Repository owner | `scripts/render_skills.py`, `scripts/validate.py` |
| Governance standards | Repository owner | `docs/governance/`, `registry/risk-tiers.json` |
| Score history | Whoever runs the evaluator, reviewed by the owner | `reports/skill-quality/` |

`CODEOWNERS` is the source of truth for review. Add a named co-owner there when more maintainers join.

## Review cadence

- Each skill change: version bump, lock update, changelog line, `make all`.
- Each release: run the evaluator on all 20 skills and append the rows.
- Each quarter: review the findings tracker, the decision rules and examples for drift from the registries.
