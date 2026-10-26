# Template: Technical Design & QA Test Scenarios (TDD)

> **Instructions**: Use this template to design technical code changes and define the QA test scenarios, verification matrices, and edge-case behaviors before implementation begins.

---

# TDD-XXXX: [Feature / Module Technical Design & Test Plan]

- **Status**: [ Draft | Approved | In Testing | Verified ]
- **Author**: [Developer / Agent]
- **Target Spec**: [Link to Spec, e.g., `doc/spec/001-salesforce-integration-spec.md`]
- **Related ADR**: [Link to ADR, e.g., `doc/adrs/0002-salesforce-integration-library-selection.md`]
- **Date**: [YYYY-MM-DD]

---

## ❓ QA & Technical Driving Questions

*Answer these questions to uncover edge cases, test requirements, and operational pitfalls before writing code:*

1. **What code and schema changes are being introduced?**
   - *Which Python files, classes, methods, or Salesforce objects/fields are added or altered?*
   - [Answer here]

2. **How does QA independently verify this feature end-to-end?**
   - *What step-by-step actions can a QA tester or automated script take to prove it works?*
   - [Answer here]

3. **What happens during network degradation or Salesforce outages?**
   - *What error codes (e.g., 503 Service Unavailable, 401 Unauthorized, 429 Limit Exceeded) must be tested?*
   - [Answer here]

4. **What are the data boundary conditions and invalid input states?**
   - *Empty lists, null fields, malformed SOQL syntax, duplicates, special characters in string fields?*
   - [Answer here]

5. **What test fixtures, mocks, or sandbox configurations are required?**
   - *Do we need unit test mocks (`unittest.mock`, `responses`) or a live Salesforce Developer Org / Scratch Org?*
   - [Answer here]

---

## 1. Technical Change Summary

### 1.1 Python Modules Affected
| Module / File | Change Type | Description of Change |
| :--- | :--- | :--- |
| `src/salesforce_client.py` | Modify | Add session renewal and exponential backoff retry wrapper. |
| `src/query_runner.py` | New | Implement paginated SOQL execution and Pandas DataFrame transformation. |
| `tests/test_query_runner.py` | New | Comprehensive unit tests with mocked Salesforce HTTP payloads. |

### 1.2 Data Schema & External Contract Changes
- **Salesforce Objects / Fields**: [e.g., `Account.External_Id__c`, `Contact.Email`]
- **API Version**: [e.g., `v60.0`]
- **Environment Variables**: [e.g., new `SALESFORCE_TIMEOUT_SECONDS`]

---

## 2. Test-Driven Development (TDD) Test Scenarios

### 2.1 Unit Test Scenarios (Mocked - No External Network)

| Test ID | Scenario Description | Inputs / Setup | Expected Outcome |
| :--- | :--- | :--- | :--- |
| **UT-01** | Successful authentication initialization | Valid dummy credentials in env | Client instance returned with target domain set. |
| **UT-02** | Missing credentials failure | `SALESFORCE_USERNAME` unset | Raises `ValueError` with descriptive message. |
| **UT-03** | Auto-pagination handling | Mocked HTTP 200 with `nextRecordsUrl` | Follows pagination link and merges record lists. |
| **UT-04** | Transient 429 Rate Limit error | Mock 429 response followed by 200 | Retries after exponential backoff delay; succeeds. |
| **UT-05** | Malformed SOQL response | Mock HTTP 400 `MALFORMED_QUERY` | Catches `SalesforceMalformedRequest` without crashing. |

---

### 2.2 Integration Test Scenarios (Salesforce Sandbox / Scratch Org)

| Test ID | Scenario Description | Preconditions | Steps | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| **IT-01** | Live Org metadata inspection | Active sandbox credentials | Call `sf.describe()` on standard `Account` object. | Returns valid object metadata schema. |
| **IT-02** | Live SOQL query execution | Pre-seeded test records | Query `SELECT Id, Name FROM Account LIMIT 5`. | Returns dictionary with `totalSize >= 1` and `records`. |
| **IT-03** | Upsert via External ID | Test record with unique External ID | Upsert record twice with updated description. | 1st call creates record; 2nd call updates in place. |

---

### 2.3 QA Manual & Exploratory Test Scenarios

```text
Scenario QA-01: Invalid Password or Expired Security Token
Preconditions: .env contains an incorrect security token.
Execution:
  1. Run: python -m src.salesforce_client
Expected Result:
  - System logs an explicit authentication error ("INVALID_LOGIN").
  - Process exits cleanly with non-zero exit code.
  - Credentials are NEVER printed in the console or logs.
```

```text
Scenario QA-02: Large Dataset Pagination (> 2,000 Records)
Preconditions: Salesforce sandbox contains > 2,500 Contact records.
Execution:
  1. Execute query_all("SELECT Id, Email FROM Contact")
Expected Result:
  - Client retrieves first 2,000 records.
  - Automatically fetches remaining records via nextRecordsUrl.
  - Returned dataset length matches totalSize reported by Salesforce.
```

---

## 3. Regression & Security Scenarios

- [ ] **No Secret Leakage**: Verify no stdout logs, exception tracebacks, or file artifacts contain `password`, `security_token`, or `client_secret`.
- [ ] **Salesforce API Limit Verification**: Verify API consumption via `sf.limits()` before and after test execution to ensure no quota overrun.
- [ ] **Cross-Platform Path Validation**: Verify script executes identically on Windows PowerShell and Linux/macOS bash.

---

## 4. Definition of Done (DoD)

- [ ] All Unit Tests pass (`pytest tests/`).
- [ ] Code syntax and typing verified (`py_compile` & type hints present).
- [ ] Test coverage exceeds project target (e.g., > 85%).
- [ ] QA integration test checklist completed in sandbox.
- [ ] Documentation updated in `doc/` and `CODEBASE_MAP.md`.
