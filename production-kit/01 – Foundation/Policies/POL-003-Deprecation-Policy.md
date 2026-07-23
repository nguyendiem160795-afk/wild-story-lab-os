---
document_id: POL-003
module: 01
category: Policies
title: Deprecation Policy (Chính sách Ngừng sử dụng)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Deprecation Policy (Chính sách Ngừng sử dụng)

> Official artifact deprecation policy for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This policy defines the governance rules for identifying, marking, managing, replacing, and retiring deprecated EAOSS artifacts.

The purpose is to ensure controlled evolution while preserving historical knowledge, traceability, and repository integrity.

---

# 2. Objectives (Mục tiêu)

This policy aims to:

- Prevent uncontrolled deletion of valuable artifacts.
- Maintain historical traceability.
- Provide clear migration paths.
- Reduce confusion between active and obsolete content.
- Support long-term repository evolution.

---

# 3. Scope (Phạm vi)

This policy applies to:

- Documents
- Standards
- Policies
- Principles
- Templates
- Architecture artifacts
- Baselines
- Repository structures
- Future EAOSS assets

---

# 4. Deprecation Definition

An artifact is considered deprecated when:

- It is no longer the recommended approach.
- A newer replacement exists.
- Its usage should gradually decrease.
- It remains available for historical reference.

Deprecated does not mean deleted.

---

# 5. Artifact Lifecycle

EAOSS artifact lifecycle:

```text
Draft
  ↓
Review
  ↓
Approved
  ↓
Production Ready
  ↓
Deprecated
  ↓
Archived
```

---

# 6. Deprecation Reasons

An artifact may be deprecated because of:

| Reason | Description |
|--------|-------------|
| Replacement | New artifact supersedes old version |
| Obsolescence | No longer applicable |
| Redundancy | Functionality duplicated elsewhere |
| Architecture Change | System direction changed |
| Standard Evolution | New standard introduced |

---

# 7. Deprecation Requirements

Before deprecation, the artifact shall include:

- Deprecation reason
- Deprecation date
- Replacement artifact (if available)
- Migration guidance
- Owner confirmation

---

# 8. Deprecation Metadata

Deprecated artifacts shall update metadata:

Example:

```yaml
status: Deprecated
deprecated_date: YYYY-MM-DD
replacement:
  - NEW-ARTIFACT-ID
```

---

# 9. Deprecation Notice

A deprecated artifact shall contain a notice:

Example:

```markdown
> Deprecated:
> This artifact has been replaced by [NEW ARTIFACT].
> It remains available for historical reference.
```

---

# 10. Replacement Rules

Replacement artifacts should:

- Clearly identify the previous artifact.
- Provide migration guidance.
- Preserve important historical decisions.
- Maintain cross references.

---

# 11. Deprecation Review

Before approval, review shall verify:

- Deprecation reason is valid.
- Replacement exists or justification is provided.
- Dependencies are analyzed.
- References are updated.

---

# 12. Archive Rules

An artifact may be archived when:

- Replacement adoption is complete.
- No active dependencies remain.
- Historical value has been preserved.
- Governance approval is obtained.

---

# 13. Deletion Restrictions

Permanent deletion is prohibited when an artifact:

- Supports historical decisions.
- Is referenced by approved documents.
- Provides audit evidence.
- Contains architectural rationale.

---

# 14. Deprecation Checklist

| Requirement | Mandatory |
|-------------|-----------|
| Reason documented | Yes |
| Owner approved | Yes |
| Replacement identified | Recommended |
| References updated | Yes |
| Metadata updated | Yes |
| Changelog updated | Yes |

---

# 15. Compliance

All deprecated EAOSS artifacts shall comply with this policy.

Uncontrolled deletion of governed artifacts is prohibited.

---

# 16. References

- FP-005 Governance Principles
- FP-007 Versioning Policy
- FS-003 Versioning Standard
- FS-007 Cross Reference Standard
- POL-001 Change Control Policy
- POL-002 Release Policy

---

# 17. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Deprecation Policy |

---

# End of Document