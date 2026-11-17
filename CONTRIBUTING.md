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

## Good first contributions
- **Prove or correct a stage.** Pick a stage in `registry/stage-content/`, run its validation commands on a real project, and fix the
  procedure, commands or failure modes where they were wrong. Keep the worked example labelled `ILLUSTRATIVE`. Do not reference scripts that do not exist.
- Add a scenario to `tests/scenarios/` or an eval case to `evals/cases/`.
- Run an eval against a model and submit the dated result (see `evals/README.md`).
- See `docs/community/GOOD_FIRST_ISSUES.md`.

## Rules we enforce
- No fabricated evidence, results, adopters or integrations. An example must say `ILLUSTRATIVE` or `"example": true`.
- A platform is "tested" only with a dated log in the pull request; otherwise it stays "documented".
- Every claim in the README must be reproducible by a command.
- Commit messages: `type(scope): summary`, with the reason in the body.
