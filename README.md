# Python & Salesforce Project

A structured Python project designed for integrating with Salesforce via the REST APIs, Bulk APIs, and SOQL queries using `simple-salesforce`.

---

## 📁 Project Structure

```text
python-salesforce-project/
├── .venv/                   # Python virtual environment (ignored in git)
├── doc/                     # Architecture, design, specs, and ADRs
│   ├── architecture/        # High-level architecture & security models
│   ├── design/              # Component design & data flow pipelines
│   ├── spec/                # Functional & technical specifications
│   └── adrs/                # Architecture Decision Records
├── src/
│   ├── __init__.py
│   └── salesforce_client.py # Salesforce connection manager & sample query
├── .env.example             # Template for Salesforce credentials
├── .gitattributes           # Cross-platform line ending normalization (LF)
├── .gitignore               # Ignored files for Python, Salesforce DX, secrets
├── CODEBASE_MAP.md          # Comprehensive index, architecture pointers & agent guide
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Virtual Environment Activation

The virtual environment is already initialized at `.venv`. To activate it:

**On Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

> **Note for PowerShell execution policy:** If script execution is restricted, run:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
> ```

**On Windows (Command Prompt):**
```cmd
.\.venv\Scripts\activate.bat
```

**On Git Bash / WSL:**
```bash
source .venv/Scripts/activate
```

---

### 2. Install Dependencies

Activate your environment and install required packages:
```powershell
pip install -r requirements.txt
```

---

### 3. Configure Credentials

1. Copy `.env.example` to create `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```
2. Open `.env` and fill in your Salesforce credentials:
   - `SALESFORCE_USERNAME`: Salesforce login username (e.g., `user@domain.com`)
   - `SALESFORCE_PASSWORD`: Salesforce user password
   - `SALESFORCE_SECURITY_TOKEN`: Security token reset from Salesforce (*Settings > Reset My Security Token*)
   - `SALESFORCE_DOMAIN`: `login` (for Developer Edition / Production) or `test` (for Sandbox)

---

### 4. Run the Client

Verify connection to Salesforce:
```powershell
python -m src.salesforce_client
```

---

## 🛡️ Git & Security Guidelines

- **Never commit `.env` or certificates (`*.key`, `*.pem`)**: `.gitignore` is pre-configured to prevent sensitive credentials and Salesforce DX cache directories (`.sf/`, `.sfdx/`) from being tracked.
- **Line endings**: `.gitattributes` automatically enforces `LF` for Python, JSON, and Salesforce metadata files to prevent spurious git diffs on Windows.
