# Enterprise Engineering Skills Library

A vendor-neutral, evidence-driven operating system for AI-assisted software delivery. It maps all 190 mandatory SDLC stages to reusable skills, accountable agents, workflows, approvals, and deterministic validation.

## Quick start

```powershell
python scripts/validate.py
python scripts/generate_reports.py
```

Read [getting started](docs/getting-started/GETTING_STARTED.md), the [execution model](docs/architecture/EXECUTION_MODEL.md), and [security model](docs/security/SECURITY_MODEL.md). Production and other irreversible actions always require explicit human approval.

## Design

- `skills/`: 15 category-specific skills plus cross-cutting controls.
- `agents/`: registry-defined specialist roles with least-privilege contracts.
- `workflows/`: 23 workflow definitions in the workflow registry.
- `registry/`: canonical stage, skill, agent, and workflow traceability.
- `scripts/`: dependency-free deterministic validators and report generation.

## Status

Generated artifacts are validated locally; tool integrations and platform adapters document capabilities rather than claiming untested full support.
