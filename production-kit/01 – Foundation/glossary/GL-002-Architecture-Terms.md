---
document_id: GL-002
module: 01
category: Glossary
title: Architecture Terms (Thuật ngữ Kiến trúc)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Architecture Terms (Thuật ngữ Kiến trúc)

> Official architecture terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This glossary defines architecture-related terminology used throughout EAOSS.

The purpose is to create a consistent architectural language for:

- Architecture design.
- Architecture decisions.
- System modeling.
- AI-assisted architecture reasoning.

---

# 2. Architecture

## Vietnamese:
Kiến trúc

## Definition:

Architecture is the fundamental structure of a system, including its components, relationships, constraints, and design principles.

Architecture describes:

- What exists.
- How components interact.
- Why decisions are made.

---

# 3. Enterprise Architecture (EA)

## Vietnamese:
Kiến trúc Doanh nghiệp

## Definition:

Enterprise Architecture defines the overall structure, capabilities, processes, information, and technologies of an organization.

Purpose:

- Align business and technology.
- Support strategic decisions.
- Manage complexity.

---

# 4. System Architecture

## Vietnamese:
Kiến trúc Hệ thống

## Definition:

System Architecture describes the structure of a specific system, including components, interfaces, data flows, and behaviors.

---

# 5. Architecture Layer

## Vietnamese:
Lớp kiến trúc

## Definition:

A Layer is a logical separation of responsibilities within an architecture.

Examples:

```text
Presentation Layer
        ↓
Application Layer
        ↓
Data Layer
        ↓
Infrastructure Layer
```

Purpose:

- Reduce complexity.
- Separate concerns.
- Improve maintainability.

---

# 6. Component

## Vietnamese:
Thành phần

## Definition:

A Component is a distinct architectural element responsible for a specific capability or function.

A component has:

- Responsibility.
- Interface.
- Dependencies.
- Ownership.

---

# 7. System Boundary

## Vietnamese:
Ranh giới hệ thống

## Definition:

A System Boundary defines what is inside and outside the responsibility of a system.

Purpose:

- Clarify ownership.
- Control complexity.
- Define interactions.

---

# 8. Interface

## Vietnamese:
Giao diện kết nối

## Definition:

An Interface defines how components communicate and exchange information.

Examples:

- API.
- Message interface.
- Data contract.

---

# 9. Dependency

## Vietnamese:
Sự phụ thuộc

## Definition:

A Dependency exists when one component requires another component to function.

Example:

```text
AI Agent
    ↓
Knowledge Base
    ↓
Vector Database
```

---

# 10. Architecture Pattern

## Vietnamese:
Mẫu kiến trúc

## Definition:

An Architecture Pattern is a reusable solution approach for common architecture problems.

Examples:

- Layered Architecture.
- Event-driven Architecture.
- Microservices Architecture.

---

# 11. Reference Architecture

## Vietnamese:
Kiến trúc tham chiếu

## Definition:

A Reference Architecture is a reusable architecture model that guides future designs.

Purpose:

- Standardization.
- Faster design.
- Reduced risk.

---

# 12. Architecture Decision

## Vietnamese:
Quyết định kiến trúc

## Definition:

An Architecture Decision is a documented choice that influences system structure or evolution.

Example:

Choosing:

- Database technology.
- Integration approach.
- AI model strategy.

---

# 13. Architecture Decision Record (ADR)

## Vietnamese:
Bản ghi quyết định kiến trúc

## Definition:

ADR is a document that records:

- Context.
- Decision.
- Alternatives.
- Consequences.

Purpose:

Preserve architectural knowledge.

---

# 14. Architecture View

## Vietnamese:
Góc nhìn kiến trúc

## Definition:

An Architecture View represents a specific perspective of a system.

Examples:

- Security View.
- Data View.
- Deployment View.
- Logical View.

---

# 15. Architecture Model

## Vietnamese:
Mô hình kiến trúc

## Definition:

An Architecture Model is a representation of system structure and relationships.

Examples:

- Diagram.
- Graph.
- Documentation model.

---

# 16. Architecture Governance

## Vietnamese:
Quản trị kiến trúc

## Definition:

Architecture Governance ensures architecture decisions follow principles, standards, and policies.

---

# 17. Constraint

## Vietnamese:
Ràng buộc

## Definition:

A Constraint is a limitation or requirement affecting architecture decisions.

Examples:

- Security requirement.
- Performance limit.
- Technology restriction.

---

# 18. Architecture Evolution

## Vietnamese:
Sự phát triển kiến trúc

## Definition:

Architecture Evolution describes how architecture changes over time.

Includes:

- New capabilities.
- Migration.
- Optimization.
- Retirement.

---

# 19. Architecture Quality Checklist

| Requirement | Mandatory |
|---|---|
| Terms clearly defined | Yes |
| Vietnamese meaning included | Yes |
| Related concepts mapped | Yes |
| Usage context provided | Yes |

---

# 20. References

- GL-001 Core Terms
- TMP-005 Architecture Template
- TMP-007 ADR Template
- POL-004 Governance Policy

---

# 21. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Architecture Terms Glossary |

---

# End of Document