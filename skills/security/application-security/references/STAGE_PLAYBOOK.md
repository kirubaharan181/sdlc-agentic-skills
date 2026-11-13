# Application security engineering — Stage Playbook

> Generated from the canonical stage registry. Use the parent skill first, then load only the relevant stage entry.

## 98. Threat Modeling

**Purpose:** identify abuse paths and prioritize security treatment

**Procedure:**
- Inventory entry points, identities, privileged operations and sensitive data.
- Enumerate threats/abuse cases using a repeatable taxonomy and attacker capability.
- Rate likelihood/impact and map mitigations to design controls and tests.
- Track accepted residual risks with owner, expiry and monitoring trigger.

**Inputs:** system/data-flow diagrams, assets, actors and trust boundaries, security assumptions
**Artifact:** threat model
**Verification:** Independent security design review.
**Handoff:** Transfer threat model with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 99. SAST

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 100. DAST

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 101. SCA

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 102. Container Security

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 103. Infrastructure Security

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 104. Penetration Testing

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 105. Authentication Security

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 106. Data Protection

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 107. Compliance Review

**Purpose:** review contractual and regulatory obligations before commitment

**Procedure:**
- Identify service, data, security, availability, audit, retention, subcontracting and exit obligations.
- Map each obligation to an internal control owner and evidence source.
- Flag ambiguous liability, data processing, IP, jurisdiction, renewal and termination terms.
- Record legal review questions and do not provide legal approval outside delegated authority.

**Inputs:** contract version and counterparties, applicable policy/control obligations, legal/compliance owner
**Artifact:** obligation matrix
**Verification:** Legal and compliance owner sign-off.
**Handoff:** Transfer obligation matrix with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 108. License Compliance

**Purpose:** identify software license obligations and distribution risk

**Procedure:**
- Generate an SBOM or equivalent inventory from resolved dependencies.
- Identify direct/transitive licenses, copyleft triggers, attribution and source-disclosure obligations.
- Compare obligations with product distribution and company policy; escalate ambiguous licenses.
- Record approved substitutions, notices and exception expiry.

**Inputs:** dependency inventory and lockfiles, license policy and distribution model, notice/attribution requirements
**Artifact:** SBOM
**Verification:** Legal/compliance review.
**Handoff:** Transfer SBOM with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 109. Vulnerability Remediation

**Purpose:** assess and remediate a defined security attack surface

**Procedure:**
- Confirm asset ownership, scope, exclusions and written authorization before active testing.
- Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
- Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
- Assign remediation, retest the exact fix and record residual risk or approved exception.

**Inputs:** authorized scope and asset inventory, scanner/tool configuration and version, severity policy and remediation SLA
**Artifact:** scan/test report
**Verification:** Security owner and system owner disposition.
**Handoff:** Transfer scan/test report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 110. Security Sign-off

**Purpose:** prepare a controlled decision with sufficient evidence and independent authority

**Procedure:**
- Check the decision request is complete, in scope and owned by an authorized requester.
- Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
- Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
- Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

**Inputs:** decision request and accountable sponsor, impact/risk assessment, supporting evidence and alternatives
**Artifact:** decision record
**Verification:** Independent approval record and audit trail.
**Handoff:** Transfer decision record with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
