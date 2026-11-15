# New product development

> Generated from `registry/workflows/new-product-development.json`. Edit the source, then run `python scripts/build.py`.

**Purpose.** The full journey from business problem to operated, continuously improved product.

**Trigger.** A business problem or product idea with no existing codebase.

## Entry criteria
- A named business sponsor
- A business problem statement

## Required inputs
- business_problem
- sponsor
- market_context

## Steps


| # | Stage | Owner (accountable or responsible) | Needs | Notes |
|---:|---|---|---|---|
| 1 | Business Strategy | `business-strategist` | - |  |
| 2 | Market Research | `market-research-analyst` | 1 |  |
| 3 | Client Engagement | `client-engagement-specialist` | 1 |  |
| 4 | Product Discovery | `product-manager` | 2, 3 |  |
| 5 | Business Analysis | `business-analyst` | 4 |  |
| 6 | Product Planning | `product-manager` | 5 |  |
| 7 | Feasibility Analysis | `solution-architect` | 6 |  |
| 8 | Budget & Estimation | `finops-specialist` | 7 |  |
| 9 | Project Approval | `product-manager` | 8 | approval: business-sponsor |
| 10 | Contract & Compliance | `compliance-specialist` | 9 | approval: legal-owner |
| 11 | Requirement Elicitation | `requirements-engineer` | 9 |  |
| 12 | Requirement Documentation | `requirements-engineer` | 11 |  |
| 13 | Functional Requirements | `requirements-engineer` | 12 |  |
| 14 | Non-Functional Requirements | `requirements-engineer` | 12 |  |
| 15 | User Research | `ux-researcher` | 4 |  |
| 16 | User Journey Mapping | `ux-researcher` | 15 |  |
| 17 | Wireframing | `ui-ux-designer` | 16, 13 |  |
| 18 | UI Design | `ui-ux-designer` | 17 |  |
| 19 | UX Design | `ui-ux-designer` | 17 |  |
| 20 | Prototype Development | `ui-ux-designer` | 18, 19 |  |
| 21 | Accessibility Review | `accessibility-testing-specialist` | 20 |  |
| 22 | Requirement Validation | `product-owner` | 13, 14, 21 |  |
| 23 | Solution Architecture | `solution-architect` | 22 |  |
| 24 | System Architecture | `software-architect` | 23 |  |
| 25 | Application Architecture | `software-architect` | 24 |  |
| 26 | Database Architecture | `database-architect` | 25 |  |
| 27 | API Architecture | `api-architect` | 25 |  |
| 28 | Cloud Architecture | `cloud-architect` | 24 |  |
| 29 | Security Architecture | `security-architect` | 24 |  |
| 30 | Data Architecture | `data-architect` | 25 |  |
| 31 | Integration Architecture | `integration-architect` | 24 |  |
| 32 | Technology Selection | `enterprise-architect` | 24 |  |
| 33 | Architecture Documentation | `technical-writer` | 26, 27, 28, 29, 30, 31, 32 |  |
| 34 | Architecture Review | `architecture-reviewer` | 33 |  |
| 35 | Project Initiation | `project-manager` | 9 |  |
| 36 | Resource Planning | `project-manager` | 35 |  |
| 37 | Work Breakdown | `project-manager` | 34 |  |
| 38 | Effort Estimation | `project-manager` | 37 |  |
| 39 | Sprint Planning | `scrum-master` | 38 |  |
| 40 | Agile Management | `agile-delivery-manager` | 39 |  |
| 41 | Progress Tracking | `agile-delivery-manager` | 39 |  |
| 42 | Risk Management | `program-manager` | 35 |  |
| 43 | Stakeholder Management | `program-manager` | 35 |  |
| 44 | Change Management | `engineering-governance-specialist` | 35 | approval: change-board |
| 45 | Repository Setup | `platform-engineer` | 34 |  |
| 46 | Branching Strategy | `engineering-governance-specialist` | 45 |  |
| 47 | Development Environment | `platform-engineer` | 34 |  |
| 48 | Coding Standards | `engineering-governance-specialist` | 32 |  |
| 49 | Environment Configuration | `devops-engineer` | 47 |  |
| 50 | Secrets Management | `devsecops-engineer` | 49 | approval: secrets-owner |
| 51 | Developer Documentation | `documentation-engineer` | 45, 47 |  |
| 52 | Engineering Governance | `engineering-governance-specialist` | 46, 48 |  |
| 53 | Frontend Development | `frontend-engineer` | 18, 27, 52 |  |
| 54 | Backend Development | `backend-engineer` | 25, 52 |  |
| 55 | Full Stack Development | `full-stack-engineer` | 52 |  |
| 56 | Mobile Development | `mobile-engineer` | 18, 27, 52 |  |
| 57 | API Development | `api-engineer` | 27, 52 |  |
| 58 | Database Development | `database-engineer` | 26, 52 |  |
| 59 | Authentication Development | `authentication-and-authorization-engineer` | 29, 52 |  |
| 60 | Authorization Development | `authentication-and-authorization-engineer` | 29, 52 |  |
| 61 | Third-party Integration | `integration-engineer` | 31, 52 |  |
| 62 | Real-time Development | `backend-engineer` | 25, 52 |  |
| 63 | Data Engineering | `data-engineer` | 30, 52 |  |
| 64 | AI/ML Development | `ai-ml-engineer` | 30, 52 |  |
| 65 | Caching & Optimization | `performance-engineer` | 25, 52 |  |
| 66 | Error Handling | `backend-engineer` | 25, 52 |  |
| 67 | Developer Testing | `full-stack-engineer` | 53, 54 |  |
| 68 | Pull Request Creation | `full-stack-engineer` | 67 |  |
| 69 | Peer Code Review | `code-reviewer` | 68 |  |
| 70 | Architecture Review | `architecture-reviewer` | 68 |  |
| 71 | Static Code Analysis | `devsecops-engineer` | 68 |  |
| 72 | Dependency Review | `devsecops-engineer` | 68 |  |
| 73 | Code Coverage Review | `code-reviewer` | 67 |  |
| 74 | Coding Standards Validation | `code-reviewer` | 68, 48 |  |
| 75 | Merge Approval | `merge-steward` | 69, 71, 72, 73, 74 | approval: code-owner |
| 76 | Technical Debt Review | `software-architect` | 71 |  |
| 77 | Test Strategy | `qa-lead` | 22, 34 |  |
| 78 | Test Planning | `qa-lead` | 77 |  |
| 79 | Unit Testing | `unit-testing-specialist` | 54 |  |
| 80 | Integration Testing | `integration-testing-specialist` | 78, 79 |  |
| 81 | API Testing | `api-testing-specialist` | 57, 78 |  |
| 82 | UI Testing | `automation-qa-engineer` | 53, 78 |  |
| 83 | Functional Testing | `manual-qa-engineer` | 78 |  |
| 84 | End-to-End Testing | `e2e-testing-specialist` | 78 |  |
| 85 | Regression Testing | `automation-qa-engineer` | 78 |  |
| 86 | Smoke Testing | `automation-qa-engineer` | 78 |  |
| 87 | Sanity Testing | `manual-qa-engineer` | 78 |  |
| 88 | Cross-browser Testing | `e2e-testing-specialist` | 78 |  |
| 89 | Mobile Compatibility Testing | `automation-qa-engineer` | 56, 78 |  |
| 90 | Accessibility Testing | `accessibility-testing-specialist` | 21, 78 |  |
| 91 | Performance Testing | `performance-testing-specialist` | 14, 78 |  |
| 92 | Load Testing | `performance-testing-specialist` | 14, 78 |  |
| 93 | Stress Testing | `performance-testing-specialist` | 14, 78 |  |
| 94 | Soak Testing | `performance-testing-specialist` | 14, 78 |  |
| 95 | UAT | `qa-lead` | 78 | approval: uat-acceptor |
| 96 | Defect Management | `qa-lead` | 79 |  |
| 97 | Test Sign-off | `qa-lead` | 96 |  |
| 98 | Threat Modeling | `security-architect` | 29 |  |
| 99 | SAST | `devsecops-engineer` | 54 |  |
| 100 | DAST | `devsecops-engineer` | 57 |  |
| 101 | SCA | `devsecops-engineer` | 54 |  |
| 102 | Container Security | `devsecops-engineer` | 115 |  |
| 103 | Infrastructure Security | `devsecops-engineer` | 117 |  |
| 104 | Penetration Testing | `penetration-testing-specialist` | 98 | approval: security-lead |
| 105 | Authentication Security | `application-security-engineer` | 59, 60 |  |
| 106 | Data Protection | `application-security-engineer` | 30 |  |
| 107 | Compliance Review | `compliance-specialist` | 10 |  |
| 108 | License Compliance | `license-compliance-specialist` | 101 | approval: compliance-owner |
| 109 | Vulnerability Remediation | `application-security-engineer` | 99, 100, 101 |  |
| 110 | Security Sign-off | `security-auditor` | 104, 109 | approval: security-lead |
| 111 | CI Pipeline | `devops-engineer` | 45 |  |
| 112 | Automated Test Pipeline | `devops-engineer` | 111, 78 |  |
| 113 | Build Management | `devops-engineer` | 111 |  |
| 114 | Artifact Management | `platform-engineer` | 113 |  |
| 115 | Containerization | `devops-engineer` | 113 |  |
| 116 | Container Orchestration | `kubernetes-engineer` | 115 |  |
| 117 | Infrastructure as Code | `infrastructure-engineer` | 28 | approval: infra-owner |
| 118 | Configuration Management | `platform-engineer` | 49 |  |
| 119 | CD Pipeline | `devops-engineer` | 111, 114 |  |
| 120 | Environment Provisioning | `infrastructure-engineer` | 117 |  |
| 121 | Network Engineering | `network-engineer` | 28 | approval: infra-owner |
| 122 | Database Operations | `database-administrator` | 26 |  |
| 123 | CDN & Edge Configuration | `platform-engineer` | 28 |  |
| 124 | Deployment Automation | `deployment-engineer` | 119 |  |
| 125 | Pipeline Security | `devsecops-engineer` | 119 |  |
| 126 | Release Planning | `release-manager` | 75 |  |
| 127 | Release Notes | `release-manager` | 126 |  |
| 128 | Release Readiness | `release-manager` | 97, 110, 126 |  |
| 129 | Change Approval | `release-manager` | 128, 137 | approval: change-board |
| 130 | Staging Deployment | `deployment-engineer` | 129, 124 |  |
| 131 | Staging Validation | `qa-lead` | 130 |  |
| 132 | Database Migration | `database-administrator` | 58, 147, 131 | approval: dba-owner |
| 133 | Production Deployment | `deployment-engineer` | 131, 132, 137 | approval: production-approver |
| 134 | Domain & DNS | `cloud-engineer` | 120 |  |
| 135 | SSL/TLS Setup | `network-engineer` | 134 |  |
| 136 | Load Balancer Setup | `network-engineer` | 121 |  |
| 137 | Rollback Planning | `release-manager` | 126 |  |
| 138 | Production Smoke Test | `sre` | 133 |  |
| 139 | Deployment Sign-off | `release-manager` | 138 |  |
| 140 | Cloud Hosting | `cloud-engineer` | 120 |  |
| 141 | Compute Management | `cloud-engineer` | 140 |  |
| 142 | Database Hosting | `database-administrator` | 140 |  |
| 143 | Storage Management | `cloud-engineer` | 140 |  |
| 144 | DNS Management | `network-engineer` | 134 |  |
| 145 | SSL Certificate Management | `cloud-engineer` | 135 |  |
| 146 | Network Operations | `network-engineer` | 121 |  |
| 147 | Backup Management | `database-administrator` | 122 |  |
| 148 | Disaster Recovery | `sre` | 147 | approval: dr-owner |
| 149 | High Availability | `cloud-architect` | 28 |  |
| 150 | Auto Scaling | `infrastructure-engineer` | 91, 92 |  |
| 151 | Cost Optimization | `finops-specialist` | 140 | approval: finops-owner |
| 152 | Infrastructure Maintenance | `infrastructure-engineer` | 140 |  |
| 153 | Application Monitoring | `observability-engineer` | 133 |  |
| 154 | Infrastructure Monitoring | `observability-engineer` | 140 |  |
| 155 | Centralized Logging | `observability-engineer` | 133 |  |
| 156 | Metrics Monitoring | `observability-engineer` | 133 |  |
| 157 | Distributed Tracing | `observability-engineer` | 133 |  |
| 158 | Alert Management | `sre` | 156 |  |
| 159 | Uptime Monitoring | `observability-engineer` | 133 |  |
| 160 | SLA/SLO Management | `sre` | 156 |  |
| 161 | Capacity Planning | `sre` | 156, 92 |  |
| 162 | Incident Detection | `incident-manager` | 158 |  |
| 163 | Incident Response | `incident-manager` | 162 |  |
| 164 | Root Cause Analysis | `sre` | 163 |  |
| 165 | Postmortem | `incident-manager` | 164 |  |
| 166 | Reliability Improvement | `sre` | 165 |  |
| 167 | L1 Support | `technical-support-engineer` | - |  |
| 168 | L2 Support | `production-support-engineer` | 167 |  |
| 169 | L3 Support | `backend-engineer` | 168 |  |
| 170 | Bug Fixing | `backend-engineer` | 169 |  |
| 171 | Patch Management | `devops-engineer` | 101 |  |
| 172 | Dependency Updates | `backend-engineer` | 101 |  |
| 173 | Database Maintenance | `database-administrator` | 122 | approval: dba-owner |
| 174 | Performance Optimization | `performance-engineer` | 91 |  |
| 175 | Technical Debt Reduction | `backend-engineer` | 76 |  |
| 176 | Feature Enhancement | `product-owner` | 177 |  |
| 177 | Customer Feedback | `product-manager` | 167 |  |
| 178 | Knowledge Base | `technical-writer` | 167 |  |
| 179 | Maintenance Release | `release-manager` | 170, 171 |  |
| 180 | Product Lifecycle Management | `product-manager` | 177 | approval: business-sponsor |
| 181 | Engineering Governance | `engineering-governance-specialist` | 52 |  |
| 182 | Quality Governance | `quality-governance-specialist` | 97 |  |
| 183 | Security Governance | `security-auditor` | 110 |  |
| 184 | Access Governance | `compliance-specialist` | 120 | approval: access-owner |
| 185 | Compliance Auditing | `security-auditor` | 107 |  |
| 186 | Documentation Governance | `documentation-engineer` | 33 |  |
| 187 | Change Governance | `engineering-governance-specialist` | 44 |  |
| 188 | Vendor Management | `vendor-management-specialist` | 10 |  |
| 189 | FinOps Governance | `finops-specialist` | 151 |  |
| 190 | Process Improvement | `process-improvement-specialist` | 181, 182, 165 |  |

