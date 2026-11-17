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
**Threat Modeling** (complete). Purpose: find and rank ways an attacker can abuse the system before it is built or changed, and tie each to a control and a test.

Entry criteria: Architecture or data-flow diagram exists for the feature or system in scope; Assets and data classifications are listed; Accountable security-architect and a developer who knows the design are available

Inputs: data-flow diagram with trust boundaries; asset and data classification list; identity and privilege model; existing threat model (if any)

Procedure:
1. Draw or confirm the data-flow diagram; mark every trust boundary, entry point, data store and external dependency.
2. Enumerate threats per element with a named taxonomy (for example STRIDE) and an attacker capability (unauthenticated, authenticated user, insider, compromised dependency).
3. Score each threat by likelihood and impact on one fixed scale; record the scale in the document.
4. For each threat above the agreed threshold, name a mitigation, the control that implements it, and the test or scan that will verify it.
5. Record accepted residual risks with owner, rationale and an expiry date.
6. Link each mitigation to a backlog item and each verification to a later stage (SAST 99, DAST 100, Penetration Testing 104).

Deliverables: threat model document; abuse-case catalogue; mitigation-to-test matrix; residual risk log

Acceptance: Every trust boundary crossing has at least one enumerated threat or a written reason for none Every high or critical threat has a mitigation with a verifying test Every accepted risk has a named owner and an expiry date Diagram and document are versioned with the design they describe

Validation: Independent security design review by someone who did not author the model.

- manual: independent reviewer walks the diagram and confirms each trust-boundary crossing has a threat entry expect: reviewer initials and date recorded in the document
- `grep -c 'residual-risk-expiry:' docs/threat-model.md   # example` expect: count equals the number of accepted risks

Failure modes:
- Diagram is out of date with the code | detect: Reviewer cannot map a code path to a diagram element | respond: Return to step 1; model is BLOCKED until the diagram matches the current design
- Threats listed without mitigations | detect: Mitigation-to-test matrix has empty cells | respond: Mark INCONCLUSIVE; assign owners and dates, or record explicit risk acceptance
- Risk accepted by the author of the feature | detect: Approver equals implementer in the residual risk log | respond: Reject; the security-architect or risk owner must accept

ILLUSTRATIVE: A new file-upload endpoint crosses the browser-to-API boundary. Enumerated threats include oversized or malicious files (denial of service, malware storage) and path traversal in filenames. Mitigations: size limit and content-type allow-list at the gateway, random server-side object names, virus scan before the file becomes readable. Each maps to an integration test and to DAST scope in stage 100.

Gate: 09-098. Approval: none required

## 99
**SAST** (complete). Purpose: find vulnerabilities in first-party source code by analysis before it runs, and drive findings to a fix or a recorded exception.

Entry criteria: Code builds from a clean checkout at a pinned commit; Scanner and ruleset versions are chosen and recorded; A baseline of previously triaged findings exists, or an empty baseline is stated

Inputs: source at an exact commit; SAST tool configuration and ruleset; baseline of triaged findings; language and framework list

Procedure:
1. Run the configured scanner on the exact commit; save the raw report (SARIF) and tool version.
2. Triage each new finding as true positive, false positive or accepted risk; a false positive needs a written reason and a suppression with owner and expiry.
3. For true positives rate severity by reachability and data exposure, not by rule severity alone.
4. Fix or open a tracked issue with SLA for every true positive; block the merge on critical and high findings.
5. Rerun the scanner on the fix commit and confirm the finding is gone and no new ones appeared.
6. Publish the report and the updated baseline with the commit id.

Deliverables: raw scanner report (SARIF); triage log; suppression register with expiries; fix verification run

Acceptance: Scan ran on the commit under review and covers all in-scope languages No open critical or high true positive, or each has an approved exception Every suppression has a reason, owner and expiry Rerun after fixes shows zero regression

Validation: Compare the rerun report against the pre-fix report for the same ruleset version.

- `semgrep scan --config auto --sarif -o reports/sast.sarif --error   # example; use the project's configured scanner` expect: exit 0 and no critical/high findings outside the approved baseline
- `python3 -c "import json;r=json.load(open('reports/sast.sarif'));print(sum(len(x['results']) for x in r['runs']))"` expect: number of results matches the triage log

Failure modes:
- Scanner skipped part of the code | detect: Report file count is below the repository's source file count | respond: Mark INCONCLUSIVE; fix includes/excludes and rerun
- Blanket suppressions hide real issues | detect: Suppression register has entries without reason or expiry | respond: Reject the suppression; reopen the finding
- Findings reported on a different commit | detect: Report commit id differs from the merge commit | respond: Discard report; rerun on the correct commit

