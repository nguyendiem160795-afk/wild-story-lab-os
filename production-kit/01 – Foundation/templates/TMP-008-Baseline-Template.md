---
document_id: TMP-008
module: 01
category: Templates
title: Baseline Template (Mẫu Phiên bản Chuẩn)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Baseline Template (Mẫu Phiên bản Chuẩn)

> Official reusable template for creating baseline records within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for creating EAOSS baseline records.

The objective is to establish controlled snapshots of approved artifacts, architectures, standards, and governance states.

---

# 2. Usage (Cách sử dụng)

Baseline records are used for:

- Official releases.
- Architecture milestones.
- Governance checkpoints.
- Production states.
- Historical reference points.

Naming format:

```text
BASELINE-XXX-Baseline-Name.md
```

Example:

```text
BASELINE-001-Foundation-v1.md
```

---

# 3. Metadata Template

Every baseline document shall begin with:

```yaml
---
document_id: BASELINE-XXX
module:
category: Baseline
title:
baseline_version:
release_date:
status:
owner:
approved_by:
last_updated:
---
```

---

# 4. Baseline Document Structure

Every baseline shall follow:

```markdown
# Baseline Title

> Short description of baseline purpose.

---

# 1. Baseline Purpose

Why this baseline exists.

---

# 2. Baseline Scope

What is included.

---

# 3. Included Artifacts

Approved components.

---

# 4. Version Information

Version details.

---

# 5. Approval Information

Governance approval.

---

# 6. Change Summary

Major changes.

---

# 7. Dependencies

Required relationships.

---

# 8. Validation Results

Verification status.

---

# 9. References

Related documents.

---

# 10. Revision History

Change records.

---

# End of Document
```

---

# 5. Baseline Identification

Every baseline shall contain:

| Field | Description |
|---|---|
| Baseline ID | Unique identifier |
| Version | Official version |
| Date | Creation date |
| Owner | Responsible authority |
| Status | Lifecycle state |

---

# 6. Baseline Scope

Scope shall define:

- Included modules.
- Included artifacts.
- Excluded items.
- Known limitations.

Example:

```markdown
Included:

- Foundation Principles v1.0
- Foundation Standards v1.0
- Foundation Policies v1.0
```

---

# 7. Artifact Inventory

Every baseline should list included artifacts.

Example:

| ID | Artifact | Version |
|---|---|---|
| FP-001 | Architecture Principles | 1.0.0 |
| FS-001 | Documentation Standard | 1.0.0 |
| POL-001 | Change Control Policy | 1.0.0 |

---

# 8. Approval Section

Baseline approval shall record:

```markdown
Approved By:

Role:

Approval Date:

Decision:
```

---

# 9. Validation Section

Validation should confirm:

- Required artifacts exist.
- Versions are correct.
- References are valid.
- Reviews are completed.
- Compliance requirements are satisfied.

---

# 10. Baseline Change Management

Existing baselines shall not be modified directly.

Changes require:

- New baseline version.
- Change assessment.
- Review approval.
- Updated records.

---

# 11. Baseline Quality Checklist

Before publication:

| Requirement | Mandatory |
|---|---|
| Scope defined | Yes |
| Artifacts listed | Yes |
| Versions verified | Yes |
| Approval recorded | Yes |
| Validation completed | Yes |
| References updated | Yes |

---

# 12. Lifecycle

Baseline lifecycle:

```text
Draft
 ↓
Review
 ↓
Approved
 ↓
Published
 ↓
Referenced
 ↓
Superseded
 ↓
Archived
```

---

# 13. Compliance

All official EAOSS baselines shall use this template.

Baseline changes must follow POL-001 Change Control Policy.

---

# 14. References

- POL-001 Change Control Policy
- POL-002 Release Policy
- POL-010 Lifecycle Policy
- FS-003 Versioning Standard
- FS-007 Cross Reference Standard

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Baseline Template |

---

# End of Documents