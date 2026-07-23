---
document_id: FS-010
module: 01
category: Standards
title: Template Standard (Tiêu chuẩn Mẫu Tài liệu)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Template Standard (Tiêu chuẩn Mẫu Tài liệu)

> Normative template standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the official document templates used throughout EAOSS.

Templates ensure consistency, accelerate artifact creation, improve quality, and enable predictable documentation structures across all modules.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Principles
- Standards
- Policies
- Specifications
- Architecture Documents
- Reviews
- Templates
- Baselines
- Reports

---

# 3. Template Principles

All templates shall follow these principles:

- Consistent structure
- Clear purpose
- Reusable design
- Easy validation
- AI-readable format
- Long-term maintainability

---

# 4. Common Document Template

All normative documents should follow this structure:

```markdown
---
metadata
---

# Title

> Short description

---

# 1. Purpose

Description of document purpose.

---

# 2. Objectives

Expected outcomes.

---

# 3. Scope

Applicable boundaries.

---

# 4. Main Content

Core information.

---

# 5. Compliance

Requirements and validation.

---

# 6. References

Related documents.

---

# 7. Revision History

Change records.

---

# End of Document
```

---

# 5. Principle Template

Used for FP documents.

Required structure:

```text
Metadata

Title

Purpose

Objectives

Scope

Principles

Compliance

References

Revision History
```

Example:

```text
FP-001 Architecture Principles
```

---

# 6. Standard Template

Used for FS documents.

Required structure:

```text
Metadata

Title

Purpose

Scope

Requirements

Rules

Validation

Compliance

References

Revision History
```

Example:

```text
FS-001 Documentation Standard
```

---

# 7. Policy Template

Used for POL documents.

Required structure:

```text
Metadata

Title

Purpose

Scope

Policy Statements

Responsibilities

Exceptions

Compliance

References

Revision History
```

---

# 8. Architecture Document Template

Used for architecture specifications.

Required structure:

```text
Metadata

Purpose

Architecture Overview

Components

Relationships

Dependencies

Constraints

Interfaces

Compliance

References

Revision History
```

---

# 9. Review Template

Used for review records.

Required structure:

```text
Metadata

Artifact Reviewed

Review Type

Review Participants

Review Criteria

Findings

Actions

Decision

Revision History
```

---

# 10. Baseline Template

Used for approved baseline records.

Required structure:

```text
Metadata

Baseline Purpose

Approved Artifacts

Version Information

Approval Status

Change Control

References

Revision History
```

---

# 11. Template Naming

Templates shall follow:

```text
TMP-###
```

Examples:

```text
TMP-001-Document-Template
TMP-002-Review-Template
TMP-003-Baseline-Template
```

---

# 12. Template Lifecycle

Templates follow:

```text
Draft
 ↓
Review
 ↓
Approved
 ↓
Published
 ↓
Updated
 ↓
Deprecated
```

---

# 13. Template Validation

Every template shall verify:

| Requirement | Mandatory |
|-------------|-----------|
| Metadata defined | Yes |
| Structure documented | Yes |
| Usage explained | Yes |
| Example provided | Recommended |
| Review completed | Yes |

---

# 14. Template Governance

Changes to approved templates require:

- Review approval
- Version update
- CHANGELOG update
- Impact assessment

---

# 15. Compliance

All EAOSS artifacts should use approved templates where applicable.

Deviation requires documented justification.

---

# 16. References

- FP-004 Documentation Principles
- FP-006 Naming Conventions
- FP-007 Versioning Policy
- FS-001 Documentation Standard
- FS-008 Review Standard
- FS-009 Quality Standard

---

# 17. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Template Standard |

---

# End of Document