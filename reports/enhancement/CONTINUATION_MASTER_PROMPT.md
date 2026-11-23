# SDLC Agentic Skills: Detailed Continuation Master Prompt (v2)

Paste everything below the dashed line into a new Claude chat. It is self-contained.

---

You are continuing a long-running engineering project with me (Kiruba, GitHub `kirubaharan181`). Read this whole brief first. Do not restart or re-audit finished work. Start at Part 6 (In Progress) and then follow Part 7 (Roadmap).

## PART 1. PROJECT IDENTITY

- Repo: `kirubaharan181/sdlc-agentic-skills` (clone it; use the `add_repo` tool if it is not attached). Default branch `main`.
- Purpose: a portable library of SDLC agentic skills. It maps 190 SDLC stages to 20 skills, 74 agent role contracts and 23 workflows. 19 stages carry a risk tier. Agents are role contracts, not necessarily running agents.
- Audience: engineers and AI coding agents (Claude, Codex and similar) who need a stage-aware procedure, handoffs and quality gates.
- Owner goals: a trustworthy, evidence-backed, publication-ready library; honest reporting; low maintenance burden.

## PART 2. ARCHITECTURE (how the repo works)

Single source of truth, generated everything else:

| Layer | Source (edit these) | Generated (never hand-edit) |
|---|---|---|
| Stages, categories, roles | canonical JSON in `registry/` (stage registry) | derived fields, docs |
| Skill content | `registry/skill-content/<skill>.json` | `skills/<skill>/SKILL.md`, `references/`, examples |
| Risk tiers | `registry/risk-tiers.json` | stage `risk_tier` in dashboard data |
| Versions | `registry/skill-versions.lock.json` (all skills 1.1.1) | n/a |
| Selection guide | registries | `docs/architecture/SKILL_SELECTION.md` |
| Distribution | registries | `dist/` |
| Dashboard data | registries + `reports/skill-quality/SCORE_HISTORY.csv` | `dashboard/data/library.json` (git-ignored build output) |

Key scripts in `scripts/`: `build.py` (`--check` fails on drift and on non-identical consecutive builds), `render_skills.py` (skill content to SKILL.md; frontmatter `description` is always a double-quoted JSON string), `rebuild_library.py` (writes references and bundled copies), `validate.py`, `audit_duplication.py` (bundled `CORE_PROCEDURE.md` and `HANDOFF_CONTRACT.md` are exempt), `select_skill.py` (selection engine; incident wording such as "production is down" forces `incident_first`), `skill_graph.py`, `check_skill_versions.py`, `check_quality_regression.py` (`--add` requires all seven traceability options), `generate_dashboard_data.py`, `run_tests.py`.

Commands: `make all` (build, validate, tests, drift check) and `make governance`. Tests: `python -m pytest tests -q` (61 pass on Python 3.13 and 3.11). Dashboard checks: `python -m json.tool dashboard/data/library.json` and `node --check dashboard/assets/app.js`.

Skill layout rule (standalone skills): `SKILL.md` links only to files inside its own folder; supporting files live in `references/` (including bundled shared copies and `references/examples/`). There is no `reference/` or top-level `examples/` folder. `application-security` is split into four stage files (`SPLIT_STAGE_REFERENCE = {"application-security": 4}`) because the scanner has a per-file analysis budget (`static_parse_limit`).

Dashboard "Atelier": static HTML, CSS and vanilla JS in `dashboard/` (`index.html`, `assets/app.js`, `assets/styles.css`), deployed by `.github/workflows/pages.yml`. `app.js` is compact, with single-line functions; be careful when editing it.

## PART 3. STANDING RULES (from the owner; obey always)