ILLUSTRATIVE: The scanner flags string-built SQL in an export job. Triage: true positive, reachable by an authenticated user via a filter parameter, high severity. Fix replaces concatenation with a parameterized query and adds a regression test. Rerun shows the finding closed.

Gate: 09-099. Approval: none required

## 100
**DAST** (complete). Purpose: find vulnerabilities that only appear in a running application by sending hostile requests to an authorized non-production target.

Entry criteria: Written scope names the target URLs, environment and test window; Target is non-production or has explicit owner approval for testing; Test accounts and data exist; no real customer data is used

Inputs: target base URL and API definition; authenticated test accounts per role; scope and window approval; DAST tool configuration

Procedure:
1. Confirm scope and window in writing; verify the target host matches the approved list before sending any traffic.
2. Run an authenticated crawl or API-definition-driven scan per role, with rate limits agreed with the environment owner.
3. Triage each alert; reproduce with a minimal request and record request and response evidence.
4. Rate by exploitability and data exposure; open fix issues with owner and SLA.
5. Retest each fixed issue with the same request and confirm the behavior changed.
6. Report coverage honestly: which routes and roles were and were not exercised.

Deliverables: scan report with raw requests and responses; triaged findings list; coverage statement; retest evidence

Acceptance: Scan stayed inside the approved scope Each reported issue has a reproduction No open critical or high finding without an approved exception Coverage gaps are listed, not hidden

Validation: Independent retest of fixed findings with the original request.

- `zap-api-scan.py -t $API_SPEC_URL -f openapi -r reports/dast.html -J reports/dast.json   # example; non-production target only` expect: report generated; no high alerts outside the approved baseline
- `grep -oE 'https?://[^/\"]+' reports/dast.json | sort -u` expect: every host listed is in the approved scope file

Failure modes:
- Scan hit an out-of-scope host | detect: Request log contains a host not in scope | respond: Stop immediately; notify the environment owner; record an incident note
- Scan unauthenticated only | detect: Coverage statement lists no authenticated routes | respond: Mark INCONCLUSIVE; rerun with role accounts
- Scan degraded the test environment | detect: Error rate rises during the window | respond: Lower the rate limit and rerun in the next window

ILLUSTRATIVE: An authenticated scan of a staging API finds that changing an order id in the URL returns another user's order. Reproduced with two test accounts, rated high, fixed with an ownership check, retested with the same request returning 403.

Gate: 09-100. Approval: none required

## 101
**SCA** (complete). Purpose: find known-vulnerable and license-problematic third-party components in what is actually shipped.

Entry criteria: Lockfiles are committed and the build is reproducible; Advisory data source and its refresh date are recorded; Policy for allowed severities and licenses exists

Inputs: lockfiles and the built artifact; SBOM or tool to generate one; advisory database snapshot; dependency policy

Procedure:
1. Generate an SBOM from resolved direct and transitive dependencies of the built artifact.
2. Match components to advisories; record advisory ids, affected range and fixed version.
3. Assess reachability and exploitability for each match; do not rate by CVSS alone.
4. Upgrade, replace or pin to a patched version; where none exists record a compensating control and an expiry.
5. Rebuild, regenerate the SBOM and compare against the earlier one to confirm the fix and spot new components.
6. Attach the SBOM and the disposition table to the release evidence.

Deliverables: SBOM (CycloneDX or SPDX); vulnerability disposition table; dependency update diff; post-fix SBOM comparison

Acceptance: SBOM matches the shipped artifact, not only the manifest No unresolved critical or high advisory without an approved exception Every exception has owner and expiry Advisory data age is stated

Validation: Compare SBOM of the packaged artifact with the lockfile and re-run the audit after fixes.

- `osv-scanner --lockfile=package-lock.json --format json > reports/sca.json   # example; use the ecosystem's audit tool` expect: exit 0 or only findings listed in the exception register
- `syft packages dir:. -o cyclonedx-json > reports/sbom.json   # example` expect: component count matches the artifact contents

Failure modes:
- Scan ran on the manifest, not the artifact | detect: SBOM lacks transitive or vendored components | respond: Regenerate from the built artifact
- Stale advisory data | detect: Advisory snapshot older than the agreed age | respond: Refresh data and rerun
- Upgrade breaks behavior | detect: Regression tests fail after bumping | respond: Revert, pin, record a compensating control and a dated follow-up

ILLUSTRATIVE: The audit reports a deserialization flaw in a transitive library. It is reachable because the service parses uploaded archives. The direct dependency is bumped to a release that pulls the patched version; the post-fix SBOM shows the new version and tests pass.

Gate: 09-101. Approval: none required

## 102
**Container Security** (complete). Purpose: find and fix vulnerabilities and unsafe configuration in container images and their runtime settings before they run in production.

