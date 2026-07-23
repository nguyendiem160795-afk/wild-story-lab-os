---
document_id: GL-006
module: 01
category: Glossary
title: Data Terms (Thuật ngữ Dữ liệu)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Data Terms (Thuật ngữ Dữ liệu)

> Official data terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This glossary defines data-related terminology used throughout EAOSS.

The purpose is to establish a common understanding of:

- Data management.
- Data architecture.
- Data governance.
- AI knowledge systems.

---

# 2. Data

## Vietnamese:
Dữ liệu

## Definition:

Data is a representation of information that can be stored, processed, analyzed, and used to generate knowledge or support decisions.

Examples:

- Text.
- Images.
- Audio.
- Video.
- Metadata.
- Structured records.

---

# 3. Data Asset

## Vietnamese:
Tài sản dữ liệu

## Definition:

A Data Asset is a data resource that has business, operational, analytical, or knowledge value.

Examples:

- Customer data.
- Training data.
- Knowledge documents.
- AI datasets.

---

# 4. Data Element

## Vietnamese:
Phần tử dữ liệu

## Definition:

A Data Element is the smallest meaningful unit of data.

Examples:

```text
Customer_Name
Creation_Date
Document_ID
```

---

# 5. Data Source

## Vietnamese:
Nguồn dữ liệu

## Definition:

A Data Source is the origin where data is created, collected, or obtained.

Examples:

- Database.
- Document repository.
- API.
- External system.

---

# 6. Data Repository

## Vietnamese:
Kho dữ liệu

## Definition:

A Data Repository is a managed location where data is stored and organized.

Examples:

- Database.
- Data warehouse.
- Knowledge repository.

---

# 7. Metadata

## Vietnamese:
Siêu dữ liệu

## Definition:

Metadata is information that describes, manages, and provides context about data.

Examples:

```yaml
name:
owner:
created_date:
version:
classification:
```

Metadata enables:

- Discovery.
- Search.
- Governance.
- Lifecycle management.

---

# 8. Data Model

## Vietnamese:
Mô hình dữ liệu

## Definition:

A Data Model defines how data is structured, related, and organized.

Types:

- Conceptual model.
- Logical model.
- Physical model.

---

# 9. Data Schema

## Vietnamese:
Lược đồ dữ liệu

## Definition:

A Data Schema defines the structure and organization of data.

Example:

```text
User

- ID
- Name
- Email
```

---

# 10. Structured Data

## Vietnamese:
Dữ liệu có cấu trúc

## Definition:

Data organized according to a predefined format.

Examples:

- Tables.
- Databases.
- Records.

---

# 11. Unstructured Data

## Vietnamese:
Dữ liệu phi cấu trúc

## Definition:

Data without a predefined structure.

Examples:

- Documents.
- Images.
- Videos.
- Audio.

---

# 12. Semi-Structured Data

## Vietnamese:
Dữ liệu bán cấu trúc

## Definition:

Data with partial organization but flexible structure.

Examples:

- JSON.
- XML.
- Metadata documents.

---

# 13. Data Pipeline

## Vietnamese:
Luồng dữ liệu

## Definition:

A Data Pipeline is a sequence of processes that move and transform data.

Example:

```text
Collect
 ↓
Process
 ↓
Transform
 ↓
Store
 ↓
Use
```

---

# 14. Data Processing

## Vietnamese:
Xử lý dữ liệu

## Definition:

Data Processing is the transformation of raw data into usable information.

Activities:

- Cleaning.
- Formatting.
- Transformation.
- Analysis.

---

# 15. Data Quality

## Vietnamese:
Chất lượng dữ liệu

## Definition:

Data Quality measures how suitable data is for intended use.

Quality dimensions:

| Dimension | Meaning |
|-|-|
| Accuracy | Chính xác |
| Completeness | Đầy đủ |
| Consistency | Nhất quán |
| Timeliness | Kịp thời |
| Validity | Hợp lệ |

---

# 16. Data Validation

## Vietnamese:
Xác thực dữ liệu

## Definition:

Data Validation verifies that data meets defined quality requirements.

Examples:

- Format checking.
- Rule checking.
- Completeness checking.

---

# 17. Data Governance

## Vietnamese:
Quản trị dữ liệu

## Definition:

Data Governance defines policies, responsibilities, and controls for managing data.

Includes:

- Ownership.
- Security.
- Quality.
- Lifecycle.

---

# 18. Data Ownership

## Vietnamese:
Quyền sở hữu dữ liệu

## Definition:

Data Ownership identifies who is responsible for managing and protecting data assets.

Owner responsibilities:

- Quality.
- Access.
- Maintenance.

---

# 19. Data Classification

## Vietnamese:
Phân loại dữ liệu

## Definition:

Data Classification categorizes data based on importance, sensitivity, and usage requirements.

Example:

```text
Public
Internal
Restricted
Confidential
```

---

# 20. Data Lifecycle

## Vietnamese:
Vòng đời dữ liệu

## Definition:

Data Lifecycle describes the stages data goes through.

Example:

```text
Create
 ↓
Store
 ↓
Use
 ↓
Maintain
 ↓
Archive
 ↓
Dispose
```

---

# 21. Data Lineage

## Vietnamese:
Nguồn gốc dữ liệu

## Definition:

Data Lineage tracks where data comes from, how it changes, and where it is used.

Purpose:

- Traceability.
- Audit.
- Quality management.

---

# 22. Data Integration

## Vietnamese:
Tích hợp dữ liệu

## Definition:

Data Integration combines data from multiple sources into a unified view.

---

# 23. Knowledge Data

## Vietnamese:
Dữ liệu tri thức

## Definition:

Knowledge Data is data organized to support understanding, reasoning, and knowledge retrieval.

Examples:

- Documents.
- Rules.
- Relationships.
- Context.

---

# 24. AI Training Data

## Vietnamese:
Dữ liệu huấn luyện AI

## Definition:

Training Data is data used to train AI models.

Requirements:

- Quality.
- Relevance.
- Diversity.
- Validation.

---

# 25. Data Quality Checklist

| Requirement | Mandatory |
|---|---|
| Data ownership defined | Yes |
| Metadata available | Yes |
| Quality measured | Yes |
| Lifecycle managed | Yes |
| Security classified | Yes |

---

# 26. References

- GL-001 Core Terms
- GL-005 AI Terms
- FS-004 Metadata Standard
- POL-008 Data Management Policy

---

# 27. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Data Terms Glossary |

---

# End of Document