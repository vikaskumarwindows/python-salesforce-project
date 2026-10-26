# Template: Architecture Decision Record (ADR)

> [!IMPORTANT]
> **Threshold Rule**: An ADR should **NOT** be created for routine, standard, or small tasks (e.g. minor field additions, standard SOQL queries).
> 
> Only create this ADR document if the specification is **large, complex, or introduces major architectural decisions** (e.g., cross-system integrations, new external libraries, custom authentication flows, Salesforce Governor / 24-hr API quota shifts, or new persistence boundaries).

---

# ADR-XXXX: [Short Title of the Decision, e.g., Adopt Bulk API 2.0 for Contact Synchronization]

- **Status**: [ Proposed | Accepted | Deprecated | Superseded by ADR-YYYY ]
- **Deciders**: [List of engineers, architects, or agents involved]
- **Date**: [YYYY-MM-DD]
- **Related Spec**: [Link to Spec, e.g., `doc/spec/001-salesforce-integration-spec.md`]

---

## ❓ Spec & Necessity Discovery Questionnaire

*Before writing this ADR, answer the following driving questions to ensure an ADR is genuinely required:*

1. **Why is this ADR needed instead of a simple code change?**
   - *Does this change alter how data flows, introduce new libraries, change security credentials, or affect system boundaries?*
   - [Answer here]

2. **Which Spec requirement(s) or business objective drives this decision?**
   - *Reference specific functional requirements (e.g., FR-1, FR-3) or non-functional constraints from the Spec.*
   - [Answer here]

3. **What Salesforce platform constraints influence this decision?**
   - *Consider 24-hour API call limits, Governor Limits, SOQL 50,000-row limits, concurrent requests, or bulk job timeouts.*
   - [Answer here]

4. **What are the security, credential, and compliance implications?**
   - *Does this require OAuth scopes, JWT keys, user permission sets, or handling sensitive PII?*
   - [Answer here]

5. **What happens if we do nothing (Status Quo)?**
   - *What bottlenecks, technical debt, or failures will occur?*
   - [Answer here]

---

## 1. Context and Problem Statement

[Describe the context, problem, technical debt, or requirement from the spec that necessitates this decision. Provide sufficient background so future developers understand why this problem mattered.]

---

## 2. Decision Drivers

* [Driver 1, e.g., Salesforce rolling 24-hour API limit conservation]
* [Driver 2, e.g., Cross-platform Windows/Linux execution compatibility]
* [Driver 3, e.g., Zero-secret exposure in source control]
* [Driver 4, e.g., Sub-second query latency for user-facing workflows]

---

## 3. Considered Options

* **Option 1**: [Name of Option, e.g., Synchronous REST API with auto-pagination]
* **Option 2**: [Name of Option, e.g., Asynchronous Bulk API 2.0 Ingest Jobs]
* **Option 3**: [Name of Option, e.g., Custom Apex REST Endpoint with payload compression]

---

## 4. Comparison Matrix

| Evaluation Criteria | Option 1: [Name] | Option 2: [Name] | Option 3: [Name] |
| :--- | :--- | :--- | :--- |
| **Salesforce API Usage** | High (1 call per 2,000 records) | Low (1 call per batch job) | Medium |
| **Throughput / Latency** | Low latency, low throughput | High latency, massive throughput | Custom |
| **Implementation Complexity** | Low | Medium | High (Apex required) |
| **Maintenance Burden** | Minimal | Low | High |
| **Spec Alignment** | Meets FR-X | Meets FR-X, FR-Y | Partial |

---

## 5. Decision Outcome

**Chosen Option**: **Option X: [Name]**, because [provide concise rationale combining drivers and trade-offs].

### Positive Consequences
* [Advantage 1]
* [Advantage 2]
* [Advantage 3]

### Negative Consequences & Trade-offs
* [Disadvantage / Trade-off 1]
* [Disadvantage / Trade-off 2]

---

## 6. Implementation & Validation Checklist

- [ ] Spec updated to reflect this decision: [Link to Spec]
- [ ] Technical Design / TDD document created or updated: [Link to TDD]
- [ ] Dependencies updated in `requirements.txt` (if applicable)
- [ ] Environment variables or `.env.example` updated (if applicable)
- [ ] Security reviewed against Salesforce Least Privilege access guidelines
