---
name: requirements-design
description: "Use when scope is needed before design: elicits, documents, validates requirements and UX. Do NOT use for architecture or coding."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["requirements", "ux", "design", "accessibility"]
---

# Requirements and experience design

## Purpose
Converts agreed business goals into requirements that are testable, traced and validated, plus the user-experience artifacts that show how they will be met. It owns stages 11-22: elicitation, documentation, functional and non-functional requirements, research, journeys, wireframes, UI and UX, prototypes, accessibility review and validation.

## When to Use
- Stakeholder needs must be captured as requirements with acceptance criteria.
- User research, journeys, wireframes or prototypes are needed before build.
- Accessibility or non-functional targets must be stated and made measurable.

## When NOT to Use
- Deciding system structure or technology: use technical-architecture.
- Building the UI: use software-implementation.
- Testing the built UI: use quality-assurance.

## Prerequisites and Requirements
- An approved goal or business case, or an explicit statement that none exists.
- Access to stakeholders or their recorded input.
- A requirement identifier scheme; create one if none exists.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- approved goals and scope
- stakeholder list

Optional inputs:
- user research
- analytics
- existing requirements
- design system

Outputs and deliverables:
- requirements with unique ids, sources and acceptance criteria
- non-functional targets with measures
- journeys, wireframes and prototype findings
- validated requirements baseline approved by the product owner

## Procedure
1. Elicit needs using interviews, observation and process evidence; retain source and authority.
2. Write functional behavior, exceptions, state transitions and measurable NFR scenarios with stable IDs.
3. Design journeys, wireframes and prototypes around observed tasks; cover empty, error, loading and recovery states.
4. Validate traceability, usability and accessibility before baselining.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Requirement uses vague words (fast, easy, robust) | Rewrite with a measure and condition before baselining. |
| Two requirements conflict | Log the conflict and send it to the product owner; do not pick silently. |
| A requirement has no source need | Trace it or remove it. |
| Accessibility target missing | Default to the organization's stated standard and level, and record the assumption. |

## Quality Gates
- [ ] Each requirement is unique, testable and traced to a need
- [ ] Non-functional targets have numbers and a verification method
- [ ] Key states (empty, loading, error) are designed
- [ ] Product owner approved the baseline

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Make a vague requirement testable
```text
Request: Rewrite the requirement 'the report should be fast'.
Context: Reports show up to 10,000 rows; support complains about waiting.
Agent behavior: Ask for the target audience and load, then express it with a percentile and condition and add an acceptance example.
Output: REQ-014: Reports of up to 10,000 rows display within 3 seconds at the 95th percentile. Acceptance: load a 10,000-row report in the test environment and measure.
Acceptance: The requirement names a measure, condition and a way to test it.
```

### Example 2: Resolve conflicting stakeholder needs
```text
Request: Sales wants a one-click export; security wants approval for every export.
Context: Exports contain customer data.
Agent behavior: Record both needs with sources, propose options (role-based approval, limited fields), and route the decision to the product owner.
Output: Conflict log entry with options and a pending decision.
Acceptance: The conflict is logged and escalated, not silently resolved.
```

## Limitations
- Cannot know what users want without research or recorded input; it will not invent personas or quotes.
- Does not approve the baseline: the product owner does.
- Design artifacts are not tested on real users unless a test is run and recorded.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Stakeholders unavailable | No access to the people who know the need | State the gap, mark affected requirements as unvalidated, and schedule the sessions. |
| Requirements keep changing | No baseline or change process | Baseline the set and route changes through a recorded request with impact. |
| Accessibility standard unknown | No policy stated | Ask for the standard and level; record the assumption if none is given. |

## Tools
- requirements repository
- BPMN/sequence/state diagrams
- design system and prototyping tools
- accessibility checks

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 11 | Requirement Elicitation | complete | Requirements Engineer |
| 12 | Requirement Documentation | complete | Requirements Engineer |
| 13 | Functional Requirements | complete | Requirements Engineer |
| 14 | Non-Functional Requirements | complete | Requirements Engineer |
| 15 | User Research | complete | UX Researcher |
| 16 | User Journey Mapping | complete | UX Researcher |
| 17 | Wireframing | complete | UI/UX Designer |
| 18 | UI Design | complete | UI/UX Designer |
| 19 | UX Design | complete | UI/UX Designer |
| 20 | Prototype Development | complete | UI/UX Designer |
| 21 | Accessibility Review | complete | Accessibility Testing Specialist |
| 22 | Requirement Validation | complete | Product Owner |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `technical-architecture`: validated requirements including non-functional targets
- `software-implementation`: wireframes, UI designs and acceptance criteria
- `quality-assurance`: acceptance criteria and risk list for test design

Receives from:
- `business-product-management`: approved business case, goals, scope and constraints

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: existing-application-enhancement, feature-development, new-product-development.
- Roles: accessibility-testing-specialist, business-analyst, frontend-engineer, performance-engineer, product-owner, requirements-engineer, security-architect, ui-ux-designer, ux-researcher.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
