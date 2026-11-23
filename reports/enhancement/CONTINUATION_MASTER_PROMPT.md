# SDLC Agentic Skills: Continuation Master Prompt

Paste everything below the line into a new Claude chat.

---

You are continuing a long-running project with me (Kiruba, GitHub `kirubaharan181`). Read this whole brief, then pick up at "Phase 6" below. Do not restart or re-audit what is already done.

## 1. Project

- Repo: `kirubaharan181/sdlc-agentic-skills` (clone it first; use `add_repo` if needed). Default branch `main`.
- It is an SDLC Agentic Skills library: 190 SDLC stages, 20 skills, 74 agents, 23 workflows, 19 stages with risk tiers.
- Source of truth is canonical JSON in `registry/` (stage registry, `registry/skill-content/<skill>.json`, `registry/risk-tiers.json`, `registry/skill-versions.lock.json`). Everything else is generated: `SKILL.md` files, agents, workflows, `docs/architecture/SKILL_SELECTION.md`, `dist/`, and `dashboard/data/library.json` (git-ignored build output). Never hand-edit generated files; change the source and rebuild.
- Key scripts: `scripts/build.py` (`--check` detects drift), `scripts/render_skills.py`, `scripts/rebuild_library.py`, `scripts/validate.py`, `scripts/audit_duplication.py`, `scripts/select_skill.py`, `scripts/check_quality_regression.py`, `scripts/generate_dashboard_data.py`. `make all` and `make governance` run the gates. Tests: `python -m pytest tests -q` (61 passing), `scripts/run_tests.py`.
- Dashboard "Atelier": static HTML/CSS/vanilla JS in `dashboard/` (`index.html`, `assets/app.js`, `assets/styles.css`), published by `.github/workflows/pages.yml`.

## 2. Working rules (standing, from me)

- I authorise you to commit, push, pull and merge yourself. Use feature branches, never force-push, wait for green CI, squash-merge via `gh api`, then sync `main`.
- No fabricated scores or evidence. No claims of security certification or publication eligibility. A quality score of 100 is not publication approval.
- Static validation only. No application, integration, end-to-end or deployment tests. No paid external services.
- Never share my email address.
- Keep the dashboard a static snapshot, not a live console. No unnecessary dependencies.
- Reports go in `reports/enhancement/`. Skill-quality evidence goes in `reports/skill-quality/`.
- Work in phases. Use a task list. Verify before claiming. Finish every reply with: what was completed, and clear next steps.

## 3. What is COMPLETED

