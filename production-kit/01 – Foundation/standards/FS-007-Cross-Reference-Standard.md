---
document_id: FS-007
module: 01
category: Standards
title: Cross Reference Standard (Tiêu chuẩn Tham chiếu Chéo)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Cross Reference Standard (Tiêu chuẩn Tham chiếu Chéo)

> Normative standard for creating, maintaining, and validating cross references across the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines how artifacts shall reference one another within the EAOSS repository.

A consistent cross-reference system improves navigation, traceability, governance, dependency analysis, impact assessment, and AI-assisted knowledge retrieval.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Principles
- Standards
- Policies
- Templates
- Architecture documents
- Specifications
- Reviews
- Baselines
- Repository indexes

---

# 3. Objectives

Cross references shall:

- Improve discoverability.
- Support impact analysis.
- Enable bidirectional navigation.
- Reduce duplication.
- Preserve document relationships.

---

# 4. Types of References

EAOSS recognizes the following reference types.

| Type | Purpose |
|------|---------|
| Normative | Required dependency |
| Informative | Additional context |
| Parent | Higher-level artifact |
| Child | Lower-level artifact |
| Related | Peer relationship |
| External | Outside EAOSS |

Every reference should clearly indicate its intent.

---

# 5. Reference Format

Document references shall use the artifact identifier followed by its official title.

Example:

```text
FP-004 Documentation Principles
FS-001 Documentation Standard
POL-002 Review Policy
```

Avoid referencing documents only by filename.

---

# 6. Internal Links

Repository links shall use relative paths.

Example:

```markdown
[Documentation Standard](FS-001-Documentation-Standard.md)
```

Relative links improve portability and repository independence.

---

# 7. Reference Placement

Normative documents shall include a dedicated **References** section near the end of the document.

Example:

```text
13. References
```

References shall appear before the Revision History section.

---

# 8. Reference Integrity

Every reference shall:

- Point to an existing artifact.
- Use the correct identifier.
- Use the official title.
- Remain valid after repository updates.

Broken references shall be corrected immediately.

---

# 9. Bidirectional Relationships

Where practical, significant relationships should be reciprocal.

Example:

```text
FP-004
    ↓
FS-001
    ↑
Referenced By
```

Bidirectional references improve traceability.

---

# 10. Circular References

Circular references shall be avoided unless they represent legitimate architectural relationships.

Unnecessary circular dependencies are prohibited.

---

# 11. External References

External references shall:

- Identify the source.
- Include the publication title when available.
- Remain stable over time.
- Prefer official sources.

Examples include:

- ISO standards
- IEEE standards
- RFC documents
- W3C specifications

---

# 12. Reference Validation

Cross references shall be validated for:

- Existing targets
- Correct identifiers
- Correct titles
- Valid relative links
- Duplicate references
- Broken links

Validation should be automated whenever practical.

---

# 13. Cross Reference Matrix

Large modules should maintain a reference matrix documenting major dependencies.

Example:

| Artifact | References |
|----------|------------|
| FS-001 | FP-004, FP-010 |
| FS-003 | FP-007, FS-001 |

Reference matrices support governance and impact analysis.

---

# 14. Compliance

Compliance with this standard is mandatory.

Repository reviews shall verify:

- Reference accuracy
- Link validity
- Identifier consistency
- Dependency correctness

---

# 15. References

- FP-004 Documentation Principles
- FP-005 Governance Principles
- FP-008 Dependency Rules
- FS-001 Documentation Standard
- FS-002 Naming Standard

---

# 16. Revision History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-07-23 | Initial Cross Reference Standard |

---

# End of Document