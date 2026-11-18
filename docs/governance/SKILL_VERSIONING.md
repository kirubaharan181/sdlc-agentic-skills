# Skill versioning policy

Each skill has a version in `registry/skill-content/<skill>.json` (`version`), rendered as `metadata.version` in its `SKILL.md`.
Versions use semantic versioning, applied to the skill's contract: what it asks for, what it produces and who it hands to.
The repository version is in `VERSION` and is independent of skill versions.

## When to bump

| Bump | Change | Examples |
|---|---|---|
| MAJOR | The contract changes in a way that breaks users or other skills | Required input added or removed; output format changed; a responsibility moved to another skill; a skill renamed, split or removed; a handoff removed |
| MINOR | New capability or guidance that is compatible | New example, decision rule, prerequisite or quality gate; new optional input; new handoff; clarified scope that does not move ownership |
| PATCH | Wording, typo or correction that does not change behavior | Fix a sentence; correct a limitation; adjust a keyword |

When unsure between two levels, choose the higher one.

## Procedure

1. Edit `registry/skill-content/<skill>.json`.
2. Bump `version` according to the table.
3. Run `python3 scripts/build.py` to regenerate `SKILL.md` and `docs/architecture/SKILL_SELECTION.md`.
4. Run `python3 scripts/check_skill_versions.py --update` to record the new version and content hash.
5. Add a line under the unreleased section of `CHANGELOG.md` naming the skill, the new version and the reason.
6. Run `make all`.

## Enforcement

`python3 scripts/check_skill_versions.py` fails when a skill's content changed without a higher version, when a version was
bumped without recording it, or when a version changed without a content change. CI runs it.

## Deprecation and removal

1. Mark the skill deprecated in its `purpose` and add the replacement to `when_not_to_use`; bump MINOR.
2. Keep it for at least one minor release of the repository.
3. Remove it in a MAJOR change: update the registries, stage skill assignments, handoffs, `CHANGELOG.md` and the lock file together.

## Compatibility promise

Skill ids (the `name`) are stable. Renaming a skill is a MAJOR change that needs an alias note in `CHANGELOG.md`. Stage ids 1-190 and stage names never change.
