# Inventory Application Walkthrough

1. Product and requirements roles produce PRD, user journeys, acceptance criteria, and non-functional constraints.
2. Architecture roles produce ADRs, threat model, data/API contracts, and deployment design; an independent reviewer approves the architecture gate.
3. Engineering implements a thin vertical slice with tests mapped to acceptance criteria. QA and AppSec validate independent reports.
4. CI produces an immutable artifact; staging deploys that artifact and records smoke, migration, performance, and security evidence.
5. A designated human grants or rejects production approval. On approval, deploy with health checks, rollback owner, dashboards, alert routes, and operational handoff.

The walkthrough is illustrative; it is not production evidence.
