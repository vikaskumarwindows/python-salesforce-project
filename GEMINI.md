# Salesforce Project Guidelines (Antigravity)

Project-level guidelines for `python-salesforce-project`.

---

## 🛠️ Environment & Commands

- **Virtual Environment**: `.venv\`
- **Activate (PowerShell)**:
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Dependencies**:
  ```powershell
  pip install -r requirements.txt
  ```
- **Run Salesforce Client**:
  ```powershell
  python src\salesforce_client.py
  ```

---

## 🔒 Security & Code Quality

- Store Salesforce credentials in `.env` (never commit `.env`).
- Always verify syntax: `python -m py_compile src\salesforce_client.py`.
- Adhere to PEP 8, strict type hints, and structured logging.

---

## 📋 Specification & Codebase Map Synchronization (/spec & /build)

- **Specification Workflow (`/spec`)**:
  1. Inspect workspace safeguards (`.agents/scripts/safety_guard.py` and `doc/architecture/security-and-compliance.md`).
  2. Create container folder `doc/spec/<SPEC-Number - Spec Reason>/`.
  3. Author the 4 core files (`Requirement.md`, `Implementation_plan.md`, `TDD.md`, `Scenario.md`), adding `ADR-<Count>.md` only for large/complex architectural specs.
  4. Immediately update `CODEBASE_MAP.md` and verify with: `.venv\Scripts\python.exe .agents\scripts\verify_and_sync_map.py`.

- **Development Workflow (`/build`)**:
  1. Ask/identify which spec from `doc/spec/` to develop.
  2. Ingest `Requirement.md`, `Implementation_plan.md`, `TDD.md`, `Scenario.md`, and any `ADR`.
  3. Develop modular Python code using design patterns (Adapter, Factory, Repository), strict type hints, structured logging, and unit tests under `tests/`.
  4. Verify syntax (`py_compile`), run tests, and immediately update `CODEBASE_MAP.md`.
  5. Verify synchronization by running: `.venv\Scripts\python.exe .agents\scripts\verify_and_sync_map.py`.

