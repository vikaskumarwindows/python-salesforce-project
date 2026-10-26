# ADR 0001: Record Architecture Decisions

- **Status**: Accepted
- **Deciders**: Engineering Team
- **Date**: 2026-10-27

---

## Context and Problem Statement

As this Salesforce and Python codebase evolves with multiple integrations, authentication methods, and data handling requirements, we need a lightweight, auditable way to track significant design and architectural decisions. Without documentation, the rationale behind past decisions is easily lost.

---

## Decision Drivers

- Maintain architectural transparency across team members and contributors.
- Keep documentation close to code in Git for revision control.
- Avoid overhead of external, disconnected wikis.

---

## Considered Options

1. **Architecture Decision Records (ADRs) using Markdown in Git**
2. **External Wiki (e.g. Confluence / Notion)**
3. **Commit Messages & Pull Request Descriptions Only**

---

## Decision Outcome

Chosen option: **Architecture Decision Records (ADRs) in Git** under `doc/adrs/`.

### Positive Consequences
- Architecture decisions are versioned alongside the code they affect.
- Pull requests can include the ADR and code changes in a single review.
- Easy to search, read offline, and inspect in any IDE or GitHub.

### Negative Consequences
- Requires discipline to write and review ADRs during major architectural shifts.