## Parallel work
- Stages 1, 167
- Stages 2, 3, 168, 177, 178
- Stages 4, 169, 176, 180
- Stages 5, 15, 170
- Stages 6, 16
- Stages 10, 11, 35
- Stages 12, 36, 42, 43, 44, 107, 188
- Stages 13, 14, 185, 187
- Stages 18, 19
- Stages 25, 28, 29, 31, 32
- Stages 26, 27, 30, 48, 98, 117, 121, 123, 149
- Stages 33, 103, 104, 106, 120, 122, 136, 146

## Human approval points

| Stage | Approver | When |
|---:|---|---|
| 9 Project Approval | `business-sponsor` | always |
| 10 Contract & Compliance | `legal-owner` | always |
| 44 Change Management | `change-board` | always |
| 50 Secrets Management | `secrets-owner` | when rotating or revoking production secrets |
| 75 Merge Approval | `code-owner` | always |
| 95 UAT | `uat-acceptor` | always |
| 104 Penetration Testing | `security-lead` | always |
| 108 License Compliance | `compliance-owner` | when a license exception is requested |
| 110 Security Sign-off | `security-lead` | always |
| 117 Infrastructure as Code | `infra-owner` | before applying a plan to production; always when the plan destroys resources or changes IAM |
| 121 Network Engineering | `infra-owner` | for production firewall, security-group or routing changes |
| 129 Change Approval | `change-board` | always |
| 132 Database Migration | `dba-owner` | always |
| 133 Production Deployment | `production-approver` | always |
| 148 Disaster Recovery | `dr-owner` | always |
| 151 Cost Optimization | `finops-owner` | when resizing, deleting or committing spend on billing-sensitive resources |
| 173 Database Maintenance | `dba-owner` | for destructive or locking maintenance on production data |
| 180 Product Lifecycle Management | `business-sponsor` | always |
| 184 Access Governance | `access-owner` | when granting or widening privileged or break-glass access, or revoking access in bulk |

