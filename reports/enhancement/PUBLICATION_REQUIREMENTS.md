# Publication requirements (SkillEvaluator 1.0.1)

Source: the installed package's own help output and source code (`skillevaluator --help`, `tier1 --help`, `validate --help`,
`reporting/base.py::assess_publication`). No publication command was invented; the evaluator has no separate publication validator.

## How eligibility is decided

`Publication eligibility` is computed by `assess_publication` from the results of the run:

- **Incomplete** when any validator reports incomplete scanner evidence, or a publication-required validator was skipped.
- **Fail** when any validator failed (or Tier 3 failed).
- **Eligible** only when the required tiers pass with complete evidence.

So `quality-check` alone (one Tier 1 check) can never produce "Eligible"; and a quality score of 100 is not publication approval.
Tiers: Tier 1 static, security and quality checks (gates the exit code); Tier 2 deduplication (blocking); Tier 3 live agent evaluation (advisory unless `--block-on-agent-eval`); LLM checks join when configured.

## Requirement-to-evidence matrix (state at commit `66e223e`)

| Requirement | Source | Status | Evidence | Missing | Action |
|---|---|---|---|---|---|
| Quality check passes | `quality-check` | **met** | 20 x 100.0, 0 findings (`SCORE_HISTORY.csv`) | none | keep regression check in CI |
| Tier 1 schema, version, PII, license, code-integrity, dependency, unicode, quality, lint, harness checks | `tier1` | **met for 19 of 20** | `TIER1_RESULTS.csv` | `application-security` (security scan incomplete) | F-008 |
| Tier 1 security scan complete (SkillSpector 2.13.4) | `tier1` | **met for 19 of 20** | same | parse-limit warning on `application-security` | report reproducer to SkillSpector; split reference file if needed |
| Skill is standalone (no references outside the skill folder) | SkillSpector reference resolution | **met** (after layout change) | `tests/test_governance.py::test_every_skill_is_standalone` | none | none |
| Valid frontmatter (`name`, string `description`) | schema check, harness checks | **met** | all 20 parse as YAML | none | none |
| Tier 2 deduplication | `validate --tiers 1,2` | **not run** | none | run result | run where permitted |
| Tier 3 live agent evaluation | `validate` | **not run, not in scope** | none | needs agent runtime and model access | owner decision |
| LLM rubric and security checks | `tier1` with LLM configured | **not run** | none | LLM configuration | owner decision |
| Advisory: nesting depth, `## Instructions` heading, author email | `tier1` | **open** | `BASELINE_FINDINGS.csv` F-010, F-011, F-013 | owner decision | decide |

**Verdict:** publication eligibility is not satisfied and is not claimed. Required evidence is missing for Tier 2, Tier 3 and LLM checks, and `application-security` has an unresolved scanner limitation.
