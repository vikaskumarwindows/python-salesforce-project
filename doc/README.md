# Project Documentation

Welcome to the documentation repository for the **Python Salesforce Project**.

This folder contains architectural guides, design documents, functional/technical specifications, and Architectural Decision Records (ADRs).

---

## 📂 Documentation Directory

| Directory | Purpose | Key Documents |
| :--- | :--- | :--- |
| [`architecture/`](./architecture/) | High-level system architecture, integrations, boundaries, and security models. | [`system-architecture.md`](./architecture/system-architecture.md), [`security-and-compliance.md`](./architecture/security-and-compliance.md) |
| [`design/`](./design/) | Low-level component design, module contracts, error handling, and data flow. | [`component-design.md`](./design/component-design.md), [`data-flow.md`](./design/data-flow.md) |
| [`spec/`](./spec/) | Specification containers (`<SPEC-Number - Spec Reason>/`) containing `Requirement.md`, `Implementation_plan.md`, `TDD.md`, `Scenario.md`, and optional `ADR-<Count>.md`. | [`SPEC-001 - Salesforce Baseline Integration/`](./spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/) |
| [`adrs/`](./adrs/) | Architectural Decision Records tracking decisions, alternatives, and rationale. | [`README.md`](./adrs/README.md), [`0001-record-architecture-decisions.md`](./adrs/0001-record-architecture-decisions.md), [`0002-salesforce-integration-library-selection.md`](./adrs/0002-salesforce-integration-library-selection.md) |
| [`templates/`](./templates/) | Standardized templates with driving discovery questionnaires for Specs, ADRs, and TDD plans. | [`SPEC_TEMPLATE.md`](./templates/SPEC_TEMPLATE.md), [`ADR_TEMPLATE.md`](./templates/ADR_TEMPLATE.md), [`TDD_TEMPLATE.md`](./templates/TDD_TEMPLATE.md) |

---

## 🛠️ Contribution Guidelines for Documentation

1. **Keep documentation updated alongside code changes**: Any PR that alters module boundaries, adds API integrations, or changes authentication patterns must include corresponding documentation updates.
2. **ADR First**: Significant design changes or technology additions (e.g., adding an asynchronous worker like Celery or switching to JWT bearer authentication) require a new ADR in [`adrs/`](./adrs/).
3. **Diagrams**: Use Markdown Mermaid diagrams (`flowchart`, `sequenceDiagram`) rather than static binary images for maintainability and version tracking.
