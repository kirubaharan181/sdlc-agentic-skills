# Skill authoring

Skills follow Anthropic's [skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices):
concise, progressively disclosed, one bounded procedure each. `SKILL.md` files are **generated** by
`scripts/render_skills.py` from the registries and `scripts/execution_profiles.py`; edit the sources, then run
`python3 scripts/build.py`. `python3 scripts/validate.py` enforces the rules below.

## Layout
```
skills/<group>/<skill>/SKILL.md             overview: frontmatter, procedure, stage index, links
skills/<group>/<skill>/references/stages.md per-stage detail (loaded only when needed)
skills/<group>/<skill>/references/CORE_PROCEDURE.md, HANDOFF_CONTRACT.md  generated copies so each skill is standalone
skills/<group>/<skill>/references/examples/  generated examples, marked illustrative
skills/_shared/CORE_PROCEDURE.md            rules every skill shares (evidence, approvals, failure, handoff)
```

## Rules (all validator-enforced)
- Frontmatter has `name` (equal to the skill id: lowercase letters, digits, hyphens, at most 64 characters, no
  `anthropic` or `claude`) and `description` (1-1024 characters, no XML tags).
- The description is third person, says what the skill does, and includes "Use when ..." with the stage names
  that trigger it. No "I can" or "You can".
- `SKILL.md` is under 500 lines and states shared rules once by linking `_shared/CORE_PROCEDURE.md`.
- Links resolve, and reference files do not link onward (one level deep).
- Role contracts and skills must not be near-copies of each other (`scripts/audit_duplication.py`).

## Adding a skill
Add it to `registry/SKILL_REGISTRY.json`, give it a profile in `scripts/execution_profiles.py`, map stages to it in
`registry/SDLC_STAGE_REGISTRY.json`, then build and validate. Prefer evidence-driven iteration: write at least three
scenarios that fail without the skill before adding text (see the guide's evaluation section).
