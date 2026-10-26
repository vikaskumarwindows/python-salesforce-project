# SPEC-001: Implementation Plan - Salesforce Baseline Integration

- **Specification ID**: SPEC-001
- **Reason / Title**: Salesforce Baseline Integration & SOQL Query Pipeline
- **Status**: Implemented / In Verification

---

## 1. Architecture & Module Breakdown

| Phase | Module / Artifact | Action | Description |
| :--- | :--- | :--- | :--- |
| **1.1** | `.env.example` | Create | Define environment variable template for credentials. |
| **1.2** | `requirements.txt` | Update | Pin `simple-salesforce`, `python-dotenv`, `requests`, `pandas`, `cryptography`. |
| **1.3** | `src/__init__.py` | Create | Package initialization. |
| **1.4** | `src/salesforce_client.py` | Create | Implement `get_salesforce_connection()` and smoke test execution. |
| **1.5** | `.agents/scripts/safety_guard.py` | Integrate | Pre-tool check to block secret commits and destructive actions. |

---

## 2. Step-by-Step Implementation Sequence

1. **Environment Setup**:
   - Initialize Python virtual environment `.venv` with Python 3.15.
   - Install core dependencies from `requirements.txt`.
2. **Credential & Connection Layer**:
   - Implement `dotenv.load_dotenv()` in `src/salesforce_client.py`.
   - Validate credentials presence; raise descriptive `ValueError` if missing.
   - Initialize `simple_salesforce.Salesforce` with explicit API version `60.0`.
3. **Execution & Verification**:
   - Provide standalone `if __name__ == "__main__":` block to verify live connectivity by querying `Organization` object.
4. **Codebase Map Synchronization**:
   - Register modules in `CODEBASE_MAP.md`.
   - Run `.venv\Scripts\python.exe .agents\scripts\verify_and_sync_map.py`.
