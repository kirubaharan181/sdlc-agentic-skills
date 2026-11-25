# OpenCode Integration / Compatibility Report

**Target:** OpenCode v2.3.0
**Library:** kirubaharan181/sdlc-agentic-skills v1.1.0
**Evaluation date:** 2026-11-24
**Read-only:** Yes

---

## 1. Skill discovery

OpenCode scans `.opencode/skills` (project), `.claude/skills`, `.agents/skills` (project) and the user-wide equivalents under `~`. This evaluation installed all 20 skills into `.opencode/skills` via `python scripts/install.py --target opencode --dest .`.

- `scripts/install.py --list` returned 20 skills.
- Install copied all 20 skills; `--check` reported CHECK PASSED: 20/20 skills match.
- OpenCode auto-detected and advertised all 20 skills to the model at startup (confirmed by the system-provided skill list covering all 20 IDs).

**Verdict:** Discovery works. A restart of OpenCode is required after installation for it to rescan skill folders (documented by the installer and by `docs/agent-guide/OPENCODE_USAGE.md`). Automatic discovery without restart was NOT separately re-verified; per the framework this limitation is recorded rather than claimed.

## 2. Skill metadata parsing

Each skill uses YAML frontmatter:
```yaml
---
name: <skill-id>
description: "..."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: [...]
---
```
- Every skill has a `description` (required for OpenCode to advertise it).
- The skill ID comes from the folder name, matching `name` in frontmatter.
- All 20 skills parsed correctly (installer `--check` verifies tree identity, which includes SKILL.md).

**Verdict:** Metadata format compatible; all 20 skills parse and advertise.

## 3. Skill loading

All 20 skills loaded into `.opencode/skills/<skill-id>/` with SKILL.md plus `references/` (CORE_PROCEDURE.md, HANDOFF_CONTRACT.md, stages.md / stages-part-*.md). Installed copies are byte-identical to source (`--check` PASSED).

**Verdict:** Loading works; no missing files or broken relative paths detected.

## 4. Instruction following

Tested across 16 skills. In every executed transcript the agent followed the skill's documented procedure (classify → select → delegate/enforce → report), applied decision rules and quality gates, and respected safety boundaries (no self-approval, no destructive action, human approval for production/security changes).

Example: evidence-quality-gates TEST-002 correctly returned INCONCLUSIVE (a source file is not test-run evidence) rather than inventing a PASS — direct evidence of instruction following.

**Verdict:** OpenCode can follow skill instructions; verified by execution transcripts.

## 5. Relative file references

Skills reference `references/CORE_PROCEDURE.md`, `references/HANDOFF_CONTRACT.md`, and `references/stages.md` (or stages-part-*.md). All referenced files exist in source and were copied to `.opencode/skills/`. Spot-checked master-orchestration, code-review-quality, application-security — all references resolve.

**Verdict:** Relative references resolve correctly; no broken paths.

## 6. Repository instruction handling

`AGENTS.md` was read and provides the agent operating rules (evidence over assertion, no unverified PASS, human approvals, read-only inspection, no secrets). `docs/agent-guide/OPENCODE_USAGE.md` documents install/entry point/use and is candid that integration is "documented, not tested." This evaluation closes that gap with real execution evidence.

**Verdict:** Repository instructions are present, readable, and consistent with the evaluation's evidence rules.

## 7. Tool availability

Skills reference generic tools (Git diff/blame, static analysis, test/coverage reports, security scanners, CI/CD platform, telemetry). None of these are OpenCode-specific tool calls; they are described capabilities the agent invokes through its own tool set. In this eval, no linter/scanner/CI was configured, so results were recorded as missing rather than fabricated.

**Verdict:** Tool references are compatible (generic, platform-neutral); execution is bounded by what the eval environment provides.

## 8. Multi-step workflow handling

master-orchestration TEST-005 demonstrated multi-skill routing (7 skills in dependency order) with handoffs and approval gates (NEEDS_HUMAN_APPROVAL on release). Cross-skill references were corroborated (e.g., release-deployment TEST-012 cross-referenced evidence-quality-gates TEST-002; technical-architecture TEST-011 cross-referenced by maintenance-support TEST-016).

**Verdict:** Multi-step workflow handling works; handoffs and cross-skill references are consistent.

## 9. Context preservation

Each transcript is self-contained and references related test IDs where skills build on one another. No context loss observed within the evaluation session.

**Verdict:** Context preserved within the evaluation; long-running cross-session context not tested.

## 10. Error handling

Skills document troubleshooting tables and decision rules for failure conditions (e.g., "No workflow fits", "Loop between two skills", "Finding cannot be reproduced => INCONCLUSIVE", "Evidence has no revision => INCONCLUSIVE"). These were exercised in transcripts where applicable (evidence-quality-gates INCONCLUSIVE; release-deployment missing evidence reported).

**Verdict:** Error handling is documented and consistent; partially exercised via execution.

## 11. Permission and approval behavior

All skills respect the boundary that production/security changes require named human approval; none self-approve. Examples: definition-of-done (BLOCKED without approver), release-deployment (production withheld), secure-change-control (NEEDS_HUMAN_APPROVAL), master-orchestration (NEEDS_HUMAN_APPROVAL on release), incident-command (emergency change via human authority).

**Verdict:** Approval behavior is correct and consistent; no skill claims authority it does not have.

## 12. Output consistency

All 16 executed skills produced outputs matching their documented deliverables (checklists, evidence records, review findings, incident records, routing plans, threat models, QA plans, release plans). Outputs were consistent with the skill's own worked examples (labelled illustrative).

**Verdict:** Outputs consistent with documented deliverables.

---

## Compatibility verdict

OpenCode can reliably discover, load, parse, and follow the skills in this library. All 20 skills are installed and detected. Metadata format, relative references, instruction following, multi-step workflow handling, and approval behavior are verified by execution evidence.

**Limitation:** OpenCode must be restarted after installation to rescan skill folders (documented, not separately re-verified). Four skills (cloud-hosting-operations, devops-platform, enterprise-governance, sre-observability) could not be executed because they require external infrastructure (cloud account, CI/CD platform, org control framework, telemetry) not present in this environment — an environment limitation, not a library defect.

**Overall:** OpenCode compatibility is strong for the skills that can be exercised; the library is well-suited to OpenCode.
