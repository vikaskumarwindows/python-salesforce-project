# High-Level System Architecture

This document describes the high-level architecture of the Python & Salesforce integration platform.

---

## 1. System Context & Overview

The system acts as an integration bridge between local Python automation / data analytics workloads and Salesforce CRM (Sales Cloud, Service Cloud, custom objects).

```mermaid
flowchart TD
    subgraph Client["Python Application Environment"]
        App["Business Application / Scripts"]
        ClientLib["Salesforce Client Wrapper (src/salesforce_client.py)"]
        Env[".env Configuration / Secrets Store"]
        DataTransform["Data Transformation & Pandas Processor"]
    end

    subgraph Salesforce["Salesforce Platform"]
        AuthGateway["Salesforce Identity & OAuth 2.0 / SOAP Auth"]
        REST["Salesforce REST API (v60.0)"]
        BulkAPI["Salesforce Bulk API 2.0"]
        MetadataAPI["Metadata API / Tooling API"]
        DB[(Salesforce Standard & Custom Objects)]
    end

    App --> ClientLib
    ClientLib -. reads .-> Env
    ClientLib -->|1. Authenticate| AuthGateway
    ClientLib -->|2. SOQL / CRUD Requests| REST
    ClientLib -->|3. High-volume Batch Data| BulkAPI
    ClientLib -->|4. Inspect Schema| MetadataAPI
    REST --> DB
    BulkAPI --> DB
    REST -->|5. Query Results| DataTransform
    DataTransform --> App
```

---

## 2. Core Architectural Components

### 2.1 Configuration & Secret Management
- Local configurations are sourced from `.env` via `python-dotenv`.
- Production and automated CI/CD runners inject credentials via environment variables or secret vaults (e.g., AWS Secrets Manager, Azure Key Vault, or HashiCorp Vault).
- No sensitive keys or tokens are stored in source control (enforced via `.gitignore`).

### 2.2 Salesforce Client Wrapper
- Encapsulates authentication session lifecycle and re-authentication on token expiry.
- Provides unified abstraction across:
  - Standard REST API operations (record queries, inserts, updates, deletes).
  - Bulk API 2.0 queries and batch operations for large datasets (>10,000 records).
  - Raw SOQL query execution with automated pagination.

### 2.3 Data Transformation Engine
- Converts Salesforce JSON responses into typed Python models or `pandas.DataFrame` structures for ETL operations.
- Manages timezone normalization (Salesforce UTC timestamps to local application time) and nested relationship traversal (e.g., `Account.Owner.Name`).

---

## 3. Network & Connectivity Model

```mermaid
sequenceDiagram
    autonumber
    participant App as Python Application
    participant TokenEndpoint as Salesforce Login Endpoint
    participant REST as Salesforce REST API
    participant DB as Salesforce Database

    App->>TokenEndpoint: POST /services/oauth2/token (or SOAP login)
    TokenEndpoint-->>App: Access Token + Instance URL
    
    App->>REST: GET /services/data/v60.0/query?q=SELECT+Id,Name+FROM+Account
    REST->>DB: Execute SOQL
    DB-->>REST: Records
    REST-->>App: JSON response { records: [...], done: true }
```

---

## 4. Scalability & Performance Strategies

- **SOQL Query Optimization**: Always filter using indexed fields (`Id`, `ExternalId`, `CreatedDate`, `RecordType`).
- **Bulk API vs REST API**:
  - `< 2,000 records`: Synchronous REST API.
  - `> 2,000 records`: Asynchronous Bulk API 2.0 to minimize API limit consumption.
- **Connection Reuse**: Persist the `requests.Session` created by `simple-salesforce` to leverage HTTP keep-alive connections.
