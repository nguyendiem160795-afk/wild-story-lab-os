---
document_id: FS-004
module: 01
category: Standards
title: Metadata Standard (Tiêu chuẩn Metadata)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Metadata Standard (Tiêu chuẩn Metadata)

> Normative metadata standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the mandatory metadata schema for all EAOSS documentation.

Metadata provides structured information that enables identification, traceability, governance, search, indexing, validation, and AI-assisted processing.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Principles
- Standards
- Policies
- Templates
- Architecture documents
- Specifications
- Baselines
- Reviews
- Future EAOSS artifacts

---

# 3. Metadata Objectives

Metadata shall:

- Identify every artifact uniquely.
- Support version management.
- Enable repository automation.
- Improve discoverability.
- Facilitate AI processing.
- Preserve governance information.

---

# 4. Required Metadata Schema

Every normative document shall begin with YAML Front Matter.

Required fields:

```yaml
document_id:
module:
category:
title:
version:
status:
classification:
owner:
last_updated:
```

These fields are mandatory.

---

# 5. Optional Metadata

When applicable, the following fields may be added.

```yaml
baseline_id:
review_status:
approved_by:
approved_date:
review_cycle:
parent_document:
related_documents:
tags:
keywords:
```

Optional metadata shall only be used when relevant.

---

# 6. Metadata Naming Rules

Metadata keys shall:

- use snake_case
- remain lowercase
- be stable over time
- avoid abbreviations unless standardized

Example:

```yaml
last_updated:
review_status:
baseline_id:
```

Incorrect examples:

```yaml
LastUpdated
lastUpdated
LAST_UPDATED
```

---

# 7. Metadata Values

Metadata values shall be:

- accurate
- complete
- synchronized with document content
- maintained throughout the artifact lifecycle

Example:

```yaml
version: 2.1.0
status: Production Ready
classification: Public
```

---

# 8. Metadata Consistency

Metadata shall remain synchronized with:

- Revision History
- CHANGELOG
- BASELINE
- Review Records

Conflicting metadata is considered a documentation defect.

---

# 9. Metadata Validation

Every metadata block shall be validated for:

- Required fields present
- Correct field names
- Valid version format
- Valid status
- Valid dates
- YAML syntax correctness

Validation should be automated whenever practical.

---

# 10. Metadata Lifecycle

Metadata shall evolve together with the artifact.

Whenever an artifact changes:

- Version shall be updated.
- Last updated date shall be revised.
- Review status shall be refreshed when applicable.

---

# 11. Reserved Metadata Fields

The following metadata fields are reserved across EAOSS:

| Field | Purpose |
|---------|---------|
| document_id | Unique artifact identifier |
| module | Module ownership |
| category | Artifact classification |
| title | Official title |
| version | Artifact version |
| status | Lifecycle status |
| classification | Visibility level |
| owner | Responsible owner |
| last_updated | Last modification date |

Reserved fields shall not change meaning.

---

# 12. Validation Checklist

Every metadata block shall satisfy:

| Requirement | Mandatory |
|-------------|-----------|
| Required fields present | Yes |
| YAML valid | Yes |
| Field names correct | Yes |
| Version synchronized | Yes |
| Date updated | Yes |
| Status valid | Yes |

---

# 13. Compliance

All EAOSS documentation shall comply with this metadata standard.

Compliance shall be verified during Documentation Review and Compliance Review.

---

# 14. References

- FP-004 Documentation Principles
- FP-005 Governance Principles
- FP-007 Versioning Policy
- FS-001 Documentation Standard
- FS-003 Versioning Standard

---

# 15. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Metadata Standard |

---

# End of Document