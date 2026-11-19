# Validation results

All commands were run on the working tree that became the pull request (base `main` at `79384e0`), Python 3.13 unless stated. Exit code 0 means pass.

| Check | Command | Result |
|---|---|---|
| Generated files up to date | `python3 scripts/build.py --check` | PASSED: 208 generated files, two builds identical |
| Registry, skills, handoff graph, versions | `python3 scripts/validate.py` | PASSED: 190 stages, 20 skills, 74 agents, 23 workflows |
| References | `python3 scripts/check_references.py --fail-on-orphans` | PASS |
| Links | `python3 scripts/check_links.py` | 261 relative links, 0 broken |
| Duplication | `python3 scripts/audit_duplication.py --threshold 0.85 --fail-on-findings` | exit 0 (0 exact, 0 near duplicates; bundled shared copies exempt by design) |
| Skill versions | `python3 scripts/check_skill_versions.py` | PASSED: 20 skills match the lock |
| Quality regression | `python3 scripts/check_quality_regression.py` | PASSED: 20 skills, no regression |
| Templates and traceability | `python3 scripts/trace_evidence.py --templates` | PASSED |
| Tests, Python 3.13 | `python3 -m pytest -q` | 59 passed |
| Tests, Python 3.11 (CI version) | `python3.11 -m pytest -q` | 59 passed |
| Legacy scenario tests | `python3 scripts/run_tests.py` | PASSED |
| SkillEvaluator quality check | `skillevaluator quality-check skills/<group>/<skill>` x 20 | 20 x 100.0, 0 findings (commit `66e223e`) |
| SkillEvaluator Tier 1, no LLM | `skillevaluator tier1 skills/<group>/<skill> --no-llm` x 20 | 19 pass; `application-security` fails (scanner parse limit) |

One earlier pytest run failed `test_repo_has_no_exact_duplicate_files` because the bundled per-skill copies were not yet exempt; the exemption was added and the full suite was re-run (results above).

## Not run

Application, integration, end-to-end, browser and deployment tests; SkillEvaluator Tier 2, Tier 3 and LLM checks; agent-platform tests (Codex, Claude Code); security certification of any kind.
