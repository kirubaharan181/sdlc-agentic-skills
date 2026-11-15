---
name: devops-platform
description: Provides a specialist procedure to build reproducible source-to-artifact-to-environment paths. Use when the work involves CI Pipeline, Automated Test Pipeline, Build Management, Artifact Management, Containerization, Container Orchestration, Infrastructure as Code, Configuration Management and 7 more stages.
---

# Secure delivery platform

Build reproducible source-to-artifact-to-environment paths.

## Procedure
1. Map source, runner, secret, artifact and deployment trust boundaries.
2. Implement pinned/reproducible builds, tests, scans and artifact provenance.
3. Protect credentials, environments, deployment identities and immutable promotion.
4. Exercise failure/recovery paths and publish platform ownership/runbooks.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- CI/CD platform
- IaC and policy-as-code
- artifact registry
- supply-chain scanners

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 111 | CI Pipeline | complete | DevOps Engineer |
| 112 | Automated Test Pipeline | complete | DevOps Engineer |
| 113 | Build Management | stub | DevOps Engineer |
| 114 | Artifact Management | stub | Platform Engineer |
| 115 | Containerization | stub | DevOps Engineer |
| 116 | Container Orchestration | stub | Kubernetes Engineer |
| 117 | Infrastructure as Code | complete | Infrastructure Engineer |
| 118 | Configuration Management | stub | Platform Engineer |
| 119 | CD Pipeline | stub | DevOps Engineer |
| 120 | Environment Provisioning | complete | Infrastructure Engineer |
| 121 | Network Engineering | stub | Network Engineer |
| 122 | Database Operations | stub | Database Administrator |
| 123 | CDN & Edge Configuration | stub | Platform Engineer |
| 124 | Deployment Automation | stub | Deployment Engineer |
| 125 | Pipeline Security | stub | DevSecOps Engineer |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: ci-cd-pipeline-creation, environment-configuration, infrastructure-provisioning, new-product-development.
- Roles: automation-qa-engineer, cloud-engineer, database-administrator, database-engineer, deployment-engineer, devops-engineer, devsecops-engineer, infrastructure-engineer, kubernetes-engineer, network-engineer, platform-engineer.
