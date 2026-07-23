---
document_id: TMP-010
module: 01
category: Templates
title: README Template (Mẫu README)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# README Template (Mẫu README Chuẩn)

> Official reusable README structure for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for README documents across EAOSS repositories.

The objective is to provide a consistent entry point for every module, library, directory, and knowledge domain.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Repository README
- Module README
- Library README
- Directory README
- Knowledge domain README

Examples:

```text
README.md

01-foundation/README.md

standards/README.md
```

---

# 3. README Structure

Every README should follow:

```markdown
# Title

> Short description.

---

# 1. Overview

Introduction.

---

# 2. Purpose

Why this area exists.

---

# 3. Scope

What is included.

---

# 4. Structure

Directory or content organization.

---

# 5. Usage

How to use this area.

---

# 6. Navigation

Important links.

---

# 7. Related Documents

Connected artifacts.

---

# 8. Maintenance

Ownership information.

---

# End of Document
```

---

# 4. Overview Section

The overview should answer:

- What is this?
- Why does it exist?
- Who should use it?

Example:

```markdown
This module provides foundational governance capabilities for EAOSS.
```

---

# 5. Purpose Section

Define:

- Business purpose.
- Technical purpose.
- Knowledge purpose.

Example:

```markdown
The purpose is to establish reusable standards for enterprise documentation.
```

---

# 6. Scope Section

Define boundaries.

Include:

- Included content.
- Excluded content.
- Dependencies.

Example:

```markdown
Included:

- Standards
- Policies
- Templates

Excluded:

- Application implementation details
```

---

# 7. Structure Section

Document internal organization.

Example:

```text
foundation/

├── principles/
├── standards/
├── policies/
└── templates/
```

---

# 8. Navigation Section

Provide important paths.

Example:

```markdown
## Navigation

- Principles
- Standards
- Policies
- Templates
```

---

# 9. Related Documents Section

Reference connected artifacts.

Example:

```markdown
Related:

- ARCHITECTURE.md
- INDEX.md
- BASELINE.md
```

---

# 10. Maintenance Section

Every README should identify:

| Field | Description |
|---|---|
| Owner | Responsible person/team |
| Status | Current lifecycle |
| Last Updated | Latest revision |
| Review Cycle | Maintenance frequency |

---

# 11. README Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Overview defined | Yes |
| Purpose defined | Yes |
| Scope defined | Yes |
| Structure documented | Yes |
| Navigation provided | Yes |
| Related documents linked | Yes |
| Owner defined | Yes |

---

# 12. Lifecycle

README documents follow:

```text
Created
 ↓
Reviewed
 ↓
Published
 ↓
Maintained
 ↓
Updated
 ↓
Archived
```

---

# 13. Compliance

All EAOSS modules and major directories should contain an approved README document.

Exceptions require approval according to POL-005 Exception Policy.

---

# 14. References

- TMP-001 Document Template
- FS-005 Repository Structure Standard
- FS-007 Cross Reference Standard
- FS-010 Template Standard
- POL-010 Lifecycle Policy

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial README Template |

---

# End of Document