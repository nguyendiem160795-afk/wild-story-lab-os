---
document_id: TMP-006
module: 01
category: Templates
title: Review Template (Mẫu Đánh giá)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Review Template (Mẫu Đánh giá)

> Official reusable template for creating review records within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for recording reviews, evaluations, findings, decisions, and improvement actions across EAOSS.

The objective is to ensure every review activity is consistent, traceable, objective, and auditable.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Documentation Review
- Architecture Review
- Compliance Review
- Quality Review
- Security Review
- Governance Review
- Release Review

Naming format:

```text
RV-XXX-Review-Name.md
```

Example:

```text
RV-001-Architecture-Review.md
```

---

# 3. Metadata Template

Every review document shall begin with:

```yaml
---
document_id: RV-XXX
module:
category: Review
title:
review_type:
artifact_reviewed:
version_reviewed:
reviewer:
review_date:
status:
---
```

---

# 4. Review Document Structure

Every review record should follow:

```markdown
# Review Title

> Short description of review purpose.

---

# 1. Review Purpose

Why this review was conducted.

---

# 2. Artifact Reviewed

Information about reviewed artifact.

---

# 3. Review Scope

Boundaries of evaluation.

---

# 4. Review Criteria

Evaluation requirements.

---

# 5. Review Participants

People or systems involved.

---

# 6. Findings

Issues and observations.

---

# 7. Recommendations

Suggested improvements.

---

# 8. Decision

Final review outcome.

---

# 9. Action Items

Required follow-up activities.

---

# 10. References

Related artifacts.

---

# 11. Revision History

Change records.

---

# End of Document
```

---

# 5. Review Information Section

Every review shall identify:

| Field | Description |
|---|---|
| Review ID | Unique review identifier |
| Review Type | Type of evaluation |
| Artifact | Object being reviewed |
| Version | Version evaluated |
| Date | Review date |
| Participants | Review members |

---

# 6. Review Criteria Section

Criteria should be measurable.

Example:

```markdown
## Criterion 01: Documentation Compliance

Requirement:

Document follows FS-001 Documentation Standard.

Result:

Pass / Fail / Partial
```

---

# 7. Findings Section

All findings should follow:

```markdown
## Finding ID: F-001

Category:

Severity:

Description:

Impact:

Recommendation:
```

---

# 8. Finding Severity

Standard severity levels:

| Level | Meaning |
|---|---|
| Critical | Immediate correction required |
| Major | Significant issue |
| Minor | Limited issue |
| Observation | Improvement suggestion |

---

# 9. Review Decision

Possible outcomes:

| Decision | Meaning |
|---|---|
| Approved | Meets requirements |
| Approved with Changes | Minor corrections required |
| Revision Required | Additional work needed |
| Rejected | Does not meet requirements |

---

# 10. Action Item Template

```markdown
## Action ID: A-001

Action:

Owner:

Due Date:

Status:
```

---

# 11. Review Quality Checklist

Before closing review:

| Requirement | Mandatory |
|---|---|
| Scope defined | Yes |
| Criteria defined | Yes |
| Evidence recorded | Yes |
| Findings documented | Yes |
| Decision recorded | Yes |
| Actions assigned | Yes |

---

# 12. Lifecycle

Review records follow:

```text
Created
 ↓
Conducted
 ↓
Findings Recorded
 ↓
Decision Made
 ↓
Actions Completed
 ↓
Closed
 ↓
Archived
```

---

# 13. Compliance

All formal EAOSS reviews should use this template.

Exceptions require approval according to POL-005 Exception Policy.

---

# 14. References

- FS-008 Review Standard
- POL-004 Governance Policy
- POL-009 Audit Policy
- TMP-001 Document Template
- TMP-010 README Template

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Review Template |

---

# End of Document