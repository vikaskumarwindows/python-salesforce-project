# Data Flow & Transformation Design

This document details data flow pipelines for reading from and writing to Salesforce.

---

## 1. SOQL Query Ingestion Flow

```mermaid
flowchart LR
    A[Python Client] -->|1. SOQL Query| B(Salesforce REST API)
    B -->|2. Initial Batch 2000 Records| A
    A -->|3. QueryMore via nextRecordsUrl| B
    B -->|4. Next Batch Records| A
    A -->|5. Aggregate JSON Records| C[Flatten Nested Dicts]
    C -->|6. Pandas DataFrame| D[Output CSV / Parquet / DB Sync]
```

### Steps:
1. **Query Construction**: Ensure field selection explicitly names required fields (avoid `SELECT FIELDS(ALL)` in automated integrations due to performance penalties).
2. **Relationship Flattening**: Flatten parent fields (e.g. `Account.Owner.Email` -> `Account_Owner_Email`) to provide clean tabular data structures.
3. **Type Casting**: Map Salesforce datatypes (`xsd:dateTime`, `xsd:boolean`, `xsd:double`) to Python native or Pandas datatypes.

---

## 2. Bulk Ingestion / Upsert Flow

For writing large volumes (>10,000 records) to Salesforce:

```mermaid
sequenceDiagram
    autonumber
    participant App as Python Application
    participant SFBulk as Salesforce Bulk API 2.0
    participant SFDB as Salesforce DB

    App->>SFBulk: Create Job (operation=upsert, object=Contact, externalIdFieldName=External_Id__c)
    SFBulk-->>App: Job ID (state=Open)
    App->>SFBulk: Upload CSV batch data
    App->>SFBulk: Close Job (state=UploadComplete)
    
    loop Poll Job Status
        App->>SFBulk: GET /services/data/v60.0/jobs/ingest/{jobId}
        SFBulk-->>App: Status (InProgress / JobComplete)
    end
    
    App->>SFBulk: GET /services/data/v60.0/jobs/ingest/{jobId}/successfulResults/
    App->>SFBulk: GET /services/data/v60.0/jobs/ingest/{jobId}/failedResults/
    SFBulk-->>App: Detailed Error Report (row-by-row)
```
