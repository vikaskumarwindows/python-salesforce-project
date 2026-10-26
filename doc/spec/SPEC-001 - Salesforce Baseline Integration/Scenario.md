# SPEC-001: QA Test Scenarios & Edge Cases

- **Specification ID**: SPEC-001
- **Reason / Title**: Salesforce Baseline Integration & SOQL Query Pipeline

---

## 1. End-to-End QA Test Scenarios

### Scenario QA-01: First-Time Initialization Smoke Test
- **Preconditions**: `.env` file copied from `.env.example` with valid Sandbox credentials.
- **Execution**:
  ```powershell
  .venv\Scripts\python.exe src/salesforce_client.py
  ```
- **Expected Outcome**:
  - Console outputs: `Connecting to Salesforce...`
  - Successfully authenticates and prints: `Successfully authenticated! Connected to Salesforce instance: ...`
  - Executes `SELECT Id, Name FROM Organization` and prints connected organization name.
  - Process exits with code 0.

### Scenario QA-02: Missing Environment Configuration
- **Preconditions**: No `.env` file present and no environment variables set.
- **Execution**:
  ```powershell
  .venv\Scripts\python.exe src/salesforce_client.py
  ```
- **Expected Outcome**:
  - Script catches `ValueError`: `Missing Salesforce credentials! Please copy '.env.example' to '.env' and set SALESFORCE_USERNAME and SALESFORCE_PASSWORD.`
  - No uncaught stack traces or password dumps.

### Scenario QA-03: Invalid Credentials / Expired Security Token
- **Preconditions**: `.env` contains invalid password or token.
- **Execution**:
  ```powershell
  .venv\Scripts\python.exe src/salesforce_client.py
  ```
- **Expected Outcome**:
  - Logs `Connection failed: ... [INVALID_LOGIN]`.
  - Credentials remain unprinted.

---

## 2. Boundary & Negative Scenarios

- [x] **Rate Limit / Concurrent Request Exhaustion**: Must handle HTTP 429 / 503 without unhandled crashes.
- [x] **Network Drop**: Timeouts must return explicit error message rather than hanging indefinitely.
