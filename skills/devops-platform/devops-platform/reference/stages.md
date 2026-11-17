# Secure delivery platform: stage reference

## Contents
- [111 CI Pipeline](#111)
- [112 Automated Test Pipeline](#112)
- [113 Build Management](#113)
- [114 Artifact Management](#114)
- [115 Containerization](#115)
- [116 Container Orchestration](#116)
- [117 Infrastructure as Code](#117)
- [118 Configuration Management](#118)
- [119 CD Pipeline](#119)
- [120 Environment Provisioning](#120)
- [121 Network Engineering](#121)
- [122 Database Operations](#122)
- [123 CDN & Edge Configuration](#123)
- [124 Deployment Automation](#124)
- [125 Pipeline Security](#125)

## 111
**CI Pipeline** (complete). Purpose: turn each commit into a repeatable, trusted build-and-check result that gates merging.

Entry criteria: Repository builds from a clean checkout with documented commands; CI runner and secrets store are available; Required checks are agreed (build, tests, lint, security scans)

Inputs: repository and build instructions; required-check list; runner and cache configuration; secret store references

Procedure:
1. Define the pipeline as code in the repository; pin tool and action versions.
2. Run build, unit tests, lint and security scans on every pull request, with least-privilege tokens.
3. Cache dependencies by lockfile hash; never cache secrets.
4. Publish build artifacts with the commit id and a checksum.
5. Protect the default branch: required checks must pass before merge.
6. Measure duration and flake rate; investigate regressions.

Deliverables: pipeline definition; run history; artifact with checksum; branch protection settings

Acceptance: Pipeline runs on every pull request and on the default branch Required checks block merge Actions and tools are pinned Failed runs show the failing step and logs

Validation: A deliberately failing change is blocked from merging.

- `gh run list --limit 5 --json conclusion,headSha` expect: latest run on the default branch concluded success for the current head
- `gh api repos/{owner}/{repo}/branches/main/protection --jq .required_status_checks.contexts` expect: lists every required check

Failure modes:
- Checks are advisory only | detect: A failing PR can still be merged | respond: Enable required status checks
- Unpinned actions or tools | detect: Workflow uses moving tags | respond: Pin to versions or digests
- Secrets exposed to forked PRs | detect: Workflow runs with secrets on fork events | respond: Restrict secrets to trusted events

ILLUSTRATIVE: A new service gets a workflow that builds, tests and scans on each pull request. A test PR with a failing unit test is blocked from merging until fixed.

Gate: 10-111. Approval: none required

## 112
**Automated Test Pipeline** (complete). Purpose: run the right automated tests on every change in a pipeline that is fast, reliable and trusted.

Entry criteria: Test suites exist at unit, integration and end-to-end levels; CI pipeline exists (stage 111); Test environments or containers can be created on demand

Inputs: test suites and their runtimes; CI configuration; environment definitions; flake history

Procedure:
1. Order the stages so cheap, fast tests run first and fail early; run slow suites only when relevant paths change.
2. Run independent suites in parallel with isolated data and environments.
3. Publish test reports and logs as artifacts, with failing test names in the summary.
4. Track flaky tests with owner and expiry; quarantine rather than retry-until-green.
5. Set a time budget for the pipeline and alert when it is exceeded.
6. Make the test stage a required check on the default branch.

Deliverables: pipeline definition with test stages; test reports; flaky-test register; duration and pass-rate trend

Acceptance: Required checks block merging Failures show which test failed and why Flaky tests have owners and expiry dates Pipeline duration is within the agreed budget

Validation: Platform and security review plus a clean pipeline run from scratch.

- `gh run list --workflow=ci.yml --limit 10 --json conclusion,createdAt,updatedAt   # example` expect: recent runs succeed; durations within budget
- manual: open a pull request with a deliberately failing test expect: merge is blocked and the report names the test

Failure modes:
- Retrying hides flakes | detect: Pass after rerun with no investigation | respond: Quarantine with owner; fix root cause
- Tests share data | detect: Parallel run fails, serial passes | respond: Isolate data per test
- Pipeline too slow | detect: Duration above budget | respond: Split suites, cache dependencies, run slow tests on a schedule

ILLUSTRATIVE: Unit tests finish in two minutes and gate integration tests, which run in four parallel jobs. Two flaky end-to-end tests are quarantined with owners and a one-month expiry.

Gate: 10-112. Approval: none required

## 113
**Build Management** (complete). Purpose: turn source into a deterministic, reproducible build that anyone can rerun and get the same result.

Entry criteria: Source is in version control with a lockfile; Build instructions are documented; A clean build environment is available

Inputs: source at a commit; lockfiles and build configuration; build toolchain versions; build environment definition

Procedure:
1. Pin the toolchain and dependency versions and build in a clean, defined environment.
2. Build with a single documented command that needs no manual steps or local state.
3. Stamp the build with the commit id and build number, and avoid embedding timestamps that change the output.
4. Build twice and compare outputs (checksums) to check reproducibility; investigate differences.
5. Keep build logs and fail on warnings the team treats as errors.
6. Hand the output to artifact management (stage 114) with its checksum.

Deliverables: build output; build log; checksum and build metadata; reproducibility comparison

Acceptance: Build runs from a clean checkout with one command Two builds of the same commit produce identical checksums or differences are explained Toolchain and dependencies are pinned Output carries commit id

Validation: Rebuild in CI on a clean runner.

- `make build && sha256sum dist/app.tar.gz > /tmp/a.sum && make clean && make build && sha256sum -c /tmp/a.sum   # example` expect: checksum verification OK
- manual: read the build log for steps that pull unpinned inputs expect: none found

Failure modes:
- Build works only on one machine | detect: CI build fails on a clean runner | respond: Move local state into declared inputs
- Unpinned dependency changes output | detect: Checksums differ between builds | respond: Pin and lock
- Timestamps in output | detect: Two builds differ only by time | respond: Normalize or strip

ILLUSTRATIVE: Two builds of commit a1b2c3 on clean runners produce the same archive checksum after the team sets a fixed file ordering and strips the build-time field.

Gate: 10-113. Approval: none required

## 114
**Artifact Management** (complete). Purpose: store built artifacts immutably with their provenance so that what is tested is exactly what is deployed.

Entry criteria: Build produces a versioned artifact with a checksum; An artifact repository or registry is available; Retention policy is defined

Inputs: built artifact and checksum; build metadata (commit, builder); artifact repository; retention policy

Procedure:
1. Publish each artifact once under an immutable version tied to the commit; forbid overwriting.
2. Record provenance: source commit, build run, builder, dependencies (SBOM) and checksum.
3. Restrict write access to the pipeline; give consumers read-only access.
4. Promote the same artifact through environments by reference to its digest, never by rebuilding.
5. Apply retention rules: keep released artifacts, expire snapshots, and never delete what production runs.
6. Scan and sign artifacts where supported, and verify the signature before deployment.

Deliverables: published artifact with immutable version; provenance record; access and retention configuration; signature or digest record

Acceptance: An existing version cannot be overwritten Provenance links the artifact to its commit and build Only the pipeline can publish Deployment verifies the digest

Validation: Platform review of access and retention settings.

- `docker manifest inspect registry.example.com/app:1.4.0 | sha256sum   # example` expect: digest equals the one in the provenance record
- manual: try to republish an existing version expect: the repository refuses

Failure modes:
- Tag overwritten | detect: Same tag points to a different digest | respond: Enforce immutability and deploy by digest
- Artifact without provenance | detect: No commit or build link | respond: Rebuild through the pipeline
- Humans can publish | detect: Non-pipeline account has write access | respond: Remove it

ILLUSTRATIVE: The pipeline publishes app 1.4.0 with its digest, commit and SBOM. A later attempt to push another image under 1.4.0 is rejected, and staging and production both deploy the same digest.

Gate: 10-114. Approval: none required

## 115
**Containerization** (complete). Purpose: package the application and its runtime into a small, secure, reproducible container image.

Entry criteria: Application builds and runs outside a container; Runtime requirements are known; Base image policy exists

Inputs: application build output; runtime requirements; approved base images; container security policy

Procedure:
1. Write a Dockerfile with a pinned, minimal base image and a multi-stage build so build tools do not ship.
2. Run as a non-root user, copy only what the application needs, and keep secrets out of layers and build arguments.
3. Define the entrypoint, health check, exposed ports and resource expectations.
4. Build the image in CI, tag it by commit, and record its digest.
5. Run the container locally or in CI and verify it starts, passes the health check and shuts down cleanly on a termination signal.
6. Hand the digest to container security scanning (stage 102).

Deliverables: Dockerfile; built image digest; container run verification; image size and layer notes

Acceptance: Image runs as non-root No secrets in layers or build arguments Container starts, is healthy and stops cleanly Base image and tools are pinned

Validation: Platform and security review of the Dockerfile.

- `docker build -t app:test . && docker run --rm -d --name t app:test && sleep 5 && docker inspect --format '{{.State.Health.Status}}' t` expect: healthy
- `docker history --no-trunc app:test | grep -iE 'password|secret|token'` expect: no matches

Failure modes:
- Build tools shipped in the final image | detect: Large image with compilers | respond: Use multi-stage builds
- Container ignores termination | detect: Takes the kill timeout to stop | respond: Handle the signal; run the process as PID 1 correctly
- Secret passed as a build argument | detect: Appears in history | respond: Use build secrets and rotate it

ILLUSTRATIVE: A two-stage Dockerfile compiles in a builder image and copies only the binary into a minimal base running as user 10001. The container reports healthy within five seconds and stops on SIGTERM in under a second.

Gate: 10-115. Approval: none required

## 116
**Container Orchestration** (complete). Purpose: run containers reliably at scale with scheduling, networking, configuration and safe updates managed by the platform.

Entry criteria: Container images and their requirements are known; A cluster exists with defined environments; Platform standards for namespaces, quotas and policies exist

Inputs: container images and digests; resource and scaling requirements; cluster standards and policies; configuration and secret sources

Procedure:
1. Define workloads declaratively with resource requests and limits, health probes and a rolling update strategy.
2. Separate configuration and secrets from images; mount secrets from the secret store, never in manifests.
3. Apply network policies, a non-root security context and pod security standards.
4. Set disruption budgets and spread replicas across failure domains.
5. Deploy through the pipeline from version control (no manual kubectl in production) and verify rollout status.
6. Observe and tune: resource use, restarts, scheduling failures.

Deliverables: workload manifests or charts; policy and security context settings; rollout verification; observability dashboards

Acceptance: Every workload has resource limits and probes Security context and network policies are applied Replicas are spread across failure domains Changes arrive through version control

Validation: Platform review of manifests.

- `kubectl apply --dry-run=server -f k8s/ && kubectl rollout status deployment/app` expect: applies cleanly and rolls out
- `kubectl get pods -o jsonpath='{range .items[*]}{.metadata.name}{" "}{.spec.containers[*].resources.limits}{"\n"}{end}'` expect: every pod has limits

Failure modes:
- No resource limits | detect: Pod can exhaust a node | respond: Set requests and limits
- Probes missing or wrong | detect: Traffic reaches an unready pod | respond: Add readiness and liveness probes
- Manual edits in production | detect: Cluster differs from version control | respond: Reconcile from the repository

ILLUSTRATIVE: The service runs three replicas spread across zones with readiness probes, a pod disruption budget of one, and a rolling update that never takes more than one pod down at a time.

Gate: 10-116. Approval: none required

## 117
**Infrastructure as Code** (complete). Purpose: describe infrastructure as reviewed, versioned code so environments are reproducible and drift is visible.

Entry criteria: Target environments and ownership are defined; State storage and locking are decided; Infra-owner is named

Inputs: environment requirements; current infrastructure inventory; IaC tooling and module standards; state backend configuration

Procedure:
1. Model resources in code with parameters per environment; keep secrets out of code.
2. Run format, validate and policy checks in CI.
3. Produce a plan against the target environment and review the diff, especially deletions and replacements.
4. Apply through the pipeline with the infra-owner's approval for production.
5. Detect drift on a schedule and reconcile by code, not by hand.
6. Record rollback: previous version of the code and state backup.

Deliverables: IaC modules and environment configs; plan output; policy check results; drift report

Acceptance: Plan shows only expected changes Policy checks pass State is remote, locked and backed up Production apply has infra-owner approval

Validation: Infra-owner review of the plan before production apply.

- `terraform fmt -check -recursive && terraform validate   # example; use the project's IaC tool` expect: exit 0
- `terraform plan -detailed-exitcode -out=plan.out` expect: exit 2 means changes pending; review diff; exit 0 means no drift

Failure modes:
- Plan includes unexpected destroys | detect: Plan lists replacements of stateful resources | respond: Stop; review before any apply
- Manual change in console | detect: Drift report shows differences | respond: Reconcile in code; document who changed what
- Secrets in state or code | detect: Scanner finds values | respond: Rotate and move to the secret manager

ILLUSTRATIVE: Adding a database replica changes one module. The plan shows one resource created and none destroyed; the infra-owner approves and drift check afterwards is clean.

Gate: 10-117. Approval: infra-owner (before applying a plan to production; always when the plan destroys resources or changes IAM)

## 118
**Configuration Management** (complete). Purpose: keep configuration controlled, versioned and consistent across environments so behavior is predictable.

Entry criteria: Configuration items and environments are listed; A source of truth for configuration is chosen; Secrets handling exists (stage 50)

Inputs: configuration inventory; environment definitions; change process; secrets store

Procedure:
1. Keep configuration in version control, separate from code where it varies by environment, and separate from secrets.
2. Define defaults once and override per environment with a small, visible difference.
3. Validate configuration against a schema at build or startup and fail fast on invalid values.
4. Roll configuration changes out through the same review and pipeline as code, with a rollback.
5. Detect drift between the declared and the running configuration and reconcile from the source.
6. Record who changed what and when.

Deliverables: configuration repository or files; schema validation; environment difference report; change history

Acceptance: Configuration changes are reviewed and versioned Invalid configuration fails before taking traffic Secrets are not stored with configuration Drift is detected

Validation: Platform owner review.

- `python3 -c "import json,jsonschema;jsonschema.validate(json.load(open('config/prod.json')),json.load(open('config/schema.json')))"   # example` expect: no exception
- `diff <(sort config/staging.env) <(sort config/prod.env)` expect: differences are only the expected environment values

Failure modes:
- Hotfix edit on the server | detect: Running config differs from the repository | respond: Reconcile from version control
- Secret in configuration file | detect: Scanner finds a value | respond: Move to the secret store and rotate
- Unvalidated value takes the service down | detect: Startup crash on bad config | respond: Add schema validation

ILLUSTRATIVE: A pull request changes the connection pool size for production only. Schema validation passes, the diff against staging shows that single line, and the change deploys through the pipeline.

Gate: 10-118. Approval: none required

## 119
**CD Pipeline** (complete). Purpose: deliver approved artifacts to environments through an automated, auditable and repeatable pipeline.

Entry criteria: Immutable artifacts exist (stage 114); Environments are defined as code; Approval points and deployment strategy are agreed

Inputs: artifact digest; environment definitions; deployment strategy and approvals; health checks

Procedure:
1. Model deployment as a pipeline from the artifact digest to each environment in order.
2. Use the same deployment steps in every environment; vary only configuration.
3. Run automated checks after each deployment (health, smoke) and stop on failure.
4. Require human approval before production in the pipeline, with the approver recorded.
5. Use short-lived credentials for deployment and keep them out of logs.
6. Record who deployed what, when and with what result.

Deliverables: deployment pipeline definition; run records with approvals; health and smoke results; deployment history

Acceptance: The same digest moves through all environments Production requires a recorded approval A failed check stops the pipeline Credentials are short-lived and not logged

Validation: Platform and change-authority review.

- `gh run view --json conclusion,jobs   # example for the deployment run` expect: all jobs succeeded; production job shows an approval
- manual: compare the digest deployed to production with the artifact record expect: identical

Failure modes:
- Different build per environment | detect: Digest differs between environments | respond: Promote one artifact
- Approval skipped | detect: Production run with no approver | respond: Make the approval mandatory in the pipeline
- Long-lived deploy key | detect: Static credential in the pipeline | respond: Replace with short-lived tokens

ILLUSTRATIVE: The pipeline deploys digest sha256:9f2c to staging, runs smoke checks, waits for the production approver, then deploys the same digest to production and records the approver and times.

Gate: 10-119. Approval: none required

## 120
**Environment Provisioning** (complete). Purpose: create environments from code so every environment is reproducible, isolated and safe to change.

Entry criteria: Environment purpose and ownership are defined; Infrastructure as code exists or is created in this stage (stage 117); Cloud account and access controls are in place

Inputs: environment requirements; IaC modules and configuration; network and access design; cost budget

Procedure:
1. Define the environment from code with per-environment parameters; no manual console changes.
2. Isolate environments by account or project, network and credentials; production credentials never exist in lower environments.
3. Provision through the pipeline and record the plan and the applied changes.
4. Seed non-production data with synthetic or properly masked data only.
5. Verify the environment with health checks and a baseline smoke test.
6. Tag every resource with owner, purpose and expiry; schedule teardown for temporary environments.

Deliverables: environment definition in code; plan and apply records; verification results; resource inventory with owners and expiry

Acceptance: The environment can be destroyed and recreated from code No production secrets or unmasked customer data exist in it Resources are tagged with owner and expiry Smoke checks pass

Validation: Platform and security review plus a clean pipeline run.

- `terraform plan -detailed-exitcode   # example; exit 0 means code matches reality` expect: exit 0 after apply
- manual: list resources without an owner tag expect: none

Failure modes:
- Environment drifts from code | detect: Plan shows differences after manual edits | respond: Reconcile in code and document the change
- Real customer data copied to test | detect: Data scan or review finds real records | respond: Delete, mask and report to the data owner
- Orphaned resources keep costing | detect: Resources past expiry | respond: Tear down or extend with a reason

ILLUSTRATIVE: A short-lived review environment is created for a pull request from code, receives synthetic data, passes smoke checks, and is destroyed automatically when the pull request closes.

Gate: 10-120. Approval: none required

## 121
**Network Engineering** (complete). Purpose: design and operate the network so services can reach each other as intended and nothing else, with changes controlled.

Entry criteria: Connectivity requirements between systems and users exist; Address plan and zones are defined; Network owner is named

Inputs: connectivity requirements; address plan and zones; security zones and policies; monitoring requirements

Procedure:
1. Define zones and the allowed flows between them; default is deny.
2. Plan address ranges so they do not overlap with partners or other environments.
3. Implement routing, firewalls and segmentation from code, with each rule tied to a requirement.
4. Test allowed flows and test that forbidden flows fail.
5. Monitor latency, loss and denied traffic, and review rules regularly for stale entries.
6. Control changes with review, a window and a rollback for production.

Deliverables: network design and address plan; rules as code with requirement references; flow test results; monitoring and review records

Acceptance: Default is deny and each rule references a requirement Allowed and forbidden flows were both tested Address ranges do not overlap Production changes had approval and rollback

Validation: Infrastructure owner approval.

- `nc -zv db.internal 5432   # example from the app zone` expect: connection succeeds
- `nc -zv db.internal 5432   # example from an unrelated zone` expect: connection refused or times out

Failure modes:
- Overly broad rule | detect: 0.0.0.0/0 on an internal port | respond: Narrow to the required source
- Overlapping address ranges | detect: Routing conflicts after peering | respond: Re-plan addresses
- Rules never reviewed | detect: Rules without requirement links | respond: Review and remove

ILLUSTRATIVE: The database zone accepts connections only from the application zone on one port. A test from the application zone connects; the same test from the build zone is refused.

Gate: 10-121. Approval: infra-owner (for production firewall, security-group or routing changes)

## 122
**Database Operations** (complete). Purpose: run the production databases so they stay available, correct, performant and recoverable, with changes made safely.

Entry criteria: Databases and their owners are inventoried; Backup and monitoring tools exist; Recovery objectives are defined

Inputs: database inventory; recovery objectives (RPO, RTO); monitoring and slow query data; change calendar

Procedure:
1. Monitor availability, replication lag, connection use, disk growth, lock waits and slow queries, and alert on thresholds with runbook links.
2. Verify backups by restoring them into a test instance on a schedule and checking data and application connectivity; an untested backup is not a backup.
3. Tune with evidence: review the slowest and most frequent queries, check query plans, and add or remove indexes by measured effect.
4. Apply patches and schema changes through the change process, using online and backward-compatible migrations (expand then contract).
5. Manage access: named accounts, least privilege, rotated credentials and audited administrative access.
6. Rehearse failover and point-in-time recovery, record the actual recovery time and data loss against the objectives.

Deliverables: monitoring and alert configuration; restore test records; tuning changes with before and after plans; failover rehearsal results

Acceptance: Restores are tested on a schedule Measured recovery meets RPO and RTO or the gap is recorded Schema changes are backward compatible Administrative access is named and audited

Validation: Database administrator and service owner review.

- `pg_restore --list backup.dump | head   # example; then restore into a scratch instance and run row-count checks` expect: restore completes and counts match the source
- `psql -c "select now()-pg_last_xact_replay_timestamp() as lag"   # example on a replica` expect: lag within the alert threshold

Failure modes:
- Backup never restored | detect: First restore attempt fails during an incident | respond: Schedule restore tests
- Migration locks a hot table | detect: Writes blocked | respond: Use online, batched migration
- Index added without measuring | detect: Writes slow, plan unchanged | respond: Verify with the plan and drop it

ILLUSTRATIVE: A monthly restore test brings the latest backup up in a scratch instance in 38 minutes against a 60-minute target, and row counts match; a column rename is done by adding the new column, backfilling in batches, switching reads, then dropping the old.

Gate: 10-122. Approval: none required

## 123
**CDN & Edge Configuration** (complete). Purpose: serve content quickly and safely from locations close to users, with caching rules that are correct and reversible.

Entry criteria: Traffic patterns and cacheable content are identified; Origin and domain setup exist; Purge and rollback process is known

Inputs: content types and traffic; origin configuration; cache and security requirements; domain and certificate setup

Procedure:
1. Classify content by cacheability: static assets, public pages, personalized or private responses.
2. Set cache keys, time-to-live values and headers per class; never cache private or personalized responses publicly.
3. Configure origin protection so users cannot bypass the edge and the origin accepts only edge traffic.
4. Enable TLS, security headers and rate limiting or web-application rules at the edge.
5. Test cache behavior with repeated requests and with varying headers; test purge and a rollback of the configuration.
6. Monitor hit rate, origin load and edge errors.

Deliverables: edge configuration as code; cache rules per content class; test results for caching and purge; monitoring dashboards

Acceptance: Private responses are never publicly cached The origin accepts only edge traffic Purge works within the target time Hit rate and origin load are monitored

Validation: Platform owner review.

- `curl -sI https://www.example.com/static/app.js | grep -iE 'cache-control|age|x-cache'   # example` expect: long cache lifetime and a cache hit on repeat
- `curl -sI -H 'Cookie: session=test' https://www.example.com/account | grep -i cache-control` expect: private or no-store

Failure modes:
- Personalized page cached publicly | detect: One user sees another's data | respond: Mark as private and purge now; treat as an incident
- Origin reachable directly | detect: Direct request bypasses the edge | respond: Restrict the origin to edge addresses
- Stale content after release | detect: Old assets served | respond: Use versioned asset names and purge

ILLUSTRATIVE: Static assets get a one-year lifetime with versioned names, the account page is no-store, and a test shows a cache hit on the second request for an asset and none for the account page.

Gate: 10-123. Approval: none required

## 124
**Deployment Automation** (complete). Purpose: automate the mechanics of releasing so deployments are fast, consistent and low-risk.

Entry criteria: Deployment procedure is written and has been done by hand successfully; Target environment is defined as code; Rollback approach exists

Inputs: manual deployment runbook; environment and configuration definitions; health checks and thresholds; rollback plan

Procedure:
1. Convert each manual step into a scripted, idempotent step with clear success and failure output.
2. Add pre-checks: the right artifact digest, healthy targets, free capacity, no active incident.
3. Use a progressive strategy (rolling, canary or blue-green) with automated health gates between stages.
4. Make rollback one automated action that restores the previous version and configuration.
5. Run the automation in staging repeatedly, including a forced failure, before using it in production.
6. Document how to run, stop and debug it.

Deliverables: deployment automation scripts or pipeline; pre-check and gate definitions; rollback automation; rehearsal results

Acceptance: Automation is idempotent and rerunnable Pre-checks block unsafe deployments Automated rollback was rehearsed A forced failure was handled correctly in staging

Validation: Release engineering review and rehearsal evidence.

- `./deploy.sh --env staging --digest sha256:<digest> && ./deploy.sh --env staging --digest sha256:<digest>   # example: run twice` expect: second run makes no change and succeeds
- manual: inject a failing health check in staging and run the deployment expect: deployment stops and rolls back

Failure modes:
- Not idempotent | detect: Second run fails or duplicates | respond: Make each step safe to repeat
- Rollback untested | detect: No rehearsal record | respond: Rehearse before production
- Pre-checks bypassed with a flag | detect: Flag used in production | respond: Remove the bypass or require approval

ILLUSTRATIVE: A canary deployment script sends five percent of traffic to the new version, checks error rate for ten minutes, then continues or rolls back automatically; a staging rehearsal with a failing check shows the rollback working.

Gate: 10-124. Approval: none required

## 125
**Pipeline Security** (complete). Purpose: protect the pipeline itself, since whoever controls it controls what reaches production.

Entry criteria: Pipeline definitions are in version control; Secrets and permissions used by the pipeline are listed; Required checks are known

Inputs: pipeline definitions; pipeline secrets and permissions; runner configuration; branch protection and required checks

Procedure:
1. Give each pipeline job the least privilege it needs; use short-lived credentials from the identity provider instead of stored keys.
2. Pin third-party actions and tools to a version or digest and review changes to them.
3. Protect pipeline files: changes need review, and untrusted code from forks cannot access secrets.
4. Isolate runners; do not run untrusted builds on runners that can reach production.
5. Log pipeline runs and alert on unusual changes to pipeline definitions or permissions.
6. Test the controls by trying to bypass them in a safe repository.

Deliverables: pipeline permission matrix; pinned dependency list; runner isolation notes; bypass test results

Acceptance: No long-lived production credential is stored in the pipeline Third-party steps are pinned Fork builds cannot read secrets Pipeline changes require review

Validation: Security review of pipeline configuration and bypass tests.

- `grep -rnE 'uses: .+@(main|master|latest|v[0-9]+)$' .github/workflows` expect: no moving references, or each justified
- manual: open a pull request from a fork that tries to print a secret expect: secret is not available

Failure modes:
- Pipeline can deploy anywhere | detect: Single admin credential | respond: Split permissions by environment
- Moving tags for third-party steps | detect: Workflow uses a branch reference | respond: Pin to a digest or version
- Secrets exposed to forks | detect: Fork run can read secrets | respond: Restrict to trusted events

ILLUSTRATIVE: A review replaces a stored cloud key with short-lived federation, pins five third-party actions to versions, and confirms that a fork pull request cannot read secrets.

Gate: 10-125. Approval: none required