1. Git: I authorise you to commit, push, pull and merge yourself. Use feature branches. Never force-push. Wait for green CI. Squash-merge through `gh api`, then sync local `main`. Commit messages end with the attribution lines the environment's system reminder specifies; PR bodies end with the line "🤖 Generated with [Claude Code](https://claude.com/claude-code)" plus the session link if one is given.
2. Evidence: no fabricated scores, results or evidence. Every score row must be traceable (skill version, source commit, evaluator version).
3. Claims: never claim security certification or publication eligibility. A quality score of 100 is not publication approval. Use the verdict wording in `FINAL_READINESS_REPORT.md` ("QUALITY VALIDATION PASSED") unless every required tier has passed with complete evidence.
4. Scope: static validation only. No application, integration, end-to-end or deployment tests. No paid external services without asking me.
5. Privacy: never share my email address anywhere (repo files, PRs, reports).
6. Dashboard: keep it a static snapshot, not a live console; no unnecessary dependencies.
7. Reports: planning and audit reports go in `reports/enhancement/`; evidence goes in `reports/skill-quality/`.
8. Process: use a task list, verify before claiming done, finish every reply with "completed" and "clear next steps". If the repo disagrees with this brief, trust the repo and tell me.
9. Ask me before: changing the author email, folder layout (F-010), license holder name, version numbers or tags, spending money, or anything irreversible.

## PART 4. WHAT IS COMPLETED (chronological)

### Stage 0. Early roadmap (phases A–E, ten items), PR #40 merged
- Enhanced `LICENSE` (MIT, holder "kirubaharan181 and contributors"), `SECURITY.md`, `CONTRIBUTING.md`.
- Added `AGENTS.md` (agent entry point), `docs/agent-guide/CODEX_USAGE.md`, `.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/dependabot.yml`.
- Saved requirements and roadmap in `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md`; created `docs/quality/FINDINGS_TRACKER.md`.

### Stage 1. Master Improvement Prompt (phases A–M), PRs #46, #47, #48 merged
- Baseline audit: `BASELINE_AUDIT.md`, `BASELINE_FINDINGS.csv` (F-001 to F-015). Status: F-008 resolved; F-012 partially resolved; F-009 and F-014 blocked on owner action; F-010, F-011, F-013 open advisories.
- Skill intelligence and governance layer: selection engine, skill graph, risk tiers, version lock, score-history regression guard, policy-file tests.
- Skill rewrite to the standalone layout described in Part 2; trigger-first descriptions ("Use when …"); descriptions always quoted so the YAML is valid.
- Real quality measurement with NVIDIA SkillEvaluator 1.0.1 (skillspector 2.13.4): `quality-check` and `tier1 --no-llm`. Results: baseline average 87.3 at commit `a8be547`; interim run at `66e223e`; latest at `b1b1739` where all 20 skills score 100.0 and Tier 1 passes 20/20.
- Reports: `IMPLEMENTATION_SUMMARY.md`, `FILE_CHANGE_MATRIX.csv`, `VALIDATION_RESULTS.md`, `PUBLICATION_REQUIREMENTS.md`, `QUALITY_RECONCILIATION.md`, `FINAL_READINESS_REPORT.md` (includes suggested GitHub About description and topics). In `reports/skill-quality/`: `SCORE_HISTORY.csv`, `SKILL_SCORE_COMPARISON.csv`, `TIER1_RESULTS.csv`, `BASELINE_*.csv`, `IMPROVEMENT_SUMMARY.md`, `REMAINING_FINDINGS.md`, `VALIDATION_SCOPE.md`.
- Dependabot PRs #44, #41, #45 merged. #42 and #43 (GitHub Pages actions) intentionally not merged until a Pages deploy is watched.

### Lessons and fixes worth remembering
- Evaluator's `quality-check` missed invalid YAML (unquoted `: ` in two descriptions). Fixed by always quoting, plus a validator check and a test.
- Tier 1 was incomplete when SKILL.md linked outside its folder. Fixed by the standalone layout.
- Scanner false positives were reworded; failure-mode hits and one untagged Docker-image hit in `devops-platform` remain and are documented.
- Running the duplicate audit and pytest at the same time caused a spurious failure; run them sequentially.
- The GitHub About and topics write returned 403 through the proxy; it needs the owner.
- Fonts from fonts.googleapis.com are blocked in the sandbox; harmless for tests.

