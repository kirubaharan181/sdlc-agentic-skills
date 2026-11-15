# Getting Started

## 1. Validate the library first

```powershell
python scripts/validate.py
python scripts/run_tests.py
```

These commands validate mappings and controlled fixtures. They do **not** prove a production deployment, security assessment, or external platform integration.

## 2. Start from the request, not a favorite skill

| Request | Recommended workflow | First roles |
|---|---|---|
| New product | `new-product-development` | Business Strategist, Product Manager, Requirements Engineer |
| New capability | `feature-development` | Product Owner, Architect, Engineer, QA |
| Defect | `bug-fix` | Production Support, Engineer, QA |
| Urgent customer impact | `emergency-hotfix` | Incident Manager, Engineer, Release Manager |
| Vulnerability | `security-vulnerability-remediation` | AppSec Engineer, Vulnerability Analyst, Engineer |
| Production issue | `incident-response` | Incident Manager, SRE, Production Support |

## 3. Resolve the execution contract

1. Open the selected workflow in [`workflows/`](../../workflows).
2. Look up its stages in [the canonical registry](../../registry/SDLC_STAGE_REGISTRY.json).
3. Load the mapped category skill and its stage playbook.
4. Confirm inputs, permissions, dependencies, acceptance criteria, and applicable standards.
5. Create evidence and handoff records as work progresses.

## 4. Respect the stop signs

Pause and escalate when requirements are ambiguous, dependencies are missing, authority is absent, a gate fails, evidence is inconclusive, a security/privacy risk appears, or an irreversible/prod-impacting action is proposed. The correct status is often `BLOCKED` or `NEEDS_HUMAN_APPROVAL` — never a guessed `PASS`.

## 5. Explore deeper

- [Architecture](../architecture/OVERVIEW.md)
- [Workflow guide](../workflows/WORKFLOW_GUIDE.md)
- [Role operating model](../../agents/ROLE_OPERATING_MODEL.md)
- [Evidence gate policy](../../orchestrator/policies/GATE_POLICY.md)
- [Example inventory journey](../examples/INVENTORY_APPLICATION_WALKTHROUGH.md)
