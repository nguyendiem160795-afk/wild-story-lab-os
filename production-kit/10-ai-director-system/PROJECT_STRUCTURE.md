# PROJECT_STRUCTURE

# Wild Story Lab OS — Module 10 AI Director System

Version: 1.0.0

---

# Purpose

Tài liệu này mô tả cấu trúc thư mục chuẩn của Module 10 và quy ước tổ chức tài liệu, giúp việc phát triển, bảo trì và mở rộng diễn ra nhất quán.

---

# Repository Structure

```text
10-ai-director-system/
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── RELEASE_NOTES.md
├── LICENSE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── SUPPORTED_VERSIONS.md
├── ACKNOWLEDGEMENTS.md
├── MAINTAINERS.md
├── GOVERNANCE.md
├── ARCHITECTURE_DECISIONS.md
├── PROJECT_STRUCTURE.md
│
├── docs/
│   ├── 00-index.md
│   ├── 01-introduction.md
│   ├── 02-architecture.md
│   ├── 03-core-systems.md
│   ├── 04-workflow.md
│   ├── 05-documentation-portal.md
│   ├── 06-developer-guide.md
│   ├── 07-examples.md
│   ├── 08-repository.md
│   ├── glossary.md
│   ├── navigation.md
│   ├── faq.md
│   ├── diagrams/
│   └── templates/
│
├── *.md (Technical Specifications)
└── assets/
```

---

# Directory Rules

## Root

Chứa các tài liệu quản trị và định hướng của Module.

## docs/

Chứa tài liệu hướng dẫn và Documentation Portal.

## diagrams/

Chứa sơ đồ Mermaid.

## templates/

Chứa mẫu tài liệu chuẩn.

## Technical Specifications

Mỗi chủ đề kỹ thuật là một file Markdown độc lập.

---

# Naming Convention

- README.md
- UPPER_CASE.md cho tài liệu quản trị.
- kebab-case.md cho tài liệu trong docs/.
- *_SPEC.md cho đặc tả kỹ thuật.

---

# Design Principles

- Modular
- Reusable
- Documentation First
- Repository First
- Easy Navigation

---

# Related Documents

- README.md
- docs/00-index.md
- GOVERNANCE.md
- ARCHITECTURE_DECISIONS.md

---

Status: Active
Version: 1.0.0