### Stage 2. Phase I, Atelier dashboard (done on a branch, not yet merged)
Commits `08cbb5f` and `2b5df8b` on `feat/atelier-dashboard-governance`, pushed. Local gate passed (`make all`, 61 tests, `node --check`, `json.tool`).
- Data: real source commit, per-skill version, description, tags, owned responsibilities, handoffs, limitations, recorded quality; per-stage risk tier; `governance` block (risk tiers; quality summary of 20 skills recorded, average 100.0, with an explicit note).
- UI: richer skill cards and detail drawer (quality labelled "Recorded result, not live. Not publication approval."), stage risk tier, search over descriptions and tags, governance page with risk and quality panels, "Static snapshot / Generated from the registries, not live" label.
- Accessibility: skip link, `:focus-visible` outlines, `aria-label`s, `role="dialog" aria-modal`, status toast, keyboard activation (Enter or Space) for cards and rows, focus returns to content when the drawer closes.
- Bug fix: stage table rows never opened the detail drawer (the click binding was missing in `rows()`); fixed with a delegated handler and verified in headless Chromium with mouse and keyboard.
- Tests: two new tests in `tests/test_governance.py` (enriched data; accessible static page).

## PART 5. CURRENT STATE SNAPSHOT

- `main` contains PRs #40, #46, #47, #48 and Dependabot #44, #41, #45.
- Branch `feat/atelier-dashboard-governance` is pushed; **no PR is open yet, so it is not merged**.
- Desktop and mobile (390px, dark) governance-page screenshots were captured with zero console errors, but the images were **not visually reviewed**.
- Evaluator venv from the old session is gone; reinstall `SkillEvaluator` in a fresh venv when needed.

## PART 6. IN PROGRESS: do this first, without asking

1. Pull the repo; confirm state with `git branch -a`, `git log --oneline -5`, open PRs.
2. Re-run the gate on the dashboard branch: `make all`, `node --check dashboard/assets/app.js`, `python -m json.tool dashboard/data/library.json`.
3. Visual review with Playwright (Chromium and Playwright are preinstalled; do not reinstall): serve `dashboard/` with `python3 -m http.server`, take screenshots of Overview, Stages, Skills, a skill drawer, a stage drawer and Governance in light and dark, at 1280 and 390 widths. Fix layout problems found (overflow, clipped text, contrast).
4. Open the PR with `gh api` (title "feat(dashboard): governance, skill detail, accessibility"). Wait for green CI on Python 3.13 and 3.11.
5. Squash-merge and sync `main`.
6. Record Phase I: add a dashboard section to `IMPLEMENTATION_SUMMARY.md`, rows to `FILE_CHANGE_MATRIX.csv`, a `CHANGELOG` entry (create one if missing), a README dashboard note and the dashboard result in `VALIDATION_RESULTS.md`. Branch, gate, PR, merge.
7. Report "completed / next steps".

## PART 7. ROADMAP (phases still to do, in order)

Each phase: goal, tasks, acceptance criteria. Mark proposals that need my approval.

### Phase 6. Dashboard completion and Pages
- Goal: the dashboard is merged, accurate and deployed.
- Tasks: finish Part 6; confirm `.github/workflows/pages.yml` publishes `dashboard/` including generated `library.json` and that links resolve under the repo sub-path; check that the Pages deployment settings are enabled (owner action if not); then evaluate Dependabot #42/#43 only after a watched deploy.
- Acceptance: PR merged; Pages run green; the live page loads with no console errors; snapshot timestamp and commit are shown; no dependency added.
- Optional extras (ask first): a print-friendly governance view; a "copy skill install path" button; a deep-link hash for each skill or stage.

### Phase 7. Open findings and advisories
- Goal: every finding has an owner decision recorded.
- Tasks: F-010 (folder nesting advisory), F-011 (`## Instructions` heading advisory), F-013 (author email advisory), F-012 (finish), F-009 and F-014 (blocked; restate exactly what the owner must do). Present options with trade-offs; wait for my decision before touching the email or folder layout. Update `BASELINE_FINDINGS.csv`, `FINDINGS_TRACKER.md`, `REMAINING_FINDINGS.md`.
- Acceptance: no finding is left without a status, reason and next action.

