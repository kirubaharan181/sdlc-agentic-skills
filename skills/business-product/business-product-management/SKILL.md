---
name: business-product-management
description: "Use when assessing a business case: strategy, discovery, estimates, approval. Do NOT use for detailed requirements or sprint planning."
metadata:
  author: kirubaharan181
  version: "1.1.1"
  tags: ["product", "strategy", "discovery", "business-case"]
---

# Product strategy and discovery

## Purpose
Turns a business problem into a validated, costed and approved opportunity so engineering effort starts on something worth building. It owns stages 1-10: strategy, market research, client engagement, discovery, analysis, planning, feasibility, budget, approval and contract compliance.

## When to Use
- A new product, feature or client request needs a business case before requirements are written.
- A funding, go or no-go, or contract decision needs evidence.
- Market, feasibility or budget assumptions need to be tested.

## When NOT to Use
- Writing testable requirements or designs: use requirements-design.
- Planning sprints or tracking delivery: use project-agile-management.
- Choosing technology or system structure: use technical-architecture.

## Prerequisites and Requirements
- A stated problem, opportunity or client request and a named sponsor.
- Access to existing strategy, market, cost and contract documents the team may use.
- No external API keys, paid services or network access are required; work uses files and tools already approved in the repository.

## Inputs and Outputs
Required inputs:
- problem or opportunity statement
- sponsor and decision maker
- constraints (budget, date, regulation)

Optional inputs:
- market data
- client interview notes
- existing contracts
- past estimates

Outputs and deliverables:
- business case with measurable goals and a do-nothing option
- market and feasibility findings with sources
- estimate ranges with assumptions
- approval record naming the human approver and conditions

## Procedure
1. Frame the outcome and decision question; identify user segments, sponsor and measurable business objective.
2. Gather source-linked market, customer, competitor and operational evidence; label assumptions and sample limitations.
3. Compare options by user value, confidence, effort, risk and strategic fit; design experiments for high-uncertainty assumptions.
4. Baseline roadmap outcomes, prioritization rationale, owner and review triggers.

Shared rules (evidence, approvals, failure, handoff): [references/CORE_PROCEDURE.md](references/CORE_PROCEDURE.md).

## Decision Rules
| Situation | Action |
|---|---|
| No measurable goal or baseline | Stop and ask for one; do not approve a case that cannot be measured. |
| Estimate is a single number | Convert it to a range with assumptions before it is used for approval. |
| Contract or regulatory obligation found | Record it in the obligations register and route to the compliance owner. |
| Approver is not a named human | Mark the decision NEEDS_HUMAN_APPROVAL; never record an agent as approver. |

## Quality Gates
- [ ] Goals have measures, baselines and dates
- [ ] Do-nothing option is compared
- [ ] Every market or cost claim cites a source or is labelled an assumption
- [ ] A named human approved funding, with conditions recorded

## Examples
Illustrative only: these show expected behavior and were not executed against a real project.

### Example 1: Assess a new feature request
```text
Request: A client asks for a self-service invoice portal. Should we build it?
Context: Support spends 30 percent of its time on invoice requests; no portal exists.
Agent behavior: Measure the current support load, list options including do-nothing and a cheaper export feature, estimate each as a range, and recommend one with risks.
Output: Business case with baseline (support hours per month), three options, estimate ranges and a recommendation awaiting sponsor approval.
Acceptance: Each option has a cost range and an expected change in the baseline measure.
```

### Example 2: Check contract obligations before approval
```text
Request: Review the draft statement of work for obligations that affect delivery.
Context: The contract requires data to stay in one country and 24-hour breach notice.
Agent behavior: List each obligation as what, owner and evidence, flag any the team cannot meet, and send gaps to legal.
Output: Obligations register with owners and a list of unmet obligations.
Acceptance: No obligation lacks an owner; gaps are raised before approval.
```

## Limitations
- Cannot verify market data it is given; sources must be cited by the user or found with approved tools.
- Does not decide funding: a named human approves.
- Estimates are ranges from stated assumptions, not commitments.

## Troubleshooting
| Error | Cause | Resolution |
|---|---|---|
| Sponsor cannot be identified | No one owns the decision | Ask who funds and accepts the outcome; do not proceed to approval without a name. |
| Market data conflicts between sources | Different dates, scopes or methods | Record both with dates and methods, use the more conservative figure, and flag the conflict. |
| Estimate has no baseline | Past delivery data missing | Use a labelled assumption and schedule a re-estimate at the first checkpoint. |

## Tools
- market research
- customer interviews
- opportunity sizing
- roadmap and experiment tracking

## Stages covered
| Stage | Name | Status | Accountable role |
|---|---|---|---|
| 1 | Business Strategy | complete | Business Strategist |
| 2 | Market Research | complete | Market Research Analyst |
| 3 | Client Engagement | complete | Client Engagement Specialist |
| 4 | Product Discovery | complete | Product Manager |
| 5 | Business Analysis | complete | Business Analyst |
| 6 | Product Planning | complete | Product Manager |
| 7 | Feasibility Analysis | complete | Solution Architect |
| 8 | Budget & Estimation | complete | FinOps Specialist |
| 9 | Project Approval | complete | Product Manager |
| 10 | Contract & Compliance | complete | Compliance Specialist |

Per-stage inputs, outputs, acceptance criteria and validation: [references/stages.md](references/stages.md).

## Handoffs
Hands to:
- `requirements-design`: approved business case, goals, scope and constraints
- `project-agile-management`: approved project charter inputs and budget
- `enterprise-governance`: contract and compliance obligations register

Contract: [references/HANDOFF_CONTRACT.md](references/HANDOFF_CONTRACT.md).

## Related
- Examples (illustrative only): see the files in references/examples/.
- Workflows: existing-application-enhancement, new-product-development.
- Roles: business-analyst, business-strategist, client-engagement-specialist, compliance-specialist, finops-specialist, market-research-analyst, product-manager, product-owner, project-manager, software-architect, solution-architect, ux-researcher, vendor-management-specialist.
- Selection and handoff guidance: the skill selection guide in the repository documentation.
