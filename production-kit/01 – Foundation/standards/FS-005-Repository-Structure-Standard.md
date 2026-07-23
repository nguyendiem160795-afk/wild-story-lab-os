---
document_id: FS-005
module: 01
category: Standards
title: Repository Structure Standard (Tiêu chuẩn Cấu trúc Repository)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Repository Structure Standard (Tiêu chuẩn Cấu trúc Repository)

> Normative repository structure standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the mandatory repository structure for EAOSS.

A standardized repository structure ensures consistency, discoverability, scalability, maintainability, and compatibility with automation and AI-assisted tooling.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Repository root
- Modules
- Subdirectories
- Documentation libraries
- Shared resources
- Future EAOSS extensions

---

# 3. Repository Design Principles

The repository shall be:

- Modular
- Predictable
- Layered
- Scalable
- Human-readable
- Machine-readable

Every artifact shall have one canonical location.

---

# 4. Root Structure

The repository root shall contain numbered modules.

Example:

```text
production-kit/

00-master/
01-foundation/
02-governance/
03-enterprise-architecture/
04-core-concepts/
05-data-model/
06-metadata-system/
...
```

Modules shall be ordered numerically.

---

# 5. Module Structure

Every module shall follow the same minimum structure.

```text
NN-module-name/

README.md
INDEX.md
ARCHITECTURE.md
CONFORMANCE.md
CHANGELOG.md
ROADMAP.md
BASELINE.md
```

Additional directories may be added according to module responsibilities.

---

# 6. Foundation Structure

The Foundation module shall organize reusable knowledge into dedicated libraries.

```text
01-foundation/

principles/
standards/
policies/
templates/
patterns/
glossary/
reviews/
```

Each library shall contain its own README.md and INDEX.md.

---

# 7. Directory Organization Rules

Directories shall:

- Represent a single responsibility.
- Avoid overlapping purposes.
- Maintain consistent naming.
- Group related artifacts together.

Nested directories should only be introduced when they improve clarity.

---

# 8. Artifact Placement

Artifacts shall be stored in their canonical location.

Examples:

| Artifact Type | Location |
|--------------|----------|
| Principle | principles/ |
| Standard | standards/ |
| Policy | policies/ |
| Template | templates/ |
| Pattern | patterns/ |
| Glossary | glossary/ |
| Review Record | reviews/ |

Duplicate copies are prohibited unless explicitly approved.

---

# 9. Shared Assets

Reusable assets shall be centralized.

Examples include:

- Templates
- Shared schemas
- Reference models
- Validation rules

Shared assets shall not be duplicated across modules.

---

# 10. Repository Evolution

The repository structure may evolve through approved governance processes.

Structural changes shall:

- Preserve backward compatibility where practical.
- Be documented.
- Update affected indexes.
- Update architecture documentation.
- Be reflected in the CHANGELOG.

---

# 11. Validation Rules

Repository structure shall satisfy:

- Required modules exist.
- Required core documents exist.
- Canonical directory names are used.
- Artifact placement is correct.
- No prohibited duplication exists.

Validation should be automated whenever possible.

---

# 12. Compliance

Compliance with this standard is mandatory.

Repository audits shall verify:

- Module organization
- Directory naming
- Artifact placement
- Structural consistency

---

# 13. References

- FP-001 Architecture Principles
- FP-006 Naming Conventions
- FP-008 Dependency Rules
- FS-001 Documentation Standard
- FS-002 Naming Standard

---

# 14. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Repository Structure Standard |

---

# End of Document