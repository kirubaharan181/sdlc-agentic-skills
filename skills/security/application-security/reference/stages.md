# Application security engineering: stage reference

## Contents
- [98 Threat Modeling](#98)
- [99 SAST](#99)
- [100 DAST](#100)
- [101 SCA](#101)
- [102 Container Security](#102)
- [103 Infrastructure Security](#103)
- [104 Penetration Testing](#104)
- [105 Authentication Security](#105)
- [106 Data Protection](#106)
- [107 Compliance Review](#107)
- [108 License Compliance](#108)
- [109 Vulnerability Remediation](#109)
- [110 Security Sign-off](#110)

## 98
**Threat Modeling** (stub). Purpose: identify abuse paths and prioritize security treatment.

Inputs: system/data-flow diagrams; assets, actors and trust boundaries; security assumptions

Procedure:
1. Inventory entry points, identities, privileged operations and sensitive data.
2. Enumerate threats/abuse cases using a repeatable taxonomy and attacker capability.
3. Rate likelihood/impact and map mitigations to design controls and tests.
4. Track accepted residual risks with owner, expiry and monitoring trigger.

Deliverables: threat model; abuse-case catalogue; mitigation matrix; residual risk log

Acceptance: High-impact trust-boundary threats are addressed. Mitigations are testable. Accepted risk is authorized and time-bound.

Validation: Independent security design review.
Gate: 09-098. Approval: none required

## 99
**SAST** (stub). Purpose: identify exploitable source-code weaknesses before runtime.

Inputs: source revision and language coverage; scanner configuration and severity policy; threat model and reachable entry points

Procedure:
1. Run configured static analysis on the exact source revision and include generated/critical code according to policy.
2. Trace high-impact findings from source to sink and assess reachability and sanitization.
3. Triage false positives with evidence and assign remediation owners and SLAs.
4. Retest the fixed revision and add regression coverage for the vulnerable path.

Deliverables: SAST report; validated source-to-sink findings; remediation and retest evidence

Acceptance: Findings identify file/line and reachable path. Suppressions have rationale and expiry. Critical findings are retested after fix.

Validation: Trace a high-severity taint finding to the trust boundary and verify the fix with a regression test.
Gate: 09-099. Approval: none required

## 100
**DAST** (stub). Purpose: validate runtime attack surface within explicit authorization.

Inputs: written target scope and time window; test account and safe data; running build and rules of engagement

Procedure:
1. Confirm ownership, target list, exclusions, rate limits and stop conditions before scanning.
2. Exercise approved runtime paths for injection, authentication/session and security-header weaknesses.
3. Manually validate high-severity results without destructive payloads or unnecessary data access.
4. Record exact build/environment, reproduction and remediation; retest the fixed build.

Deliverables: DAST scan report; validated runtime findings; rules-of-engagement and retest record

Acceptance: All active tests remain in written scope. Findings are reproducible against the named build. No destructive or unnecessary data access occurs.

Validation: Run only the approved test paths and manually confirm the highest-risk finding before assigning severity.
Gate: 09-100. Approval: none required

## 101
**SCA** (stub). Purpose: assess dependency vulnerabilities and license obligations.

Inputs: resolved lockfiles and packaged artifact; SBOM and advisory feeds; license policy and runtime exposure

Procedure:
1. Generate inventory from resolved direct and transitive dependencies.
2. Match versions to advisories and assess reachability, exploitability and vendor support.
3. Review license compatibility, provenance and required notices.
4. Upgrade or replace affected components, rerun regression/security checks and compare SBOM.

Deliverables: SBOM; vulnerability and license disposition; dependency update diff; retest report

Acceptance: All shipped components have known versions and license status. Critical exposure is fixed or formally accepted. Packaged artifact matches scanned dependency tree.

Validation: Compare lockfile and packaged SBOM, then verify the resolved version and notices.
Gate: 09-101. Approval: none required

## 102
**Container Security** (stub). Purpose: assess and remediate a defined security attack surface.

Inputs: authorized scope and asset inventory; scanner/tool configuration and version; severity policy and remediation SLA

Procedure:
1. Confirm asset ownership, scope, exclusions and written authorization before active testing.
2. Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
3. Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
4. Assign remediation, retest the exact fix and record residual risk or approved exception.

Deliverables: scan/test report; validated finding register; remediation and retest evidence

Acceptance: Active testing stays within authorization. Findings have reproducible evidence and severity rationale. Closure is independently retested.

Validation: Security owner and system owner disposition.
Gate: 09-102. Approval: none required

## 103
**Infrastructure Security** (stub). Purpose: assess and remediate a defined security attack surface.

Inputs: authorized scope and asset inventory; scanner/tool configuration and version; severity policy and remediation SLA

Procedure:
1. Confirm asset ownership, scope, exclusions and written authorization before active testing.
2. Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
3. Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
4. Assign remediation, retest the exact fix and record residual risk or approved exception.

Deliverables: scan/test report; validated finding register; remediation and retest evidence

Acceptance: Active testing stays within authorization. Findings have reproducible evidence and severity rationale. Closure is independently retested.

Validation: Security owner and system owner disposition.
Gate: 09-103. Approval: none required

## 104
**Penetration Testing** (stub). Purpose: perform authorized adversarial testing with controlled evidence.

Inputs: written authorization and target inventory; rules of engagement, time window and emergency contact; data handling and stop conditions

Procedure:
1. Verify authorization, scope, exclusions and escalation contacts before any active test.
2. Test agreed attack paths with bounded techniques and avoid destructive actions or persistence.
3. Capture minimal reproduction, impact and evidence while protecting customer data.
4. Report remediation and independently retest the agreed fixes.

Deliverables: rules of engagement; penetration test log; validated finding report; retest evidence

Acceptance: No out-of-scope target is tested. Unintended impact triggers immediate stop and notification. Findings include reproducible steps and safe remediation.

Validation: Validate one approved attack path and stop immediately if the test reaches out-of-scope data.
Gate: 09-104. Approval: security-lead (always)

## 105
**Authentication Security** (stub). Purpose: assess and remediate a defined security attack surface.

Inputs: authorized scope and asset inventory; scanner/tool configuration and version; severity policy and remediation SLA

Procedure:
1. Confirm asset ownership, scope, exclusions and written authorization before active testing.
2. Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
3. Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
4. Assign remediation, retest the exact fix and record residual risk or approved exception.

Deliverables: scan/test report; validated finding register; remediation and retest evidence

Acceptance: Active testing stays within authorization. Findings have reproducible evidence and severity rationale. Closure is independently retested.

Validation: Security owner and system owner disposition.
Gate: 09-105. Approval: none required

## 106
**Data Protection** (stub). Purpose: assess and remediate a defined security attack surface.

Inputs: authorized scope and asset inventory; scanner/tool configuration and version; severity policy and remediation SLA

Procedure:
1. Confirm asset ownership, scope, exclusions and written authorization before active testing.
2. Run configured static, dynamic, dependency, container or infrastructure analysis appropriate to the asset.
3. Validate findings, remove duplicates/false positives with rationale, and prioritize exploitability and impact.
4. Assign remediation, retest the exact fix and record residual risk or approved exception.

Deliverables: scan/test report; validated finding register; remediation and retest evidence

Acceptance: Active testing stays within authorization. Findings have reproducible evidence and severity rationale. Closure is independently retested.

Validation: Security owner and system owner disposition.
Gate: 09-106. Approval: none required

## 107
**Compliance Review** (stub). Purpose: review contractual and regulatory obligations before commitment.

Inputs: contract version and counterparties; applicable policy/control obligations; legal/compliance owner

Procedure:
1. Identify service, data, security, availability, audit, retention, subcontracting and exit obligations.
2. Map each obligation to an internal control owner and evidence source.
3. Flag ambiguous liability, data processing, IP, jurisdiction, renewal and termination terms.
4. Record legal review questions and do not provide legal approval outside delegated authority.

Deliverables: obligation matrix; contract exception log; review decision

Acceptance: Every material obligation has an owner and evidence path. Exceptions have an authorized risk owner. Unresolved legal interpretation is escalated.

Validation: Legal and compliance owner sign-off.
Gate: 09-107. Approval: none required

## 108
**License Compliance** (stub). Purpose: identify software license obligations and distribution risk.

Inputs: dependency inventory and lockfiles; license policy and distribution model; notice/attribution requirements

Procedure:
1. Generate an SBOM or equivalent inventory from resolved dependencies.
2. Identify direct/transitive licenses, copyleft triggers, attribution and source-disclosure obligations.
3. Compare obligations with product distribution and company policy; escalate ambiguous licenses.
4. Record approved substitutions, notices and exception expiry.

Deliverables: SBOM; license compatibility matrix; notice bundle; exception record

Acceptance: All shipped dependencies have a resolved license or approved exception. Notices and obligations are fulfilled. Unknown licenses are not silently accepted.

Validation: Legal/compliance review.
Gate: 09-108. Approval: compliance-owner (when a license exception is requested)

## 109
**Vulnerability Remediation** (stub). Purpose: remove a validated vulnerability and prove the exposure is closed.

Inputs: validated finding and affected component/version; exploitability, exposure and remediation SLA; fix owner and release constraints

Procedure:
1. Confirm affected runtime component/version and reachability before selecting a fix.
2. Prioritize using exploit maturity, exposure, privileges and data impact.
3. Apply a supported upgrade/configuration/code correction and add regression protection.
4. Rescan and independently retest the exact released artifact; record residual risk.

Deliverables: vulnerability remediation ticket; fixed version/commit evidence; rescan and retest report

Acceptance: Affected exposure is removed from the released artifact. Fix does not introduce an unapproved breaking change. Retest is independent and revision-pinned.

Validation: Verify the patched component in the packaged runtime artifact, not only the source manifest.
Gate: 09-109. Approval: none required

## 110
**Security Sign-off** (stub). Purpose: make an independent security release decision from verified evidence.

Inputs: threat model and asset scope; scan findings and remediation evidence; risk acceptance authority and exception expiry

Procedure:
1. Review threat coverage, SAST/SCA/DAST/IaC results and the exact candidate revision.
2. Verify high-severity findings have independent retest evidence or authorized exception.
3. Assess residual risk, compensating controls, exposure and release conditions.
4. Record approve, conditional approve or block with named security authority.

Deliverables: security gate report; finding disposition and retest links; time-bound exception record

Acceptance: No critical unresolved finding is hidden as PASS. Reviewer is independent from implementation. Exceptions have owner, scope and expiry.

Validation: Re-fetch the candidate revision and verify every critical finding disposition before issuing the security decision.
Gate: 09-110. Approval: security-lead (always)
