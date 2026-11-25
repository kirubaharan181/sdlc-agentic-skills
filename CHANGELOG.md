# Changelog

All notable changes are recorded here. Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versioning: [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Evaluation
- OpenCode evaluation reports added under `reports/opencode-evaluation/` with an independent review that corrects overstated evidence; OpenCode status is "discovery observed once; behaviour not tested". CONTRIBUTING now documents branching and merging.

### Release tooling
- `make_release.py` also writes `UNCOMPRESSED_TAR_SHA256` (stable across zlib versions) after finding that the v1.1.0 `.tar.gz` bytes differ on rebuild while the contents are identical. See `reports/enhancement/RELEASE_v1.1.0.md`.

### Contributor tooling
- `make new-skill` / `scripts/new_skill.py`: scaffold a skill draft in `registry/skill-drafts/`, check it (schema, no placeholders, trigger-first description, handoff targets, keyword overlap) and print the promotion checklist. Drafts are not built or published.

## [1.1.0] - 2026-11-24

First stable release after the quality, governance and agent-compatibility work. Evaluator results: 20 skills scored 100.0 by
SkillEvaluator 1.0.1 `quality-check` and passing Tier 1 without an LLM (recorded runs, not publication approval; Tier 2, Tier 3 and
LLM checks not run). Agent behaviour in Codex, OpenCode and other tools is documented but **not tested**.

### Release
- `scripts/make_release.py` and `release.yml`: reproducible archive plus `SHA256SUMS` on a version tag.

### Dashboard
- New offline "Find a skill" page: ranks a described task with the same terms, weights and incident rule as `scripts/select_skill.py` (parity tested).

### CI
- `skill-quality.yml`: runs SkillEvaluator 1.0.1 `quality-check` (minimum 100) and Tier 1 without an LLM on every skill when skills or registries change. Static checks only; not publication approval.

### Agent installers
- `scripts/install.py`: copy or symlink the standalone skills into the folders Codex (`.agents/skills`), OpenCode (`.opencode/skills`) and Claude Code (`.claude/skills`) read, with `--check` drift verification. New OpenCode usage guide.

### Atelier dashboard (static snapshot)
- Skill/stage detail views, stage risk tiers, governance risk-tier and recorded-quality panels, real source commit in the data snapshot.
- Accessibility: skip link, focus styles, dialog roles, keyboard-operable cards and rows; stage rows now open their detail drawer.

### Summary of the dedupe and integrity work
- **Workflows:** 23 distinct sources in `registry/workflows/*.json` (steps, owners, dependency graph, decisions, failure paths,
  handoffs); the old cloned workflow registry is removed. `new-product-development` covers all 190 stages.
- **Roles:** every stage has a RACI; all 74 roles own at least one stage; role contract fields are derived from RACI and the
  workflow graph; each role has a `permission_tier`; shared rules live in `docs/governance/COMMON_ROLE_POLICY.md`.
- **Skills:** adopted the Anthropic authoring format (name equals id, third-person "Use when" description, short `SKILL.md`,
  `reference/stages.md`, `skills/_shared/CORE_PROCEDURE.md`). Near-duplicate Markdown pairs at 0.80 or higher: 197 to 7.
- **Stage content:** 190 stages are `complete` (`registry/stage-content/`); none remain `stub`.
- **Tests and CI:** 35+ pytest tests (unit, golden, scenarios, broken-fixture); CI blocks on duplicates, references, orphans, links.
- **Adoption:** `make demo`, quickstart, evals harness (no model results yet), community files, issue and PR templates.

### Scanner advisories
- **Changed (stage examples, meaning unchanged):** `npx` examples use `npx --no-install` (project-installed tools only, no remote download); the DNS example uses resolver host names instead of a public IP. Tier 1 (no LLM) still passes for all 20 skills on this branch (re-run before merge; not added to the score history because skill text did not change).

### Evaluator findings and reconciliation (skills 1.1.1)
- **Fixed:** `application-security` and `incident-command` had invalid YAML frontmatter (unquoted `: ` in the description). Descriptions are now double-quoted and the validator enforces it.
- **Changed:** all 20 descriptions lead with "Use when" (trigger visible in short skill lists); `secure-change-control` no longer uses a vague word. All skills are at 1.1.1.
- **Changed (layout):** each skill is standalone: `reference/` is now `references/`, `examples/` moved to `references/examples/`, `CORE_PROCEDURE.md` and `HANDOFF_CONTRACT.md` are bundled per skill, and SKILL.md no longer links outside its folder. This lets SkillEvaluator's security scan complete.
- **Changed (stage text, meaning unchanged):** stages 50, 103 and 125 reworded where scanner patterns misread them.
- **Measured:** skillevaluator 1.0.1 on commit `66e223e`: quality-check 20 x 100.0, 0 findings; Tier 1 static checks (no LLM) pass for 19 of 20 skills.
- **Fixed:** `application-security` stage reference is split into four parts (`references/stages-part-N.md`) because SkillSpector stops analysing a file with too many shell expressions; content unchanged. Re-run on `b1b1739`: quality-check 20 x 100.0, Tier 1 (no LLM) passes for all 20 skills. Publication eligibility is not claimed (Tier 2, Tier 3 and LLM checks not run).
- **Quality history:** rows now carry skill version, source commit and evaluator version; `--add` requires them.
- **Docs:** README quality and registry statements corrected; `reports/enhancement/` added (audit, findings, publication requirements, reconciliation, validation, readiness).

### Roadmap: skill quality and governance (skills 1.1.0)
- **Skills:** all 20 skills restructured from `registry/skill-content/<skill>.json` (Purpose, When to Use / NOT, Prerequisites, Inputs and Outputs, Decision Rules, Quality Gates, 2-3 examples, Limitations, Troubleshooting, Handoffs); `metadata.author`, `version`, `tags`; descriptions 132-147 characters with "Use when" and "Do not use". Baseline SkillEvaluator average was 87.3; **post-change scores not measured**. Every skill is at version 1.1.0.
- **Skill intelligence:** `scripts/select_skill.py` (lexical selector), `scripts/skill_graph.py`, generated `docs/architecture/SKILL_SELECTION.md`; acyclic forward handoffs; one owner per responsibility.
- **Governance:** risk tiers R0-R4 (`registry/risk-tiers.json`), approval and escalation matrix, evidence traceability, decision log, conflict resolution, handoff contract standard, audit readiness, skill versioning (`registry/skill-versions.lock.json`).
- **Quality tracking:** `reports/skill-quality/` (baseline, history, comparison, remaining findings, scope), `scripts/check_quality_regression.py`.
- **Agents:** `AGENTS.md`, `docs/agent-guide/CODEX_USAGE.md`, templates for task requests, results, decisions, risk, change and incidents. Codex use is documented, not tested.
- **Policy files:** full MIT `LICENSE`, `SECURITY.md` (private reporting, scope, no certification claim), `CONTRIBUTING.md` (skill workflow), PR template, CODEOWNERS, Dependabot for GitHub Actions.
- **CI and Makefile:** new checks for skill versions, quality regression and templates (`make governance`).
- **Performance:** validator near-duplicate comparison uses a shingle prefilter (about 2 minutes to about 8 seconds on this repository).

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
