# Requirements and experience design: stage reference

## Contents
- [11 Requirement Elicitation](#11)
- [12 Requirement Documentation](#12)
- [13 Functional Requirements](#13)
- [14 Non-Functional Requirements](#14)
- [15 User Research](#15)
- [16 User Journey Mapping](#16)
- [17 Wireframing](#17)
- [18 UI Design](#18)
- [19 UX Design](#19)
- [20 Prototype Development](#20)
- [21 Accessibility Review](#21)
- [22 Requirement Validation](#22)

## 11
**Requirement Elicitation** (complete). Purpose: discover what stakeholders need by asking the right questions and recording their answers in a form others can check.

Entry criteria: Stakeholders are identified; The goal of the work is stated; Time with stakeholders is scheduled

Inputs: stakeholder list; business goals; existing documents and systems; interview guide

Procedure:
1. Identify stakeholders by role and influence, including users, operators, support and compliance, not only sponsors.
2. Prepare questions about goals, current process, pain, constraints and what success looks like.
3. Run interviews or workshops and record the answers in the stakeholders' words with the date.
4. Observe real work where possible, because what people do often differs from what they describe.
5. Write each need as a statement with its source, then play it back to the stakeholder to confirm.
6. List conflicts between stakeholders and unanswered questions, and send them to the decision maker.

Deliverables: stakeholder map; interview and workshop notes; confirmed need statements with sources; conflict and open question list

Acceptance: Each need names its source Needs were confirmed by the stakeholder Conflicts are recorded, not hidden Operations and support were asked

Validation: Product owner review.

- manual: sample five need statements and check each has a named source and confirmation date expect: all present
- manual: confirm operations and support roles appear in the stakeholder map expect: present

Failure modes:
- Only sponsors consulted | detect: Operators surprised later | respond: Add the missing roles
- Solutions recorded as needs | detect: Statements name technology | respond: Rewrite as outcomes
- Conflicts smoothed over | detect: Contradictory needs both listed as agreed | respond: Escalate to the decision maker

ILLUSTRATIVE: Interviews with sales and support show that agents need account history on one screen; sales wants a different priority. Both are recorded with sources, and the conflict goes to the product owner.

Gate: 02-011. Approval: none required

## 12
**Requirement Documentation** (complete). Purpose: write requirements so that each is clear, testable and traceable to a need, and the whole set can be reviewed and changed.

Entry criteria: Confirmed needs exist (stage 11); A template and identifier scheme exist; A reviewer is available

Inputs: confirmed need statements; business rules; existing requirements; glossary

Procedure:
1. Give every requirement a unique identifier, a single statement, a priority and the need it traces to.
2. Write in testable form: avoid vague words, state the condition, the actor and the measurable result.
3. Define terms in a glossary and use them the same way throughout.
4. Add acceptance criteria to each requirement as examples that a tester can run.
5. Review for duplicates, conflicts, gaps and untestable statements, and fix or log each finding.
6. Baseline the set and manage changes through a recorded request with impact.

Deliverables: requirements document with identifiers; glossary; traceability from need to requirement; review findings

Acceptance: Each requirement is unique, testable and traced Terms are defined once Conflicts and gaps are logged Changes follow a recorded process

Validation: Requirements review sign-off.

- manual: check every requirement id has a source need and at least one acceptance example expect: none missing
- `grep -rniE 'fast|user-friendly|easy|robust' docs/requirements | head` expect: no unmeasured vague words remain

Failure modes:
- Vague wording | detect: Tester cannot judge pass or fail | respond: Add a measure
- Orphan requirement | detect: No source need | respond: Trace it or remove it
- Conflicting statements | detect: Two requirements contradict | respond: Resolve with the owner

ILLUSTRATIVE: The statement 'the report should be fast' becomes 'the report for up to 10,000 rows is shown within 3 seconds at the 95th percentile', traced to the support team's need and given a test example.

Gate: 02-012. Approval: none required

## 13
**Functional Requirements** (complete). Purpose: state what the system must do in testable terms that stakeholders agree on.

Entry criteria: Business goals and stakeholders are identified; Scope boundary is drafted; Access to stakeholders exists

Inputs: business objectives and stakeholder input; existing processes and systems; regulatory and policy constraints; scope statement

Procedure:
1. Elicit needs from each stakeholder group through interviews, observation and existing documents.
2. Write each requirement as one verifiable statement of behavior with a unique id and a source.
3. Add acceptance criteria that a tester could check, including error and edge cases.
4. Resolve conflicts and duplicates with the stakeholders; record decisions and rejected requests.
5. Prioritize with the product owner and trace each requirement to a business objective.
6. Baseline the set and manage later changes through a recorded process.

Deliverables: requirements list with ids and sources; acceptance criteria; traceability to objectives; decision and change log

Acceptance: Each requirement is a single testable statement Each has a source and acceptance criteria Conflicts are resolved and recorded Stakeholders confirmed the baseline

Validation: Stakeholder review and product owner approval of the baseline.

- manual: ask a tester to write one test from each of five random requirements expect: tests can be written without questions
- manual: check each requirement traces to an objective expect: none orphaned

Failure modes:
- Vague requirement | detect: Words like fast or easy with no measure | respond: Quantify or split
- Requirement without a source | detect: No stakeholder named | respond: Find the source or remove
- Uncontrolled change | detect: Requirements differ from baseline without record | respond: Use the change process

ILLUSTRATIVE: The requirement says a signed-in user can export their orders as CSV within 30 seconds for up to 10,000 orders, with an error message if the limit is exceeded; a tester writes three tests from it.

Gate: 02-013. Approval: none required

## 14
**Non-Functional Requirements** (complete). Purpose: state how well the system must perform, protect and operate, in measurable terms that design and test can use.

Entry criteria: Functional scope is known; Business and operating context is known; Regulatory constraints are listed

Inputs: functional requirements; usage forecasts; regulatory and security obligations; operating model

Procedure:
1. Cover the main quality areas: performance, availability, security, privacy, usability, maintainability, portability and recoverability.
2. For each area write a measurable target with the conditions, such as load, data size and time window.
3. Base the targets on usage forecasts and obligations, and mark each as required or desirable.
4. Check for conflicts between targets and with cost, and agree the trade-offs with the sponsor.
5. Say how each will be verified: load test, failover test, audit or review.
6. Feed the targets to architecture, test planning and monitoring.

Deliverables: quality requirements with targets; verification method per target; trade-off decisions; links to test and monitoring plans

Acceptance: Each target is measurable with its conditions Each has a verification method Conflicts and trade-offs are decided Targets reach the test and monitoring plans

Validation: Architect and product owner agreement.

- manual: check each non-functional requirement has a number, a condition and a verification method expect: none missing
- manual: check each target appears in the test or monitoring plan expect: all appear

Failure modes:
- Targets without numbers | detect: Words like robust | respond: Replace with measures
- Impossible combination | detect: Availability target needs more cost than budget | respond: Agree trade-off
- Targets never tested | detect: No verification plan | respond: Add tests or monitoring

ILLUSTRATIVE: Availability of 99.9 percent per month for checkout, recovery within 30 minutes and p95 under 400 ms at 200 requests per second are agreed, each tied to a load or failover test.

Gate: 02-014. Approval: none required

## 15
**User Research** (complete). Purpose: understand users' real behavior, goals and difficulties through research, and turn it into findings the design can use.

Entry criteria: A user group and research question are defined; Access to participants is available; Consent and privacy rules are agreed

Inputs: research questions; participants; existing analytics and support data; consent process

Procedure:
1. Write the research questions and choose methods that fit them: interviews, observation, diary study, survey or usability test.
2. Recruit participants who match the real user groups, including less technical and assistive-technology users.
3. Get consent, explain how data is used and stored, and keep personal data to the minimum needed.
4. Run the sessions, record what people did and said, and avoid leading questions.
5. Analyze across participants, and report patterns with the number of people who showed each one.
6. Share findings as problems and opportunities with evidence, and note the limits of the sample.

Deliverables: research plan; consent records; session notes; findings with counts and limits

Acceptance: Participants match real user groups Consent was obtained and recorded Findings state how many people showed each pattern Limits of the sample are stated

Validation: UX lead review.

- manual: check each participant has a consent record and each finding shows a count expect: complete
- manual: check recruitment included at least one participant using assistive technology expect: yes, or reason given

Failure modes:
- Findings from one person generalized | detect: No counts | respond: Show counts and caution
- Leading questions | detect: Participants echo the facilitator | respond: Revise the guide
- Personal data kept too long | detect: Raw recordings retained | respond: Delete per the retention rule

ILLUSTRATIVE: Eight users are observed filing an expense claim. Five miss the receipt upload button; the report gives the count of five of eight, notes that all were in one department, and recommends testing with others.

Gate: 02-015. Approval: none required

## 16
**User Journey Mapping** (complete). Purpose: describe how real users move through a goal across steps and channels, so design effort goes to the real pain points.

Entry criteria: A target user group and a goal are chosen; Research access exists (interviews, analytics or support data); Service owner is available to validate

Inputs: user research and interview notes; analytics and support data; current process description; personas or user segments

Procedure:
1. Choose one user goal and the start and end of the journey.
2. List the steps users take across channels, with what they think, feel and do, using research rather than assumption.
3. Mark pain points and drop-off points with the evidence for each.
4. Walk through the map with users and the service owner and correct it.
5. Rank opportunities by user impact and effort and link them to requirements.
6. Record the sources and confidence for each claim.

Deliverables: journey map; pain-point list with evidence; ranked opportunities; source and confidence notes

Acceptance: Every pain point cites evidence The map was validated with users or the owner Opportunities link to requirements Assumptions are marked as assumptions

Validation: Walkthrough with users and service owners.

- manual: for each pain point, open the cited source and confirm it supports the claim expect: all supported or marked as assumption
- manual: ask two users to read the map and say where it is wrong expect: corrections recorded

Failure modes:
- Map built from internal opinion | detect: No sources cited | respond: Gather evidence or mark as hypothesis
- Only the happy path mapped | detect: No failure or abandonment steps | respond: Add where users give up
- Map never used | detect: No opportunity links to requirements | respond: Connect to the backlog or retire the map

ILLUSTRATIVE: Support tickets and interviews show new users abandon sign-up at the identity-check step. The map marks that step, ranks a simpler check as the top opportunity, and links it to a requirement.

Gate: 02-016. Approval: none required

## 17
**Wireframing** (complete). Purpose: sketch screens and structure early and cheaply, so the layout and flow can be judged before visual design or code.

Entry criteria: Key user flows exist; Requirements for the screens are known; Reviewers from product and engineering are available

Inputs: user flows; requirements and content list; device and breakpoint targets; design system components

Procedure:
1. List the content and actions each screen must hold, ordered by priority for the user's task.
2. Sketch low-fidelity layouts with boxes and labels, without colour or final images, so discussion is about structure and flow.
3. Show navigation, the main call to action, and all key states: empty, loading, error and filled.
4. Annotate behavior that is not visible: validation, conditional fields, permissions and what each action does.
5. Review with a developer for feasibility and with a few users or colleagues on a task, and record what confused them.
6. Revise and save the approved version with its annotations as the input to UI design.

Deliverables: wireframes for each screen and key state; annotations of behavior; review notes; approved version

Acceptance: Each screen shows its priority content and primary action Key states are drawn Behavior is annotated A task review was done and recorded

Validation: UX lead and product owner review.

- manual: ask a reviewer to complete the main task on the wireframes without help and note where they hesitate expect: hesitations recorded and addressed
- manual: check each screen has empty, loading and error states expect: none missing

Failure modes:
- Wireframes drift into visual design | detect: Debate about colours | respond: Keep low fidelity
- States missing | detect: Developers invent error screens | respond: Add the states
- No task test | detect: Layout liked but not usable | respond: Test with a task

ILLUSTRATIVE: Wireframes for a settings area show the save action, an inline error state and a read-only view for users without permission. A reviewer cannot find where to change the email, so the section is renamed and moved up.

Gate: 02-017. Approval: none required

## 18
**UI Design** (complete). Purpose: design the visible interface so people can recognize, read and operate it correctly, consistently across the product.

Entry criteria: Requirements and flows exist; A design system or style foundation exists or is planned; Brand constraints are known

Inputs: user flows and wireframes; design system or tokens; brand guidelines; accessibility requirements

Procedure:
1. Use the design system components and tokens first, and add new ones only when no existing one fits.
2. Set layout, spacing and hierarchy so the main action on each screen is clear.
3. Design every state: empty, loading, error, success and disabled, not only the filled state.
4. Check text size, contrast and touch target size against the accessibility requirements.
5. Check the designs at the supported screen sizes and with long and translated text.
6. Hand over specifications and assets with named components, so engineers do not redraw them.

Deliverables: screen designs with all states; new component specifications; handover assets; contrast and size check

Acceptance: All states are designed Components come from the design system or are specified Contrast and size meet requirements Designs hold at supported sizes and long text

Validation: Design lead review and accessibility check.

- manual: check each screen has empty, loading, error and success states expect: all present
- manual: measure text contrast of the main text and controls against the required ratio expect: all meet

Failure modes:
- Only the happy state designed | detect: Engineers invent error screens | respond: Add all states
- New component for every screen | detect: System bloats | respond: Reuse or extend
- Low contrast text | detect: Check fails | respond: Adjust tokens

ILLUSTRATIVE: A settings screen uses the standard form components, adds an inline error state and a disabled save button, and the grey helper text is darkened to meet the contrast ratio.

Gate: 02-018. Approval: none required

## 19
**UX Design** (complete). Purpose: shape the whole experience of a task so that users can finish it with little effort, by structuring flows, content and feedback.

Entry criteria: Research findings exist (stage 15); Key tasks are identified; Success measures for the tasks are defined

Inputs: research findings; key tasks; information needs; current flow analytics

Procedure:
1. Describe the key tasks as flows from start to finish, including where users arrive from and what they do next.
2. Reduce steps and decisions: remove unneeded fields, set sensible defaults and show only what is relevant.
3. Organize content and navigation around the words and groupings users use, and test them with a card sort or a tree test.
4. Design feedback for every action and every failure, with messages that say what happened and what to do.
5. Test the flows with real users using prototype tasks, and measure completion, time and errors.
6. Revise and record the changes with the evidence that drove them.

Deliverables: task flows; information structure tested with users; message and feedback copy; usability test results

Acceptance: Key tasks have measured completion and error rates Navigation was tested with users Errors say what to do next Changes link to evidence

Validation: UX lead review.

- manual: check each key task has a completion rate from a test with at least five participants expect: recorded
- manual: read every error message and check it states cause and next step expect: all do

Failure modes:
- Flow has too many steps | detect: Users drop at step four | respond: Remove or combine steps
- Labels use internal words | detect: Users cannot find items | respond: Use users' words
- Opinion over evidence | detect: Changes not linked to tests | respond: Test and record

ILLUSTRATIVE: A booking flow of seven steps is reduced to four by defaulting known details; a test with six users shows five complete it unaided, and error text now tells the user how to correct a date.

Gate: 02-019. Approval: none required

## 20
**Prototype Development** (complete). Purpose: build a testable model of an idea quickly and cheaply, to learn before the real build.

Entry criteria: A question to answer is defined; Flows or screens to test exist; Test participants are available

Inputs: design flows; the question the prototype must answer; test participants; design system

Procedure:
1. State the question the prototype is meant to answer and the tasks users will do.
2. Choose the lowest fidelity that can answer it: paper, clickable screens or a coded spike.
3. Build only the paths needed for the tasks, with realistic content, not placeholders.
4. Test with real users, observe where they hesitate or fail, and record it.
5. Decide what to change, drop or build, and note what the prototype could not tell you.
6. Label the prototype as throwaway unless it has been reviewed for production.

Deliverables: prototype; test script and tasks; observations and decisions; list of what was not tested

Acceptance: The prototype answers a stated question Realistic content was used Findings drive decisions Production use needs a separate review

Validation: Design lead review.

- manual: check the prototype test report names the question and the decision it supports expect: present
- manual: confirm the prototype is labelled throwaway or reviewed for production expect: labelled

Failure modes:
- Prototype becomes production by accident | detect: No review | respond: Label and review before reuse
- Too high fidelity | detect: Weeks spent polishing | respond: Use lower fidelity
- No question defined | detect: Findings not actionable | respond: State the question first

ILLUSTRATIVE: A clickable prototype of a new onboarding flow is tested with six users in two days; four stall at identity verification, so the team redesigns that step before any code is written.

Gate: 02-020. Approval: none required

## 21
**Accessibility Review** (complete). Purpose: check that people with disabilities can use the product, by testing against standards and with assistive technology.

Entry criteria: Screens or a working build exist; The target standard and level are chosen; Assistive technology is available for testing

Inputs: designs or build; accessibility standard and target level; assistive technologies in scope; known issues

Procedure:
1. Run automated checks first to catch the easy failures, and fix them.
2. Test keyboard use: every function reachable, visible focus, logical order and no traps.
3. Test with a screen reader on the main tasks, checking names, roles, labels and announcements.
4. Check contrast, text resizing, zoom, motion and use of colour as the only signal.
5. Record each issue with the standard criterion, severity, location and the fix.
6. Retest fixes and report the remaining issues with owners and dates.

Deliverables: test report by criterion; issue list with severity; retest results; remaining issues with owners

Acceptance: Automated and manual checks both ran Main tasks work with keyboard and screen reader Each issue cites a criterion and severity Remaining issues have owners and dates

Validation: Accessibility specialist sign-off.

- `npx --no-install pa11y http://localhost:3000   # example; use the project's checker and URL` expect: no errors reported on tested pages
- manual: complete the main task using only the keyboard and again with a screen reader expect: task completed without help

Failure modes:
- Automated pass treated as compliance | detect: Manual problems remain | respond: Do the manual tests
- Focus not visible | detect: Keyboard users lose position | respond: Add a visible focus style
- Fixes untested | detect: Issues reopened | respond: Retest every fix

ILLUSTRATIVE: Automated checks find missing form labels; a keyboard test finds a modal that traps focus; a screen reader test finds an unlabeled icon button. All three are logged with criteria and fixed, then retested.

Gate: 02-021. Approval: none required

## 22
**Requirement Validation** (complete). Purpose: confirm with the right people that the written requirements are correct, complete, consistent and testable before design and build rely on them.

Entry criteria: Requirements are documented with identifiers (stage 12); Stakeholders and a product owner are available; Acceptance criteria exist for the requirements

Inputs: requirements document; business goals and rules; stakeholder list; traceability to needs

Procedure:
1. Check each requirement against the quality attributes: necessary, unambiguous, testable, consistent, feasible and traceable to a need.
2. Check the set for gaps against the process models and the goals, and for conflicts between requirements and with the rules.
3. Walk the stakeholders through scenarios built from the requirements, and record where the scenario does not match their expectations.
4. Review with developers and testers: can it be built and can each criterion be tested.
5. Log each finding with the requirement id, the problem and the decision, and update the requirements.
6. Have the product owner approve the validated baseline in writing and set the change process from then on.

Deliverables: review findings log; scenario walkthrough notes; updated requirements baseline; product owner approval

Acceptance: Every requirement was checked against the named attributes Gaps and conflicts are logged with decisions Testers and developers reviewed it The product owner approved the baseline

Validation: Product owner approval of the baseline.

- manual: check every requirement id has a source need, an acceptance criterion and a review result expect: none missing
- manual: trace three goals to the requirements that satisfy them expect: all traced

Failure modes:
- Approval without review | detect: No findings log | respond: Perform the review
- Conflict found late | detect: Two requirements contradict in design | respond: Resolve with the owner and record
- Untestable requirement | detect: Tester cannot judge pass or fail | respond: Rewrite with a measure

ILLUSTRATIVE: A walkthrough of the refund scenario shows two requirements give different time limits. The owner decides on 30 days, both are corrected, and the baseline is approved with the finding logged.

Gate: 02-022. Approval: none required
