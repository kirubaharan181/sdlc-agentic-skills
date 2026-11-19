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
**Client Engagement** (complete). Purpose: build a working relationship with a client in which expectations, responsibilities and communication are agreed in writing.

Entry criteria: A client or client sponsor is identified; The team's service scope is known; A named contact exists on each side

Inputs: client background and goals; service scope; contacts and decision makers; past engagement notes

Procedure:
1. Meet the client sponsor and record the business goals, success measures and constraints in the client's own words.
2. Agree who decides what on each side, how often the teams talk, and which channel is used for what.
3. Write down the scope, what is not included, and how changes to scope are raised and priced.
4. Agree how issues are escalated and the response times each side expects.
5. Share a one-page engagement summary and ask the client to confirm it in writing.
6. Hold a short review at an agreed interval and record satisfaction and open concerns.

Deliverables: engagement summary signed off by the client; contact and decision-maker list; change and escalation procedure; review notes

Acceptance: Goals and measures are in the client's words Decision makers are named on both sides Change and escalation paths are written The client confirmed the summary

Validation: Client sponsor confirmation.

- manual: check the engagement summary has a dated written confirmation from the client expect: confirmation present
- manual: check each contact has a named backup expect: none missing

Failure modes:
- Verbal agreements only | detect: Dispute about scope | respond: Write and confirm them
- Wrong decision maker | detect: Decisions reversed later | respond: Confirm authority in writing
- No review cadence | detect: Concerns found late | respond: Schedule the reviews

ILLUSTRATIVE: A new client's sponsor confirms in writing three goals, a weekly status call and a change request route; a review at week six records one concern about report timing.

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
**Business Analysis** (complete). Purpose: turn a business problem into analyzed needs, process models and options with costs and benefits, so the right thing gets specified.

Entry criteria: A business problem or opportunity is stated; Stakeholders can be reached; A sponsor is named

Inputs: problem statement and goals; current process descriptions and data; stakeholder input; constraints

Procedure:
1. Describe the current process end to end (who, steps, systems, volumes, delays and error rates) using observation and data, not only descriptions.
2. Model it with a standard notation such as BPMN, and mark where work waits, loops back or is done by hand.
3. Find root causes with a method such as five whys or cause-and-effect analysis, and test each cause against data.
4. Define options including the do-nothing case, and compare them on cost, benefit, risk and effort with the assumptions shown.
5. Recommend an option and state the measurable change expected, such as handling time or error rate, with the baseline.
6. Hand over the analysis and the recommendation to requirements work with the open questions listed.

Deliverables: current-state process model with measures; root cause analysis; options comparison including do-nothing; recommendation with baseline and expected change

Acceptance: Process models match what people do, confirmed by them Causes are supported by data Do-nothing is one of the options The expected benefit has a baseline

Validation: Sponsor review of the recommendation.

- manual: walk two process participants through the model and record corrections expect: corrections applied
- manual: recompute the benefit estimate from the cited baseline figures expect: same result

Failure modes:
- Model shows the official process, not the real one | detect: Staff describe different steps | respond: Observe the work and revise
- Benefit without baseline | detect: No measure to compare | respond: Collect baseline first
- Only one option compared | detect: No alternatives | respond: Add do-nothing and a cheaper option

ILLUSTRATIVE: Observation shows invoice approvals wait a median of 6 days, mostly for one approver. Options are compared, including a delegation rule, and the recommendation targets a 2-day median with the 6-day figure as the baseline.

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
**Budget & Estimation** (complete). Purpose: estimate cost and effort honestly, with ranges and stated assumptions, so budget decisions are made on realistic numbers.

Entry criteria: Scope or requirements exist at some level; Rate and cost information is available; Past delivery data exists or is being gathered

Inputs: scope and requirements; past project actuals; rates and infrastructure prices; risk list

Procedure:
1. Break the work into parts small enough to estimate, and list what is excluded.
2. Estimate each part as a range (best, likely, worst) using past actuals where possible, and note the assumptions.
3. Add running costs, not only build costs: hosting, licences, support and the team time to operate.
4. Add a contingency tied to the largest risks, not a flat guess, and show it separately.
5. Compare the total with the available budget and show what could be cut or deferred to fit.
6. Re-estimate at agreed checkpoints and report the variance from the first estimate.

