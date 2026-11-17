# Delivery planning and flow management: stage reference

## Contents
- [35 Project Initiation](#35)
- [36 Resource Planning](#36)
- [37 Work Breakdown](#37)
- [38 Effort Estimation](#38)
- [39 Sprint Planning](#39)
- [40 Agile Management](#40)
- [41 Progress Tracking](#41)
- [42 Risk Management](#42)
- [43 Stakeholder Management](#43)
- [44 Change Management](#44)

## 35
**Project Initiation** (complete). Purpose: start a project with an agreed purpose, scope, roles and first steps, so everyone begins with the same understanding.

Entry criteria: The project is approved (stage 9); A project manager and sponsor are named; Initial budget and time frame exist

Inputs: approval decision and conditions; business case; stakeholder list; constraints

Procedure:
1. Write a short charter: purpose, objectives, scope, exclusions, success measures and constraints.
2. Name the sponsor, project manager and team leads, and state who decides what.
3. List the stakeholders and how each will be kept informed.
4. Set up the working basics: repository, backlog, communication channels and meeting rhythm.
5. List the first risks, assumptions and dependencies, with owners.
6. Hold a kickoff, share the charter and get written acknowledgement from the sponsor.

Deliverables: project charter; role and decision list; stakeholder communication plan; initial risks, assumptions and dependencies

Acceptance: Scope and exclusions are written Roles and decision rights are named Conditions of approval are carried into the plan The sponsor acknowledged the charter

Validation: Sponsor acknowledgement.

- manual: check every approval condition from stage 9 appears in the plan with an owner expect: all present
- manual: check the charter has a dated sponsor acknowledgement expect: present

Failure modes:
- Scope vague | detect: Different views at kickoff | respond: Add exclusions and agree
- Conditions dropped | detect: Approval items missing | respond: Add them to the plan
- Roles unclear | detect: Decisions stall | respond: Name decision makers

ILLUSTRATIVE: A charter for a data migration lists three objectives, excludes decommissioning the old system, names the sponsor as the budget decision maker, and carries over the approval condition about a security review.

Gate: 04-035. Approval: none required

## 36
**Resource Planning** (complete). Purpose: match people, skills, tools and time to the work, and show where there are gaps before they delay delivery.

Entry criteria: The work plan exists; Team availability is known; Skill needs are identified

Inputs: work plan and estimates; team members and availability; skills inventory; tool and environment needs

Procedure:
1. List the skills and roles needed for each phase and the amount of effort in each.
2. Compare with available people, counting leave, support duties and other commitments.
3. Find the gaps and decide how to close each: hire, borrow, train, contract or change the plan.
4. Plan lead times for access, equipment, licences and environments, which often take longer than expected.
5. Avoid single points of knowledge by pairing or planned handover on critical skills.
6. Review the plan at checkpoints and when people join or leave.

Deliverables: resource plan by phase; gap list with actions; lead-time list; single point of knowledge list

Acceptance: Availability counts leave and other duties Each gap has an action and an owner Lead times for access and tools are planned Critical skills are covered by more than one person

Validation: Project manager review with team leads.

- manual: compare allocated percentages per person with their available hours expect: no one above 100 percent
- manual: check each gap has an action, owner and date expect: none missing

Failure modes:
- Person allocated over 100 percent | detect: Sums exceed availability | respond: Rebalance or add people
- Access delay | detect: New joiner idle for weeks | respond: Request access in advance
- One person holds a critical skill | detect: Delivery depends on them | respond: Pair or document

ILLUSTRATIVE: A plan needs two backend engineers for six months. One is available at 50 percent, so the gap is closed by a contractor with access requested three weeks ahead and a handover plan for the integration knowledge.

Gate: 04-036. Approval: none required

## 37
**Work Breakdown** (stub). Purpose: decompose approved scope into estimable and verifiable work.

Inputs: approved scope and deliverables; dependencies and constraints; definition of done

Procedure:
1. Decompose deliverables into work packages with clear boundaries and owners.
2. Identify dependencies, integration points, external approvals and critical path.
3. Define acceptance evidence and estimate-ready assumptions for each package.
4. Review decomposition with delivery and technical owners before estimating.

Deliverables: WBS/backlog hierarchy; dependency network; work package acceptance criteria

Acceptance: Every scope item maps to a work package. No package is too broad to estimate or verify. Dependencies and ownership are explicit.

Validation: Cross-functional planning review.

Gate: 04-037. Approval: none required

## 38
**Effort Estimation** (complete). Purpose: estimate the effort for planned work in a way the team can calibrate and improve against actual results.

Entry criteria: Work items are described; Past delivery data exists or can be collected; The team doing the work is available to estimate

Inputs: work items with acceptance criteria; historical velocity or cycle time; team capacity; known risks

Procedure:
1. Have the people who will do the work estimate it, with the item and acceptance criteria in front of them.
2. Use a relative or range method and compare with similar completed items rather than guessing from nothing.
3. Split items that are too large to estimate with confidence, and note what remains unknown.
4. Convert to a delivery forecast using past throughput, giving a range and a confidence level.
5. Record the estimate and assumptions, then compare with actuals when each item completes.
6. Use the differences to adjust the method and the forecast.

Deliverables: estimates with assumptions; forecast range; estimate versus actual record; method adjustments

Acceptance: Estimates come from the doers Large items were split The forecast is a range based on past throughput Actuals are compared and used

Validation: Project manager review.

- manual: compare estimates and actuals for the last ten completed items expect: variance recorded
- manual: check every item over the size limit has been split expect: none remain

Failure modes:
- Estimates given by someone else | detect: Large gaps against actuals | respond: Estimate with the team
- Estimate treated as a promise | detect: Pressure to hit one date | respond: Report as a range
- No feedback loop | detect: Same error repeats | respond: Review variance each iteration

ILLUSTRATIVE: A team's last ten items averaged 1.4 times their estimates, so the forecast for the next release is stated as eight to twelve weeks with a note that the range reflects that history.

Gate: 04-038. Approval: none required

## 39
**Sprint Planning** (complete). Purpose: choose a realistic set of work for the next iteration, agreed by the team and tied to a clear goal.

Entry criteria: A refined, ordered backlog exists; Team capacity for the iteration is known; The product owner is available

Inputs: ordered backlog; team capacity; recent throughput; dependencies and risks

Procedure:
1. Set one sprint goal with the product owner that says what value the team will deliver.
2. Check capacity for the sprint: working days, leave, planned support and carry-over.
3. Pull items from the top of the backlog that serve the goal, confirming each has clear acceptance criteria.
4. Break the items into tasks the team can finish in about a day, and surface dependencies and risks.
5. Check the plan against recent throughput; remove items rather than overload.
6. Agree the plan with the whole team and publish the goal and the board.

Deliverables: sprint goal; selected items with acceptance criteria; task breakdown; risks and dependencies

Acceptance: There is one clear sprint goal Planned work fits capacity and recent throughput Each item has acceptance criteria The team agreed the plan

Validation: Scrum master facilitation; team commitment.

- manual: compare planned points or items with the average of the last three sprints expect: within an agreed margin
- manual: check every selected item has acceptance criteria expect: none missing

Failure modes:
- Overcommitment | detect: Half the items carry over | respond: Plan to throughput
- No goal | detect: Sprint is a list of items | respond: Write a goal first
- Unready items | detect: Questions during the sprint | respond: Return to refinement

ILLUSTRATIVE: With 9 working days and one person on leave, the team plans 22 points against a recent average of 24 and sets the goal 'customers can reset their password without support'.

Gate: 04-039. Approval: none required

## 40
**Agile Management** (complete). Purpose: keep the way a team plans, delivers and improves healthy and consistent, so delivery is predictable and problems surface early.

Entry criteria: Teams work in iterations or flow; Delivery measures can be collected; Teams hold regular reviews

Inputs: team practices; delivery measures; retrospective outcomes; impediment list

Procedure:
1. Agree the few practices all teams share, such as definition of done, backlog refinement and review, and leave the rest to teams.
2. Track a small set of flow measures: cycle time, throughput, work in progress and escaped defects.
3. Read the measures with the teams as signals for conversation, not as targets for individuals.
4. Collect impediments from every team, and have an owner remove or escalate each in a stated time.
5. Check that retrospective actions are done, and that the same problem is not raised repeatedly without action.
6. Review the practices each quarter and drop ones that no longer help.

Deliverables: shared practice list; flow measure report; impediment log with owners; retrospective action tracking

Acceptance: Shared practices are few and written Flow measures are tracked per team Each impediment has an owner and date Retrospective actions are tracked to done

Validation: Delivery manager review.

- manual: count open impediments older than the agreed time expect: each has an escalation record
- manual: check the last three retrospectives' actions for completion expect: completion rate recorded

Failure modes:
- Measures used to rank people | detect: Gaming starts | respond: Use them for team learning
- Impediments stay open | detect: Same blockers every sprint | respond: Assign owners and escalate
- Practices imposed in full | detect: Teams ignore them | respond: Keep the shared set small

ILLUSTRATIVE: Cycle time rises from 4 to 9 days on one team. The log shows reviews waiting on one person; a review rota is agreed, and the cycle time is checked again in two sprints.

Gate: 04-040. Approval: none required

## 41
**Progress Tracking** (complete). Purpose: show the real state of delivery against the plan, so decisions are based on facts and slippage is found early.

Entry criteria: A plan with milestones exists; Work items are tracked in a shared tool; A reporting rhythm is agreed

Inputs: plan and milestones; work item status; defects and risks; budget actuals

Procedure:
1. Define what done means for an item and a milestone, so status is judged the same way everywhere.
2. Take status from the tracking tool, not from memory or manual updates.
3. Compare progress with the plan using completed work, not effort spent, and show the trend.
4. Report risks, blockers and decisions needed next to the progress, with owners and dates.
5. Forecast the completion as a range and say what would change it.
6. Publish the report on the agreed schedule and record decisions taken from it.

Deliverables: progress report; trend against plan; forecast range; decision log

Acceptance: Status comes from the tracking tool Progress counts completed work Forecast is a range with its drivers Decisions needed are listed with owners

Validation: Delivery manager review.

- manual: recompute the completion percentage from the tracking tool export expect: matches the report
- manual: check every red item has an owner and a next step expect: none missing

Failure modes:
- Watermelon reporting | detect: Green status with problems underneath | respond: Use measured criteria
- Effort mistaken for progress | detect: Hours spent but items not done | respond: Count completed items
- No decisions listed | detect: Blockers wait for weeks | respond: Add decisions with owners

ILLUSTRATIVE: A report shows 60 percent of items complete against 70 percent planned, forecasts delivery one to three weeks late, and lists a pending decision on the payment provider with the product owner.

Gate: 04-041. Approval: none required

## 42
**Risk Management** (complete). Purpose: find, rank and handle the things that could harm the delivery or the business, before they happen.

Entry criteria: Project or program scope is defined; A risk owner role exists; A review rhythm is agreed

Inputs: plan and dependencies; past incidents and lessons; stakeholder concerns; assumption list

Procedure:
1. Identify risks with the team and stakeholders, writing each as cause, event and effect.
2. Rate likelihood and impact on a common scale, and rank by exposure.
3. Choose a response for each: avoid, reduce, transfer or accept, and say who decides on acceptance.
4. Assign an owner and a trigger for each risk, and plan the action to take if the trigger occurs.
5. Review the register on schedule, close the retired risks and add new ones.
6. Report the top risks and changes to the sponsor, with the decisions needed.

Deliverables: risk register; response plans with triggers; review records; top risk report

Acceptance: Each risk has cause, event, effect, owner and response Ranking uses a shared scale Triggers are defined for the top risks The register is reviewed on schedule

Validation: Program manager review; sponsor decision on accepted risks.

- manual: check each top-ten risk has an owner, a response and a trigger expect: none missing
- manual: check the register was reviewed within the agreed interval expect: review date within the interval

Failure modes:
- Risk written as a worry | detect: No clear event | respond: Rewrite as cause, event, effect
- No owner | detect: Risk never reviewed | respond: Assign
- Register never updated | detect: Old dates | respond: Review on schedule

ILLUSTRATIVE: A risk reads 'Because the vendor is the only supplier of the SDK, if they end support, the migration slips by three months'. The owner sets a trigger on the vendor's end-of-life notice and plans an alternative evaluation.

Gate: 04-042. Approval: none required

## 43
**Stakeholder Management** (stub). Purpose: align decision-makers and affected parties through the lifecycle.

Inputs: stakeholder and influence map; decision calendar; communication needs

Procedure:
1. Identify decision authority, affected users, veto points and information needs.
2. Set communication cadence and channel by stakeholder group.
3. Capture decisions, concerns, commitments and unresolved conflicts.
4. Escalate missing decisions before they block downstream work.

Deliverables: stakeholder map; communications plan; decision log

Acceptance: Every key decision has an owner and due date. Affected parties are informed before impact. Conflicts are resolved or explicitly escalated.

Validation: Sponsor and stakeholder review.

Gate: 04-043. Approval: none required

## 44
**Change Management** (complete). Purpose: control changes to systems and processes so each one is assessed, approved by the right person, scheduled and reversible.

Entry criteria: A change process and approval roles are defined; A record of the systems and owners exists; A change calendar is available

Inputs: change request; affected systems and owners; test and rollback evidence; change calendar

Procedure:
1. Record each change with what, why, who, systems affected and the planned time.
2. Classify by risk using the written criteria: standard (pre-approved), normal or emergency.
3. Assess the impact, including dependencies, users affected, test results and the rollback plan.
4. Route the request to the named human approver for its class; an agent prepares the pack but does not approve.
5. Check the calendar for clashes, apply the change in the approved window and record the outcome.
6. Review failed and emergency changes afterwards and feed the lessons back into the criteria.

Deliverables: change record with risk class; impact assessment and rollback plan; approval record with a human name; outcome and review notes

Acceptance: Each change has a risk class and a rollback plan A named human approved normal and emergency changes No clash on the calendar Failed changes were reviewed

Validation: Named change approver; emergency changes reviewed afterwards.

- manual: sample ten recent changes and check each has a risk class, rollback plan and approver name expect: all complete
- manual: compare production changes seen in deploy logs with change records expect: every deployment has a record

Failure modes:
- Changes made without a record | detect: Deploy log entry has no change | respond: Raise it as an incident and record retrospectively
- Approver is not a person | detect: Approval field names an agent | respond: Reject and obtain human approval
- Rollback never tested | detect: Rollback plan has no evidence | respond: Test it before approval

ILLUSTRATIVE: A database index change is classed as normal; the approver asks for the rollback script to be tested in staging, schedules it in the quiet window, and the outcome is recorded with the measured query time.

Gate: 04-044. Approval: change-board (always)
