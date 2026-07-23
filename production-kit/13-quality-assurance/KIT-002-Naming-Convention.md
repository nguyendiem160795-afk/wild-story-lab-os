# KIT-002 — Naming Convention

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Naming Convention defines standardized rules for naming every file, folder, asset, prompt, render, and document used within Wild Story Lab OS.

Consistent naming improves discoverability, automation, version control, and collaboration.

---

# Objectives

- Standardize naming
- Improve searchability
- Reduce ambiguity
- Enable automation
- Support version control
- Simplify maintenance

---

# General Naming Rules

Always use:

- lowercase
- hyphens (-)
- descriptive names
- consistent prefixes

Avoid:

- spaces
- special characters
- abbreviations without definition
- duplicate names

---

# Naming Format

```
<category>-<type>-<name>-v<version>
```

Example

```
char-profile-mochi-v2
```

---

# Folder Naming

Examples

```
characters/
environments/
props/
audio/
renders/
exports/
metadata/
reports/
archive/
```

---

# Character Assets

Format

```
char-<name>-<type>-v<version>
```

Examples

```
char-mochi-profile-v2
char-mochi-turnaround-v1
char-ollie-expression-v3
```

---

# Environment Assets

Format

```
env-<name>-v<version>
```

Examples

```
env-classroom-v3
env-kitchen-v2
env-forest-v1
```

---

# Prop Assets

Format

```
prop-<name>-v<version>
```

Examples

```
prop-alphabet-board-v2
prop-red-apple-v1
prop-story-book-v4
```

---

# Prompt Files

Format

```
prompt-<recipe>-scene-<number>-v<version>
```

Examples

```
prompt-alphabet-scene-01-v1
prompt-cooking-scene-05-v2
```

---

# Render Files

Format

```
render-<project>-scene-<number>-<quality>
```

Examples

```
render-eng001-scene-03-production
render-eng001-scene-08-final
```

---

# Metadata Files

Format

```
metadata-<project>-v<version>
```

Example

```
metadata-eng001-v1
```

---

# Report Files

Format

```
report-<type>-<project>
```

Examples

```
report-qa-eng001
report-runtime-eng001
report-render-eng001
```

---

# Project Naming

Format

```
<series>-<episode>-<topic>
```

Examples

```
eng-001-alphabet-a
eng-015-colors
story-008-friendship
cook-003-pancakes
```

---

# Versioning Rules

Major

```
v2
```

Minor

```
v2.1
```

Patch

```
v2.1.3
```

---

# Reserved Prefixes

| Prefix | Meaning |
|---------|---------|
| char | Character |
| env | Environment |
| prop | Prop |
| audio | Audio |
| prompt | Prompt |
| render | Render |
| report | Report |
| metadata | Metadata |
| recipe | Prompt Recipe |
| qa | Quality Assurance |
| runtime | Production Runtime |

---

# Validation Rules

Every name must be

✓ Unique

✓ Descriptive

✓ Versioned

✓ Automation-friendly

✓ Searchable

---

# Best Practices

- Use meaningful names.
- Keep names concise.
- Never rename released assets.
- Increment versions instead of overwriting.
- Follow reserved prefixes consistently.

---

# Related Documents

- KIT-001 Project Folder Template
- KIT-003 Metadata Template
- KIT-004 Production Manifest
- KIT-006 Versioning Guide
- RT-003 Asset Resolver