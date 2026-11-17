# Product strategy and discovery: stage reference

## Contents
- [1 Business Strategy](#1)
- [2 Market Research](#2)
- [3 Client Engagement](#3)
- [4 Product Discovery](#4)
- [5 Business Analysis](#5)
- [6 Product Planning](#6)
- [7 Feasibility Analysis](#7)
- [8 Budget & Estimation](#8)
- [9 Project Approval](#9)
- [10 Contract & Compliance](#10)

## 1
**Business Strategy** (complete). Purpose: set the direction that product and engineering work will serve, in terms the organization can test and fund.

Entry criteria: Business context and leadership input are available; Market and financial data can be gathered; A sponsor is accountable for the strategy

Inputs: company goals and finances; market and competitor information; customer evidence; capability assessment

Procedure:
1. State the business goals and the time horizon in measurable terms.
2. Describe the market position, customers served and what makes the offering different, using evidence.
3. Assess strengths, gaps and constraints in people, technology and money.
4. Set a small number of strategic choices, including what not to do, with reasons.
5. Turn each choice into outcomes and measures that product teams can plan against.
6. Review on a schedule and revise when evidence changes, recording what changed and why.

Deliverables: strategy statement; evidence summary; outcomes and measures; review schedule

Acceptance: Goals have measures and dates Choices include what is not pursued Claims cite evidence A review date and owner exist

Validation: Business sponsor approval.

- manual: check every strategic goal has a measure, an owner and a date expect: none missing
- manual: trace each claim about the market to a cited source expect: all traced or marked as assumption

Failure modes:
- Goals not measurable | detect: No way to judge progress | respond: Rewrite with measures
- Strategy lists everything | detect: No trade-offs shown | respond: Add what is not pursued
- Assumptions unmarked | detect: Claims lack sources | respond: Label them and plan to test

ILLUSTRATIVE: A company sets a goal of 20 percent more recurring revenue in two years by focusing on mid-sized customers and deliberately not building a consumer product, with quarterly review of three measures.

Gate: 01-001. Approval: none required

## 2
**Market Research** (complete). Purpose: learn what the market and the customers actually do and want, with sources that others can check.

Entry criteria: A decision depends on market knowledge; Access to data sources or customers exists; Questions are agreed with the requester

Inputs: research questions; published market data; competitor information; customer interviews or surveys

Procedure:
1. Write the decisions the research should inform and turn them into specific questions.
2. Choose methods per question: published data, competitor analysis, interviews, survey or usage data.
3. Record every source with date and type, and note limits such as sample size and bias.
4. Separate findings (what the data shows) from interpretation (what it may mean).
5. Size the opportunity with the method shown, and give a range, not one number.
6. Report answers to each question and what remains unknown.

Deliverables: research plan; source log; findings report; market size with method

Acceptance: Each question is answered or marked unanswered Sources are dated and logged Findings are separate from interpretation Estimates show their method and range

Validation: Requester review.

- manual: check every number in the report against the source log expect: each traceable
- manual: confirm interview sample and selection method are stated expect: stated

Failure modes:
- Leading questions | detect: Interviews confirm what was expected | respond: Revise the guide and repeat
- Stale data | detect: Source older than needed | respond: Find newer or flag
- Single number for market size | detect: No range | respond: Show low and high cases

ILLUSTRATIVE: To decide on entering a new region, the team compiles public data, six competitor price pages and eight customer interviews. The report gives a market size range from 40 to 70 million with the method shown and lists unknowns.

Gate: 01-002. Approval: none required

## 3
**Client Engagement** (stub). Purpose: establish an agreed client outcome and a controlled decision trail.

Inputs: client stakeholders and decision authority; statement of need and current commitments; communication constraints

Procedure:
1. Map sponsor, users, approvers and operational contacts; identify who can accept scope, cost and risk.
2. Run a structured discovery conversation and capture needs, constraints, success measures and unresolved questions.
3. Record commitments, decision owners, dates and changes in a client decision log; do not treat informal discussion as approval.
4. Confirm the agreed next action, accountable owner and acceptance route with the client.

Deliverables: stakeholder map; engagement notes; decision and commitment log; confirmed action register

Acceptance: Every commitment has an owner and due date. Client acceptance and internal approval are distinguishable. Conflicting expectations are recorded and escalated before scope is baselined.

Validation: Client confirmation of decisions and review by the accountable engagement owner.

Gate: 01-003. Approval: none required

## 4
**Product Discovery** (complete). Purpose: find real problems worth solving and test the idea cheaply before committing to build it.

Entry criteria: A target user group or problem area is named; Access to users exists; The team has time for short experiments

Inputs: user research; usage data; problem hypotheses; competing solutions

Procedure:
1. Write the problem hypotheses as who has the problem, what happens, and why it matters.
2. Interview users about past behavior, not opinions about your idea, and record what they say.
3. Rank problems by frequency, pain and willingness to change, using evidence from the interviews.
4. For the best problem, run the cheapest test of a solution: prototype, concierge version or landing page.
5. Set the success threshold before the test, then judge by it.
6. Decide to proceed, change direction or stop, and record the evidence.

Deliverables: problem hypotheses; interview notes; experiment design and result; decision record

Acceptance: Success threshold was set before the test Interview notes are recorded Decision is based on the threshold Stopping is a valid recorded outcome

Validation: Product manager decision.

- manual: confirm the success threshold was written before the experiment started expect: dated record exists
- manual: count interviews supporting each ranked problem expect: counts shown in the ranking

Failure modes:
- Leading interviews | detect: Users agree with everything | respond: Ask about past behavior
- Threshold moved afterwards | detect: Result passes only after change | respond: Treat as failed
- Only friendly users | detect: Sample not representative | respond: Recruit outside the network

ILLUSTRATIVE: Eight interviews show that small teams re-enter data between two tools weekly. A concierge version run by hand for five teams meets the pre-set threshold of three repeat uses, so the idea proceeds to planning.

Gate: 01-004. Approval: none required

## 5
**Business Analysis** (stub). Purpose: translate business needs into process and decision requirements.

Inputs: business objectives and stakeholders; current-state process evidence; policy and data constraints

Procedure:
1. Map current actors, events, inputs, decisions, exceptions and downstream outcomes.
2. Identify process pain points, business rules, data ownership and control points.
3. Model the proposed state and compare impacts, dependencies and exception paths.
4. Trace each requirement to a business objective and a measurable acceptance condition.

Deliverables: current/future process model; business rule catalogue; gap analysis; requirements traceability

Acceptance: Process paths include normal, exception and failure cases. Rules have an owner and source. Requirements are testable and trace to a business outcome.

Validation: Walkthrough with process owners and affected users.

Gate: 01-005. Approval: none required

## 6
**Product Planning** (complete). Purpose: turn a validated opportunity into a plan with scope, order, owners and dates that the team can commit to.

Entry criteria: The opportunity is validated (stage 4); Capacity of the teams is known; Dependencies on other teams are listed

Inputs: validated opportunity; feasibility and estimates; team capacity; strategy and goals

Procedure:
1. State the outcome and the measure of success, and what is explicitly out of scope.
2. Break the work into releasable increments, each delivering value alone.
3. Order increments by value, risk and dependency, and put the riskiest assumptions earliest.
4. Estimate with ranges against known capacity, and mark the assumptions behind them.
5. Name the owner of each increment and each dependency, and agree dates with those teams.
6. Set review points where scope or order can change, and publish the plan.

Deliverables: product plan with scope and out-of-scope; ordered increments; estimates with ranges; dependency and owner list

Acceptance: Outcome and measure are stated Out of scope is written Every increment has an owner and a range estimate Dependencies are agreed with the other teams

Validation: Product manager and sponsor sign-off.

- manual: check each increment delivers value on its own and has an owner expect: none fails
- manual: confirm each external dependency has an agreed date from the other team expect: all confirmed

Failure modes:
- Plan is a single date | detect: No ranges or assumptions | respond: Add ranges and list assumptions
- Dependency not agreed | detect: Other team unaware | respond: Agree before committing
- Riskiest work last | detect: Late discovery | respond: Move the riskiest assumption first

ILLUSTRATIVE: A billing revamp is split into three increments. The one testing the new provider's API comes first because it carries the most risk; estimates are ranges, and the finance team confirms the cut-over window.

Gate: 01-006. Approval: none required

## 7
**Feasibility Analysis** (complete). Purpose: judge whether an idea can be built and run within technical, time, cost and legal limits, before it is committed.

Entry criteria: A candidate solution or options exist; Constraints on time, budget and compliance are known; An architect is available to assess

Inputs: solution options; constraints and requirements; existing architecture; team skills

Procedure:
1. List the requirements that most affect feasibility, such as scale, integration, data and compliance.
2. For each option, assess technical fit, integration effort, skill gaps, operating cost and legal constraints.
3. Identify the largest unknown for each option and run a small spike to test it.
4. Compare options with the same criteria and show the scoring and the evidence.
5. Recommend an option, or recommend not to proceed, with the main risks and how to reduce them.
6. Record the assumptions that, if wrong, would change the recommendation.

Deliverables: feasibility assessment; spike results; options comparison; recommendation with risks and assumptions

Acceptance: Options are scored on the same criteria The largest unknown was tested Risks have a reduction step Key assumptions are listed

Validation: Solution architect recommendation; sponsor decision.

- manual: confirm each option row has evidence or marked assumption expect: no unsupported scores
- manual: check the spike output is attached to the assessment expect: attached

Failure modes:
- Preferred option wins by design | detect: Criteria written after the choice | respond: Fix criteria first
- Unknown never tested | detect: Risk unsupported by evidence | respond: Run a spike
- Cost counted only to build | detect: Operating cost missing | respond: Add run cost

ILLUSTRATIVE: Two options for ingesting partner data are compared. A one-day spike shows the partner's API limits rule out near-real-time polling, so the batch option is recommended with a note that the assumption about volume must be rechecked.

Gate: 01-007. Approval: none required

## 8
**Budget & Estimation** (stub). Purpose: produce a transparent estimate and funding baseline.

Inputs: scope breakdown and assumptions; rates, capacity and supplier estimates; contingency policy

Procedure:
1. Break work into measurable cost drivers and separate one-time from recurring spend.
2. Estimate effort, infrastructure, licensing, vendor, migration and support costs using ranges.
3. Document confidence, exclusions, currency, tax treatment and contingency basis.
4. Reconcile the estimate against available funding and define variance thresholds.

Deliverables: estimate workbook; assumption and exclusion log; funding request; cost baseline

Acceptance: Totals recalculate from traceable line items. Uncertainty and contingency are visible. Estimate owner and approval authority are named.

Validation: Finance review and independent arithmetic check.

Gate: 01-008. Approval: none required

## 9
**Project Approval** (stub). Purpose: prepare a controlled decision with sufficient evidence and independent authority.

Inputs: decision request and accountable sponsor; impact/risk assessment; supporting evidence and alternatives

Procedure:
1. Check the decision request is complete, in scope and owned by an authorized requester.
2. Evaluate acceptance evidence, residual risks, dependencies, rollback/recovery readiness and affected parties.
3. Record independent reviewer input and unresolved objections; do not approve work you personally verified where segregation is required.
4. Issue approve, reject, defer or conditional decision with conditions, expiry and accountable approver.

Deliverables: decision record; evidence index; conditions and waiver log

Acceptance: Decision authority is verified. Conditions are measurable, owned and time-bound. No missing or failed critical evidence is silently waived.

Validation: Independent approval record and audit trail.

Gate: 01-009. Approval: business-sponsor (always)

## 10
**Contract & Compliance** (stub). Purpose: review contractual and regulatory obligations before commitment.

Inputs: contract version and counterparties; applicable policy/control obligations; legal/compliance owner

Procedure:
1. Identify service, data, security, availability, audit, retention, subcontracting and exit obligations.
2. Map each obligation to an internal control owner and evidence source.
3. Flag ambiguous liability, data processing, IP, jurisdiction, renewal and termination terms.
4. Record legal review questions and do not provide legal approval outside delegated authority.

Deliverables: obligation matrix; contract exception log; review decision

Acceptance: Every material obligation has an owner and evidence path. Exceptions have an authorized risk owner. Unresolved legal interpretation is escalated.

Validation: Legal and compliance owner sign-off.

Gate: 01-010. Approval: legal-owner (always)