**Phases A–E, the ten-item roadmap (PR #40, merged).** Enhanced `LICENSE` (MIT, holder "kirubaharan181 and contributors"), `SECURITY.md`, `CONTRIBUTING.md`; added `AGENTS.md`, `docs/agent-guide/CODEX_USAGE.md`, `.github/CODEOWNERS`, PR template, Dependabot config, `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md`, `docs/quality/FINDINGS_TRACKER.md`. Requirements are saved in the repo.

**Master-prompt phases (PRs #46, #47, #48, merged).**
- Baseline audit: `BASELINE_AUDIT.md` and `BASELINE_FINDINGS.csv` (F-001 to F-015).
- Skill intelligence and governance layer: selection engine (incident terms force `incident_first`), skill graph, risk tiers, version lock (all skills 1.1.1), traceable score history.
- Skills rewritten to a standalone layout: links stay inside the skill folder, `references/` with bundled `CORE_PROCEDURE.md` and `HANDOFF_CONTRACT.md`, examples under `references/examples`. `application-security` is split into four stage files to fit the scanner's per-file analysis budget.
- Frontmatter descriptions are always quoted JSON strings (valid YAML) and trigger-first ("Use when…"). `validate.py` and a test enforce this.
- Real measurement with NVIDIA SkillEvaluator 1.0.1 (skillspector 2.13.4): `quality-check` and `tier1 --no-llm`. Result at commit `b1b1739`: all 20 skills 100.0, Tier 1 20/20. Baseline was an average of 87.3 at `a8be547`.
- Reconciliation and readiness reports: `QUALITY_RECONCILIATION.md`, `PUBLICATION_REQUIREMENTS.md`, `FINAL_READINESS_REPORT.md` (verdict "QUALITY VALIDATION PASSED"; it holds the suggested GitHub About description and topics).
- Dependabot PRs #44, #41, #45 merged. #42 and #43 (Pages actions) deliberately not merged.

**Phase I, Atelier dashboard (this session).** Commit `08cbb5f` is pushed to branch `feat/atelier-dashboard-governance`. **It is NOT yet merged and has no PR.**
- `scripts/generate_dashboard_data.py`: adds real source commit, per-skill version, description, tags, owned responsibilities, handoffs, limitations and recorded quality; per-stage risk tier; a top-level `governance` block (risk tiers and quality summary: 20 skills recorded, average 100.0).
- `app.js`: richer skill cards and detail drawer (quality labelled "Recorded result, not live. Not publication approval."), risk tier in stage detail, expanded search index, governance page with risk and quality panels, keyboard access (Enter/Space on cards and rows, focus return on drawer close). It also fixes a bug where **stage table rows never opened the detail drawer** (mouse or keyboard); verified in headless Chromium.
- `index.html`: skip link, "Static snapshot / Generated from the registries, not live" label, `aria-label`s, `role="dialog" aria-modal`, `tabindex="-1"` on `#content`, status toast.
- `styles.css`: skip link and `:focus-visible` styles.
- Two new tests in `tests/test_governance.py`. Local gate passed before the commit: `make all` (61 tests, validate, build check, run_tests), `node --check`, `json.tool`.

## 4. What is IN PROGRESS (do this first)

1. Open a PR for `feat/atelier-dashboard-governance` into `main` using `gh api`. The PR body ends with the line "🤖 Generated with [Claude Code](https://claude.com/claude-code)".
2. Wait for green CI. Fix anything that fails; do not skip checks.
3. Squash-merge, then sync local `main`.
4. Add the Phase I record: a short dashboard section in `reports/enhancement/IMPLEMENTATION_SUMMARY.md` and `FILE_CHANGE_MATRIX.csv`, a `CHANGELOG` entry, and a README note. Then run `make all` and `build.py --check` and merge that too.
5. Look at the governance page on desktop and a 390px dark-mode mobile view for layout. Screenshots were captured and the console showed no errors, but the images were not reviewed yet.

## 5. Phases still TO DO (in this order)

- **Phase 6, finish the dashboard (Phase I):** items in section 4, plus confirm the Pages workflow publishes `dashboard/` correctly. Dependabot #42/#43 stay unmerged until a Pages deploy has been watched.
- **Phase 7, open findings:** F-010 (skill folder nesting advisory), F-011 (`## Instructions` heading advisory), F-013 (author email advisory) are open. F-012 is partially resolved. F-009 and F-014 are blocked on owner actions. For each, propose a fix or document the decision in `BASELINE_FINDINGS.csv` and `FINDINGS_TRACKER.md`. Ask me before changing anything about the author email or folder layout.
- **Phase 8, regression guard:** after any future skill change, re-run SkillEvaluator (`quality-check`, `tier1 --no-llm`) and append a fully traceable row to `reports/skill-quality/SCORE_HISTORY.csv` using `check_quality_regression.py --add` (all seven traceability options). Install the evaluator in a fresh venv, because the old one is gone with the session.
- **Phase 9, publication readiness:** Tier 2 needs an embedding API key (NVIDIA Build or OpenAI), and Tier 3 and the LLM checks have not been run. Keep reporting these as "not run". Ask me whether to supply a key before attempting them. Do not claim eligibility until all required tiers pass with complete evidence.
- **Phase 10, release hygiene:** tag and release notes after Phase 6 and 7, only after I confirm the version number. Re-check README tables against `SCORE_HISTORY.csv`.
- **Phase 11, real-world trials:** independent adapter and stage runs on real projects. Needs me to provide a project; do not simulate results.

## 6. Owner actions I still need to do (remind me)

- Set the GitHub About description and topics (values in `FINAL_READINESS_REPORT.md`). The API write was blocked with a 403.
- Confirm the legal name for the LICENSE holder.
- Decide on advisories F-010, F-011, F-013.
- Decide whether to provide an embedding key for Tier 2, and whether to run Tier 3 or LLM checks.
- Dependabot #42/#43: only after a watched Pages deploy.

## 7. How to start the new chat

First, clone or pull the repo, read `reports/enhancement/FINAL_READINESS_REPORT.md`, `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md` and this file, and check `git branch -a` and open PRs to confirm the state above. If anything differs from this brief, trust the repo and tell me. Then begin with Section 4 without asking permission, and end with a "completed / next steps" report.
