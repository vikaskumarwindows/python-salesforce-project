# Security & Compliance Model

This document outlines the security considerations, threat mitigation, and compliance standards for integrating Python with Salesforce.

---

## 1. Authentication & Credential Safety

### 1.1 Authentication Modes
1. **Username, Password + Security Token (Development / Sandbox)**:
   - Suitable for isolated development and sandbox validation.
   - Requires disabling multi-factor authentication (MFA) exemptions or using API-only integration users.
2. **OAuth 2.0 JWT Bearer Flow (Production Recommendation)**:
   - Uses an RSA private key certificate pair uploaded to a Salesforce Connected App.
   - Does not require storing static passwords.
   - Certificates must be loaded from secure secret managers or protected file paths excluded from Git.

### 1.2 Zero-Secrets in Source Control
- `.gitignore` strictly excludes `.env`, `*.key`, `*.pem`, `*.crt`, and `jwt/`.
- Pre-commit checks and hooks prevent accidental staging of sensitive patterns.

---

## 2. API Rate Limiting & Resource Protection

Salesforce enforces rolling 24-hour API limits based on org tier.

| Consideration | Mitigation Strategy |
| :--- | :--- |
| **API Call Quota Exhaustion** | Use Bulk API 2.0 for large batch ingestion (1 Bulk job counts as 1 API call regardless of record count up to limits). |
| **Concurrent Request Limits** | Implement client-side exponential backoff and request throttling. |
| **SOQL Query Timeout** | Restrict queries with bounded `LIMIT` clauses and avoid full table scans on non-indexed custom fields. |

---

## 3. Data Privacy & Least Privilege Access

- **Principle of Least Privilege (PoLP)**:
  - The Salesforce integration user must only be assigned profiles and permission sets granting access to required objects and fields.
  - Never run integrations under a System Administrator user in production.
- **Data Protection in Transit**:
  - All communication occurs over TLS 1.2 / TLS 1.3.
- **PII / Sensitive Data Masking**:
  - Local query dumps and logs must not print plaintext PII (Customer SSN, passwords, banking data).
