---
name: application-security
description: "Use when checking a change for security risk: threats, scans, remediation, sign-off. Do NOT use for infrastructure operations."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["security", "threat-modeling", "sast", "remediation"]
---

# Application security engineering

## Purpose
Finds and drives fixes for security weaknesses in applications and their supply chain: threat modeling, SAST, DAST, dependency and container scanning, penetration testing, data protection, compliance review, remediation and sign-off. It owns stages 98-110.

## When to Use
- A feature or architecture needs a threat model.
- Scan or penetration test results need triage and remediation tracking.
- A security sign-off is needed before release.

## When NOT to Use
- Operating cloud accounts and networks: use cloud-hosting-operations.
- Governing change approval in production: use secure-change-control.
- Writing feature code: use software-implementation.

## Prerequisites and Requirements
- Written authorization for any active testing, with scope and window.
- Architecture and data flow descriptions.
- A safe environment for dynamic testing.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- architecture and data flows
- code or build under review
- authorization and scope

Optional inputs:
- previous findings
- compliance obligations
- scan results

Outputs and deliverables:
- threat model with ranked threats and controls
- triaged findings with severity method named
- remediation tracking with owners
- security sign-off recommendation

## Procedure
1. Map assets, entry points, trust boundaries, identities and sensitive data.
2. Use configured SAST/SCA/DAST/container/IaC tools and validate findings against actual exposure.
3. Prioritize by exploitability, impact and reachability; assign owner, SLA and compensating controls.
4. Retest exact fixes independently and record residual risk/exception.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| No written authorization for active testing | Do not test; request authorization. |
| Finding cannot be reproduced | Mark INCONCLUSIVE with steps tried. |
| Critical issue found in production | Stop testing, notify the owner and hand to incident-command if active. |
| Risk acceptance requested | Route to a named human with authority. |

## Quality Gates
- [ ] Each high threat has a control or an accepted risk
- [ ] Findings have reproduction steps and evidence
- [ ] Severity has a stated method
- [ ] Fixes were retested

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Threat model an upload feature
```text
Request: Threat model the document upload.
Context: Files are stored and later previewed by other users.
Agent behavior: List assets and trust boundaries, rank threats, propose controls and mark residual risk with an owner.
Output: Ranked threats led by malicious files; controls: type and size limits, scanning, storage outside the web root.
Acceptance: High threats each have a control or accepted-risk entry.
```

### Example 2: Triage scan results
```text
Request: Triage 120 SAST findings.
Context: Many duplicates and low-severity items.
Agent behavior: Group by rule, confirm exploitable items with reproduction, and assign owners and dates.
Output: Triage list with 6 confirmed findings and the dismissals with reasons.
Acceptance: Every dismissal has a stated reason.
```

## Limitations
- Scans and reviews do not prove the absence of vulnerabilities.
- Active testing needs authorization and cannot be done without it.
- This repository makes no security certification claim.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Scanner reports excessive false positives | Rules not tuned | Tune with owner approval and record changes. |
| No safe test environment | Only production exists | Limit to passive review and request an environment. |
| Authorization unclear | Scope not written | Stop and obtain a written scope. |

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

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `release-deployment`: security sign-off and open accepted risks
- `software-implementation`: remediation items with severity
- `enterprise-governance`: security evidence for audit

Receives from:
- `devops-platform`: pipeline findings for review
- `software-implementation`: code and dependency changes for scanning
- `technical-architecture`: architecture and data flows for threat modeling

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: dependency-update, infrastructure-provisioning, new-product-development, security-vulnerability-remediation.
- Roles: application-security-engineer, authentication-and-authorization-engineer, backend-engineer, compliance-specialist, devsecops-engineer, infrastructure-engineer, kubernetes-engineer, license-compliance-specialist, penetration-testing-specialist, security-architect, security-auditor, vulnerability-analyst.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
