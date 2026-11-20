# Remaining findings

| # | Finding | Status | Next step |
|---|---|---|---|
| 1 | Post-change quality score | closed: 20 x 100.0 at `b1b1739` | repeat after skill changes |
| 2 | Publication eligibility | open: Tier 2, Tier 3, LLM checks not run | `reports/enhancement/PUBLICATION_REQUIREMENTS.md` |
| 3 | `application-security` scanner parse-limit warning | closed: stage reference split into parts; Tier 1 passes | none |
| 4 | Advisory evaluator findings (nesting depth, `## Instructions`, author email) | open, owner decision | `reports/enhancement/BASELINE_FINDINGS.csv` F-010, F-011, F-013 |
| 5 | Skill examples are illustrative and have not been run in a real project | open | dated runs by contributors (issues #27-#29) |
| 6 | Selection engine is lexical, not semantic | known limitation | add golden cases when real misroutes are found |
| 7 | Codex and other adapters documented, not tested | open | independent runner with a dated log |
| 8 | 190 stages authored, none run on a real project | open | contributors |
| 9 | GitHub About description and topics | open, owner action | values in `reports/enhancement/FINAL_READINESS_REPORT.md` |
| 10 | `LICENSE` holder is the GitHub handle | open, owner action | confirm or replace |
