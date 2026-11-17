# Changelog

All notable changes are recorded here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Summary of the dedupe and integrity work
- **Workflows:** 23 distinct sources in `registry/workflows/*.json` (steps, owners, dependency graph, decisions, failure paths,
  handoffs); the old cloned workflow registry is removed. `new-product-development` covers all 190 stages.
- **Roles:** every stage has a RACI; all 74 roles own at least one stage; role contract fields are derived from RACI and the
  workflow graph; each role has a `permission_tier`; shared rules live in `docs/governance/COMMON_ROLE_POLICY.md`.
- **Skills:** adopted the Anthropic authoring format (name equals id, third-person "Use when" description, short `SKILL.md`,
  `reference/stages.md`, `skills/_shared/CORE_PROCEDURE.md`). Near-duplicate Markdown pairs at 0.80 or higher: 197 to 7.
- **Stage content:** 97 stages are `complete` (`registry/stage-content/`); 93 remain `stub`.
- **Tests and CI:** 35+ pytest tests (unit, golden, scenarios, broken-fixture); CI blocks on duplicates, references, orphans, links.
- **Adoption:** `make demo`, quickstart, evals harness (no model results yet), community files, issue and PR templates.

### Changed
- **Breaking (paths):** registry files renamed from `*.yaml` to `*.json` because they always contained JSON:
  `registry/{SDLC_STAGE,AGENT,SKILL,WORKFLOW}_REGISTRY.json` and `adapters/capability-matrix.json`.
  Update any external tooling that read the old names.
- Registries are stored compactly: shared values live once in `registry/{stage,role,workflow}-defaults.json`;
  `scripts/registry_io.py` resolves them. Resolved records are unchanged.
- Stage status is now explicit (`status: stub|complete`, default `stub`); `generated_on` removed from the stage registry.
- Coverage is reported as several separate measures instead of a single "100%".
- Fourteen stages now require human approval (was 7) and each carries an `approval_rationale`; see `docs/governance/APPROVAL_POLICY.md`.

### Added
- `scripts/audit_duplication.py`, `scripts/check_references.py`, `scripts/build.py`, `Makefile`.
- JSON Schemas in `registry/schemas/`, enforced by `scripts/validate.py`.
- `docs/audit/BASELINE.md` (measured baseline) and `docs/audit/PROGRESS.md`.

### Removed
- Hand-maintained copies of derived data: `registry/SDLC_STAGE_SKILL_MAPPING.csv`, `registry/COVERAGE_REPORT.md`,
  all `references/STAGE_PLAYBOOK.md` and the committed `dashboard/data/library.json`. They are generated into
  `dist/` (git-ignored) by `python scripts/build.py`.
- `.github/workflows/regenerate-library.yml`, which targeted a long-deleted branch and held `contents: write`.

## [1.0.0] - 2026-11-13

Initial evidence-driven library.
