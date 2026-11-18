# Architecture enhancements

```
registry/skill-content/<skill>.json  --build-->  skills/**/SKILL.md
registry/risk-tiers.json                         docs/architecture/SKILL_SELECTION.md (selection table, graph, matrices)
registry/skill-versions.lock.json  <--check--    scripts/check_skill_versions.py
reports/skill-quality/SCORE_HISTORY.csv <--check-- scripts/check_quality_regression.py
templates/*.json  <--check--                      scripts/trace_evidence.py --templates
```

| Component | Purpose | Limit |
|---|---|---|
| Content model + renderer | One authored source per skill; consistent sections | Content correctness is still reviewed by humans |
| Selection engine (`scripts/select_skill.py`) | Rank skills for a request from keywords, tags and stage names; advise single skill, orchestrate, incident first, or no match | Lexical matching only; the skill's "When NOT to Use" decides |
| Dependency graph (`scripts/skill_graph.py`) | Handoff edges between skills; forward edges must be acyclic; rework loops marked `feedback` | Shows declared handoffs, not runtime behavior |
| Responsibility ownership | Each `owns` entry has exactly one skill | Responsibilities are labels written by authors |
| Handoff standard | Record with id, from/to, artifacts with revisions, acceptance rule | Unacknowledged handoff is BLOCKED; enforcement is by review and template check |
| Risk tiers R0-R4 | Each approval-gated stage has a tier; tier sets approver and evidence needs | Tier choices are policy; they are not a risk assessment of any real system |
| Evidence traceability | requirement -> stage -> gate -> evidence record (exact revision) -> approver | Checks records' shape, not whether the evidence is true |
| Versioning lock | Content hash must change with version | Hash proves a change happened, not that it was reviewed |
| Regression tracking | Fails on score drop over 0.5, dimension drop over 5, or more findings | Uses only recorded real runs |
