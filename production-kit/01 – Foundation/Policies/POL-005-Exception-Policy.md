---
document_id: POL-005
module: 01
category: Policies
title: Exception Policy (Chính sách Ngoại lệ)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Exception Policy (Chính sách Ngoại lệ)

> Official exception management policy for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This policy defines the governance rules for requesting, evaluating, approving, monitoring, and retiring exceptions to EAOSS principles, standards, policies, and requirements.

The purpose is to ensure that deviations are controlled, justified, temporary, and traceable.

---

# 2. Objectives (Mục tiêu)

This policy aims to:

- Prevent uncontrolled deviations.
- Protect architectural consistency.
- Provide a formal exception process.
- Maintain accountability.
- Reduce long-term technical and governance risks.

---

# 3. Scope (Phạm vi)

This policy applies to exceptions involving:

- Architecture principles
- Documentation standards
- Naming conventions
- Versioning rules
- Repository structures
- Review requirements
- Governance processes
- Quality requirements

---

# 4. Exception Definition

An exception is:

> An approved deviation from an established EAOSS requirement.

An exception does not invalidate the original requirement.

The original standard remains the default expectation.

---

# 5. Exception Principles

All exceptions shall follow these principles:

## Justified

Every exception requires a documented reason.

---

## Temporary

Exceptions should have a defined review or expiration date.

---

## Controlled

Exceptions require approval before implementation.

---

## Traceable

Every exception must maintain records.

---

# 6. Exception Categories

| Category | Description |
|---|---|
| Documentation Exception | Deviation from documentation rules |
| Technical Exception | Technical constraint prevents compliance |
| Architecture Exception | Deviation from architecture rules |
| Process Exception | Deviation from workflow requirements |
| Emergency Exception | Urgent deviation requiring rapid approval |

---

# 7. Exception Request Requirements

Every exception request shall include:

| Field | Required |
|---|---|
| Exception ID | Yes |
| Requester | Yes |
| Affected Requirement | Yes |
| Reason | Yes |
| Impact Analysis | Yes |
| Risk Assessment | Yes |
| Proposed Duration | Yes |
| Approval Status | Yes |

---

# 8. Exception Lifecycle

Exceptions follow:

```text
Request
   ↓
Assessment
   ↓
Risk Evaluation
   ↓
Approval
   ↓
Implementation
   ↓
Monitoring
   ↓
Review
   ↓
Closure
```

---

# 9. Impact Assessment

Before approval, evaluate:

## Architectural Impact

- System consistency
- Dependencies
- Future scalability

## Operational Impact

- Maintenance effort
- Additional complexity
- Long-term cost

## Governance Impact

- Compliance risks
- Review requirements

---

# 10. Approval Authority

Approval depends on impact.

| Exception Type | Approval |
|---|---|
| Documentation Exception | Artifact Owner |
| Standard Exception | Technical Reviewer |
| Architecture Exception | Architecture Review |
| Governance Exception | Governance Authority |

---

# 11. Exception Duration

Every exception shall define:

- Start date
- Review date
- Expiration date (when applicable)

Permanent exceptions require formal governance approval.

---

# 12. Exception Records

Approved exceptions shall maintain:

- Exception ID
- Requirement affected
- Approval decision
- Owner
- Expiration status
- Related artifacts

---

# 13. Exception Monitoring

Active exceptions should be reviewed periodically.

Review should determine:

- Continue exception
- Modify exception
- Remove exception
- Convert exception into a permanent standard change

---

# 14. Exception Closure

An exception is closed when:

- The original requirement is satisfied.
- Replacement solution is implemented.
- Exception expires.
- Governance approval removes the exception.

---

# 15. Prohibited Exceptions

Exceptions shall not be used to:

- Avoid required reviews indefinitely.
- Ignore security requirements.
- Bypass governance.
- Hide poor planning.

---

# 16. Exception Checklist

| Requirement | Mandatory |
|---|---|
| Reason documented | Yes |
| Impact assessed | Yes |
| Risk evaluated | Yes |
| Approval recorded | Yes |
| Review date defined | Yes |
| Closure tracked | Yes |

---

# 17. Compliance

All EAOSS exceptions shall comply with this policy.

Unapproved deviations are considered non-compliance.

---

# 18. References

- FP-005 Governance Principles
- FP-009 Review Process
- FP-010 Quality Principles
- POL-001 Change Control Policy
- POL-004 Governance Policy
- FS-008 Review Standard

---

# 19. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Exception Policy |

---

# End of Document