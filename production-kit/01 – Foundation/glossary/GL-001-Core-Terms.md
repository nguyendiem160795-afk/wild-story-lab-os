---
document_id: GL-001
module: 01
category: Glossary
title: Core Terms (Thuật ngữ Cốt lõi)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Core Terms (Thuật ngữ Cốt lõi)

> Official foundational terminology dictionary for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This glossary defines the fundamental terms used throughout EAOSS.

The purpose is to establish a shared vocabulary for:

- Humans.
- AI Agents.
- Documentation.
- Architecture.
- Governance processes.

---

# 2. Usage (Cách sử dụng)

All EAOSS documents should use terminology defined in this glossary.

If a new important term is introduced:

- It should be added to the glossary.
- Its meaning should be documented.
- Related concepts should be linked.

---

# 3. Core Terminology

---

# Term: Artifact

## Vietnamese:
Tài sản hệ thống / Đối tượng quản lý

## Definition:

An Artifact is any managed object created, maintained, reviewed, or governed within EAOSS.

## Examples:

- Document.
- Standard.
- Policy.
- Template.
- Architecture record.
- Baseline.

## Related:

- Asset
- Document
- Repository

---

# Term: Asset

## Vietnamese:
Tài sản

## Definition:

An Asset is a valuable resource that provides knowledge, capability, or operational value.

## Examples:

- Character asset.
- Knowledge asset.
- Template asset.
- AI prompt asset.

## Related:

- Artifact
- Library
- Repository

---

# Term: Repository

## Vietnamese:
Kho lưu trữ

## Definition:

A Repository is an organized location where EAOSS artifacts are stored, managed, versioned, and accessed.

## Purpose:

Provides:

- Organization.
- Traceability.
- Collaboration.
- Lifecycle management.

---

# Term: Module

## Vietnamese:
Mô-đun

## Definition:

A Module is a logical organizational unit containing related capabilities, documents, and assets.

## Example:

```text
01-foundation
02-architecture
03-ai-system
```

---

# Term: Framework

## Vietnamese:
Khung hệ thống

## Definition:

A Framework is a structured collection of principles, standards, processes, and tools designed to solve a specific class of problems.

---

# Term: Principle

## Vietnamese:
Nguyên lý

## Definition:

A Principle is a fundamental belief or guideline that guides decisions.

## Characteristics:

- Long-lasting.
- Strategic.
- Directional.

Example:

"Repository-first architecture."

---

# Term: Standard

## Vietnamese:
Tiêu chuẩn

## Definition:

A Standard is a mandatory rule that defines how something should be implemented.

## Characteristics:

- Specific.
- Measurable.
- Enforceable.

---

# Term: Policy

## Vietnamese:
Chính sách

## Definition:

A Policy defines governance rules, responsibilities, and control mechanisms.

## Purpose:

Ensures consistent management and decision-making.

---

# Term: Template

## Vietnamese:
Mẫu chuẩn

## Definition:

A Template is a reusable structure used to create consistent artifacts.

Examples:

- Document Template.
- Review Template.
- ADR Template.

---

# Term: Governance

## Vietnamese:
Quản trị

## Definition:

Governance is the system of authority, responsibility, decision-making, and control.

---

# Term: Lifecycle

## Vietnamese:
Vòng đời

## Definition:

Lifecycle describes the complete journey of an artifact from creation to retirement.

Example:

```text
Create
 ↓
Review
 ↓
Approve
 ↓
Maintain
 ↓
Archive
```

---

# Term: Baseline

## Vietnamese:
Phiên bản chuẩn

## Definition:

A Baseline is an approved snapshot of system artifacts at a specific point in time.

Purpose:

- Reference.
- Comparison.
- Stability.

---

# Term: Version

## Vietnamese:
Phiên bản

## Definition:

A Version identifies a specific state of an artifact.

Example:

```text
v1.0.0
```

---

# Term: Review

## Vietnamese:
Đánh giá

## Definition:

A Review is a structured evaluation process to verify quality, correctness, and compliance.

---

# Term: Compliance

## Vietnamese:
Tuân thủ

## Definition:

Compliance means satisfying defined requirements, standards, and policies.

---

# Term: Change

## Vietnamese:
Thay đổi

## Definition:

A Change is a controlled modification to an existing artifact or system element.

---

# Term: Deprecation

## Vietnamese:
Ngừng khuyến nghị

## Definition:

Deprecation means an artifact remains available but is no longer the preferred approach.

---

# Term: Archive

## Vietnamese:
Lưu trữ

## Definition:

Archive is the process of preserving inactive artifacts for historical reference.

---

# Term: Knowledge Base

## Vietnamese:
Cơ sở tri thức

## Definition:

A Knowledge Base is an organized collection of information used by humans and AI systems.

---

# Term: AI Agent

## Vietnamese:
Tác nhân AI

## Definition:

An AI Agent is an intelligent system capable of performing tasks based on defined goals, knowledge, and permissions.

---

# Term: Canonical

## Vietnamese:
Chuẩn chính thức

## Definition:

Canonical means the officially accepted source of truth.

Example:

```text
Canonical Document
=
Official Reference
```

---

# Term: Source of Truth

## Vietnamese:
Nguồn sự thật duy nhất

## Definition:

A Source of Truth is the authoritative location containing the approved version of information.

---

# 4. Terminology Rules

All EAOSS documents should:

- Use approved terms.
- Avoid ambiguous terminology.
- Link new concepts to existing definitions.
- Maintain consistency.

---

# 5. Quality Checklist

| Requirement | Mandatory |
|---|---|
| Definition provided | Yes |
| Vietnamese explanation provided | Yes |
| Related terms mapped | Yes |
| Usage context defined | Yes |

---

# 6. References

- TMP-001 Document Template
- FS-001 Documentation Standard
- FS-007 Cross Reference Standard
- POL-010 Lifecycle Policy

---

# 7. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial Core Terms Glossary |

---

# End of Document