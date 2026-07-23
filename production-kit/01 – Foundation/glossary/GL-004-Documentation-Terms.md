---
document_id: GL-004
module: 01
category: Glossary
title: Documentation Terms (Thuật ngữ Tài liệu)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Documentation Terms (Thuật ngữ Tài liệu)

> Official documentation terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This glossary defines documentation-related terminology used throughout EAOSS.

The purpose is to establish a consistent language for creating, managing, reviewing, and maintaining documentation artifacts.

---

# 2. Document

## Vietnamese:
Tài liệu

## Definition:

A Document is a structured information artifact created to communicate knowledge, requirements, decisions, rules, or specifications.

A document may contain:

- Information.
- Rules.
- Decisions.
- References.
- Historical records.

Examples:

- Principle document.
- Standard document.
- Policy document.
- Architecture document.

---

# 3. Documentation

## Vietnamese:
Hoạt động tài liệu hóa

## Definition:

Documentation is the process of creating, organizing, maintaining, and managing documents.

Purpose:

- Preserve knowledge.
- Enable communication.
- Support governance.

---

# 4. Document Artifact

## Vietnamese:
Tài liệu như một tài sản quản lý

## Definition:

A Document Artifact is a document that has:

- Identity.
- Owner.
- Version.
- Lifecycle.
- Governance status.

---

# 5. Specification

## Vietnamese:
Đặc tả

## Definition:

A Specification defines detailed requirements, behaviors, constraints, or expected characteristics of a system or component.

Examples:

- System specification.
- API specification.
- Architecture specification.

---

# 6. Standard Document

## Vietnamese:
Tài liệu tiêu chuẩn

## Definition:

A document that defines mandatory rules and requirements.

Example:

```text
FS-003 Versioning Standard
```

---

# 7. Policy Document

## Vietnamese:
Tài liệu chính sách

## Definition:

A document defining governance rules, responsibilities, and control mechanisms.

Example:

```text
POL-001 Change Control Policy
```

---

# 8. Record

## Vietnamese:
Bản ghi

## Definition:

A Record is evidence of an activity, decision, event, or transaction.

Examples:

- Review Record.
- Audit Record.
- Approval Record.
- Change Record.

---

# 9. Reference

## Vietnamese:
Tài liệu tham chiếu

## Definition:

A Reference is a connection to another artifact that provides supporting information.

Purpose:

- Maintain relationships.
- Provide context.
- Enable traceability.

---

# 10. Metadata

## Vietnamese:
Siêu dữ liệu

## Definition:

Metadata is information describing an artifact.

Examples:

```yaml
document_id:
version:
owner:
status:
created_date:
```

Metadata enables:

- Search.
- Classification.
- Lifecycle management.

---

# 11. Document Identifier

## Vietnamese:
Mã định danh tài liệu

## Definition:

A unique identifier assigned to each managed document.

Example:

```text
POL-001
FS-003
TMP-010
```

Purpose:

- Identification.
- Traceability.
- Reference management.

---

# 12. Document Structure

## Vietnamese:
Cấu trúc tài liệu

## Definition:

The organized arrangement of sections, content, metadata, and references within a document.

Example:

```text
Metadata
 ↓
Purpose
 ↓
Scope
 ↓
Main Content
 ↓
References
 ↓
Revision History
```

---

# 13. Revision

## Vietnamese:
Lần sửa đổi

## Definition:

A Revision is a modification made to an existing document version.

A revision may include:

- Corrections.
- Improvements.
- Updates.

---

# 14. Revision History

## Vietnamese:
Lịch sử sửa đổi

## Definition:

A record of changes made throughout the document lifecycle.

Example:

| Version | Change |
|-|-|
| 1.0.0 | Initial release |
| 1.1.0 | Added requirements |

---

# 15. Version History

## Vietnamese:
Lịch sử phiên bản

## Definition:

A chronological record of all released versions of an artifact.

Purpose:

- Track evolution.
- Support rollback.
- Preserve history.

---

# 16. Document Status

## Vietnamese:
Trạng thái tài liệu

## Definition:

The current lifecycle state of a document.

Common states:

```text
Draft
Review
Approved
Production Ready
Deprecated
Archived
```

---

# 17. Documentation Quality

## Vietnamese:
Chất lượng tài liệu

## Definition:

The degree to which documentation is:

- Accurate.
- Complete.
- Clear.
- Consistent.
- Maintainable.

---

# 18. Canonical Document

## Vietnamese:
Tài liệu chuẩn chính thức

## Definition:

A Canonical Document is the authoritative source accepted as the official reference.

Characteristics:

- Approved.
- Maintained.
- Trusted.

---

# 19. Document Dependency

## Vietnamese:
Sự phụ thuộc tài liệu

## Definition:

A relationship where one document relies on information from another document.

Example:

```text
Policy
   ↓
Standard
   ↓
Template
```

---

# 20. Documentation Lifecycle

## Vietnamese:
Vòng đời tài liệu

## Definition:

The complete journey of a document.

```text
Create
 ↓
Review
 ↓
Approve
 ↓
Publish
 ↓
Maintain
 ↓
Archive
```

---

# 21. Documentation Quality Checklist

| Requirement | Mandatory |
|---|---|
| Clear purpose | Yes |
| Metadata complete | Yes |
| Owner defined | Yes |
| Version managed | Yes |
| References maintained | Yes |
| Lifecycle controlled | Yes |

---

# 22. References

- GL-001 Core Terms
- FS-001 Documentation Standard
- FS-004 Metadata Standard
- TMP-001 Document Template
- TMP-009 Changelog Template

---

# 23. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Documentation Terms Glossary |

---

# End of Document