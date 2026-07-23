---
document_id: TMP-004
module: 01
category: Templates
title: Policy Template (Mẫu Chính sách)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Policy Template (Mẫu Chính sách)

> Official reusable template for creating Foundation Policies (POL-xxx) within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for creating EAOSS Policy documents.

The objective is to ensure every policy clearly defines governance rules, responsibilities, enforcement mechanisms, and controlled exceptions.

---

# 2. Usage (Cách sử dụng)

This template is used for:

- Governance Policies
- Security Policies
- Change Policies
- Release Policies
- Access Policies
- Data Policies
- Audit Policies
- Lifecycle Policies

Naming format:

```text
POL-XXX-Policy-Name.md
```

Example:

```text
POL-001-Change-Control-Policy.md
```

---

# 3. Metadata Template

Every policy shall begin with:

```yaml
---
document_id: POL-XXX
module: 01
category: Policies
title:
version:
status:
classification:
owner:
last_updated:
---
```

---

# 4. Policy Document Structure

Every Policy shall follow:

```markdown
# Policy Title

> Short description of policy purpose.

---

# 1. Purpose

Why this policy exists.

---

# 2. Objectives

Expected governance outcomes.

---

# 3. Scope

Where this policy applies.

---

# 4. Policy Principles

Core governance statements.

---

# 5. Policy Requirements

Mandatory rules.

---

# 6. Responsibilities

Roles and ownership.

---

# 7. Enforcement

How compliance is ensured.

---

# 8. Exceptions

Controlled deviation process.

---

# 9. Compliance

Validation requirements.

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

# 5. Policy Principles Section

This section defines the foundation of the policy.

Format:

```markdown
## Policy Principle 01: Principle Name

Statement:

The organization shall...

Rationale:

Explanation of governance purpose.
```

Policy principles should align with:

- Foundation Principles
- Governance Principles
- Security Principles

---

# 6. Policy Requirements Section

Requirements define mandatory governance rules.

Format:

```markdown
## Requirement 01: Requirement Name

Rule:

The system shall...

Owner:

Responsible role.

Validation:

How compliance is checked.
```

Requirements should be:

- Clear.
- Enforceable.
- Measurable.

---

# 7. Responsibilities Section

Every policy shall define ownership.

Example:

| Role | Responsibility |
|---|---|
| Owner | Maintains policy |
| Reviewer | Validates compliance |
| Approver | Authorizes changes |
| Contributor | Provides updates |

---

# 8. Enforcement Section

This section defines how the policy is applied.

Examples:

- Review process.
- Automated validation.
- Governance checks.
- Audit activities.

---

# 9. Exception Section

Every policy shall define:

- When exceptions are allowed.
- Who approves exceptions.
- How exceptions are tracked.

Example:

```markdown
Exceptions require:

- Documented justification.
- Impact assessment.
- Approval record.
```

---

# 10. Compliance Section

Recommended format:

```markdown
# Compliance

Compliance is achieved when:

- Requirements are satisfied.
- Responsibilities are assigned.
- Reviews are completed.
- Exceptions are controlled.
```

---

# 11. Policy Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Purpose defined | Yes |
| Scope defined | Yes |
| Requirements documented | Yes |
| Responsibilities defined | Yes |
| Enforcement defined | Yes |
| Exceptions defined | Yes |
| References added | Yes |

---

# 12. Lifecycle

Policies follow:

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

# 13. Compliance

All POL-xxx documents shall follow this template.

Any deviation requires approval according to POL-005 Exception Policy.

---

# 14. References

- TMP-001 Document Template
- TMP-003 Standard Template
- FS-010 Template Standard
- POL-004 Governance Policy
- POL-010 Lifecycle Policy

---

# 15. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Policy Template |

---

# End of Document