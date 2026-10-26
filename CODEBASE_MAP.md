# Codebase Map: Python & Salesforce Integration Platform

> **Primary Audience**: Autonomous Coding Agents & Software Engineers  
> **Purpose**: Serves as the first point of contact and primary index for the codebase. Provides deep architectural pointers, directory blueprints, module contracts, environment runtimes, development workflows, and specifications developed so far.

---

## 🗺️ High-Level System Overview

This repository provides an enterprise-ready, modular integration platform between **Python 3.15** and **Salesforce CRM** (Sales Cloud, Service Cloud, custom objects). It handles authentication, SOQL querying with automated pagination, bulk data extraction, and schema inspection using `simple-salesforce`.

---

## 📁 Repository Directory Structure

```text
python-salesforce-project/
├── .agents/                              # Agent customizations, lifecycle hooks, and skills
│   ├── hooks.json                        # PreToolUse, PostToolUse, SessionStart lifecycle hooks
│   ├── scripts/                          # Hook & utility scripts (safety_guard.py, verify_and_sync_map.py)
│   └── skills/                           # Workspace skills: build, spec, salesforce-dev, code-quality
│       ├── build/SKILL.md                # /build workflow skill (spec ingestion & Python best practices)
│       └── spec/SKILL.md                 # /spec workflow skill (safeguards & map sync)
├── .venv/                                # Python 3.15 isolated virtual environment (git-ignored)
│   ├── Scripts/                          # Executables: python.exe, pip.exe, activate
│   └── Lib/site-packages/                # Installed wheels: simple-salesforce, pandas, requests...
│
├── doc/                                  # Complete engineering & architectural documentation
│   ├── README.md                         # Documentation index & contribution guide
│   ├── architecture/                     # System-level diagrams, boundaries, and security
│   │   ├── system-architecture.md        # Mermaid component & sequence diagrams
│   │   └── security-and-compliance.md    # Auth models, API quotas, PoLP, PII masking
│   ├── design/                           # Module specifications & data flows
│   │   ├── component-design.md           # Internal contracts & error handling matrix
│   │   └── data-flow.md                  # SOQL query pagination & Bulk API 2.0 flow
│   ├── spec/                             # Specification containers (<SPEC-Number - Reason>)
│   │   └── SPEC-001 - Salesforce Baseline Integration/
│   │       ├── Requirement.md            # Business discovery, personas, Salesforce rules, agent mandate
│   │       ├── Implementation_plan.md    # Architecture breakdown, sequence, dependencies
│   │       ├── TDD.md                    # Technical design, unit test contracts, DoD
│   │       ├── Scenario.md               # QA end-to-end scenarios, edge cases, boundaries
│   │       └── ADR-001.md                # (Conditional) Architecture Decision Record (only for large/complex specs)
│   ├── adrs/                             # Architecture Decision Records (MADR format)
│   │   ├── README.md                     # ADR index & authoring template
│   │   ├── 0001-record-architecture-decisions.md
│   │   └── 0002-salesforce-integration-library-selection.md
│   └── templates/                        # Templates with discovery questionnaires for development
│       ├── README.md                     # Lifecycle guide (Spec -> ADR -> TDD -> Code)
│       ├── SPEC_TEMPLATE.md              # Business questionnaire & Agent/Skill prompt generator
│       ├── ADR_TEMPLATE.md               # Architecture decision necessity & trade-offs template
│       └── TDD_TEMPLATE.md               # Technical design & QA test scenario matrix template
│
├── src/                                  # Application source code
│   ├── __init__.py                       # Top-level Python package marker
│   └── salesforce_client.py              # Auth manager, client initialization, sample SOQL execution
│
├── .env.example                          # Blueprint for local environment variables & Salesforce credentials
├── .gitattributes                        # Line-ending normalization (LF for code/XML, CRLF for scripts)
├── .gitignore                            # Comprehensive ignore rules (Python, Salesforce DX, secrets)
├── CODEBASE_MAP.md                       # (This file) Repository navigator & agent reference
├── GEMINI.md                             # Agent workspace guidelines & runtime instructions
├── README.md                             # Human-facing project overview & quickstart
└── requirements.txt                      # Pinned Python package dependencies
```

