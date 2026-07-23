---
document_id: FS-002
module: 01
category: Standards
title: Naming Standard (Tiêu chuẩn Đặt tên)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Naming Standard (Tiêu chuẩn Đặt tên)

> Normative naming standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the mandatory naming rules for all EAOSS artifacts.

The objective is to establish a predictable naming system that improves readability, repository navigation, automation, traceability, and AI-assisted processing.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Modules
- Directories
- Documents
- Standards
- Principles
- Policies
- Templates
- Reviews
- Metadata
- Future EAOSS artifacts

---

# 3. General Requirements

All names shall be:

- Unique
- Stable
- Human-readable
- Machine-readable
- Descriptive
- Consistent

Names shall avoid unnecessary abbreviations unless officially defined.

---

# 4. Module Naming

Modules shall follow the format:

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

Rules:

- Two-digit numeric prefix is mandatory.
- Use lowercase letters.
- Separate words with hyphens.
- Module numbers shall never be reused.

---

# 5. Directory Naming

Directories shall use:

```text
lowercase-with-hyphens
```

Examples:

```text
design-patterns
review-templates
shared-assets
metadata-schema
```

Rules:

- No spaces.
- No underscores.
- No special characters except hyphen.

---

# 6. File Naming

Core documents shall use reserved uppercase filenames:

```text
README.md
INDEX.md
ARCHITECTURE.md
CONFORMANCE.md
CHANGELOG.md
ROADMAP.md
BASELINE.md
```

All other documentation shall use:

```text
Pascal-Case-Words.md
```

Examples:

```text
Architecture-Principles.md
Documentation-Standard.md
Review-Checklist.md
```

---

# 7. Artifact Identifiers

Every normative artifact shall have a permanent identifier.

Examples:

```text
FP-001
FS-002
POL-003
TMP-001
RV-005
```

Rules:

- Identifiers shall be unique.
- Identifiers shall never be reassigned.
- Identifiers remain stable across versions.

---

# 8. Metadata Naming

Metadata keys shall use snake_case.

Examples:

```yaml
document_id:
baseline_id:
last_updated:
review_status:
owner:
```

CamelCase and kebab-case shall not be used for metadata keys.

---

# 9. Reserved Prefixes

The following prefixes are reserved:

| Prefix | Meaning |
|---------|---------|
| FP | Foundation Principle |
| FS | Foundation Standard |
| POL | Policy |
| TMP | Template |
| RV | Review |
| ADR | Architecture Decision Record |
| MPP | Master Planning Package |

New prefixes require governance approval.

---

# 10. Reserved Filenames

The following filenames are reserved across the repository:

- README.md
- INDEX.md
- ARCHITECTURE.md
- CONFORMANCE.md
- CHANGELOG.md
- ROADMAP.md
- BASELINE.md

These filenames shall retain their canonical purpose.

---

# 11. Validation Rules

A valid name shall:

- Follow the correct format.
- Use approved casing.
- Use approved separators.
- Avoid ambiguity.
- Match the associated artifact type.

---

# 12. Compliance

Compliance with this standard is mandatory for all EAOSS artifacts.

Non-compliant names shall be corrected before approval.

---

# 13. References

- FP-006 Naming Conventions
- FS-001 Documentation Standard
- FP-005 Governance Principles
- FP-010 Quality Principles

---

# 14. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Naming Standard |

---

# End of Document