---
name: project-agile-management
description: "Use when scoping, estimating or running iterations: plans, tracks, governs delivery and risk. Do NOT use for requirements or code."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["project", "agile", "planning", "risk"]
---

# Delivery planning and flow management

## Purpose
Keeps delivery predictable and visible: scope broken into owned work, estimates as ranges, iteration plans, progress from evidence, and risks with owners. It owns stages 35-44: initiation, resources, work breakdown, estimation, sprint planning, agile management, progress, risk, stakeholders and change management.

## When to Use
- A project needs a charter, work breakdown, estimate or plan.
- An iteration must be planned or flow and impediments reviewed.
- Risks, stakeholders or changes to scope need managing.

## When NOT to Use
- Writing requirements: use requirements-design.
- Approving funding: that is a named human decision under business-product-management.
- Approving production changes: use secure-change-control.

## Prerequisites and Requirements
- An approved project or a stated scope.
- Team capacity and availability.
- A tracking tool or a written list to record work.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- scope
- team and capacity
- constraints and dates

Optional inputs:
- past throughput
- risk history
- dependency list

Outputs and deliverables:
- project charter with scope and exclusions
- work breakdown with owners and definitions of done
- estimates as ranges and a forecast
- risk register with owners and triggers
- progress report from tracked data

## Procedure
1. Establish charter, scope, decision rights, constraints and success measures.
2. Decompose deliverables into estimable work packages with acceptance evidence and dependencies.
3. Plan capacity, iteration goals, risk treatments and stakeholder cadence.
4. Track flow and forecast variance from evidence; control changes and escalate blockers.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Estimate given as one number | Report a range and the assumptions. |
| Planned work exceeds recent throughput | Remove items rather than overload the iteration. |
| Status reports green with blocked items | Recompute status from the tracker and report the difference. |
| Scope change requested | Record it as a change request with impact before accepting. |

## Quality Gates
- [ ] Lower breakdown levels add up to the whole scope
- [ ] Every package has one owner and acceptance criteria
- [ ] Forecast is a range from past throughput
- [ ] Each top risk has an owner, response and trigger

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Plan an iteration
```text
Request: Plan the next two-week sprint.
Context: Nine working days remain, one person is on leave, recent average is 24 points.
Agent behavior: Set one goal with the product owner, plan about 22 points, confirm acceptance criteria, and list dependencies.
Output: Sprint goal, selected items with criteria, and a risk list.
Acceptance: Planned work fits recent throughput and the team agreed.
```

### Example 2: Write a risk entry
```text
Request: Record the risk of a single-vendor SDK.
Context: The vendor may end support.
Agent behavior: Write cause, event and effect, rate it, assign an owner, and set a trigger and response.
Output: Risk: because the vendor is the sole SDK supplier, if support ends the migration slips three months; trigger: end-of-life notice; response: evaluate alternatives.
Acceptance: The entry has owner, trigger and response.
```

## Limitations
- Cannot see work that is not recorded in the tracker or provided.
- Forecasts are ranges based on past data and are not commitments.
- Does not replace people's decisions on priority; the product owner decides.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Tracker data is stale | Items not updated | State the age of the data and ask owners to update before reporting. |
| Dependencies unagreed | Other team unaware | Mark the date as unconfirmed and request agreement. |
| No past throughput | New team or tool | Use a wide range and revisit after two iterations. |

## Tools
- issue/project tracker
- capacity and flow metrics
- RAID and decision registers
- facilitation tools

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 35 | Project Initiation | complete | Project Manager |
| 36 | Resource Planning | complete | Project Manager |
| 37 | Work Breakdown | complete | Project Manager |
| 38 | Effort Estimation | complete | Project Manager |
| 39 | Sprint Planning | complete | Scrum Master |
| 40 | Agile Management | complete | Agile Delivery Manager |
| 41 | Progress Tracking | complete | Agile Delivery Manager |
| 42 | Risk Management | complete | Program Manager |
| 43 | Stakeholder Management | complete | Program Manager |
| 44 | Change Management | complete | Engineering Governance Specialist |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `software-implementation`: sprint backlog with acceptance criteria
- `release-deployment`: release scope and dependency list
- `enterprise-governance`: change and risk records for audit

Receives from:
- `business-product-management`: approved project charter inputs and budget
- `enterprise-governance`: improvement actions for planning

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: existing-application-enhancement, new-product-development, product-retirement.
- Roles: agile-delivery-manager, engineering-coordinator, engineering-governance-specialist, program-manager, project-manager, scrum-master.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
