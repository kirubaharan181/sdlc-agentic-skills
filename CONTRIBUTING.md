# Contributing

## Setup (about two minutes)
```
pip install jsonschema pytest
make all        # build, validate, references, links, tests, drift check
make demo       # print the plan the library produces for a workflow
```
Everything must pass before you open a pull request. CI runs the same checks and blocks on failure.

## How the repository is organised
- **Edit sources, not generated files.** `registry/*.json`, `registry/workflows/*.json`, `registry/stage-content/*.json`
  and `scripts/execution_profiles.py` are sources. `agents/*.md`, `workflows/*.md`, `skills/**/SKILL.md` and
  `skills/**/reference/` are generated: change the source, then run `make build`. `make check` fails if you hand-edit them.
- Never change stage IDs 1-190 or stage names.
- **Skill documentation is authored in `registry/skill-content/<skill>.json`**, rendered into `SKILL.md` by `make build`. Never edit `SKILL.md` by hand.
- Governance rules live in `docs/governance/`; risk tiers in `registry/risk-tiers.json`; reusable templates in `templates/`.
- Start-here for coding agents: [AGENTS.md](AGENTS.md).

## Good first contributions
- **Prove or correct a stage.** Pick a stage in `registry/stage-content/`, run its validation commands on a real project, and fix the
  procedure, commands or failure modes where they were wrong. Keep the worked example labelled `ILLUSTRATIVE`. Do not reference scripts that do not exist.
- Add a scenario to `tests/scenarios/` or an eval case to `evals/cases/`.
- Run an eval against a model and submit the dated result (see `evals/README.md`).
- See `docs/community/GOOD_FIRST_ISSUES.md`.

## Changing a skill
1. Edit `registry/skill-content/<skill>.json` (start from `templates/skill-content.template.json` for a new one).
2. Bump `version` by the [versioning policy](docs/governance/SKILL_VERSIONING.md): MAJOR contract change, MINOR compatible addition, PATCH wording.
3. `make build`, then `python3 scripts/check_skill_versions.py --update`.
4. Keep the description to 150 characters, with "Use when ..." and "Do not use ...". Keep 2 or more examples (3 for cross-cutting skills), troubleshooting rows with Error / Cause / Resolution, and each responsibility owned by exactly one skill.
5. Add a `CHANGELOG.md` line naming the skill, new version and reason.

## Documentation quality scores
Scores come only from a real SkillEvaluator run. Record them with
`python3 scripts/check_quality_regression.py --add ... --date --source --run-by --library-version`
(see [docs/quality/QUALITY_MANAGEMENT.md](docs/quality/QUALITY_MANAGEMENT.md)). Never estimate, round up or invent a score.
A change that lowers a recorded score beyond tolerance fails `check_quality_regression.py`.

## Approvals, risk and evidence
Changes to approval gates, risk tiers or approver roles must update `registry/risk-tiers.json` and
[docs/governance/](docs/governance/) together, and name the human approver. Use the [templates](templates/README.md) for decisions, risk assessments and handoffs.

## Before you open a pull request
```
make all
python3 scripts/check_skill_versions.py
python3 scripts/check_quality_regression.py
python3 scripts/trace_evidence.py --templates
```
The pull request template lists the checklist. Run the checks on Python 3.11 if you can, because CI uses it.

## Reporting security problems
Do not use public issues. Follow [SECURITY.md](SECURITY.md).

## License of contributions
By submitting a contribution you agree it is licensed under the repository's [MIT License](LICENSE) and that you have the right to submit it.
Do not paste text you copied from sources with incompatible licenses, and do not include secrets or personal data.

## Rules we enforce
- No fabricated evidence, results, adopters or integrations. An example must say `ILLUSTRATIVE` or `"example": true`.
- A platform is "tested" only with a dated log in the pull request; otherwise it stays "documented".
- Every claim in the README must be reproducible by a command.
- Commit messages: `type(scope): summary`, with the reason in the body.
