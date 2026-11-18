---
name: technical-architecture
description: Defines system boundaries, interfaces and trade-offs. Use when designing or reviewing architecture. Do NOT use for feature coding or release.
metadata:
  author: kirubaharan181
  version: "1.1.0"
  tags: ["architecture", "design", "adr", "trade-offs"]
---

# Architecture and technical decision-making

## Purpose
Produces reviewable architecture: boundaries, interfaces, data, security and cloud design, with the trade-offs and decisions recorded. It owns stages 23-34: solution, system, application, database, API, cloud, security, data and integration architecture, technology selection, documentation and architecture review.

## When to Use
- A new system or major change needs structure, interfaces and quality targets designed.
- A technology or integration choice needs evidence and a decision record.
- An implemented system must be checked against its intended architecture.

## When NOT to Use
- Writing or changing feature code: use software-implementation.
- Running threat tests or scans: use application-security.
- Operating cloud resources: use cloud-hosting-operations.

## Prerequisites and Requirements
- Validated requirements with quality targets, or a stated list of assumptions.
- Description of the current landscape and constraints.
- Access to existing architecture records, if any.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- requirements and quality targets
- current landscape
- constraints

Optional inputs:
- existing ADRs
- capacity data
- cost limits

Outputs and deliverables:
- context and component views
- decision records with options and consequences
- interface contracts and data ownership map
- architecture review report with findings

## Procedure
1. Inspect existing runtime, deployment, data and interface boundaries before proposing change.
2. Model components, data flows, trust zones, dependencies and failure domains.
3. Evaluate measurable quality scenarios, alternatives, lifecycle cost, migration and operational burden.
4. Publish ADRs, diagrams, control implications and review triggers.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Quality target has no number | Ask for it or record an assumption; do not design against a word. |
| Options are close in score | Choose the one that is cheaper to reverse and record the reopen condition. |
| Design adds multi-region | Require a recovery objective that justifies it. |
| Implemented system diverges from the design | Classify as accepted evolution, defect or risk, each with an owner. |

## Quality Gates
- [ ] Each quality target maps to a design element
- [ ] Each significant decision has a record with rejected options
- [ ] Interfaces have owners and versioned contracts
- [ ] Review was by someone who did not design it

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Choose between two message brokers
```text
Request: Pick a broker for order events.
Context: Peak 2,000 events per second, ordering per customer required, team knows neither.
Agent behavior: Write criteria and weights first, run a short proof of concept on ordering at peak, score both with evidence, and record the decision.
Output: ADR naming the chosen broker, rejected option, test evidence and the condition for reopening.
Acceptance: Criteria dated before scoring; proof of concept result attached.
```

### Example 2: Review implemented architecture
```text
Request: Check the billing service against the approved design.
Context: Approved design says only the orders service reads the orders database.
Agent behavior: Compare the import and data-access graph with the rules, list divergences and classify each.
Output: Conformance report with one risk finding: reporting module reads the orders database directly.
Acceptance: Each divergence has a class, owner and date.
```

## Limitations
- Cannot measure real performance without test data or a proof of concept.
- Does not approve its own designs: an independent reviewer and the architecture board do.
- Cost estimates depend on provider prices that change.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Requirements contradict a quality target | Latency and cost targets cannot both be met | Show the trade-off and ask the sponsor to choose. |
| No existing documentation | Landscape is unknown | Inspect code and deployment definitions, record findings as assumptions. |
| Decision keeps being reopened | No stated reopen condition | Add the condition to the decision record. |

## Tools
- architecture modelling
- OpenAPI/schema tooling
- threat modelling
- cost and resilience analysis

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 23 | Solution Architecture | complete | Solution Architect |
| 24 | System Architecture | complete | Software Architect |
| 25 | Application Architecture | complete | Software Architect |
| 26 | Database Architecture | complete | Database Architect |
| 27 | API Architecture | complete | API Architect |
| 28 | Cloud Architecture | complete | Cloud Architect |
| 29 | Security Architecture | complete | Security Architect |
| 30 | Data Architecture | complete | Data Architect |
| 31 | Integration Architecture | complete | Integration Architect |
| 32 | Technology Selection | complete | Enterprise Architect |
| 33 | Architecture Documentation | complete | Technical Writer |
| 34 | Architecture Review | complete | Architecture Reviewer |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Handoffs
Hands to:
- `software-implementation`: decision records, interface contracts and dependency rules
- `application-security`: architecture and data flows for threat modeling
- `cloud-hosting-operations`: cloud design and recovery objectives

Receives from:
- `requirements-design`: validated requirements including non-functional targets

Contract: [orchestrator/handoff-contracts/STANDARD_HANDOFF.md](../../../orchestrator/handoff-contracts/STANDARD_HANDOFF.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, database-migration, documentation-update, feature-development, infrastructure-provisioning, new-product-development.
- Roles: api-architect, architecture-reviewer, cloud-architect, data-architect, database-architect, enterprise-architect, integration-architect, security-architect, software-architect, solution-architect.
- Selection and handoff guidance: [docs/architecture/SKILL_SELECTION.md](../../../docs/architecture/SKILL_SELECTION.md).
