# Templates

Reusable, copy-and-fill templates. They are not evidence. Anything filled with placeholders must keep `"example": true` or be deleted.

| Template | Used by | Standard |
|---|---|---|
| `decision-record.md` | one decision per file | `docs/governance/DECISION_LOG_STANDARD.md` |
| `decision-log.md` | running log of decisions | `docs/governance/DECISION_LOG_STANDARD.md` |
| `evidence-record.json` | a gate result for an exact revision | `docs/governance/EVIDENCE_TRACEABILITY.md` |
| `handoff-record.json` | passing work between skills | `docs/governance/HANDOFF_CONTRACT_STANDARD.md` |
| `risk-assessment.md` | classifying a change | `docs/governance/RISK_CLASSIFICATION.md` |
| `change-request.md` | `secure-change-control` | `docs/governance/APPROVAL_ESCALATION_MATRIX.md` |
| `incident-timeline.md` | `incident-command` | `skills/cross-cutting/incident-command/SKILL.md` |
| `agent-task-request.md`, `agent-task-result.md` | asking an agent for work and reading its result | `docs/agent-guide/CODEX_USAGE.md` |
| `skill-content.template.json` | writing a new skill's documentation | `docs/skill-authoring/SKILL_AUTHORING.md` |
| `definition-of-done/*.md` | completion profiles | `skills/cross-cutting/definition-of-done/SKILL.md` |

Check the JSON templates with `python3 scripts/trace_evidence.py --templates`.
