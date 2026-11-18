# Requirements and roadmap: enterprise quality enhancement

This file records what the repository owner asked for, what was done, and what is still open. Status words are literal:
**done** = the file exists and a repository check or test covers it; **authored** = written but not proven by a run;
**not measured / not run** = it needs something this work did not have. Nothing here claims a score, certification or adoption.

## 1. Source requirements

1. **Roadmap message (2026-11-17):** phases A-E and ten items (below); enhance `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md` to fit the repository; analyze and save the requirements and work.
2. **Attached master prompt "SDLC Agentic Skills Enterprise Quality Enhancement (target 97+/100)":** improve all 20 skills (frontmatter `name`, `description`, `author`, `tags`; description 50-150 characters with negative triggers; sections Purpose, When to Use, When NOT to Use, Prerequisites, Inputs/Outputs, Workflow, Decision Rules, Quality Gates, 2-3 Examples, Limitations, Troubleshooting (Error / Cause / Resolution), Related); extra depth for the five weakest skills; no filler or keyword stuffing; run SkillEvaluator quality check only (no application tests); report real scores; produce reports under `reports/skill-quality/`; state clearly what was inspected, quality-scored, not tested and not validated; no security certification claims; no invented identity.
3. **Attached SkillEvaluator output (2026-11-17, run by the owner):** 20 skills, average 87.3, lowest 84.5 (five cross-cutting skills), highest 88.5, none at 97+, 163 findings. Stored in `reports/skill-quality/BASELINE_SCORES.csv` and `BASELINE_FINDINGS.csv`.
4. **Standing owner instruction:** commit, push, pull and merge by myself. **Decision:** this overrides the master prompt's "do not commit, push or merge" line. Work happens on a feature branch, goes through a pull request, and merges only when CI is green. No force-push.

## 2. Roadmap phases and status

| Phase | Deliverable | Status | Where |
|---|---|---|---|
| A Documentation quality | All 20 skills restructured with standard metadata, 50-150 character descriptions with negative triggers, examples, troubleshooting, prerequisites, limitations | authored, enforced by `validate.py`; **97+ not measured** | `registry/skill-content/*.json` -> `skills/**/SKILL.md` |
| B Skill intelligence | Selection matrix, dependency graph, handoff contracts, duplicate-responsibility detection | done (generated and validated) | `docs/architecture/SKILL_SELECTION.md`, `scripts/skill_graph.py`, `scripts/select_skill.py` |
| C Enterprise governance | Approval and escalation matrix, risk framework, evidence traceability, audit readiness | done as documents plus checks; not audited | `docs/governance/`, `registry/risk-tiers.json`, `scripts/trace_evidence.py` |
| D Agent usability | Codex guidance, input/output templates, context handoff standard, failure and recovery | authored; Codex use **not tested** | `AGENTS.md`, `docs/agent-guide/CODEX_USAGE.md`, `templates/` |
| E Continuous quality | Score history, change log, regression tracking, ownership | done (tracking mechanism); history holds the baseline only | `reports/skill-quality/SCORE_HISTORY.csv`, `scripts/check_quality_regression.py`, `docs/quality/`, `CHANGELOG.md`, `.github/CODEOWNERS` |

## 3. The ten items

| # | Item | Status | Deliverable | Enforcement |
|---|---|---|---|---|
| 1 | Skill Selection Engine | done (lexical matcher, not semantic) | `scripts/select_skill.py`, selection table in `SKILL_SELECTION.md` | `tests/test_governance.py` |
| 2 | Skill Dependency Graph | done | mermaid graph and handoff matrix in `SKILL_SELECTION.md`; forward edges acyclic, `feedback` edges marked | `validate.py` cycle check |
| 3 | Handoff Contract Standard | done | `docs/governance/HANDOFF_CONTRACT_STANDARD.md`, `registry/schemas/handoff.schema.json`, `templates/handoff-record.json` | `trace_evidence.py --templates` |
| 4 | Evidence Traceability | done | `docs/governance/EVIDENCE_TRACEABILITY.md`, `scripts/trace_evidence.py` | CI step |
| 5 | Decision Log Standard | done | `docs/governance/DECISION_LOG_STANDARD.md`, `templates/decision-log.md` | review |
| 6 | Risk-Based Approval | done | `docs/governance/RISK_CLASSIFICATION.md`, `APPROVAL_ESCALATION_MATRIX.md`, `registry/risk-tiers.json` | `tests/test_governance.py` (every approval-gated stage has a tier) |
| 7 | Conflict Resolution Rules | done | `docs/governance/CONFLICT_RESOLUTION.md`; one owner per responsibility | `validate.py` duplicate `owns` check |
| 8 | Reusable Templates | done | `templates/` and `templates/README.md` | schema checks for JSON templates |
| 9 | Skill Versioning Policy | done | `docs/governance/SKILL_VERSIONING.md`, `registry/skill-versions.lock.json` | `check_skill_versions.py` |
| 10 | Quality Regression Tracking | done (mechanism) | `scripts/check_quality_regression.py`, `docs/quality/QUALITY_MANAGEMENT.md` | CI step |

Policy files enhanced as asked: `LICENSE` (full MIT text), `SECURITY.md` (private reporting, scope, targets, no certification claim), `CONTRIBUTING.md` (skill workflow, versioning, scores, checklist, license of contributions), plus `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS`, `.github/dependabot.yml`.

## 4. What is not done, and why

| Open item | Why | Who can close it |
|---|---|---|
| Re-run SkillEvaluator and record the 20 new scores | SkillEvaluator is not installed in the build environment, so "after" scores are **not measured**; 97+ is unverified | Owner: run it, then `check_quality_regression.py --add` per skill |
| Findings marked "addressed" | The 163 baseline findings were addressed by construction (see `docs/quality/FINDINGS_TRACKER.md`) but not re-measured | Same evaluator run |
| Codex, Claude Code and other adapter tests | Adapters are documented, not tested (`adapters/COMPATIBILITY.md`) | Independent runner with a dated log |
| Stage procedures on real projects | 190 stages are authored, none run on a real project | Contributors (issues #27-#29) |
| Release tag `v1.1.0-rc.1` and GitHub release | Creation is blocked for this session | Owner |
| Private vulnerability reporting | Setting is currently disabled on the GitHub repository | Owner: Settings -> Code security -> enable |
| Legal name in `LICENSE` | Holder is written as `kirubaharan181 and contributors` | Owner: confirm or replace |

## 5. Scope statements (also in `reports/skill-quality/VALIDATION_SCOPE.md`)

- **Inspected:** repository structure, registries, skill content and generated skill files.
- **Checked by repository tooling:** schemas, structure, handoff graph, versions, links, references, duplication, tests.
- **Quality-scored by SkillEvaluator:** only the baseline run supplied by the owner.
- **Not tested:** application, integration, end-to-end, browser, deployment, and agent-platform behavior.
- **Not validated:** security posture, compliance, real-world outcomes. No certification is claimed.
