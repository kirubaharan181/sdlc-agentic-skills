# Application security engineering: stage reference (part 2 of 4)

## Contents
- [102 Container Security](#102)
- [103 Infrastructure Security](#103)
- [104 Penetration Testing](#104)
- [105 Authentication Security](#105)

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

- `ss -tlnp   # example; list listening ports on a host you own and compare with the approved list` expect: only intended ports are open
- `trivy config terraform/   # example baseline check` expect: no high findings outside the exception register

Failure modes:
- Scan of systems without authorization | detect: Target not in scope | respond: Stop; use only approved targets
- Fixed by console edit | detect: IaC differs from reality | respond: Fix in code
- Public storage bucket | detect: Anonymous access enabled | respond: Remove public access and review data exposure

ILLUSTRATIVE: A review finds a database port reachable from the internet and an administrative role with a wildcard permission. Both are fixed in infrastructure code and the rescan shows them closed.

Gate: 09-103. Approval: none required

## 104
**Penetration Testing** (complete). Purpose: attempt, within agreed scope and rules, to break into the system as an attacker would, and report what was achieved and how to fix it.

Entry criteria: Written authorization from the system owner exists; Scope, rules of engagement and test windows are agreed; A safe environment or a coordinated production window is arranged

Inputs: signed authorization and scope; architecture and threat model; test accounts; emergency contacts

Procedure:
1. Confirm the authorization, targets, excluded systems, time window and stop conditions in writing before any test traffic is sent.
2. Gather information within scope: exposed services, versions, endpoints and trust boundaries, then compare with the threat model.
3. Test for the highest-risk classes: broken access control, injection, authentication and session flaws, insecure deserialization, SSRF and misconfiguration, chaining findings where it shows real impact.
4. Use the minimum action needed to prove each issue, avoid damaging data or availability, and stop and report at once on a critical finding or an unexpected impact.
5. Record every finding with reproducible steps, evidence, affected asset, severity with the scoring method named, and a specific remediation.
6. Hold a readout with the owners, agree fix dates, retest every fix, and securely delete or hand over test data and access.

Deliverables: rules of engagement and authorization; findings report with reproduction steps; remediation plan with owners and dates; retest results

Acceptance: Testing stayed within written scope Each finding is reproducible with evidence Severity has a stated method Every fix was retested

Validation: System owner authorization before testing; named human approves scope and accepts residual risk.

- manual: compare the tester's source addresses and activity log with the authorized window and targets expect: all within scope
- manual: repeat each reported exploit step on the fixed build expect: no longer succeeds

Failure modes:
- Test outside scope | detect: Traffic to an excluded system | respond: Stop, notify the owner and record the incident
- Finding without steps | detect: Developer cannot reproduce | respond: Add steps and evidence
- Production impact | detect: Errors or slowdowns during testing | respond: Stop at the defined condition and call the contact

ILLUSTRATIVE: Within an authorized window the tester finds that changing an order id returns another customer's invoice; the report gives the request, the response excerpt with data masked, a high rating, and a fix to check ownership on the server, retested after release.

Gate: 09-104. Approval: security-lead (always)

## 105
**Authentication Security** (complete). Purpose: verify that sign-in, session and credential handling resist real attacks, using tests aimed at the weaknesses that attackers use.

Entry criteria: Authentication is implemented (stage 59); Test accounts and an isolated environment exist; The threat model covers sign-in

Inputs: authentication design and code; threat model; test accounts including privileged ones; session and token configuration

Procedure:
1. Test credential attacks: brute force and credential stuffing against rate limits and lockout, and check that responses do not reveal whether an account exists.
2. Inspect session handling: cookie flags (Secure, HttpOnly, SameSite), token lifetime, rotation after sign-in and privilege change, and invalidation at logout and password change.
3. Examine tokens: signature verification, rejected algorithm substitution, expiry enforcement and audience checks.
4. Test recovery and multi-factor flows for bypass, reuse of codes or links, and weak fallback channels.
5. Check password storage and policy: slow salted hashing, breach-list checks and no reversible storage.
6. Record findings by severity with reproduction steps, and add each as a regression test.

Deliverables: authentication test report; reproduction steps for each finding; regression tests; configuration findings

Acceptance: Rate limits and lockout were tested under attack-like load Tokens and cookies were inspected for each listed property Recovery and multi-factor bypass were attempted Each finding became a regression test

Validation: Application security engineer sign-off.

- `curl -sI https://test.example.com/login | grep -i set-cookie   # example` expect: cookie shows Secure, HttpOnly and SameSite
- manual: send an expired and a tampered token to a protected endpoint expect: both rejected with the same generic response

Failure modes:
- Token accepted after logout | detect: Old token still works | respond: Revoke server-side
- Account enumeration | detect: Different responses for unknown users | respond: Return one response and timing
- Recovery link reusable | detect: Second use succeeds | respond: Single use with short expiry

ILLUSTRATIVE: Testing finds that a password-reset token remains valid after use and that the 'unknown user' response is faster than 'wrong password'. Both are fixed, each with a regression test.

Gate: 09-105. Approval: none required
