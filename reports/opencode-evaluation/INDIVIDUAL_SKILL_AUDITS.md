# Individual Skill Audits

**Method:** Each skill's complete SKILL.md was read and assessed across five categories (instruction quality, practical usability, engineering quality, safety & security, OpenCode compatibility), each scored 0–10 with evidence. Execution results reference transcripts in `reports/opencode-evaluation/transcripts/`.

---

## 1. application-security

**Transcript:** `application-security_TEST-007.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Clear purpose (threat modeling, SAST/DAST, dependency scanning, remediation, sign-off), when to use / not to use, prerequisites (written authorization for active testing), inputs/outputs, procedure, decision rules (no authorization -> do not test), quality gates, troubleshooting. |
| Practical usability | 8 | Actionable threat-model steps; requires authorization + scanner tooling not present in eval, so partially usable. |
| Engineering quality | 8 | Prioritize by exploitability/impact/reachability; assign owner/SLA; retest fixes; residual risk recorded. |
| Safety & security | 10 | Explicitly forbids active testing without written authorization; routes risk acceptance to named human; makes no security certification claim. |
| OpenCode compatibility | 10 | Standard SKILL.md frontmatter; local references present; no unsupported features. |

---

## 2. business-product-management

**Transcript:** `business-product-management_TEST-010.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (business case: strategy, discovery, estimates, approval), boundaries (not detailed requirements or sprint planning), inputs/outputs. |
| Practical usability | 8 | Actionable business-case structure; estimates must be labelled illustrative. |
| Engineering quality | 7 | Estimates illustrative (no velocity data); approval is a recommendation not a decision. |
| Safety & security | 9 | Correctly defers detailed requirements to requirements-design and sprint planning to project-agile-management. |
| OpenCode compatibility | 10 | Standard format; local references present. |

---

## 3. cloud-hosting-operations

**Status:** BLOCKED — not executed (requires cloud account access, provider credentials, and a reachable cloud environment; none available in this read-only eval). No transcript created.

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Clear purpose (compute/storage/network/DR/cost), prerequisites (least-privilege cloud access, RPO/RTO), decision rules (destructive change needs human approval; backup never restored => schedule restore test), quality gates. |
| Practical usability | 5 | Cannot be meaningfully exercised without a cloud account; lists commands to run rather than acting. |
| Engineering quality | 8 | Restore-tested backups, owner tags, expiry monitoring, blast-radius checks. |
| Safety & security | 9 | Least-privilege access; destructive/production actions require human approval; no broader credentials. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 4. code-review-quality