Deliverables: estimate with ranges and assumptions; running cost forecast; contingency with reasons; variance reports

Acceptance: Every estimate is a range with stated assumptions Running cost is included Contingency is linked to named risks Variance is reported at checkpoints

Validation: FinOps review of the cost model.

- manual: recompute the totals from the line items in a second spreadsheet or script expect: totals match
- manual: check each assumption maps to a line in the risk list or is marked accepted expect: none orphaned

Failure modes:
- One-number estimate | detect: No range shown | respond: Add best, likely and worst
- Run cost omitted | detect: Budget exceeded in year one | respond: Add operating cost
- Contingency padded | detect: Flat percentage with no reason | respond: Tie it to risks

ILLUSTRATIVE: A reporting feature is estimated at 40 to 70 person-days with hosting of 300 per month; the contingency of 10 days is tied to the unknown data quality, and the budget fits only if one export format is deferred.

Gate: 01-008. Approval: none required

## 9
**Project Approval** (complete). Purpose: decide, with the right people and on stated evidence, whether a project may proceed and with what funding and conditions.

Entry criteria: A business case, plan and estimate exist; The approving person or board is named; Risks and dependencies are listed

Inputs: business case; plan and estimate; risk list; strategy fit assessment

Procedure:
1. Check the submission is complete: goals, measures, costs, risks, dependencies and the plan.
2. Review it against the approval criteria written in the approval policy, scoring each criterion with evidence.
3. List conditions and the questions that must be answered before funding, and track them to closure.
4. Take the decision from the named approver, and record approve, approve with conditions, defer or reject, with the reason.
5. Release funding and the team in stages tied to checkpoints, not all at once.
6. Tell all affected teams the decision and conditions, and set the date for the first checkpoint.

Deliverables: completeness check; criteria scoring with evidence; decision record with conditions; staged funding plan

Acceptance: Approver is a named human Decision and reason are recorded Conditions have owners and dates Funding is tied to checkpoints

Validation: Named business sponsor decision; an agent only prepares the pack.

- manual: confirm the decision record names the human approver and the date expect: present
- manual: check each condition has an owner and a due date expect: none missing

Failure modes:
- Approval without evidence | detect: Criteria not scored | respond: Return for scoring
- Conditions forgotten | detect: Funding released with open items | respond: Track and gate funding on them
- Agent treated as approver | detect: Decision has no human name | respond: Reject the record and obtain approval

ILLUSTRATIVE: A proposal for a payments rebuild is approved with two conditions, a security review and a vendor price confirmation; funding is released for the first phase only, with a checkpoint in eight weeks.

Gate: 01-009. Approval: business-sponsor (always)

## 10
**Contract & Compliance** (complete). Purpose: make sure contracts and legal and regulatory obligations are understood, assigned and checked before work begins and during it.

Entry criteria: A contract or obligation applies to the work; Legal or compliance contact is known; The work scope is defined

Inputs: contracts and statements of work; applicable regulations and policies; data and security obligations; scope of work

Procedure:
1. List each obligation from the contract and regulations in plain terms: what, who, by when and how it is evidenced.
2. Map every obligation to an owner and a delivery stage, and flag any obligation the team cannot meet.
3. Check the work plan against restrictions such as data location, subcontractors, licences and reporting duties.
4. Raise conflicts and gaps with legal before work starts, and record the answers.
5. Collect evidence of compliance as the work proceeds, and keep it where audit can find it.
6. Review obligations at each major change and at contract milestones.

Deliverables: obligations register; conflict and gap log; evidence file; review records

Acceptance: Each obligation has an owner and evidence Unmeetable obligations were raised with legal Restrictions are checked against the plan Evidence is retrievable

Validation: Legal or compliance approval.

- manual: sample five obligations and trace each to an owner and evidence item expect: all traced
- manual: check the register lists every contract in scope expect: none missing

Failure modes:
- Obligation without owner | detect: Register row empty | respond: Assign before work starts
- Data location breached | detect: Plan uses a region the contract forbids | respond: Change the plan or seek approval
- Evidence not kept | detect: Audit cannot confirm compliance | respond: Collect during the work

ILLUSTRATIVE: A client contract requires data to stay in one country and 24-hour breach notice. The register assigns owners to both, and a plan using an overseas log service is changed before work begins.

Gate: 01-010. Approval: legal-owner (always)
