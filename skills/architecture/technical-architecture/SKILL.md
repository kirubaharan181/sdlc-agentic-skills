---
name: technical-architecture
description: Provides a specialist procedure to define system boundaries and quality attributes with explicit, reviewable trade-offs. Use when the work involves Solution Architecture, System Architecture, Application Architecture, Database Architecture, API Architecture, Cloud Architecture, Security Architecture, Data Architecture and 4 more stages.
---

# Architecture and technical decision-making

Define system boundaries and quality attributes with explicit, reviewable trade-offs.

## Procedure
1. Inspect existing runtime, deployment, data and interface boundaries before proposing change.
2. Model components, data flows, trust zones, dependencies and failure domains.
3. Evaluate measurable quality scenarios, alternatives, lifecycle cost, migration and operational burden.
4. Publish ADRs, diagrams, control implications and review triggers.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

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

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: api-version-upgrade, database-migration, documentation-update, feature-development, infrastructure-provisioning, new-product-development.
- Roles: api-architect, architecture-reviewer, cloud-architect, data-architect, database-architect, enterprise-architect, integration-architect, security-architect, software-architect, solution-architect.
