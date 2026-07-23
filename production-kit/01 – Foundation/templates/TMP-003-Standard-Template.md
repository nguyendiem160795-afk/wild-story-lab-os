---
document_id: TMP-003
module: 01
category: Templates
title: Standard Template (Mẫu Tiêu chuẩn)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Standard Template (Mẫu Tiêu chuẩn)

> Official reusable template for creating Foundation Standards (FS-xxx) within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for creating EAOSS Standard documents.

The objective is to ensure every standard provides clear, measurable, and enforceable requirements that transform principles into operational rules.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Documentation Standards
- Naming Standards
- Versioning Standards
- Metadata Standards
- Repository Standards
- Quality Standards
- Future Standard documents

Naming format:

```text
FS-XXX-Standard-Name.md
```

Example:

```text
FS-001-Documentation-Standard.md
```

---

# 3. Metadata Template

Every standard shall begin with:

```yaml
---
document_id: FS-XXX
module: 01
category: Standards
title:
version:
status:
classification:
owner:
last_updated:
---
```

---

# 4. Standard Document Structure

Every Standard shall follow:

```markdown
# Standard Title

> Short description of standard purpose.

---

# 1. Purpose

Why this standard exists.

---

# 2. Scope

Where this standard applies.

---

# 3. Definitions

Important terms and concepts.

---

# 4. Requirements

Mandatory requirements.

---

# 5. Rules

Detailed implementation rules.

---

# 6. Validation

How compliance is verified.

---

# 7. Compliance

Acceptance criteria.

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

# 5. Requirements Section

Every standard shall define mandatory requirements.

Format:

```markdown
## Requirement 01: Requirement Name

Description:

The system shall...

Reason:

Explanation of requirement importance.
```

Requirements should be:

- Clear.
- Testable.
- Specific.
- Consistent.

---

# 6. Rules Section

Rules define implementation details.

Example:

```markdown
## Rule 01: Naming Format

All document identifiers shall follow:

FS-XXX-Name.md
```

Rules should avoid ambiguity.

---

# 7. Validation Section

Every standard shall define validation methods.

Example:

```markdown
# Validation

Compliance is verified through:

- Document review.
- Automated checks.
- Repository validation.
```

---

# 8. Compliance Section

Recommended format:

```markdown
# Compliance

A document complies with this standard when:

- All mandatory requirements are satisfied.
- Validation checks pass.
- Exceptions are approved.
```

---

# 9. Relationship Mapping

Standards should identify:

## Based On

Higher-level principles.

Example:

```text
Based On:

- FP-004 Documentation Principles
```

---

## Supports

Related policies or processes.

Example:

```text
Supports:

- POL-001 Change Control Policy
```

---

# 10. Standard Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Purpose defined | Yes |
| Scope defined | Yes |
| Requirements included | Yes |
| Rules documented | Yes |
| Validation defined | Yes |
| Compliance defined | Yes |
| References added | Yes |

---

# 11. Lifecycle

Standards follow:

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
Deprecated
 ↓
Archived
```

---

# 12. Compliance

All FS-xxx documents shall follow this template.

Any deviation requires approval according to POL-005 Exception Policy.

---

# 13. References

- TMP-001 Document Template
- TMP-002 Principle Template
- FS-001 Documentation Standards
- FS-010 Template Standard
- POL-010 Lifecycle Policy

---

# 14. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Standard Template |

---

# End of Document