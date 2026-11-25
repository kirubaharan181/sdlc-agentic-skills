# Skill Scorecard — Weighted Scores, Ratings, and Test Statuses

**Scoring model (100 points):** Instruction quality 15 | Practical usability 15 | Engineering quality 15 | Safety & security 15 | OpenCode compatibility 15 | Execution success 20 | Documentation 5
**Rating bands:** 95–100 Excellent | 85–94 Very Good | 75–84 Good | 60–74 Needs Improvement | 40–59 Poor | 0–39 Critical
**Test statuses:** PASS | PARTIAL PASS | FAIL | NOT TESTED | BLOCKED

**Evaluation basis:** Category scores 0–10 assigned from evidence (SKILL.md audit + execution transcript). Execution success reflects actual test results; BLOCKED/NOT TESTED skills receive 0 for execution success and are not converted to PASS.

---

## Scorecard

| # | Skill name | Test status | Instr. (15) | Usability (15) | Engineering (15) | Safety (15) | OC compat (15) | Execution (20) | Docs (5) | **Total /100** | Rating |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | evidence-quality-gates | PASS | 10 | 9 | 9 | 10 | 10 | 10 | 9 | **97** | Excellent |
| 2 | application-security | PARTIAL PASS | 9 | 8 | 8 | 10 | 10 | 8 | 8 | **88** | Very Good |
| 3 | definition-of-done | PARTIAL PASS | 9 | 9 | 8 | 9 | 10 | 8 | 8 | **88** | Very Good |
| 4 | release-deployment | PARTIAL PASS | 8 | 8 | 8 | 10 | 10 | 8 | 7 | **86** | Very Good |
| 5 | secure-change-control | PARTIAL PASS | 8 | 8 | 8 | 10 | 10 | 8 | 7 | **86** | Very Good |
| 6 | code-review-quality | PARTIAL PASS | 9 | 8 | 8 | 9 | 10 | 8 | 8 | **86** | Very Good |
| 7 | incident-command | PARTIAL PASS | 9 | 8 | 8 | 9 | 10 | 8 | 8 | **86** | Very Good |
| 8 | master-orchestration | PARTIAL PASS | 9 | 9 | 8 | 9 | 10 | 8 | 8 | **86** | Very Good |
| 9 | technical-architecture | PARTIAL PASS | 8 | 8 | 8 | 9 | 10 | 8 | 7 | **84** | Good |
| 10 | software-implementation | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 11 | business-product-management | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 12 | requirements-design | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 13 | project-agile-management | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 14 | quality-assurance | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 15 | maintenance-support | PARTIAL PASS | 8 | 8 | 7 | 9 | 10 | 8 | 7 | **83** | Good |
| 16 | engineering-governance | PARTIAL PASS | 8 | 7 | 7 | 9 | 10 | 7 | 7 | **79** | Good |
| 17 | cloud-hosting-operations | BLOCKED | 9 | 5 | 8 | 9 | 10 | 0 | 8 | **66** | Needs Improvement |
| 18 | devops-platform | BLOCKED | 9 | 5 | 9 | 9 | 10 | 0 | 9 | **68** | Needs Improvement |
| 19 | enterprise-governance | BLOCKED | 9 | 5 | 9 | 10 | 10 | 0 | 9 | **69** | Needs Improvement |
| 20 | sre-observability | BLOCKED | 9 | 5 | 9 | 9 | 10 | 0 | 9 | **68** | Needs Improvement |

---

## Summary

| Metric | Value |
|---|---|
| Skills discovered | 20 |
| Skills executed/tested | 16 |
| PASS | 1 |
| PARTIAL PASS | 15 |
| FAIL | 0 |
| NOT TESTED | 0 |
| BLOCKED | 4 |
| Overall (simple average of skill totals) | **82 / 100** |
| Overall rating band | Good (75–84) |
| Skills at 85+ (Very Good/Excellent) | 8 |
| Skills below 75 (Needs Improvement) | 4 (all BLOCKED on execution) |

---

## Notes on scoring

- The 4 BLOCKED skills (cloud-hosting-operations, devops-platform, enterprise-governance, sre-observability) score 0/20 on execution success because they could not be executed without external infrastructure (cloud account, CI/CD platform + secrets store, org control framework, telemetry sources). Their instruction/usability/engineering/safety/compatibility scores reflect actual SKILL.md content read; they are NOT converted to PASS.
- A high documentation/instruction score cannot compensate for failed or missing execution (per the scoring framework). Consequently the 4 BLOCKED skills fall into "Needs Improvement" despite strong documentation.
- No skill scored FAIL; no critical defects were found in any SKILL.md.
- Evidence-quality-gates is the only skill with a clean PASS; all other tested skills achieved PARTIAL PASS because their execution was necessarily simulated or limited by the read-only, no-external-services evaluation environment (correctly — results were not fabricated).
