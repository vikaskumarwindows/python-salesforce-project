# SPEC-001: Technical Design & Test Plan (TDD)

- **Specification ID**: SPEC-001
- **Reason / Title**: Salesforce Baseline Integration & SOQL Query Pipeline
- **Status**: Active / In Verification

---

## 1. Technical Change Summary

- **Source Files**: `src/salesforce_client.py`, `src/__init__.py`.
- **Runtime Dependencies**: `simple-salesforce>=1.12.6`, `python-dotenv>=1.0.1`.
- **Target Salesforce API Version**: `v60.0`.

---

## 2. Test-Driven Development (TDD) Unit Test Specifications

| Test Case | Objective | Input Data | Expected Result |
| :--- | :--- | :--- | :--- |
| **TDD-01** | Missing credentials check | `SALESFORCE_USERNAME` not set | Raises `ValueError` with copy instructions for `.env.example`. |
| **TDD-02** | Default domain handling | `SALESFORCE_DOMAIN` unset | Defaults domain to `login`. |
| **TDD-03** | Sandbox domain override | `SALESFORCE_DOMAIN=test` | Configures client with `test.salesforce.com`. |
| **TDD-04** | Authentication error handling | Mocked HTTP 400 `INVALID_LOGIN` | Traps exception gracefully without crashing or leaking credentials. |

---

## 3. Definition of Done (DoD)

- [x] Syntax verified via `.venv\Scripts\python.exe -m py_compile src/salesforce_client.py`.
- [x] Tested clean import of all dependencies.
- [x] Checked that no secrets are committed or stored in git.
- [x] Codebase map synchronized and validated.
