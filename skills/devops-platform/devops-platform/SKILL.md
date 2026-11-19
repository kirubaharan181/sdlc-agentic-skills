---
name: devops-platform
description: "Use when automating delivery: CI/CD, containers, infrastructure as code, environments. Do NOT use for release approval or runtime ops."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["devops", "ci-cd", "containers", "iac"]
---

# Secure delivery platform

## Purpose
Automates secure, repeatable delivery: CI and CD pipelines, builds and artifacts, containers and orchestration, infrastructure as code, configuration, environment provisioning and deployment automation. It owns stages 111-125.

## When to Use
- A pipeline, build or deployment automation is needed or fails.
- Containers, orchestration or infrastructure as code must be defined.
- Environments must be provisioned reproducibly.

## When NOT to Use
- Approving a release: use release-deployment.
- Running production services: use cloud-hosting-operations.
- Setting repository rules: use engineering-governance.

## Prerequisites and Requirements
- Repository access and build instructions.
- Target platform and environment definitions.
- A secrets store for pipeline credentials.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- repository and build steps
- target environments

Optional inputs:
- existing pipelines
- security requirements
- artifact repository

Outputs and deliverables:
- pipeline definitions as code
- versioned, scanned artifacts
- container and infrastructure definitions
- reproducible environments and pipeline run records

## Procedure
1. Map source, runner, secret, artifact and deployment trust boundaries.
2. Implement pinned/reproducible builds, tests, scans and artifact provenance.
3. Protect credentials, environments, deployment identities and immutable promotion.
4. Exercise failure/recovery paths and publish platform ownership/runbooks.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| Pipeline needs a long-lived credential | Use short-lived federated credentials where possible. |
| Untrusted pull request triggers a privileged job | Separate the trust levels; deny secrets to untrusted code. |
| Environment differs from code | Detect drift and reapply from code. |
| Production deploy requested | Require the approval recorded under release-deployment. |

## Quality Gates
- [ ] Builds are reproducible and pinned
- [ ] Pipelines run with least privilege
- [ ] Artifacts are scanned and identifiable
- [ ] Environments are created from code

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Create a CI pipeline
```text
Request: Add CI for the notifications service.
Context: Python, tests take 4 minutes, protected main.
Agent behavior: Define build, lint, test and scan jobs with pinned versions and read-only token permissions.
Output: Pipeline file, a run record and the required-check setting.
Acceptance: Pull requests cannot merge without the checks.
```

### Example 2: Harden a pull-request workflow
```text
Request: Fork pull requests run with secrets.
Context: Workflow triggers on pull_request_target.
Agent behavior: Split into an untrusted test job without secrets and a trusted release job, then test with a fork.
Output: Workflow change and a negative test showing the fork cannot read secrets.
Acceptance: The negative test passes.
```

## Limitations
- Cannot verify pipelines against platforms it cannot reach.
- Production changes require human approval.
- Pipeline results depend on runner images and versions.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Build works locally but fails in CI | Different versions or missing files | Pin versions and compare environments. |
| Pipeline slow | No caching or parallelism | Measure stages, cache safely and parallelize. |
| Secrets exposed in logs | Unmasked output | Rotate, mask and add a log scan. |

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
| 113 | Build Management | complete | DevOps Engineer |
| 114 | Artifact Management | complete | Platform Engineer |
| 115 | Containerization | complete | DevOps Engineer |
| 116 | Container Orchestration | complete | Kubernetes Engineer |
| 117 | Infrastructure as Code | complete | Infrastructure Engineer |
| 118 | Configuration Management | complete | Platform Engineer |
| 119 | CD Pipeline | complete | DevOps Engineer |
| 120 | Environment Provisioning | complete | Infrastructure Engineer |
| 121 | Network Engineering | complete | Network Engineer |
| 122 | Database Operations | complete | Database Administrator |
| 123 | CDN & Edge Configuration | complete | Platform Engineer |
| 124 | Deployment Automation | complete | Deployment Engineer |
| 125 | Pipeline Security | complete | DevSecOps Engineer |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `release-deployment`: deployable artifacts and pipeline run records
- `cloud-hosting-operations`: infrastructure definitions
- `application-security`: pipeline findings for review

Receives from:
- `engineering-governance`: repository and configuration conventions for pipelines

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: ci-cd-pipeline-creation, environment-configuration, infrastructure-provisioning, new-product-development.
- Roles: automation-qa-engineer, cloud-engineer, database-administrator, database-engineer, deployment-engineer, devops-engineer, devsecops-engineer, infrastructure-engineer, kubernetes-engineer, network-engineer, platform-engineer.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