### Phase 8. Regression guard and CI hardening
- Goal: quality cannot silently drop.
- Tasks: CI job that runs `check_quality_regression.py` against `SCORE_HISTORY.csv`; a documented "re-run the evaluator after any skill change" procedure in `CONTRIBUTING.md`; confirm the PR template has a checklist for versions, risk tier and score row; add a drift check for `docs/architecture/SKILL_SELECTION.md` if missing; pin action versions; review Dependabot grouping.
- Acceptance: a deliberately bad skill change in a scratch branch fails CI (do not merge it); documentation describes the loop.

### Phase 9. Publication readiness
- Goal: know exactly what stands between the library and "publication-eligible".
- Tasks: re-read `PUBLICATION_REQUIREMENTS.md`; list required tiers. Tier 2 needs an embedding API key (NVIDIA Build or OpenAI): ask me whether to provide one; do not use paid services otherwise. Tier 3 and LLM checks have not been run: report them as "not run". Prepare a one-page evidence pack index mapping each requirement to the file or command that proves it.
- Acceptance: the verdict stays "QUALITY VALIDATION PASSED" unless all required tiers pass with complete evidence; then and only then use eligibility wording, and still do not claim certification.

### Phase 10. Release hygiene
- Goal: a clean first public release.
- Tasks: propose a version and tag (ask me to confirm); release notes from the CHANGELOG; README tables regenerated from `SCORE_HISTORY.csv`; link check; confirm About description and topics were set by me; confirm LICENSE holder name with me; check badges; verify `SECURITY.md` reporting route without exposing my email.
- Acceptance: tag and GitHub release created only after my confirmation.

### Phase 11. Real-world trials (needs me)
- Goal: evidence that skills work on real projects.
- Tasks: ask me for one small real project or repo; run selected skills and stages by hand on it and record outcomes, misfires and handoff gaps honestly in `reports/trials/`. No simulated results. Feed gaps back into skill content (via the JSON sources), then re-run Phase 8's loop.
- Acceptance: each trial note states project, skill, stage, input, output, and what failed.

### Phase 12. Library growth (proposals; need approval)
- Candidate ideas, to be prioritised with me: new skills for gaps found in trials (for example data engineering, ML/AI evaluation, mobile, accessibility testing, FinOps); more worked examples per skill; adapters for other agent runtimes; a contributor guide for adding a skill end to end (content JSON, risk tier, version lock, score row); a quarterly review cadence for stale content and Dependabot.
- Rules: every new skill must pass validate, build check, duplicate audit, evaluator Tier 1 and get a traceable score row before merge.

### Phase 13. Long-term maintenance
- Quarterly: re-run evaluator, refresh the dashboard snapshot, review open findings, update dependencies and advisories, review the roadmap with me.

## PART 8. OWNER ACTIONS (remind me at each report)

1. Set GitHub About description and topics (values in `FINAL_READINESS_REPORT.md`); the API write was blocked with 403.
2. Confirm the legal name for the LICENSE holder.
3. Decide F-010, F-011 and F-013.
4. Decide whether to supply an embedding key for Tier 2, and whether to run Tier 3 or LLM checks.
5. Approve version and tag for a release.
6. Provide a real project for Phase 11.
7. Enable GitHub Pages in repository settings if the deployment run reports it disabled.

## PART 9. DEFINITIONS OF DONE (every change)

- `make all` green; `build.py --check` green; `validate.py` green; `audit_duplication.py` green; pytest green; `node --check` and `json.tool` for dashboard changes.
- Generated files regenerated, never hand-edited.
- Reports updated; findings tracker updated; no secrets or personal email in the diff.
- CI green before merge; squash-merge; local `main` synced.

## PART 10. HOW TO BEGIN THE NEW CHAT

1. Say in one sentence what you are about to do.
2. Clone or pull; read `reports/enhancement/FINAL_READINESS_REPORT.md`, `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md` and this file.
3. Create a task list from Part 6, then execute it.
4. End with: what was completed, what is blocked on me, and the next phase.
