---
document_id: TMP-009
module: 01
category: Templates
title: Changelog Template (Mẫu Nhật ký Thay đổi)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Changelog Template (Mẫu Nhật ký Thay đổi)

> Official reusable template for maintaining change history within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for recording changes, updates, improvements, fixes, and evolution history of EAOSS artifacts.

The objective is to maintain transparency, traceability, and historical understanding of system evolution.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Documents
- Modules
- Standards
- Policies
- Architecture artifacts
- Releases
- Baselines

Naming format:

```text
CHANGELOG.md
```

or:

```text
CHG-XXX-Change-Record.md
```

---

# 3. Metadata Template

Every changelog document should begin with:

```yaml
---
document_id:
category: Changelog
artifact:
current_version:
owner:
last_updated:
---
```

---

# 4. Changelog Structure

Every changelog should follow:

```markdown
# Changelog

> History of changes for this artifact.

---

# Version X.X.X

Date:

Change Type:

Summary:

Impact:

Related Records:

---

# Previous Versions

Historical changes.
```

---

# 5. Change Entry Format

Every change entry shall include:

| Field | Description |
|---|---|
| Version | New artifact version |
| Date | Change date |
| Author | Person/system making change |
| Type | Category of change |
| Summary | Description |
| Impact | Effect of change |

---

# 6. Change Types

Standard change categories:

| Type | Meaning |
|---|---|
| Added | New capability |
| Changed | Modified behavior |
| Fixed | Correction |
| Removed | Deleted capability |
| Deprecated | Marked obsolete |
| Security | Security improvement |

---

# 7. Change Record Template

Example:

```markdown
## Version 1.2.0

Date:

2026-07-23

Type:

Added

Summary:

Added metadata validation requirements.

Impact:

Improves documentation consistency.

Related:

FS-004 Metadata Standard
```

---

# 8. Change Traceability

Every significant change should reference:

- Change Request ID.
- Review Record.
- Related ADR.
- Approval record.

Example:

```text
Related:

CR-001
ADR-005
RV-003
```

---

# 9. Breaking Change Documentation

Breaking changes shall clearly identify:

- Previous behavior.
- New behavior.
- Migration requirements.
- Compatibility impact.

---

# 10. Changelog Rules

A changelog shall:

- Never delete historical entries.
- Keep chronological order.
- Match version history.
- Use approved terminology.
- Maintain accuracy.

---

# 11. Quality Checklist

Before release:

| Requirement | Mandatory |
|---|---|
| Version updated | Yes |
| Date recorded | Yes |
| Change type defined | Yes |
| Impact described | Yes |
| Related artifacts linked | Yes |

---

# 12. Lifecycle

Changelog lifecycle:

```text
Created
 ↓
Updated
 ↓
Reviewed
 ↓
Published
 ↓
Maintained
 ↓
Archived
```

---

# 13. Compliance

All Production Ready artifacts shall maintain accurate change history.

Missing or inaccurate changelog information is considered a documentation quality issue.

---

# 14. References

- FS-003 Versioning Standard
- FS-007 Cross Reference Standard
- POL-001 Change Control Policy
- POL-002 Release Policy
- POL-009 Audit Policy

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Changelog Template |

---

# End of Documents