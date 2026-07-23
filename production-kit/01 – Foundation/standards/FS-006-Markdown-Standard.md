---
document_id: FS-006
module: 01
category: Standards
title: Markdown Standard (Tiêu chuẩn Markdown)
version: 1.0.0
status: Production Ready
classification: Public
owner: Wild Story Lab
last_updated: 2026-07-23
---

# Markdown Standard (Tiêu chuẩn Markdown)

> Normative Markdown authoring standard for the Enterprise AI Operating System Specification (EAOSS).

---

# 1. Purpose (Mục đích)

This standard defines the mandatory Markdown syntax, formatting conventions, and structural rules for all EAOSS documentation.

Its purpose is to ensure consistency, readability, maintainability, compatibility with GitHub, and efficient AI-assisted processing.

---

# 2. Scope (Phạm vi)

This standard applies to:

- README files
- Specifications
- Principles
- Standards
- Policies
- Templates
- Reviews
- Baselines
- Changelogs
- Roadmaps

---

# 3. General Rules

All documentation shall:

- Use GitHub Flavored Markdown (GFM).
- Be UTF-8 encoded.
- Use Unix line endings (LF).
- End with a newline.
- Avoid HTML unless no Markdown alternative exists.

---

# 4. Heading Rules

Headings shall use ATX syntax.

Example:

```markdown
# Level 1
## Level 2
### Level 3
#### Level 4
```

Requirements:

- One H1 (`#`) per document.
- Heading levels shall not be skipped.
- Headings shall use sentence case.

---

# 5. Paragraph Formatting

Requirements:

- Separate paragraphs with one blank line.
- Avoid trailing spaces.
- Wrap long paragraphs only when necessary.
- Use complete sentences.

---

# 6. Lists

Use unordered lists for collections.

Example:

```markdown
- Item A
- Item B
- Item C
```

Use ordered lists only when sequence matters.

```markdown
1. Step One
2. Step Two
3. Step Three
```

Nested lists shall use consistent indentation.

---

# 7. Tables

Tables shall be used for structured information.

Example:

| Field | Description |
|------|-------------|
| Version | Document version |
| Status | Lifecycle state |

Requirements:

- Consistent column alignment.
- Concise headers.
- Avoid excessively wide tables.

---

# 8. Code Blocks

Use fenced code blocks.

Example:

````markdown
```yaml
version: 1.0.0
```