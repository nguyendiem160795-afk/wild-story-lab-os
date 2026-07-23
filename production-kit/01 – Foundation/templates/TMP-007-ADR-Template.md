---
document_id: TMP-007
module: 01
category: Templates
title: ADR Template (Mẫu Architecture Decision Record)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# ADR Template (Mẫu Architecture Decision Record)

> Official reusable template for recording architecture decisions within the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This template defines the standard structure for Architecture Decision Records (ADR).

The objective is to preserve architectural decisions, reasoning, alternatives, consequences, and historical context throughout EAOSS evolution.

---

# 2. Usage (Cách sử dụng)

ADR is used when making decisions that impact:

- Architecture direction.
- System structure.
- Technology selection.
- Data models.
- Integration patterns.
- AI workflows.
- Governance models.

Naming format:

```text
ADR-XXX-Decision-Name.md
```

Example:

```text
ADR-001-Knowledge-Base-Architecture.md
```

---

# 3. Metadata Template

Every ADR shall begin with:

```yaml
---
document_id: ADR-XXX
module:
category: Architecture Decision Record
title:
status:
decision_date:
owner:
reviewers:
related_artifacts:
last_updated:
---
```

---

# 4. ADR Document Structure

Every ADR should follow:

```markdown
# ADR Title

> Short description of the decision.

---

# 1. Decision Status

Current state of decision.

---

# 2. Context

Background and problem statement.

---

# 3. Decision

Chosen solution.

---

# 4. Alternatives Considered

Other options evaluated.

---

# 5. Decision Rationale

Why this option was selected.

---

# 6. Consequences

Positive and negative impacts.

---

# 7. Implementation Notes

Execution considerations.

---

# 8. Related Decisions

Connected ADRs.

---

# 9. References

Supporting information.

---

# 10. Revision History

Change records.

---

# End of Document
```

---

# 5. Decision Status

ADR status shall use:

| Status | Meaning |
|---|---|
| Proposed | Under evaluation |
| Accepted | Official decision |
| Rejected | Not selected |
| Superseded | Replaced by another ADR |
| Deprecated | No longer applicable |

---

# 6. Context Section

The context shall explain:

- Current situation.
- Existing problem.
- Constraints.
- Business or technical drivers.
- Decision requirements.

A decision without context is incomplete.

---

# 7. Decision Section

The decision shall clearly describe:

- Selected approach.
- Main characteristics.
- Expected usage.

Example:

```markdown
Decision:

Adopt repository-first architecture as the canonical knowledge model.
```

---

# 8. Alternatives Section

Every significant ADR should document alternatives.

Format:

```markdown
## Alternative A

Description:

Advantages:

Disadvantages:

Reason rejected:
```

---

# 9. Rationale Section

The rationale explains:

- Why the decision was selected.
- How it aligns with principles.
- Expected long-term benefits.

---

# 10. Consequences Section

Consequences should include:

## Positive Consequences

Benefits created.

## Negative Consequences

Trade-offs introduced.

## Risks

Potential future issues.

---

# 11. Relationship Mapping

ADR should identify:

## Related Principles

Example:

```text
FP-001 Architecture Principles
```

## Related Standards

Example:

```text
FS-005 Repository Structure Standard
```

## Related Policies

Example:

```text
POL-004 Governance Policy
```

---

# 12. ADR Quality Checklist

Before approval:

| Requirement | Mandatory |
|---|---|
| Context defined | Yes |
| Decision clear | Yes |
| Alternatives evaluated | Yes |
| Rationale documented | Yes |
| Consequences identified | Yes |
| Related artifacts mapped | Yes |

---

# 13. Lifecycle

ADR lifecycle:

```text
Proposed
 ↓
Review
 ↓
Accepted
 ↓
Implemented
 ↓
Maintained
 ↓
Superseded
 ↓
Archived
```

---

# 14. Compliance

All major architecture decisions should have an ADR record.

Exceptions require governance approval.

---

# 15. References

- TMP-005 Architecture Template
- FS-007 Cross Reference Standard
- POL-004 Governance Policy
- POL-010 Lifecycle Policy

---

# 16. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial ADR Template |

---

# End of Documents