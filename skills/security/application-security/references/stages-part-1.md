# Application security engineering: stage reference (part 1 of 4)

## Contents
- [98 Threat Modeling](#98)
- [99 SAST](#99)
- [100 DAST](#100)
- [101 SCA](#101)

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
