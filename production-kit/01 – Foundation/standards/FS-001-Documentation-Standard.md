---
document_id: FS-001
module: 01
category: Standards
title: Documentation Standard (Tiêu chuẩn Tài liệu)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Documentation Standard (Tiêu chuẩn Tài liệu)

> Normative documentation standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the mandatory structure, formatting, metadata, and quality requirements for documentation within EAOSS.

Unlike FP-004 (Documentation Principles), this document specifies mandatory implementation rules.

---

# 2. Scope (Phạm vi)

This standard applies to:

- Markdown documents
- Specifications
- Standards
- Policies
- Principles
- Architecture documents
- Templates
- Review documents
- Baselines

---

# 3. Required Metadata

Every normative document shall begin with YAML front matter.

Required fields:

```yaml
document_id:
module:
title:
version:
status:
classification:
owner:
last_updated:
```

Additional fields may be added where appropriate.

---

# 4. Required Document Structure

Normative documents shall contain, where applicable:

1. Purpose
2. Objectives
3. Scope
4. Main Content
5. Compliance
6. References
7. Revision History

The section order shall remain consistent.

---

# 5. Heading Standard

Headings shall follow Markdown ATX syntax.

Example:

```markdown
# Level 1
## Level 2
### Level 3
```

Heading levels shall not be skipped.

---

# 6. Tables

Tables shall be used for structured information including:

- Metadata summaries
- Checklists
- Decision matrices
- Revision histories

Column names should be concise and descriptive.

---

# 7. Code Blocks

Examples shall use fenced code blocks.

Language identifiers should be specified whenever possible.

Example:

````text
```yaml
version: 1.0.0
```