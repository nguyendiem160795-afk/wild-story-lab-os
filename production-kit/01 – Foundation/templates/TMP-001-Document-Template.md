---
document_id: TMP-001
module: 01
category: Templates
title: Document Template (Mẫu Tài liệu Chuẩn)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Document Template (Mẫu Tài liệu Chuẩn)

> Official reusable document template for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for creating EAOSS documentation artifacts.

The objective is to ensure every document follows a consistent format, contains required metadata, and supports governance, review, and lifecycle management.

---

# 2. Usage (Cách sử dụng)

This template is used as the foundation for:

- Principles
- Standards
- Policies
- Specifications
- Architecture documents
- Reviews
- Reports

Specific document types may extend this template.

---

# 3. Metadata Template

Every document shall begin with:

```yaml
---
document_id:
module:
category:
title:
version:
status:
classification:
owner:
last_updated:
---
```

---

# 4. Document Structure Template

```markdown
# Document Title

> Short description of document purpose.

---

# 1. Purpose

Explain why this document exists.

---

# 2. Objectives

Define expected outcomes.

---

# 3. Scope

Define applicability and boundaries.

---

# 4. Main Content

Provide the primary information.

---

# 5. Compliance

Define requirements and validation.

---

# 6. References

List related documents.

---

# 7. Revision History

Track document changes.

---

# End of Document
```

---

# 5. Required Sections

Every normative document should include:

| Section | Required |
|---|---|
| Metadata | Yes |
| Title | Yes |
| Purpose | Yes |
| Scope | Yes |
| Main Content | Yes |
| References | Yes |
| Revision History | Yes |

---

# 6. Document Header Rules

The header shall contain:

- Official title.
- Short description.
- Document classification.
- Document identifier.

Example:

```markdown
# Architecture Principles

> Canonical architecture principles for EAOSS.
```

---

# 7. Content Writing Rules

Documents created from this template should:

- Use clear language.
- Avoid duplicated information.
- Reference canonical sources.
- Maintain consistent terminology.
- Follow Markdown Standard.

---

# 8. Compliance Section Template

Recommended format:

```markdown
# Compliance

This document complies with:

- FP-001 Architecture Principles
- FS-001 Documentation Standard
- POL-004 Governance Policy
```

---

# 9. References Section Template

Recommended format:

```markdown
# References

- FP-001 Architecture Principles
- FS-002 Naming Standard
- POL-001 Change Control Policy
```

---

# 10. Revision History Template

Required format:

| Version | Date | Description |
|---|---|---|
| 1.0.0 | YYYY-MM-DD | Initial release |

---

# 11. Validation Checklist

Before publishing:

| Requirement | Status |
|---|---|
| Metadata completed | Required |
| Correct template used | Required |
| References added | Required |
| Version assigned | Required |
| Review completed | Required |

---

# 12. Lifecycle

Template lifecycle:

```
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
```

---

# 13. Compliance

All new EAOSS documents should use an approved template.

Exceptions require approval according to POL-005 Exception Policy.

---

# 14. References

- FS-001 Documentation Standard
- FS-004 Metadata Standard
- FS-010 Template Standard
- POL-010 Lifecycle Policy

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Document Template |

---

# End of Document