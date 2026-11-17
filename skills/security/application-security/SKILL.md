---
name: application-security
description: Provides a specialist procedure to reduce attack surface through threat-led assessment, verified remediation and authorized testing. Use when the work involves Threat Modeling, SAST, DAST, SCA, Container Security, Infrastructure Security, Penetration Testing, Authentication Security and 5 more stages.
---

# Application security engineering

Reduce attack surface through threat-led assessment, verified remediation and authorized testing.

## Procedure
1. Map assets, entry points, trust boundaries, identities and sensitive data.
2. Use configured SAST/SCA/DAST/container/IaC tools and validate findings against actual exposure.
3. Prioritize by exploitability, impact and reachability; assign owner, SLA and compensating controls.
4. Retest exact fixes independently and record residual risk/exception.

Shared rules (evidence, approvals, failure, handoff): [../../_shared/CORE_PROCEDURE.md](../../_shared/CORE_PROCEDURE.md).

## Tools
- configured security scanners
- SBOM and dependency tools
- threat model
- vulnerability tracker

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 98 | Threat Modeling | complete | Security Architect |
| 99 | SAST | complete | DevSecOps Engineer |
| 100 | DAST | complete | DevSecOps Engineer |
| 101 | SCA | complete | DevSecOps Engineer |
| 102 | Container Security | complete | DevSecOps Engineer |
| 103 | Infrastructure Security | complete | DevSecOps Engineer |
| 104 | Penetration Testing | complete | Penetration Testing Specialist |
| 105 | Authentication Security | complete | Application Security Engineer |
| 106 | Data Protection | complete | Application Security Engineer |
| 107 | Compliance Review | complete | Compliance Specialist |
| 108 | License Compliance | complete | License Compliance Specialist |
| 109 | Vulnerability Remediation | complete | Application Security Engineer |
| 110 | Security Sign-off | complete | Security Auditor |

Per-stage inputs, outputs, acceptance criteria and validation: [reference/stages.md](reference/stages.md).

## Related
- Examples: [examples/](examples/) (illustrative only).
- Workflows: dependency-update, infrastructure-provisioning, new-product-development, security-vulnerability-remediation.
- Roles: application-security-engineer, authentication-and-authorization-engineer, backend-engineer, compliance-specialist, devsecops-engineer, infrastructure-engineer, kubernetes-engineer, license-compliance-specialist, penetration-testing-specialist, security-architect, security-auditor, vulnerability-analyst.
