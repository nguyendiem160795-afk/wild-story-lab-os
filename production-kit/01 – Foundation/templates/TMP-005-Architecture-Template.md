---
document_id: TMP-005
module: 01
category: Templates
title: Architecture Template (Mẫu Kiến trúc)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Architecture Template (Mẫu Kiến trúc)

> Official reusable template for creating architecture documents within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for architecture documentation.

The objective is to ensure architecture artifacts clearly describe:

- Architecture vision.
- System structure.
- Components.
- Relationships.
- Dependencies.
- Constraints.
- Design decisions.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Enterprise Architecture Documents.
- Solution Architecture Documents.
- System Architecture Documents.
- Data Architecture Documents.
- AI Architecture Documents.
- Platform Architecture Documents.

Naming format:

```text
ARCH-XXX-Architecture-Name.md
```

Examples:

```text
ARCH-001-Enterprise-Architecture.md

ARCH-002-AI-Architecture.md
```

---

# 3. Metadata Template

Every architecture document shall begin with:

```yaml
---
document_id: ARCH-XXX
module:
category: Architecture
title:
version:
status:
classification:
owner:
last_updated:
---
```

---

# 4. Architecture Document Structure

Every architecture document should follow:

```markdown
# Architecture Title

> Short description of architecture purpose.

---

# 1. Purpose

Why this architecture exists.

---

# 2. Scope

Architecture boundaries.

---

# 3. Architecture Overview

High-level architecture description.

---

# 4. Architecture Components

Main building blocks.

---

# 5. Component Relationships

How components interact.

---

# 6. Data Flow

Information movement.

---

# 7. Dependencies

External and internal dependencies.

---

# 8. Constraints

Limitations and assumptions.

---

# 9. Architecture Decisions

Important design decisions.

---

# 10. Security Considerations

Protection requirements.

---

# 11. Compliance

Validation requirements.

---

# 12. References

Related artifacts.

---

# 13. Revision History

Change records.

---

# End of Document
```

---

# 5. Architecture Overview Section

This section describes the complete architecture picture.

Should include:

- Purpose.
- Main concepts.
- Major layers.
- Core capabilities.

Example:

```markdown
The architecture consists of:

- Presentation Layer
- Knowledge Layer
- Processing Layer
- Data Layer
```

---

# 6. Component Definition

Every component should define:

| Field | Description |
|---|---|
| Name | Official component name |
| Purpose | Why component exists |
| Responsibility | What component does |
| Owner | Responsible party |
| Dependencies | Required connections |

---

# 7. Relationship Mapping

Architecture relationships should describe:

- Communication.
- Data exchange.
- Dependencies.
- Ownership.

Example:

```text
Component A
      ↓
Component B
      ↓
Component C
```

---

# 8. Architecture Decision Section

Major decisions should follow:

```markdown
## ADR Reference

Decision:

Why:

Alternatives:

Impact:
```

---

# 9. Constraint Definition

Constraints may include:

- Technical limitations.
- Security requirements.
- Performance requirements.
- Governance restrictions.
- Compatibility requirements.

---

# 10. Architecture Validation

Architecture documents should be validated through:

- Architecture review.
- Dependency analysis.
- Security review.
- Compliance review.

---

# 11. Architecture Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Purpose defined | Yes |
| Scope defined | Yes |
| Components documented | Yes |
| Relationships mapped | Yes |
| Dependencies identified | Yes |
| Constraints documented | Yes |
| Review completed | Yes |

---

# 12. Lifecycle

Architecture documents follow:

```text
Draft
 ↓
Architecture Review
 ↓
Approved
 ↓
Published
 ↓
Maintained
 ↓
Updated
 ↓
Deprecated
 ↓
Archived
```

---

# 13. Compliance

All architecture artifacts shall follow this template.

Major deviations require approval according to exception governance.

---

# 14. References

- TMP-001 Document Template
- TMP-003 Standard Template
- FS-005 Repository Structure Standard
- POL-004 Governance Policy
- POL-010 Lifecycle Policy

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Architecture Template |

---

# End of Documents