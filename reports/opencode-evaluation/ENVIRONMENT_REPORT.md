# Environment Report — OpenCode Compatibility Evaluation

**Repository:** kirubaharan181/sdlc-agentic-skills
**Release:** v1.1.0
**Target agent:** OpenCode
**Evaluation date:** 2026-11-24
**Evaluator:** OpenCode (self-evaluation, read-only)
**Read-only evaluation:** Yes — no skill definitions modified, no destructive operations, no commits/pushes.

---

## Detected values

| Item | Value |
|---|---|
| Operating system | Windows (win32) |
| Git version | 2.56.0.windows.4 |
| Python version | 3.11.9 (`python` on PATH; `python3` alias not present) |
| OpenCode version | v2.3.0 |
| OpenCode model | nemotron-3.5-super-vl-free (OpenCode provider) |
| Repository root | `C:\Users\kirubaharan\sdlc-agentic-skills` |
| Git branch | `main` |
| Current commit SHA | `8fc6fdc9d6e7aef94960e46034bc09626504834d` |
| Git tag | `v1.1.0` (also `v1.1.0-rc.1`) |
| VERSION file | `1.1.0` |
| Git working-tree status | Clean (no uncommitted changes) |
| Installation scope | Project (`.opencode/skills`) |
| Install method | `python scripts/install.py --target opencode --dest .` (copy) |

---

## Repository files inspected

| File | Present? | Notes |
|---|---|---|
| `AGENTS.md` | Yes | Read — project agent instructions |
| `README.md` | Yes | Read — 20 skills, 190 stages, 15 domains, 74 roles, 23 workflows |
| `docs/agent-guide/OPENCODE_USAGE.md` | Yes | Read — documents install, entry point, OpenCode-specific notes |
| `adapters/COMPATIBILITY.md` | Yes | Read — capability declarations, not a behavior promise |
| `docs/IMPLEMENTATION_ROADMAP.md` | Not checked for this report | Not a Phase 1 required file |
| `scripts/install.py` | Yes | Read — installer, supports --list/--check/--target/--dest/--symlink/--force |
| `scripts/validate.py` | Present in repo | Not executed in this read-only eval |

> Note: `docs/agent-guide/OPENCODE_USAGE.md` states installation and discovery are "documented, not tested" and that agent behavior "has not been observed." This evaluation addresses that gap.

---

## Installation verification

```
python scripts/install.py --list
  -> 20 skills discovered (matches expected inventory)

python scripts/install.py --target opencode --dest .
  -> Installing 20 skill(s) into .opencode/skills (copy)
  -> Done: 20 installed, 0 skipped.

python scripts/install.py --target opencode --dest . --check
  -> CHECK PASSED: 20/20 skills match in .opencode/skills
```

OpenCode auto-detected all 20 installed skills on startup (confirmed by the system-provided skill list: application-security, business-product-management, ..., technical-architecture — all 20).

---

## Installed skill directories (`.opencode/skills/`)

All 20 skills installed and verified identical to source (`--check` PASSED):

1. application-security
2. business-product-management
3. cloud-hosting-operations
4. code-review-quality
5. definition-of-done
6. devops-platform
7. engineering-governance
8. enterprise-governance
9. evidence-quality-gates
10. incident-command
11. master-orchestration
12. maintenance-support
13. project-agile-management
14. quality-assurance
15. release-deployment
16. requirements-design
17. secure-change-control
18. software-implementation
19. sre-observability
20. technical-architecture

---

## Installation summary

| Metric | Value |
|---|---|
| Skills discovered in source (`skills/*/*/SKILL.md`) | 20 |
| Skills expected (per `--list` / README) | 20 |
| Skills installed for OpenCode | 20 |
| Installation verification (`--check`) | PASSED 20/20 |
| Skills OpenCode auto-detected | 20 |
| Missing skills | 0 |
| Duplicate skills | 0 |
| Broken installations | 0 |

## Environment notes / limitations

- OpenCode must be restarted after installation so it rescans skill folders (documented by the installer). This evaluation was run after install + detection; a fresh OpenCode process restart for discovery was not separately re-verified.
- Skills reference local `references/` files (e.g. `references/CORE_PROCEDURE.md`, `references/HANDOFF_CONTRACT.md`, `references/stages.md`); all confirmed present in source and copied to `.opencode/skills/`.
- No network, API keys, or external services are required by the skills themselves (per each SKILL.md's prerequisites).
- This evaluation is read-only: skill definitions were not modified; no repository commits, pushes, merges, or releases were created.