Rationale for each approval is in `docs/governance/APPROVAL_POLICY.md` and the stage's `approval_rationale`.

## Decision points
- After 9 - Is the business case approved? **yes** -> 11; **no** -> end
- After 34 - Is the architecture approved? **yes** -> 35; **no** -> 23
- After 97 - Is QA sign-off granted? **yes** -> 128; **no** -> 96
- After 110 - Is security sign-off granted? **yes** -> 128; **no** -> 109
- After 138 - Did the production smoke test pass? **yes** -> 139; **no** -> workflow:rollback

## Failure and remediation

| At stage | Condition | Action | Go to |
|---:|---|---|---|
| 22 | Requirements fail validation | Return to elicitation with the reviewer notes | 11 |
| 34 | Architecture review rejects the design | Revise architecture | 23 |
| 97 | Open critical defects at sign-off | Block release; return defects to engineering | 96 |
| 110 | Open critical security findings | Block release; remediate | 109 |

## Outputs
- approved_business_case
- validated_requirements
- architecture_document
- signed_off_release
- production_deployment_record
- runbooks_and_monitoring

## Exit criteria
- Business case approved
- Release passed QA and security sign-off with evidence
- Production verified by smoke test
- Operational handover artifacts exist
- Continuous-improvement backlog created

## Communication
Stage gate reviews at each phase boundary; status report per sprint.

## Hands off to
- [rollback](rollback.md)
- [application-maintenance](application-maintenance.md)

Any FAIL, BLOCKED or INCONCLUSIVE gate halts the steps that depend on it; see `orchestrator/` for the common failure policy.
