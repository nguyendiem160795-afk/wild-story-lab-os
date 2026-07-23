---
document_id: TMP-002
module: 01
category: Templates
title: Principle Template (Mẫu Nguyên lý)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Principle Template (Mẫu Nguyên lý)

> Official reusable template for creating Foundation Principles (FP-xxx) within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for creating principle documents.

The objective is to ensure every principle clearly communicates:

- Why the principle exists.
- What value it protects.
- How it guides decisions.
- How compliance is evaluated.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Architecture Principles
- Governance Principles
- Documentation Principles
- Quality Principles
- Security Principles
- Future Foundation Principles

Naming format:

```text
FP-XXX-Principle-Name.md
```

Example:

```text
FP-001-Architecture-Principles.md
```

---

# 3. Metadata Template

Every principle shall begin with:

```yaml
---
document_id: FP-XXX
module: 01
category: Principles
title:
version:
status:
classification:
owner:
last_updated:
---
```

---

# 4. Principle Document Structure

Every principle shall follow:

```markdown
# Principle Title

> Short description explaining the role of this principle.

---

# 1. Purpose

Why this principle exists.

---

# 2. Objectives

Expected outcomes.

---

# 3. Scope

Where this principle applies.

---

# 4. Principle Statements

Core rules and beliefs.

---

# 5. Rationale

Why these principles are important.

---

# 6. Implications

Expected impact and consequences.

---

# 7. Compliance

How adherence is evaluated.

---

# 8. References

Related artifacts.

---

# 9. Revision History

Change records.

---

# End of Document
```

---

# 5. Principle Statements Section

This section defines the actual principles.

Recommended format:

```markdown
## Principle 01: Principle Name

Statement:

The system shall...

Rationale:

Explanation of why this principle exists.

Implications:

Expected consequences.
```

---

# 6. Rationale Requirements

Every principle shall explain:

- Business value.
- Architectural value.
- Operational impact.
- Long-term benefit.

A principle without rationale is incomplete.

---

# 7. Implications Requirements

Implications should describe:

Positive impact:

- Benefits.
- Improvements.
- Expected behavior.

Potential constraints:

- Limitations.
- Trade-offs.
- Required discipline.

---

# 8. Compliance Template

Recommended:

```markdown
# Compliance

This principle is satisfied when:

- Required standards are followed.
- Decisions align with this principle.
- Exceptions are documented.
- Reviews confirm compliance.
```

---

# 9. Relationship Mapping

Principles should identify relationships.

Example:

```markdown
Related Principles:

- FP-001 Architecture Principles
- FP-005 Governance Principles
```

---

# 10. Principle Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Clear purpose | Yes |
| Defined scope | Yes |
| Principle statements included | Yes |
| Rationale provided | Yes |
| Implications defined | Yes |
| Compliance defined | Yes |
| References added | Yes |

---

# 11. Lifecycle

Principles follow:

```text
Draft
 ↓
Review
 ↓
Approved
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

# 12. Compliance

All FP-xxx documents shall follow this template.

Deviations require approval according to POL-005 Exception Policy.

---

# 13. References

- TMP-001 Document Template
- FS-001 Documentation Standard
- FS-010 Template Standard
- POL-010 Lifecycle Policy

---

# 14. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Principle Template |

---

# End of Document