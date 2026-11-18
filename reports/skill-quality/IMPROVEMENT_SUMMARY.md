# Improvement summary

Scope: documentation structure and governance for the 20 skills. **After-change scores are not measured**: SkillEvaluator is
not installed in the build environment. The 97+ target is therefore unverified. See `SKILL_SCORE_COMPARISON.csv`.

## What changed, by baseline finding

| Baseline finding | Change | Enforced by |
|---|---|---|
| No examples | 2 examples per skill (3 for the five cross-cutting skills), each with request, context, behavior, output, acceptance; labelled illustrative | `validate.py`: minimum example counts |
| No `## Purpose` | Purpose section rendered from `purpose` | required-sections check |
| No limitations | Limitations section rendered from `limitations` | required-sections check |
| No prerequisites | "Prerequisites and Requirements" section | required-sections check |
| No troubleshooting | Error / Cause / Resolution rows (3 per skill, 4 for `master-orchestration`) | schema + required-sections check |
| `metadata.author` / `metadata.tags` missing | Frontmatter now has `metadata.author`, `metadata.version`, `metadata.tags` | frontmatter check |
| Descriptions too long (15) | All 20 are 132-147 characters | validator: at most 150 characters |
| Broad descriptions without negative triggers (3) | Every description contains "Use when" and "Do not use" | validator |
| Guide-only skills (5) | Full content model, decision rules, quality gates, handoffs | validator |

## Additional capabilities added

Skill selection engine, dependency graph with acyclic forward edges, handoff contracts, duplicate-responsibility detection,
risk tiers R0-R4, approval and escalation matrix, evidence traceability checker, decision log standard, conflict resolution,
skill versioning with a content-hash lock, quality regression tracking, templates and Codex usage guidance.
Details: `ARCHITECTURE_ENHANCEMENTS.md` and `docs/roadmap/REQUIREMENTS_AND_ROADMAP.md`.

## What this does not show

Passing the repository validator shows the documents have the required structure. It does not show that the skills improve
agent output, and it does not show the evaluator score. Run SkillEvaluator and record the result to close that gap.
