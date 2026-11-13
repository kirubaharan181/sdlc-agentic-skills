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

**Purpose:** identify exploitable source-code weaknesses before runtime

**Procedure:**
- Run configured static analysis on the exact source revision and include generated/critical code according to policy.
- Trace high-impact findings from source to sink and assess reachability and sanitization.
- Triage false positives with evidence and assign remediation owners and SLAs.
- Retest the fixed revision and add regression coverage for the vulnerable path.

**Inputs:** source revision and language coverage, scanner configuration and severity policy, threat model and reachable entry points
**Artifact:** SAST report
**Verification:** Trace a high-severity taint finding to the trust boundary and verify the fix with a regression test.
**Handoff:** Transfer SAST report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 100. DAST

**Purpose:** validate runtime attack surface within explicit authorization

**Procedure:**
- Confirm ownership, target list, exclusions, rate limits and stop conditions before scanning.
- Exercise approved runtime paths for injection, authentication/session and security-header weaknesses.
- Manually validate high-severity results without destructive payloads or unnecessary data access.
- Record exact build/environment, reproduction and remediation; retest the fixed build.

**Inputs:** written target scope and time window, test account and safe data, running build and rules of engagement
**Artifact:** DAST scan report
**Verification:** Run only the approved test paths and manually confirm the highest-risk finding before assigning severity.
**Handoff:** Transfer DAST scan report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 101. SCA

**Purpose:** assess dependency vulnerabilities and license obligations

**Procedure:**
- Generate inventory from resolved direct and transitive dependencies.
- Match versions to advisories and assess reachability, exploitability and vendor support.
- Review license compatibility, provenance and required notices.
- Upgrade or replace affected components, rerun regression/security checks and compare SBOM.

**Inputs:** resolved lockfiles and packaged artifact, SBOM and advisory feeds, license policy and runtime exposure
**Artifact:** SBOM
**Verification:** Compare lockfile and packaged SBOM, then verify the resolved version and notices.
**Handoff:** Transfer SBOM with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

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

**Purpose:** perform authorized adversarial testing with controlled evidence

**Procedure:**
- Verify authorization, scope, exclusions and escalation contacts before any active test.
- Test agreed attack paths with bounded techniques and avoid destructive actions or persistence.
- Capture minimal reproduction, impact and evidence while protecting customer data.
- Report remediation and independently retest the agreed fixes.

**Inputs:** written authorization and target inventory, rules of engagement, time window and emergency contact, data handling and stop conditions
**Artifact:** rules of engagement
**Verification:** Validate one approved attack path and stop immediately if the test reaches out-of-scope data.
**Handoff:** Transfer rules of engagement with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

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

**Purpose:** remove a validated vulnerability and prove the exposure is closed

**Procedure:**
- Confirm affected runtime component/version and reachability before selecting a fix.
- Prioritize using exploit maturity, exposure, privileges and data impact.
- Apply a supported upgrade/configuration/code correction and add regression protection.
- Rescan and independently retest the exact released artifact; record residual risk.

**Inputs:** validated finding and affected component/version, exploitability, exposure and remediation SLA, fix owner and release constraints
**Artifact:** vulnerability remediation ticket
**Verification:** Verify the patched component in the packaged runtime artifact, not only the source manifest.
**Handoff:** Transfer vulnerability remediation ticket with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.

## 110. Security Sign-off

**Purpose:** make an independent security release decision from verified evidence

**Procedure:**
- Review threat coverage, SAST/SCA/DAST/IaC results and the exact candidate revision.
- Verify high-severity findings have independent retest evidence or authorized exception.
- Assess residual risk, compensating controls, exposure and release conditions.
- Record approve, conditional approve or block with named security authority.

**Inputs:** threat model and asset scope, scan findings and remediation evidence, risk acceptance authority and exception expiry
**Artifact:** security gate report
**Verification:** Re-fetch the candidate revision and verify every critical finding disposition before issuing the security decision.
**Handoff:** Transfer security gate report with source/revision, validation evidence, owner, limitations, unresolved risks and the next decision to the downstream role.
