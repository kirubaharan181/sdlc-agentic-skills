# Using this library with OpenCode

Status: discovery observed once; behaviour not tested. On 2026-11-24 an OpenCode v2.3.0 session on Windows listed all 20 installed skills, and
a free-tier model then worked through 16 scenarios. That run's own reports overstate their evidence (narrated steps, self-scored), so treat it as
indicative only; see [the independent review](../../reports/opencode-evaluation/INDEPENDENT_REVIEW.md) and
[adapters/COMPATIBILITY.md](../../adapters/COMPATIBILITY.md). The folders below come from OpenCode's public skills documentation
(<https://opencode.ai/docs/skills>, read 2026-11-23); check the current documentation before relying on them.

## 1. Install the skills

OpenCode scans these folders for skills, each skill being a folder with a `SKILL.md`:

| Scope | Folders OpenCode reads |
| --- | --- |
| Project | `.opencode/skills`, plus `.claude/skills` and `.agents/skills` for compatibility |
| User | `~/.config/opencode/skills`, plus `~/.claude/skills` and `~/.agents/skills` |

Install with the bundled script (standard library only, no network):

```bash
python3 scripts/install.py --list
python3 scripts/install.py --target opencode --dest /path/to/your/project             # all 20 skills
python3 scripts/install.py --target opencode --dest . --skill code-review-quality     # only some
python3 scripts/install.py --target opencode --scope user --dry-run                    # preview a user-wide install
python3 scripts/install.py --target opencode --dest /path/to/your/project --check      # verify copies match this library
```

Use `--symlink` to stay in sync with a checkout of this repository and `--force` to replace skills that already exist.
Restart OpenCode afterwards so it rescans.

## 2. Give OpenCode the entry point

OpenCode reads an `AGENTS.md` in the project. Copy or adapt this repository's [AGENTS.md](../../AGENTS.md) so the agent knows the rules
(risk tiers, evidence, no unverified `PASS`). Skills can also be listed in `opencode.json` through its `skills` array, which accepts
local paths; see the OpenCode documentation for the exact syntax.

## 3. Ask in a way the agent can act on

Use the same request and result templates as the [Codex guide](CODEX_USAGE.md): [`templates/agent-task-request.md`](../../templates/agent-task-request.md)
and [`templates/agent-task-result.md`](../../templates/agent-task-result.md). Name the skill and state scope, constraints, acceptance criteria,
risk tier and approvers. If you are unsure which skill fits, run `python3 scripts/select_skill.py "<request>"`.

## 4. Notes from the documentation

- A skill without a `description` is not advertised to the model; every skill here has one.
- The skill ID comes from the folder name, which matches the `name` in each `SKILL.md` here.
- Permissions are the tool's own configuration; grant the least that the task needs.

## 5. What is not verified

Whether OpenCode loads each skill on demand, follows its procedure and respects its gates has not been established: the 2026-11-24 run shows
discovery, not loading, and used one free-tier model with simulated steps. See the independent review for what a real test needs.
