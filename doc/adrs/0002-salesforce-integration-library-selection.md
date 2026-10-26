# ADR 0002: Selection of `simple-salesforce` and `python-dotenv`

- **Status**: Accepted
- **Deciders**: Engineering Team
- **Date**: 2026-10-27

---

## Context and Problem Statement

The application requires an idiomatic, stable Python interface to interact with Salesforce APIs (REST, Bulk API 2.0, SOQL query pagination, and schema metadata). We need to choose an API client library and credential management strategy.

---

## Decision Drivers

- Support for standard Salesforce authentication methods (Username/Password/Token, Connected App OAuth2, JWT Bearer).
- Automatic SOQL query pagination handling.
- Active maintenance, community adoption, and compatibility with modern Python versions (3.10+ / 3.15).
- Clean separation of secrets from code.

---

## Considered Options

1. **`simple-salesforce` + `python-dotenv`**
2. **Custom REST Wrapper using raw `requests`**
3. **`salesforce-bulk` (Legacy)**

---

## Decision Outcome

Chosen option: **`simple-salesforce` + `python-dotenv`**.

### Positive Consequences
- **`simple-salesforce`**:
  - The industry-standard Python client for Salesforce.
  - Native support for REST, Bulk API 2.0, Tooling API, and automatic query pagination (`query_all`).
  - Supports custom domains and sandbox switching seamlessly.
- **`python-dotenv`**:
  - Automatically loads `.env` files for local development.
  - Zero interference in cloud / CI/CD environments where real environment variables are injected.

### Negative Consequences
- `simple-salesforce` uses synchronous HTTP (`requests`); async HTTP (`aiohttp` / `httpx`) would require threading or external wrapping if high concurrency is required in the future.
