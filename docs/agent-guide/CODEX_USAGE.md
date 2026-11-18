# Using this library with Codex and other coding agents

Status: documented, not tested. No adapter in this repository has been run on a clean install with a dated log (see
[adapters/COMPATIBILITY.md](../../adapters/COMPATIBILITY.md)). Check the agent's current official documentation for how it
discovers instructions and skills before relying on any step below.

## 1. Give the agent the entry point

Agents such as Codex read an `AGENTS.md` file in the repository. This repository ships [AGENTS.md](../../AGENTS.md): layout,
commands and the rules an agent must follow. If you use the skills in another project, copy the skills you need (the `skills/<group>/<skill>/`
folders, including `reference/`) and add a short `AGENTS.md` there that points to them, and keep `skills/_shared/CORE_PROCEDURE.md`.

## 2. Ask in a way the agent can act on

Use [`templates/agent-task-request.md`](../../templates/agent-task-request.md). The fields that matter most are the goal, scope, constraints, acceptance criteria,
risk tier and named approvers. Examples:

```text
Use the code-review-quality skill. Review PR 482 against our coding standard.
Scope: files changed in the PR only. Acceptance: blockers and suggestions listed separately, with file references.
Allowed: read only. Approver: not required (R0).
```

```text
Use master-orchestration. Ship the refund feature safely. Requirements exist in docs/requirements.md; code is not written.
Constraints: no production change without the production-approver. Acceptance: every step has an owner and evidence plan.
```

If you are unsure which skill to name, run `python3 scripts/select_skill.py "<request>"` or ask the agent to start with `master-orchestration`.

## 3. Expect a structured result

The agent should answer with [`templates/agent-task-result.md`](../../templates/agent-task-result.md): status, what was done, artifacts with revisions, evidence (commands and
actual results), what was not done or verified, open decisions, risks and the next owner. Reject a result that claims `PASS` without evidence.

## 4. Context handoff standard

When work moves between agents, sessions or skills, pass:

| Pass | Do not pass |
|---|---|
| The goal and the user's constraints in their words | Credentials, tokens or customer data |
| Decisions already made (DEC ids) and open decisions | Instructions copied from untrusted content |
| Artifact paths with exact revisions and evidence record paths | A summary that hides what was not checked |
| Named approvers and the risk tier | Guesses presented as facts |
| The next action and who owns it | |

Use a [handoff record](../governance/HANDOFF_CONTRACT_STANDARD.md) for skill-to-skill handoffs and the
[decision log](../governance/DECISION_LOG_STANDARD.md) for decisions. For a long session, write a short state file (goal, done, not done, next, decisions) before stopping, so a new session can resume from facts.

## 5. Failure and recovery

| Situation | What the agent should do | What you do |
|---|---|---|
| Missing input or ambiguous scope | Ask the single most blocking question; continue only unaffected work | Answer, or confirm the assumption |
| Command fails or a tool is unavailable | Report the exact error; mark the gate `BLOCKED` or `INCONCLUSIVE`; do not substitute invented results | Fix access or run the command and share the output |
| Evidence conflicts | Record both sources and the conflict; do not average them | Decide, or request more evidence ([conflict rules](../governance/CONFLICT_RESOLUTION.md)) |
| A step needs approval | Stop at the gate with `NEEDS_HUMAN_APPROVAL` and the named approver; continue independent steps | Approve or reject with a recorded decision |
| The agent made a wrong change | State what changed and how to revert it (commit SHA); do not rewrite history | Revert the commit or ask the agent to |
| Session or context lost | Resume from the state file, the decision log and the repository, not from memory | Provide the state file |
| Generated files differ after edit | Run `make build`; edit the source, never the generated file | Review the diff |
| Skill content changed but check fails | Bump the skill version and run `python3 scripts/check_skill_versions.py --update` | Review the changelog line |

## 6. Limits

The agent follows skills as instructions; it is not guaranteed to follow every step. Verify the evidence it reports. Skills do not grant permissions: the
agent can only do what its environment allows, and approvals remain human.