Entry criteria: Image is built from a pinned base image and a Dockerfile in the repository; Registry and scanner access are available; Runtime policy (user, capabilities, network) is defined

Inputs: Dockerfile and build context; built image digest; base image policy; runtime security policy

Procedure:
1. Build the image from a clean checkout and record its digest; scan the digest, not a tag.
2. Scan OS packages and application dependencies for known vulnerabilities; record advisory ids and fixed versions.
3. Check the image configuration: non-root user, no embedded secrets, minimal base, read-only filesystem where possible, no unnecessary capabilities.
4. Fix by updating the base image or packages, or by removing the component; document any accepted finding with owner and expiry.
5. Rebuild, rescan the new digest and compare findings with the previous scan.
6. Sign or record the approved digest so deployment can verify it matches.

Deliverables: image scan report for the digest; configuration check results; exception register; approved digest record

Acceptance: The scanned digest equals the digest that will be deployed No unresolved critical or high finding without an approved exception Image runs as a non-root user with no embedded secrets Every exception has owner and expiry

Validation: Security owner and system owner disposition of remaining findings.

- `trivy image --severity HIGH,CRITICAL --exit-code 1 registry.example.com/app@sha256:<digest>   # example; use the project's scanner` expect: exit 0, or only findings listed in the exception register
- `docker inspect --format '{{.Config.User}}' registry.example.com/app@sha256:<digest>` expect: a non-root user, not empty and not root

Failure modes:
- Scanned a tag that later moved | detect: Scan digest differs from deployed digest | respond: Rescan the deployed digest; BLOCKED until it matches
- Secret baked into an image layer | detect: Scanner or history inspection finds a credential | respond: Rotate the secret, rebuild without it, never rely on deleting a later layer
- Base image never updated | detect: Same findings reappear each scan | respond: Schedule base-image refresh and rebuild

ILLUSTRATIVE: The scan of a service image reports a critical OpenSSL issue in the base layer. The base image is bumped to the patched release, the digest changes, the rescan is clean, and the container runs as user 10001.

Gate: 09-102. Approval: none required

## 103
**Infrastructure Security** (complete). Purpose: reduce the attack surface of the networks, hosts and cloud configuration the system runs on.

Entry criteria: Infrastructure inventory and architecture exist; Security baseline or benchmark is chosen; Access to configuration data is available

Inputs: infrastructure inventory; network and cloud configuration; security baseline; previous findings

Procedure:
1. Check network exposure: which ports and services are reachable from the internet and between zones.
2. Assess cloud and host configuration against the chosen baseline (for example CIS) and record gaps.
3. Review identity and access: roles, wildcard permissions, unused credentials, and administrative paths.
4. Check encryption in transit and at rest, logging and patch status.
5. Rate findings, fix through infrastructure as code, and rescan.
6. Record accepted risks with owner and expiry.

Deliverables: exposure report; baseline assessment; fixes in code; rescan results

Acceptance: No unintended service is exposed to the internet No wildcard administrative permission without an exception Encryption and logging are enabled where required Rescan shows the findings closed

Validation: Security review of the rescan.

- `nmap -Pn -p- --open <public-ip>   # example; scan only systems you are authorized to test` expect: only intended ports are open
- `trivy config terraform/   # example baseline check` expect: no high findings outside the exception register

Failure modes:
- Scan of systems without authorization | detect: Target not in scope | respond: Stop; use only approved targets
- Fixed by console edit | detect: IaC differs from reality | respond: Fix in code
- Public storage bucket | detect: Anonymous access enabled | respond: Remove public access and review data exposure

ILLUSTRATIVE: A review finds a database port reachable from the internet and an administrative role with a wildcard permission. Both are fixed in infrastructure code and the rescan shows them closed.

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
**License Compliance** (complete). Purpose: check that third-party licenses allow how we use and distribute the software, and keep proof.

Entry criteria: Dependency inventory or SBOM exists; License policy lists allowed, review-required and forbidden licenses; Legal or compliance contact exists

Inputs: SBOM and dependency list; license policy; distribution model (internal, SaaS, shipped); license texts

Procedure:
1. List every dependency with its license from the SBOM, including transitive and vendored code.
2. Classify each license against the policy and the way the software is distributed; copyleft obligations depend on distribution.
3. Flag unknown, missing and conflicting licenses for review by compliance.
4. Resolve flagged items: replace the component, obtain permission, or document the accepted obligation.
5. Prepare required notices and attributions and include them in the release.
6. Record the decision for each flagged license with the person who made it.

Deliverables: license inventory; flagged items and decisions; notices and attribution file; compliance-owner approval

Acceptance: Every component has a recorded license No forbidden license remains Each review-required license has a decision Notices are included in the release