**Transcript:** `code-review-quality_TEST-003.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (independent PR review), when to use/not use, prerequisites (independent reviewer), inputs/outputs, procedure, decision rules (author==reviewer => reject), quality gates, troubleshooting. |
| Practical usability | 8 | Requires diff + test/tool results; tooling not configured in eval so results recorded as missing rather than fabricated. |
| Engineering quality | 8 | Findings separated into blockers vs suggestions; reviewer independence enforced; citations by file/rule/reason. |
| Safety & security | 9 | Independent reviewer (not author); merge approval by named human; static-analysis false-positive/negative acknowledged. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 5. definition-of-done

**Transcript:** `definition-of-done_TEST-001.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (completion = accepted behavior with evidence), completion profiles (bug-fix/release/etc.), inputs/outputs, procedure, decision rules (no evidence => BLOCKED; open risk without owner => do not close), quality gates. |
| Practical usability | 9 | Reusable per-profile templates (templates/definition-of-done/*.md); clear when to use / not use. |
| Engineering quality | 8 | Per-criterion results (PASS/FAIL/WAIVED/BLOCKED); waivers need owner+expiry; merged profiles for multi-type tasks. |
| Safety & security | 9 | Refuses to close with unowned open risk; human closes the work; evidence authenticity delegated to evidence-quality-gates. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 6. devops-platform

**Status:** BLOCKED — not executed (requires CI/CD platform, secrets store, artifact registry, runner access; none available). No transcript created.

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (CI/CD, containers, IaC, environments), decision rules (long-lived credential => short-lived federated; untrusted PR => separate trust levels; prod deploy => release-deployment approval), quality gates (reproducible pinned builds, least privilege, scanned artifacts). |
| Practical usability | 5 | Cannot be exercised without a CI/CD platform and secrets store. |
| Engineering quality | 9 | Pinned/reproducible builds, artifact provenance, drift detection, immutable promotion. |
| Safety & security | 9 | Least-privilege pipelines; secrets denied to untrusted code; production deploy requires release-deployment approval. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 7. engineering-governance

**Transcript:** `engineering-governance_TEST-013.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (repo setup, branching, environments, secrets, coding standards), when to use/not use. |
| Practical usability | 7 | Honestly flagged gaps (no branching policy doc, no enforced lint config) rather than fabricating compliance. |
| Engineering quality | 7 | Versioning present (VERSION file, tags); branching policy and env/secrets config absent (by design for a skills library). |
| Safety & security | 9 | Read-only assessment; no secrets handled. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 8. enterprise-governance

**Status:** BLOCKED — not executed (requires a control framework/policy set, org evidence access, agreed audit scope; none available). No transcript created.

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (independent oversight, controls, audits, exceptions), decision rules (control cannot be measured => rewrite or drop; closed by statement only => reopen), quality gates (evidence from systems not descriptions). |
| Practical usability | 5 | Requires org control framework and evidence sources; not set up in eval. |
| Engineering quality | 9 | Distinguishes design vs operating effectiveness; risk-based sampling; exceptions with expiry. |
| Safety & security | 10 | Independent oversight (does not do audited work); risk acceptance by named human only; no compliance certification claim. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 9. evidence-quality-gates

**Transcript:** `evidence-quality-gates_TEST-002.md` — PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 10 | Very thorough: purpose (gate decision PASS/FAIL/BLOCKED/INCONCLUSIVE/NEEDS_HUMAN_APPROVAL/WAIVED), prerequisites (evidence-record.json template), inputs/outputs, procedure, detailed decision rules (no revision/timestamp => INCONCLUSIVE; examples never count), quality gates. |
| Practical usability | 9 | Clear decision rules and schema; correctly rejected a source file as evidence for "tests pass" (INCONCLUSIVE). |
| Engineering quality | 9 | Schema-driven evidence record; handles conflicts, missing evidence, stale links. |
| Safety & security | 10 | Rejects stale/incomplete/self-approved evidence; high-risk gates need independent confirmation. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 10. incident-command

**Transcript:** `incident-command_TEST-004.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (incident command, not the fix), severity classification, role assignments, cadence, timeline/decision log, recovery handover. |
| Practical usability | 8 | Requires on-call platform and stakeholders; simulated in eval (roles as placeholders). |
| Engineering quality | 8 | Timeline, hypotheses, decisions, action owners; escalation rules; rollback-consider-first rule. |
| Safety & security | 9 | Does not perform the technical fix; does not page without a system; emergency changes route through human approval. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 11. master-orchestration

**Transcript:** `master-orchestration_TEST-005.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (routing, not doing), when to use/not use, procedure (classify, select workflow, delegate, enforce gates), decision rules, handoffs. |
| Practical usability | 9 | Clear entry point for multi-skill work; resolved skills in dependency order; matched the skill's own worked example. |
| Engineering quality | 8 | Separation of routing vs specialist work; NEEDS_HUMAN_APPROVAL gating; conflict escalation. |
| Safety & security | 9 | Does not approve/deploy/override; named humans approve production steps. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 12. maintenance-support

**Transcript:** `maintenance-support_TEST-016.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (support tiers, fixes, patches, lifecycle), tier classification, triage, fix path. |
| Practical usability | 8 | Actionable support handling; coordinates fix path via other skills. |
| Engineering quality | 7 | Root-cause hypothesis + fix path; no self-implementation (correct boundary). |
| Safety & security | 9 | Does not build new products; does not implement fixes itself. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 13. project-agile-management

**Transcript:** `project-agile-management_TEST-014.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (scope, estimate, track, govern delivery and risk), when to use/not use. |
| Practical usability | 8 | Actionable iteration plan with risks and mitigations. |
| Engineering quality | 7 | Estimates illustrative; no live tracking board. |
| Safety & security | 9 | Plans/tracks but does not do the work. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 14. quality-assurance

**Transcript:** `quality-assurance_TEST-015.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (risk-based testing, defect handling), test types, defect handling (fixed by implementation, not QA). |
| Practical usability | 8 | Actionable QA plan with risk-based test selection. |
| Engineering quality | 7 | Test types (unit/integration/security/performance); execution evidence deferred to evidence-quality-gates. |
| Safety & security | 9 | Does not fix defects; does not run security scans. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 15. release-deployment

**Transcript:** `release-deployment_TEST-012.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (readiness, staging, migrations, production, rollback), readiness checks, rollback plan. |
| Practical usability | 8 | Actionable release plan; correctly identified missing test evidence and security sign-off. |
| Engineering quality | 8 | Readiness criteria + rollback (redeploy previous version). |
| Safety & security | 10 | Production deployment requires named human approval; correctly withheld. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 16. requirements-design

**Transcript:** `requirements-design_TEST-009.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (elicit/document/validate requirements and UX before design), when to use/not use. |
| Practical usability | 8 | Actionable requirements spec with acceptance criteria and open questions. |
| Engineering quality | 7 | Open questions recorded rather than invented; no stakeholder validation conducted. |
| Safety & security | 9 | Correctly defers architecture to technical-architecture and coding to software-implementation. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 17. secure-change-control

**Transcript:** `secure-change-control_TEST-008.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (risky change: classification, approvals, rollback, audit trail), when to use/not use (not security code reviews). |
| Practical usability | 8 | Actionable change classification (HIGH) + NEEDS_HUMAN_APPROVAL. |
| Engineering quality | 8 | Risk classification, rollback plan, audit-trail fields. |
| Safety & security | 10 | Does not self-approve; only named humans approve; change recorded as proposal (read-only). |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 18. software-implementation

**Transcript:** `software-implementation_TEST-006.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (implement features/fixes), boundaries (not design/review/deployment). |
| Practical usability | 8 | Actionable implementation + unit tests; written to scratch file (read-only eval). |
| Engineering quality | 7 | Input validation, edge cases, tests; self-verification (not independent). |
| Safety & security | 9 | No self-review, no deployment. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 19. sre-observability

**Status:** BLOCKED — not executed (requires telemetry sources, APM/log/metric platform, on-call/escalation path; none available). No transcript created.

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 9 | Purpose (monitoring, logs, metrics, traces, alerting, SLOs, postmortems), decision rules (blameless postmortem; mask sensitive telemetry), quality gates (objectives per journey, pages map to user impact). |
| Practical usability | 5 | Requires telemetry sources and observability platform; not available. |
| Engineering quality | 9 | SLIs/SLOs/error budget; golden signals; root-cause analysis; blameless postmortems. |
| Safety & security | 9 | Sensitive telemetry masked; postmortems blameless (causes not people). |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## 20. technical-architecture

**Transcript:** `technical-architecture_TEST-011.md` — PARTIAL PASS

| Category | Score | Reasoning / evidence |
|---|---|---|
| Instruction quality | 8 | Purpose (boundaries, interfaces, trade-offs), when to use/not use. |
| Practical usability | 8 | Actionable architecture review with components, interfaces, data flows, trade-offs. |
| Engineering quality | 8 | Trade-offs recorded with rationale (async vs sync; signed URLs vs direct access). |
| Safety & security | 9 | No feature coding; no release approval. |
| OpenCode compatibility | 10 | Standard format; references present. |

---

## Cross-cutting audit observations (all 20 skills)

- **Consistent structure:** Every SKILL.md uses YAML frontmatter (name, description, metadata author/version/tags) plus purpose, when to use, when NOT to use, prerequisites, inputs/outputs, procedure, decision rules, quality gates, illustrative examples, limitations, troubleshooting, tools, stages covered, handoffs, related. This consistency is a major strength.
- **Illustrative examples:** All examples are explicitly labelled "Illustrative only ... not executed against a real project," consistent with the repository's evidence-over-assertion rule (AGENTS.md rule 3).
- **Safety:** All skills respect the "human approves production/security changes" boundary; none self-approve destructive actions.
- **References:** All skills reference local `references/CORE_PROCEDURE.md` and `references/HANDOFF_CONTRACT.md`; confirmed present. No broken relative paths found.
- **No critical defects** found in any SKILL.md during this read-only audit.