---

## 🧱 What Has Been Developed So Far

### 1. Source Code Modules (`src/`)

#### [`src/__init__.py`](./src/__init__.py)
- **Role**: Marks `src` as an importable Python package.

#### [`src/salesforce_client.py`](./src/salesforce_client.py)
- **Role**: Core authentication helper and entry point for Salesforce REST API interaction.
- **Key Functions**:
  - `get_salesforce_connection()`:
    - Reads environment variables via `dotenv.load_dotenv()`.
    - Validates presence of `SALESFORCE_USERNAME` and `SALESFORCE_PASSWORD`.
    - Initializes and returns an authenticated `Salesforce` client instance supporting custom domains (`login` vs. `test`) and API version targeting (default `60.0`).
  - **Standalone Execution Block (`__main__`)**:
    - Executes an end-to-end authentication smoke test.
    - Runs a sample SOQL query (`SELECT Id, Name FROM Organization`) to print the connected Salesforce Org name.

---

### 2. Environment & Dependency Infrastructure

| File | Purpose | Key Details |
| :--- | :--- | :--- |
| [`.venv/`](./.venv/) | Virtual Environment | Configured with Python **3.15.0**. Contains all installed packages including binary wheels. |
| [`requirements.txt`](./requirements.txt) | Dependency Manifest | `simple-salesforce>=1.12.6`, `python-dotenv>=1.0.1`, `requests>=2.32.0`, `cryptography>=42.0.0`, `pandas>=2.2.0`. |
| [`.env.example`](./.env.example) | Credential Blueprint | Templates for Direct Auth (Username/Password/Token) and Connected App OAuth 2.0 (Client ID/Secret/JWT). |

---

### 3. Git & Repository Configuration

| File | Rules & Function |
| :--- | :--- |
| [`.gitignore`](./.gitignore) | Blocks commits for `.venv/`, `.env`, secret keys (`*.pem`, `*.key`), Salesforce DX local state (`.sf/`, `.sfdx/`), logs (`*.log`), and data exports. |
| [`.gitattributes`](./.gitattributes) | Enforces `LF` for Python, JSON, XML, Apex, and Markdown files to prevent Windows CRLF git diff pollution. |
| **Git Branch** | Active default branch: `main`. |

---

### 4. Architectural & Specification Documentation (`doc/`)

| File / Directory | Key Concepts Documented |
| :--- | :--- |
| [`doc/architecture/system-architecture.md`](./doc/architecture/system-architecture.md) | High-level system context, Mermaid flowchart of Python-Salesforce boundaries, and REST/Bulk API sequence. |
| [`doc/architecture/security-and-compliance.md`](./doc/architecture/security-and-compliance.md) | OAuth JWT vs Direct Auth, zero-secret policy, API rate limits, least-privilege profiles, and PII masking. |
| [`doc/design/component-design.md`](./doc/design/component-design.md) | Module contracts, planned directory additions (`models/`, `utils/`), and HTTP retry/backoff matrix. |
| [`doc/design/data-flow.md`](./doc/design/data-flow.md) | SOQL `query_all` automatic pagination flow and Bulk API 2.0 asynchronous upsert sequence. |
| [`doc/spec/SPEC-001 - Salesforce Baseline Integration/`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/) | **SPEC-001 Container**:<br>• [`Requirement.md`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/Requirement.md): Business discovery, requirements & agent mandate.<br>• [`Implementation_plan.md`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/Implementation_plan.md): Technical breakdown & phase sequencing.<br>• [`TDD.md`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/TDD.md): Unit tests & Definition of Done.<br>• [`Scenario.md`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/Scenario.md): QA test scenarios & boundary conditions.<br>• [`ADR-001.md`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/ADR-001.md): Rationale for `simple-salesforce` & `dotenv`. |
| [`doc/adrs/`](./doc/adrs/) | **ADR 0001**: Architecture Decision Records adoption.<br>**ADR 0002**: Selection of `simple-salesforce` and `python-dotenv`. |
| [`doc/templates/`](./doc/templates/) | **SPEC_TEMPLATE**: Business discovery questions & Agent/Skill prompt builder.<br>**ADR_TEMPLATE**: Decision necessity & trade-offs questionnaire.<br>**TDD_TEMPLATE**: QA test scenarios & technical design matrix. |

