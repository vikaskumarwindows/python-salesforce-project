# Architecture Decision Records (ADRs)

Architecture Decision Records (ADRs) document important architectural choices made during the development of this project, along with their context, trade-offs, and consequences.

---

## 📋 ADR Index

| ADR Number | Title | Status | Date |
| :--- | :--- | :--- | :--- |
| [0001](./0001-record-architecture-decisions.md) | Record Architecture Decisions (MADR standard) | Accepted | 2026-10-27 |
| [0002](./0002-salesforce-integration-library-selection.md) | Selection of `simple-salesforce` and `python-dotenv` | Accepted | 2026-10-27 |

---

## 📝 ADR Template

When authoring a new ADR, copy the following structure into `doc/adrs/NNNN-<decision-title>.md`:

```markdown
# ADR NNNN: [Title of Decision]

- **Status**: [Proposed | Accepted | Superseded | Deprecated]
- **Deciders**: [List of participants]
- **Date**: [YYYY-MM-DD]

## Context and Problem Statement
[Describe the problem, requirements, and constraints that led to this decision.]

## Decision Drivers
* [Driver 1, e.g., security, API quota limits, speed to market]
* [Driver 2]

## Considered Options
1. [Option 1]
2. [Option 2]
3. [Option 3]

## Decision Outcome
Chosen option: "[Option X]", because [justification].

### Positive Consequences
* [Advantage 1]
* [Advantage 2]

### Negative Consequences
* [Trade-off 1]
* [Trade-off 2]

## Pros and Cons of Options
[Detailed breakdown of alternatives]
```
