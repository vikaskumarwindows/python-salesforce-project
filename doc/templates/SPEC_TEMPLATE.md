# Template: Business Specification & Agent/Skill Generator

> **Instructions**: Use this template to document business domain requirements and define how autonomous AI agents and specialized skills will execute the workflow.

---

# SPEC-XXXX: [Business Feature / Agent Skill Name]

- **Status**: [ Draft | In Review | Approved | Implemented ]
- **Author**: [Product Manager / Business Analyst / Engineer]
- **Target Release**: [e.g., v0.2.0]
- **Date**: [YYYY-MM-DD]
- **Assigned Agent / Skill Type**: [e.g., `salesforce-sync-agent`, `soql-report-skill`]

---

## ❓ Business Process Discovery Questionnaire

*Answer these questions to understand the current operational reality and establish business context before defining automation:*

### 1. How Does the Business Currently Run This Process?
- **Current Operational Workflow**:
  - *Is it currently performed manually by humans (e.g., spreadsheet export/import), scheduled via cron jobs, or triggered by an external event?*
  - [Answer here]
- **Frequency & Volume**:
  - *How often does this occur (real-time, hourly, daily, end-of-month)? How many records/transactions are processed per run?*
  - [Answer here]
- **Pain Points & Bottlenecks**:
  - *Why are we automating or rebuilding this? (e.g., human error, sync delays, rate limit violations, lack of auditability).*
  - [Answer here]

### 2. Personas & Stakeholders
- **Primary Business Users**:
  - *Who relies on the outcome of this process? (e.g., Sales Ops, Finance, Customer Success, System Admins).*
  - [Answer here]
- **Consumer Systems**:
  - *Which downstream databases, BI dashboards, ERP systems, or notification channels receive the results?*
  - [Answer here]

### 3. Salesforce Data Domain & Business Rules
- **Target Objects & Fields**:
  - *Which standard objects (`Account`, `Contact`, `Opportunity`) or custom objects (`Invoice__c`, `Sync_Log__c`) are touched?*
  - [Answer here]
- **Business Validation & Life Cycle Rules**:
  - *What validation rules, required fields, or stage transitions must be respected? (e.g., `StageName` cannot jump directly to `Closed Won` without a valid `CloseDate`).*
  - [Answer here]

### 4. SLAs, Errors, and Escalation
- **Service Level Agreements (SLAs)**:
  - *What is the maximum acceptable latency or execution time window?*
  - [Answer here]
- **Failure Protocols & Human Escalation**:
  - *What happens when a record fails validation or an API call drops? Who is notified, and how is the error recovered?*
  - [Answer here]

---

## 🤖 Agent & Skill Specification

*Define the personality, role, instructions, and tools for the autonomous agent or specialized skill executing this specification:*

### 1. Agent Definition

```yaml
Name: "salesforce-operations-agent"
Role: "Automated Salesforce Data Integration Specialist"
Objective: "Extract, validate, and synchronize customer account records between local datasets and Salesforce CRM without violating API limits or data integrity."
```

### 2. System Prompt & Behavioral Instructions

```markdown
You are an autonomous Salesforce integration agent. Your responsibilities are:
1. Always validate credentials against environment variables; never hardcode credentials.
2. Ensure all SOQL queries specify exact fields and avoid unindexed full-table scans.
3. Automatically check Salesforce daily API quotas before initiating batch runs.
4. If an individual record fails upsert, log the failure reason with record External ID and continue processing remaining records.
5. Report a final execution summary including total processed, succeeded, failed, and execution time.
```

### 3. Required Tools & Agent Capabilities
- [ ] **SOQL Query Tool**: Ability to execute read queries with pagination.
- [ ] **Record Upsert Tool**: Ability to perform idempotently using Salesforce External IDs.
- [ ] **Data Transformation Tool**: Ability to clean and map local data to Salesforce field types.
- [ ] **Audit Logger Tool**: Ability to output execution logs and metrics.

### 4. Safety Guardrails & Prohibitions
- **PROHIBITED**: Deleting records (`DELETE` operations) without explicit human confirmation.
- **PROHIBITED**: Executing operations in Salesforce Production (`login.salesforce.com`) without a validated Sandbox run.
- **PROHIBITED**: Logging customer passwords, tokens, or unmasked PII.

---

## 📋 Functional Requirements (FR)

| ID | Requirement Description | Priority | Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| **FR-01** | Connect securely to target Salesforce environment using environment variables. | Critical | Agent authenticates without prompting for passwords or storing plaintext secrets. |
| **FR-02** | Query target records matching business criteria. | High | Returns exact dataset matching SOQL filter criteria with all relationship fields flattened. |
| **FR-03** | Idempotent Record Upsert. | High | Running the process multiple times with the same input yields identical state without duplicates. |
| **FR-04** | Execution Telemetry & Error Summary. | Medium | Generates structured summary report (JSON/Markdown) detailing successes and failures. |

---

## 🔄 Downstream Handoff Checklist

- [ ] **Architecture**: Is an ADR required for this feature? If yes, author `doc/adrs/NNNN-[title].md` using [ADR_TEMPLATE.md](./ADR_TEMPLATE.md).
- [ ] **Test Plan**: Has a Technical Design & QA Test Plan been authored using [TDD_TEMPLATE.md](./TDD_TEMPLATE.md)?
- [ ] **Codebase Map**: Update `CODEBASE_MAP.md` once development begins.