---

### 5. Agent Customizations & Safeguards (`.agents/`)

| File / Component | Purpose | Key Details |
| :--- | :--- | :--- |
| [`.agents/skills/build/SKILL.md`](./.agents/skills/build/SKILL.md) | **`/build` Skill** | Asks which spec to develop, ingests the 4-5 files, applies enterprise design patterns, strict typing, tests, and updates `CODEBASE_MAP.md`. |
| [`.agents/skills/spec/SKILL.md`](./.agents/skills/spec/SKILL.md) | **`/spec` Skill** | Drives discovery questionnaires, creates `<SPEC-Number - Reason>` containers, validates security, and syncs `CODEBASE_MAP.md`. |
| [`.agents/scripts/safety_guard.py`](./.agents/scripts/safety_guard.py) | **Safety Guard Hook** | Pre-tool command gate intercepting destructive commands, force pushes, and secret exposure (`.env`, `id_rsa`). |
| [`.agents/scripts/verify_and_sync_map.py`](./.agents/scripts/verify_and_sync_map.py) | **Map Validator Script** | Validates that all source modules, specs, ADRs, and designs are tracked in `CODEBASE_MAP.md` and checks for invalid absolute paths. |
| **`build-agent`** | **Registered Subagent** | Autonomous Python software engineer specialized in implementing specs with design patterns, typing, and TDD. |
| **`spec-agent`** | **Registered Subagent** | Autonomous specification and architecture pair agent invoked for deep feature planning and requirement elicitation. |

---

## 🤖 Agent Guide: How to Extend This Codebase

When continuing development or building new features using an autonomous agent, follow this established protocol:

### Step 1: Read the Relevant Specifications & ADRs
- Review active specifications under [`doc/spec/`](./doc/spec/) (e.g. [`SPEC-001`](./doc/spec/SPEC-001%20-%20Salesforce%20Baseline%20Integration/)) to understand functional requirements.
- Review [`doc/adrs/`](./doc/adrs/) before proposing architectural changes or adding new libraries.

### Step 2: Use the Virtual Environment Directly
Always target the project virtual environment explicitly when executing Python commands:
- **Python Binary**: `.venv\Scripts\python.exe`
- **Pip Binary**: `.venv\Scripts\pip.exe`

### Step 3: Implement Code Under `src/`
Recommended upcoming modules to implement:
- `src/config.py`: Strongly-typed configuration class (e.g. `pydantic` or `@dataclass`) validating `.env` attributes.
- `src/query_runner.py`: Dedicated SOQL executor with DataFrame conversion and relationship flattening.
- `src/bulk_manager.py`: Bulk API 2.0 job orchestrator for batches > 10,000 records.
- `tests/`: Automated unit and mock tests using `pytest` and `responses` / `unittest.mock`.

### Step 4: Quality & Syntax Verification
Always verify syntax after editing:
```powershell
.venv\Scripts\python.exe -m py_compile src/salesforce_client.py
```

### Step 5: Update Documentation & Codebase Map
- When adding a new module or script, update this [`CODEBASE_MAP.md`](./CODEBASE_MAP.md).
- If modifying core architecture or external contracts, create a new ADR in [`doc/adrs/`](./doc/adrs/).

---

## ⚡ Quick Reference Commands

| Goal | Command |
| :--- | :--- |
| **Activate venv (PowerShell)** | `.\.venv\Scripts\Activate.ps1` |
| **Activate venv (CMD)** | `.\.venv\Scripts\activate.bat` |
| **Run Salesforce Client** | `.venv\Scripts\python.exe src\salesforce_client.py` |
| **Compile / Verify Syntax** | `.venv\Scripts\python.exe -m py_compile src\salesforce_client.py` |
| **Install New Dependency** | `.venv\Scripts\pip.exe install <package> && .venv\Scripts\pip.exe freeze > requirements.txt` |
| **Check Git Status** | `git status` |
