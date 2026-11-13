<div align="center">

# Atelier — Engineering Command Center

### A premium, source-backed explorer for the complete software engineering lifecycle.

**Discover the stages. Understand the skills. Connect the roles. Follow the workflows. Trust the evidence.**

[![Validate library](https://github.com/kirubaharan181/sdlc-agentic-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/kirubaharan181/sdlc-agentic-skills/actions/workflows/validate.yml)
![SDLC stages](https://img.shields.io/badge/SDLC%20stages-190%2F190-7967E8?style=flat-square)
![Domains](https://img.shields.io/badge/domains-15-9B8AEF?style=flat-square)
![Skills](https://img.shields.io/badge/skills-20-F18D69?style=flat-square)
![Specialist roles](https://img.shields.io/badge/roles-74-C9E77B?style=flat-square)
![Workflows](https://img.shields.io/badge/workflows-23-A69BCB?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-292A31?style=flat-square)

[Explore the library](#-explore-the-library) · [How it works](#-how-it-works) · [Quick start](#-quick-start) · [Contribute](#-contributing)

</div>

---

## What is this?

**Atelier** is the interactive command center for the [Enterprise Engineering Skills Library](https://github.com/kirubaharan181/sdlc-agentic-skills) — an evidence-driven operating model for AI-assisted software delivery.

It brings the repository's canonical SDLC stages, reusable skills, specialist role contracts, workflow routes, platform adapters and engineering controls into one navigable experience.

This is more than a prompt collection. It is a connected engineering system designed to make work **traceable, reviewable, portable and safe** — from the first business decision to production operations and continuous improvement.

## At a glance

| Library asset | Registry snapshot |
|---|---:|
| SDLC stages | **190** across **15** domains |
| Reusable skills | **20** |
| Specialist role contracts | **74** |
| Workflow routes | **23** |
| Platform adapter declarations | **7** |
| Canonical source | Structured registries + Markdown contracts |

Counts reflect the canonical registry snapshot committed with this release. Regenerate the dashboard data after changing source registries.

## ✦ Explore the library

| Area | What you can explore |
|---|---|
| **SDLC Explorer** | All 190 stages, ownership, inputs, outputs, dependencies, quality gates and traceability |
| **Skills Library** | Portable skill definitions, mapped stages and canonical source files |
| **Agent Directory** | Specialist responsibilities, required skills, permission boundaries, escalation and handoffs |
| **Workflow Studio** | Triggers, stage sequences, responsible roles, approval gates and completion criteria |
| **Evidence & Gates** | Gate state model, evidence expectations and stage-level gate references |
| **Architecture Map** | How registries, skills, roles, workflows, orchestration and evidence fit together |
| **Platform Adapters** | Capability declarations for agent and coding environments |
| **Governance Center** | Engineering standards, security policies, approval boundaries and accountability |
| **Knowledge Center** | Getting started, architecture, authoring guides, examples and troubleshooting |

### Open the dashboard

The Atelier web interface lives in the **dashboard/** directory.

- [Dashboard entry point](dashboard/index.html)
- [Dashboard styles](dashboard/assets/styles.css)
- [Dashboard interactions](dashboard/assets/app.js)
- [Generated library snapshot](dashboard/data/library.json)

The dashboard is a static, responsive application with a light editorial theme, optional dark theme, domain explorer, searchable stage register, skill and role directories, workflow details, evidence policy, architecture map and platform capability views.

## How it works

~~~mermaid
flowchart LR
    A[Canonical registries] --> B[Skills]
    A --> C[Specialist roles]
    A --> D[Workflow routes]
    B --> E[Master orchestrator]
    C --> E
    D --> E
    E --> F[Evidence and quality gates]
    F --> G[Verified handoffs]
    G --> H[Auditability and improvement]
~~~

**One source of truth, many useful views.** Registries define identifiers and mappings; Markdown contracts explain execution; workflows coordinate delivery; evidence gates make decisions reviewable. The orchestrator does not self-approve sensitive work.

## Quick start

### 1. Clone and validate

~~~bash
git clone https://github.com/kirubaharan181/sdlc-agentic-skills.git
cd sdlc-agentic-skills
python scripts/validate.py
python scripts/run_tests.py
~~~

### 2. Generate the dashboard snapshot

~~~bash
python scripts/generate_dashboard_data.py
~~~

This reads the JSON-compatible YAML registries and writes **dashboard/data/library.json**. The dashboard does not maintain a second hand-edited source of truth.

### 3. Run locally

From the repository root:

~~~bash
python -m http.server 8000
~~~

Open **http://localhost:8000/dashboard/**.

The dashboard is static: no database, API key or backend service is required. Google Fonts are progressive enhancement; system font fallbacks remain available.

## Trust & operating principles

- **Evidence over assertion:** a gate is not PASS without traceable evidence tied to an exact revision and verification method.
- **Separation of duties:** implementation, independent verification and authorization remain distinct where risk requires it.
- **Human approval:** sensitive production, security and compliance decisions require the designated authority.
- **Least privilege:** permissions are scoped by the host runtime, not inferred from a role title.
- **Portable by design:** adapters describe platform capabilities and limitations; they do not promise identical behavior everywhere.
- **Honest status:** defined roles are not necessarily running agents; example evidence is not production evidence; a dashboard snapshot is not live telemetry.

## Repository map

~~~text
registry/       Canonical stage, skill, role and workflow registries
skills/         Reusable skill instructions and stage playbooks
agents/         Specialist role contracts and operating model
workflows/      End-to-end and targeted delivery routes
orchestrator/   Routing, evidence, handoff and safety policies
adapters/       Cross-platform capability declarations
standards/      Shared engineering, security, testing and release standards
templates/      Evidence, handoff and definition-of-done templates
docs/           Architecture, guides, examples and troubleshooting
scripts/        Deterministic validation and report generation
tests/          Registry checks and controlled workflow scenarios
dashboard/      Atelier static command center and generated data snapshot
~~~

## Validation

~~~bash
python scripts/validate.py
python scripts/run_tests.py
python scripts/generate_reports.py
python scripts/generate_dashboard_data.py
~~~

These checks validate repository structure, mappings and controlled fixtures. They do not claim a production deployment, external platform integration, penetration test or live agent execution.

## Contributing

Improvements are welcome: refine a stage contract, add a reusable skill, strengthen a role boundary, improve a workflow, extend an adapter or add deterministic validation.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md).
2. Keep canonical identifiers and mappings consistent.
3. Include reproducible evidence for behavior changes.
4. Run the validation and test commands.
5. Submit a focused pull request with limitations clearly stated.

## License

Released under the [MIT License](LICENSE).

---

<div align="center">

**A clearer way to engineer software with AI.**

Built for traceability, thoughtful automation and dependable delivery.

</div>
