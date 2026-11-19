# Repository and engineering operating model: stage reference

## Contents
- [45 Repository Setup](#45)
- [46 Branching Strategy](#46)
- [47 Development Environment](#47)
- [48 Coding Standards](#48)
- [49 Environment Configuration](#49)
- [50 Secrets Management](#50)
- [51 Developer Documentation](#51)
- [52 Engineering Governance](#52)

## 45
**Repository Setup** (complete). Purpose: create a repository that is ready for a team to work in safely from the first commit.

Entry criteria: A project is approved and named; A version control platform is available; Team members and owners are known

Inputs: project name and owners; organization policies; language and tooling choices; licence decision

Procedure:
1. Create the repository with a clear name and description under the right organization.
2. Add the basic files: README with build and run steps, licence, contributing guide, code owners and an ignore file.
3. Protect the main branch: require review and passing checks, and block force pushes.
4. Set up CI to run build and tests on every pull request from the first commit.
5. Turn on secret scanning and dependency alerts, and do not commit credentials or generated files.
6. Grant access by team with least privilege and record who owns the repository.

Deliverables: repository with starter files; branch protection settings; CI workflow; access list

Acceptance: The README lets a newcomer build and run the project Main branch is protected CI runs on pull requests Secret scanning is enabled

Validation: Platform engineer and repository owner.

- `git clone <repo-url> /tmp/fresh && cd /tmp/fresh && ls README.md LICENSE CODEOWNERS   # example` expect: files exist
- `gh api repos/<org>/<repo>/branches/main/protection --jq .required_pull_request_reviews   # example` expect: review requirement is returned

Failure modes:
- Direct pushes to main | detect: Commits with no review | respond: Enable branch protection
- Secret committed | detect: Scanner alert | respond: Revoke, rotate and clean history per policy
- README out of date | detect: New joiner cannot build | respond: Fix and test the steps on a clean machine

ILLUSTRATIVE: A new service repository is created with README, licence and code owners; the main branch requires one review and a passing CI run, and a fresh clone builds with the documented commands.

Gate: 05-045. Approval: none required

## 46
**Branching Strategy** (complete). Purpose: agree how work moves through version control, so merging is predictable and releases can be built from a known state.

Entry criteria: The team size and release pattern are known; Repository protection exists (stage 45); CI is available

Inputs: release cadence; team size and structure; CI capabilities; hotfix needs

Procedure:
1. Choose a model that fits the release pattern, such as trunk-based with short-lived branches, or release branches when several versions are supported.
2. Define branch names, how long they may live, and how often they must be synchronized with the main branch.
3. Define how changes are merged: squash or merge commit, review and checks required.
4. Define how hotfixes are made and carried back into the main branch.
5. Define tagging and version numbering for releases.
6. Write the rules in the contributing guide and enforce what you can with branch rules and checks.

Deliverables: branching model; naming and merge rules; hotfix and tagging process; enforced settings

Acceptance: The model matches the release pattern Branch life limits are stated Hotfix path returns changes to main Rules are enforced by settings where possible

Validation: Engineering lead approval.

- `git for-each-ref --sort=committerdate refs/remotes --format='%(committerdate:short) %(refname:short)' | head -20` expect: no branch older than the stated life limit without a reason
- manual: follow the documented hotfix steps on a test repository expect: fix reaches main and the release branch

Failure modes:
- Long-lived branches | detect: Large painful merges | respond: Merge small and often
- Hotfix not merged back | detect: Bug reappears in next release | respond: Add the back-merge step to the checklist
- Rules only in a document | detect: People forget them | respond: Enforce in settings

ILLUSTRATIVE: A team of eight chooses short-lived branches off main, squash merges after one review and green checks, and tags releases. Branches older than five days are flagged weekly.

Gate: 05-046. Approval: none required

## 47
**Development Environment** (complete). Purpose: give every developer a quick, repeatable way to build, run and test the system locally, matching production closely enough to trust the results.

Entry criteria: The repository and its dependencies are known; A container or provisioning tool is chosen; Sample or synthetic data exists

Inputs: repository; dependency list; production configuration differences; sample data

Procedure:
1. Define the toolchain versions in a file that tools read, so everyone uses the same versions.
2. Provide a single command or short script to set up dependencies and start the system with its services.
3. Use synthetic or masked data, never raw production data or real credentials.
4. Keep configuration in environment files with an example file in the repository and secrets outside it.
5. Document the differences from production that matter and how to test them elsewhere.
6. Test the setup on a clean machine or container and record the time it takes.

Deliverables: toolchain version file; setup and start script; example configuration; documented differences from production

Acceptance: A newcomer is running within the stated time No real secrets or production data are used Versions are pinned Differences from production are listed

Validation: Platform engineer review.

- `docker compose up -d && docker compose ps   # example; use the project's start command` expect: all services healthy
- `grep -rniE 'AKIA|BEGIN PRIVATE KEY|password=' . --exclude-dir=.git | head` expect: no real secrets found

Failure modes:
- Works on one machine only | detect: Setup fails elsewhere | respond: Pin versions and test on a clean machine
- Production data in local copy | detect: Real records found | respond: Replace with synthetic data
- Setup steps drift | detect: Docs and script disagree | respond: Make the script the source and test it in CI

ILLUSTRATIVE: A single make target starts the app, database and queue in containers with pinned versions and synthetic data, and a clean laptop is ready in twelve minutes.

Gate: 05-047. Approval: none required

## 48
**Coding Standards** (complete). Purpose: agree the small set of code rules the team follows, and make tools enforce them so reviews can focus on design.

Entry criteria: Languages in use are known; A formatter and linter exist for them; CI is available

Inputs: languages and frameworks; existing code style; common review comments; security guidance

Procedure:
1. Start from the common standard for each language and write down only the departures and the rules that tools cannot check.
2. Choose an automatic formatter, so style is never discussed in review.
3. Choose lint rules that catch real defects, and set each as error or warning on purpose.
4. Cover naming, error handling, logging, secret handling and dependency use in short rules with examples.
5. Run the tools locally before commit and in CI, and block merges on errors.
6. Review the rules each quarter, using the review comments that keep recurring.

Deliverables: coding standard document; formatter and linter configuration; CI check; rule review notes

Acceptance: Style is enforced by the formatter Each lint rule has a stated severity Security-related rules are included CI blocks on errors

Validation: Engineering governance owner approval.

- `ruff check . && ruff format --check .   # example; use the language's tools` expect: no errors, formatting is clean
- manual: sample ten recent review comments and check they are not about style the formatter handles expect: none

Failure modes:
- Rules nobody follows | detect: Many suppressions | respond: Remove or fix noisy rules
- Style debated in review | detect: Comments about formatting | respond: Enable the formatter
- Suppressions added to pass CI | detect: Ignore comments grow | respond: Require a reason and review them

ILLUSTRATIVE: A team adopts the standard formatter, enables lint rules for unused variables and unsafe calls as errors, and adds a short rule that errors must never be swallowed silently.

Gate: 05-048. Approval: none required

## 49
**Environment Configuration** (complete). Purpose: define, store and apply configuration for each environment in a controlled, auditable way, with secrets kept apart and drift detected.

Entry criteria: Environments are defined; A secrets store exists; Deployments run from a pipeline

Inputs: application configuration needs; environment list; secrets inventory; deployment pipeline

Procedure:
1. Separate configuration from code, following the twelve-factor approach: the same build artifact runs in every environment with different configuration.
2. Store non-secret configuration in version control as code with per-environment overrides, and review changes like code.
3. Keep secrets in a secrets manager, inject them at runtime, never commit them, and rotate them on a schedule and on exposure.
4. Validate configuration at startup against a schema, and fail fast with a clear message for missing or invalid values.
5. Detect drift between the declared and running configuration, and alert on manual changes.
6. Document each setting with its purpose, default and owner, and keep production and non-production parity except for the documented differences.

Deliverables: configuration repository with overrides; secrets management setup; configuration schema and startup validation; drift reports

Acceptance: The same artifact is used across environments No secrets in the repository Invalid configuration fails at startup Drift is detected

Validation: DevOps engineer review.

- `git log -p --all -S'AKIA' -- . | head   # example; also run the secret scanner configured for the repository` expect: no secrets found in history
- manual: start the application with a required setting removed expect: fails immediately with a clear message

Failure modes:
- Secret in the repository | detect: Scanner alert | respond: Revoke, rotate and remove
- Different artifact per environment | detect: Works in test, fails in production | respond: Build once and configure at deploy
- Manual change on a server | detect: Drift report | respond: Revert and fix through code

ILLUSTRATIVE: One container image is deployed to staging and production with different configuration files from the repository; secrets come from the secrets manager, and a missing database URL stops startup with a clear error.

Gate: 05-049. Approval: none required

## 50
**Secrets Management** (complete). Purpose: keep credentials out of source and logs, and make every secret rotatable and owned.

Entry criteria: Inventory of secret types and stores exists or will be created in this stage; Secret manager or vault is available to the team; Named secrets-owner exists

Inputs: repository history and current tree; secret scanner configuration; secret manager inventory; rotation policy

Procedure:
1. Scan the working tree and full history for credentials; record findings without printing secret values.
2. Treat every found credential as compromised: revoke and rotate it before removing it from code.
3. Move runtime secrets to the secret manager; reference them by name, never by value, in config and CI.
4. Add a pre-commit and CI secret scan that fails the build on new findings.
5. Record owner, rotation interval and consumers for each secret.
6. Get the secrets-owner's approval of the inventory and the rotation plan.

Deliverables: secret inventory (names, owners, rotation dates; no values); scan reports; rotation log; CI secret-scan configuration

Acceptance: Scan of history and tree reports zero active secrets or each is rotated CI blocks new secrets Every secret has an owner and a rotation date No secret value appears in the evidence

Validation: Secrets-owner approval, plus a rerun of the scanner on a clean clone.

- `gitleaks detect --source . --redact --report-path reports/secrets.json   # example` expect: exit 0; zero findings or all findings marked rotated
- `git clone --quiet . /tmp/clean && gitleaks detect --source /tmp/clean --redact` expect: exit 0 on the clean clone

Failure modes:
- Credential removed but not rotated | detect: Rotation log has no entry for a found secret | respond: Rotate now; treat as BLOCKED until logged
- Secret value pasted into the report | detect: Report contains an unredacted value | respond: Delete the report, rotate the secret, rerun with redaction
- Scanner not enforced in CI | detect: A test commit with a fake secret passes CI | respond: Fix pipeline configuration before approval

ILLUSTRATIVE: History scan finds a cloud access key committed two years ago. The key is revoked first, a new key is stored in the secret manager, CI is updated to read it by name, and the scanner is added to the pipeline.

Gate: 05-050. Approval: secrets-owner (when rotating or revoking production secrets)

## 51
**Developer Documentation** (complete). Purpose: provide the documentation developers need to understand, build, run, change and operate the system, and keep it correct as the code changes.

Entry criteria: The system and its repositories exist; Common developer questions are known; A docs location under version control exists

Inputs: codebase and architecture; onboarding feedback; frequently asked questions; runbooks

Procedure:
1. Start from the tasks developers perform: set up, run tests, make a change, debug, release and handle an incident, and write a page for each.
2. Make every command copy-pasteable and test them on a clean environment, recording the versions assumed.
3. Generate reference documentation from the code (API specs, configuration tables) so it cannot drift, and write by hand only the explanations.
4. Keep docs in the repository and change them in the same pull request as the code, with a review checklist item.
5. Check the docs in CI with link checks, command checks and spelling, and give each page an owner and a review date.
6. Measure usefulness through onboarding time and questions asked in chat, and fix the pages behind repeated questions.

Deliverables: task-based developer guide; generated reference documentation; CI documentation checks; page owners and review dates

Acceptance: Commands were run on a clean environment Reference docs are generated from code Docs change in the same pull request as behavior Each page has an owner and review date

Validation: Documentation engineer review.

- `python3 scripts/check_links.py` expect: no broken links
- manual: a new developer follows the setup guide on a clean machine and notes the first failure expect: setup completes, or the failure is fixed in the guide

Failure modes:
- Setup steps fail | detect: New developer is blocked | respond: Fix and test on a clean machine
- Reference docs written by hand | detect: Out of date with code | respond: Generate from source
- Docs without owners | detect: Pages go stale | respond: Assign owners and review dates

ILLUSTRATIVE: The setup guide is followed on a clean laptop and fails at a missing environment variable. The guide is corrected, the API reference is generated from the OpenAPI file, and a CI check blocks broken links.

Gate: 05-051. Approval: none required

## 52
**Engineering Governance** (complete). Purpose: set the lightweight rules, roles and records that let many teams build quickly while staying within policy.

Entry criteria: Engineering policies exist or are being written; Teams and their owners are known; A forum for decisions exists

Inputs: policies and standards; team structure; audit and compliance needs; incident and review findings

Procedure:
1. List the few things that must be the same everywhere, such as access control, approvals, security checks and records, and leave the rest to teams.
2. Turn each rule into a check in the tools where possible, so compliance does not rely on memory.
3. Name an owner and a decision forum for each policy, and a way to request exceptions.
4. Record exceptions with reason, owner and expiry date.
5. Report compliance as measured results, such as the share of repositories meeting the checks.
6. Review rules regularly and retire those that no longer prevent a real problem.

Deliverables: policy list with owners; automated checks; exception register with expiry; compliance report

Acceptance: Each policy has an owner and a forum Rules are enforced by checks where possible Exceptions have an expiry date Compliance is reported from data

Validation: Engineering leadership approval.

- manual: list exceptions past their expiry date expect: none, or each has a renewal decision
- manual: compare reported compliance with a direct sample of five repositories expect: numbers match

Failure modes:
- Policies nobody checks | detect: No evidence of compliance | respond: Automate the check
- Exceptions never expire | detect: Register grows | respond: Add expiry and review
- Too many rules | detect: Teams route around them | respond: Remove rules that prevent no real problem

ILLUSTRATIVE: Four rules are enforced by automation across all repositories: protected main, required review, secret scanning and dependency alerts. Two repositories have exceptions that expire in 60 days.

Gate: 05-052. Approval: none required
