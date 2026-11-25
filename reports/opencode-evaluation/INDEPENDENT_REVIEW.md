# Independent review of the OpenCode evaluation (2026-11-25)

Reviewer: a separate Claude session reading the committed reports, transcripts and manifest and checking claims against the repository. It did
not run OpenCode. This review is the authoritative reading of the evaluation; the original reports are kept unmodified except for a pointer.

## What the evaluation shows, and how strongly

| Claim in the original reports | Assessment |
| --- | --- |
| Installer copied 20 skills to `.opencode/skills`; `--check` passed 20/20 | **Supported** (tool output; matches our own installer tests) |
| OpenCode v2.3.0 detected and advertised all 20 skills | **Supported, single observation.** Evidence is the agent's own skill list at startup; no screenshot or log is stored. Restart-after-install was not re-verified (the reports say so) |
| Relative references resolve inside each installed skill | **Supported** (files exist at the installed paths) |
| 16 skills "executed", "verified by execution evidence", "OpenCode can reliably ... follow these skills" | **Overstated.** See below |
| Overall score 82/100, "Good", CONDITIONALLY READY | **Not a measurement.** The score comes from a rubric the same model filled in; treat it as the model's opinion, not a benchmark |
| "Results not fabricated" | **Partly.** No invented tool output was found, but several steps are narrated rather than run |

## Why "execution evidence" is weaker than stated

1. **Narrated, not executed.** TEST-006 says "Verified tests pass locally (simulated execution)": the function and six tests were written in prose
   and never run, yet the report counts them as passing. Other transcripts describe actions ("Implemented ... in a scratch file", "timeline started")
   with no command output. `incident-command` (TEST-004) is explicitly a simulated incident.
2. **The model read SKILL.md files, then reasoned.** The transcripts list "Skill instructions followed (from SKILL.md)", a summary of the file; there is
   no record that OpenCode's skill-loading tool was called, and the reports admit OpenCode exposes no invocation telemetry. So "OpenCode loads and
   follows the skills" is **not** separated from "a model can read a Markdown file". Discovery (a listing) is evidenced; loading on demand is not.
3. **One weak, free model, one run, no control.** Nemotron 3.5 Super VL (free tier) ran every test once, wrote its own transcripts and scored itself. No
   second model, no repeat, no run without the skills to show they changed behaviour. "Instruction following" cannot be concluded from this.
4. **Scenarios are the model's own** and mostly easy ("simulate a payment failure", "validate a refund amount"); few have a wrong-answer trap. The best
   evidence is the pair that did: `evidence-quality-gates` refusing a source file as proof of a test run (INCONCLUSIVE) and `secure-change-control` /
   `release-deployment` withholding approval. Those behaviours are consistent with the skills, but one observation each is not a pass rate.
5. **Statuses were inconsistent.** The headline said "PASS 1, BLOCKED 4" while 15 results are PARTIAL PASS; PARTIAL PASS is not defined in the
   library's own status vocabulary (`PASS`, `FAIL`, `BLOCKED`, `INCONCLUSIVE`, `NEEDS_HUMAN_APPROVAL`).

## Findings against the repository

| Transcript finding | Check |
| --- | --- |
| TEST-012: test evidence for v1.1.0 "MISSING" | True for the session (tests were not run) but CI ran them: `Validate library` passed on the release commit. The evaluation did not look at CI evidence. |
| TEST-013: no branching policy document | **Valid.** The project uses feature branches and squash merges but did not document it. Fixed in this change (CONTRIBUTING). |
| TEST-013: no enforced linter/format config | Valid for the repo root; the library is Markdown/JSON/Python scripts validated by `validate.py` and CI rather than a linter. Left as an open, low-priority item. |
| TEST-013: no environment/secrets configuration | Expected for a documentation library; not a defect. |
| 4 skills BLOCKED (cloud, devops, enterprise governance, SRE) | Reasonable and honestly reported. They need real infrastructure; do not count them as passed or failed. |

No defect in the skills' content was found by this evaluation.

## Resulting status (what the library may claim)

- **OpenCode discovery:** observed once on OpenCode v2.3.0 / Windows (all 20 skills listed).
- **OpenCode skill behaviour:** *indicative only*, from one free-tier model with narrated steps. **Not tested** in the sense the library uses the word.
- No claim of OpenCode "support" beyond: the installer places skills where OpenCode scans, and OpenCode listed them.

## What would make it real evidence

1. Run each test with command output kept (exact commands and results, not a summary): run the tests you write, show the diff you review.
2. Confirm the skill was loaded by OpenCode's skill tool (screenshot or log line), not only read as a file.
3. Use a stronger model, run twice, and repeat once **without** the skills installed; compare against the same checklist.
4. Use at least a few scenarios with a known wrong answer (a missing approval, a failing test, an unsafe request) and record whether the skill caught it.
5. Re-run after a fresh restart to check discovery.
6. Use library status words only; define any extra label before using it.
