# Changelog

All notable changes are recorded here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