Validation: Compliance-owner approval.

- `pip-licenses --format=csv > reports/licenses.csv   # example; use the ecosystem's tool` expect: every dependency has a license entry
- manual: compare licenses in the report against the forbidden list expect: no matches or each has a decision

Failure modes:
- License unknown | detect: Entry says UNKNOWN | respond: Check the source; ask legal or replace
- Copyleft in a shipped product | detect: Strong copyleft licence in distributed code | respond: Replace or obtain legal approval
- Notices missing | detect: Release lacks attribution file | respond: Generate and ship it

ILLUSTRATIVE: The inventory shows one dependency with an unknown license. Compliance contacts the maintainer, receives a permissive license statement, and records the decision before release.

Gate: 09-108. Approval: compliance-owner (when a license exception is requested)

## 109
**Vulnerability Remediation** (complete). Purpose: fix confirmed vulnerabilities within agreed deadlines and prove they are closed.

Entry criteria: Vulnerability findings are triaged and confirmed (stages 99-101); Remediation deadlines by severity exist; An owner for each finding can be named

Inputs: triaged findings with severity; remediation deadline policy; affected code, dependency or configuration; exception process

Procedure:
1. Order findings by severity, exposure and exploit activity, and assign an owner and a due date to each.
2. Choose the remedy: patch or upgrade, code fix, configuration change, or compensating control when no fix exists.
3. Apply the fix on a branch with a test that fails on the vulnerable behavior where practical.
4. Run the same scan or test that found the issue and confirm it no longer reports it.
5. Release through the normal path; use the emergency path only for actively exploited issues.
6. Close the finding with evidence, or record an exception with owner, reason and expiry.

Deliverables: remediation plan with owners and due dates; fix and regression test; rescan evidence; exception register entries

Acceptance: Every critical and high finding is fixed within policy or has an approved exception Closure is shown by rerunning the original check Exceptions have owner and expiry Fixes shipped through reviewed changes

Validation: Independent rescan by security, not by the fixing engineer.

- `semgrep scan --config auto --error reports-src/   # example; rerun the scanner that found it` expect: the finding no longer appears
- manual: compare open findings with their due dates expect: none overdue without an exception

Failure modes:
- Fix closes the finding in the tracker but not in the scan | detect: Rescan still reports it | respond: Reopen the finding
- Deadline missed silently | detect: Overdue finding with no exception | respond: Escalate to the security lead
- Fix introduces a regression | detect: Tests fail after patching | respond: Revert and redesign the fix

ILLUSTRATIVE: A high-severity injection finding is assigned with a seven-day due date. The fix uses a parameterized query with a regression test; the SAST rescan no longer reports the finding and security closes it.

Gate: 09-109. Approval: none required

## 110
**Security Sign-off** (complete). Purpose: give a person independent of the implementation the evidence needed to accept the remaining security risk of a release.

Entry criteria: Security stages in scope (threat model, SAST, DAST, SCA, secrets) have recorded results; Open findings and exceptions are listed with owners; Auditor did not implement the controls being reviewed

Inputs: evidence records for security stages; open findings and exception register; threat model residual risks; release scope

Procedure:
1. Collect the evidence record of each security stage and check it names a real commit, command and result.
2. Re-run a sample of the recorded checks independently and compare results.
3. List every open finding, exception and residual risk with owner and expiry; flag any without one.
4. Decide per finding: accept, require fix, or require compensating control; state reasoning.
5. Write the sign-off record: scope, evidence reviewed, sample re-runs, decision, conditions.
6. Submit to the security-lead for the human decision; do not self-approve.

Deliverables: sign-off record; sample re-run results; open risk register; conditions list

Acceptance: Every security stage in scope has evidence or an explicit waiver Sample re-runs agree with recorded results No critical or high finding is open without a security-lead exception Decision and conditions are written and dated

Validation: Security-lead approval of the sign-off record.

- `python3 scripts/check_references.py && python3 scripts/validate.py   # repository integrity before review` expect: both exit 0
- manual: open each stage evidence record and confirm commit, command, result and that it is not flagged example expect: none missing; none flagged example

Failure modes:
- Evidence is illustrative or unrun | detect: Record flagged example or lacks a command and revision | respond: Treat as FAIL for that stage; do not sign off
- Auditor reviewed own work | detect: Auditor appears as implementer in the record | respond: Reassign review to an independent person
- Pressure to ship with open critical findings | detect: Exception without owner or expiry | respond: Decline; escalate to the security-lead

ILLUSTRATIVE: Evidence is complete except one DAST high finding with a fix merged but not retested. The auditor requires the retest as a condition; sign-off is conditional on that passing before release.

Gate: 09-110. Approval: security-lead (always)
