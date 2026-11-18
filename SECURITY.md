# Security Policy

This repository contains documentation, JSON registries, templates and Python scripts that build and check them. It is not a
running service and holds no customer data. Security problems here are mostly about what the content could cause an agent or a
person to do, or about the build and CI tooling.

## Supported versions

| Version | Supported |
|---|---|
| Latest release or `main` | Yes |
| Older releases | No. Update to the latest. |

The current repository version is in [`VERSION`](VERSION).

## Report a vulnerability privately

Do not open a public issue with details.

1. Open the repository's **Security** tab and choose **Report a vulnerability**, if that button is shown. It creates a private advisory visible only to the maintainers.
2. If the button is not shown, open a public issue titled `Security contact request` that contains **no details** (no description, no exploit, no credentials). A maintainer will arrange a private channel.

Please include, once a private channel exists: what you found, where (file and line, or workflow), how to reproduce it, and the impact you expect.
Never include credentials, tokens or personal data; redact them.

## What to expect

These are targets, not guarantees, for a project maintained by volunteers:

| Step | Target |
|---|---|
| Acknowledge the report | 7 days |
| First assessment (accepted, declined, need more detail) | 14 days |
| Fix or mitigation for confirmed issues | Depends on severity; you will be told the plan |

We credit reporters in the fix notes unless you ask us not to. We do not run a bounty programme.

## In scope

- **Skill and template content that could cause unsafe agent behavior:** instructions that bypass an approval gate, tell an agent to disclose or log secrets, run destructive commands without approval, treat untrusted text as instructions, or hide failed checks.
- **Prompt-injection paths:** generated or authored content that would pull untrusted text (issues, logs, web pages) into an agent's instructions.
- **Scripts in `scripts/`:** command injection, unsafe path handling, unsafe deserialization, writes outside the repository, unexpected network access.
- **CI and supply chain:** `.github/workflows/`, over-broad workflow permissions, unpinned or untrusted actions, dependency confusion in `requirements` or install steps.
- **Secrets:** a credential committed to the repository or its history.

## Out of scope

- Vulnerabilities in third-party tools, agents or models that use this library. Report them to their owners.
- Findings that need the reporter to already control the maintainer's account or machine.
- Missing features, and approval or risk-tier choices that are a matter of policy preference (open a normal issue or discussion).
- Automated scanner output with no demonstrated impact.
- Social engineering of maintainers, and denial of service by volume against GitHub itself.

## Your own security testing

Test only against copies of this repository on your own machine. Do not test against other people's systems using this library's content.
Active security testing of any system needs written authorization from its owner; see [docs/governance/APPROVAL_POLICY.md](docs/governance/APPROVAL_POLICY.md).

## What this policy does not claim

This repository has not been security-audited or certified, and nothing in it is a compliance or security certification.
Checks such as the credential heuristic in `scripts/validate.py` reduce risk but do not prove absence of secrets or flaws.
The security rules the content teaches are in [docs/security/SECURITY_MODEL.md](docs/security/SECURITY_MODEL.md).

## If you find a secret in the repository

Report it privately as above. The maintainers will rotate the credential first (removing it from history alone does not make it safe), then remove it and record the decision using the [decision log](docs/governance/DECISION_LOG_STANDARD.md).
