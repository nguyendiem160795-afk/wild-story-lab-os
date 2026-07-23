---
document_id: FP-006
module: 01
category: Principles
title: Naming Conventions (Quy ước Đặt tên)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Naming Conventions (Quy ước Đặt tên)

> Canonical naming conventions for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This document defines the official naming conventions used throughout EAOSS.

Consistent naming improves readability, discoverability, automation, interoperability, and long-term maintainability.

---

# 2. Objectives (Mục tiêu)

The objectives are to:

- Establish a consistent naming system.
- Reduce ambiguity.
- Improve repository navigation.
- Enable deterministic automation.
- Support AI-assisted indexing and retrieval.

---

# 3. Scope (Phạm vi)

These conventions apply to:

- Modules
- Documents
- Directories
- Standards
- Policies
- Principles
- Reviews
- Templates
- Metadata
- Future EAOSS artifacts

---

# 4. General Rules

Names shall be:

- Unique
- Descriptive
- Stable
- Human-readable
- Machine-readable

Avoid abbreviations unless officially defined.

---

# 5. File Naming

Markdown files should use:

```text
Pascal-Case-Words.md
```

Examples:

```text
Architecture-Principles.md
Documentation-Standard.md
Review-Checklist.md
```

Core repository documents may use uppercase names:

```text
README.md
INDEX.md
CHANGELOG.md
ROADMAP.md
BASELINE.md
ARCHITECTURE.md
CONFORMANCE.md
```

---

# 6. Document Identifiers

Normative documents shall use stable identifiers.

Examples:

```text
FP-001
FP-006
FS-003
POL-002
AR-004
```

Identifiers shall never be reassigned.

---

# 7. Directory Naming

Directories shall use:

```text
lowercase-with-hyphens
```

Examples:

```text
01-foundation
03-enterprise-architecture
review-templates
design-patterns
```

---

# 8. Module Naming

Modules shall follow:

```text
NN-module-name
```

Examples:

```text
00-master
01-foundation
02-governance
03-enterprise-architecture
```

The numeric prefix defines repository order.

---

# 9. Metadata Naming

Metadata keys shall use:

```text
snake_case
```

Examples:

```yaml
document_id:
last_updated:
review_status:
baseline_id:
```

Metadata keys should remain stable across all documents.

---

# 10. Principle Naming

Principles shall follow:

```text
FP-###
```

Examples:

```text
FP-001 Architecture Principles
FP-002 Engineering Principles
FP-010 Quality Principles
```

---

# 11. Standard Naming

Standards shall follow:

```text
FS-###
```

Examples:

```text
FS-001 Documentation Standard
FS-002 Naming Standard
```

---

# 12. Policy Naming

Policies shall follow:

```text
POL-###
```

Examples:

```text
POL-001 Change Control Policy
POL-002 Release Policy
```

---

# 13. Review Naming

Review artifacts shall follow:

```text
RV-###
```

Examples:

```text
RV-001 Architecture Review
RV-002 Technical Review
```

---

# 14. Reserved Names

The following filenames are reserved:

- README.md
- INDEX.md
- ARCHITECTURE.md
- CONFORMANCE.md
- CHANGELOG.md
- ROADMAP.md
- BASELINE.md

These names shall retain their canonical meaning throughout EAOSS.

---

# 15. Naming Checklist

Every new artifact should satisfy the following checklist:

| Requirement | Mandatory |
|-------------|-----------|
| Unique | Yes |
| Descriptive | Yes |
| Stable | Yes |
| Consistent with conventions | Yes |
| Uses approved identifier | Yes |
| Machine-readable | Yes |

---

# 16. Compliance

All repository artifacts shall comply with these naming conventions.

Compliance shall be verified during Documentation Review and Compliance Review.

---

# 17. References

- FP-001 Architecture Principles
- FP-004 Documentation Principles
- FP-005 Governance Principles
- 01-foundation/CONFORMANCE.md

---

# 18. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Naming Conventions |

---

# End of Document