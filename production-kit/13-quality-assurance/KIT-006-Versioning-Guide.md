# KIT-006 — Versioning Guide

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Versioning Guide defines the official version management strategy for every document, asset, prompt, runtime module, and production project within Wild Story Lab OS.

It ensures compatibility, traceability, and long-term maintenance.

---

# Objectives

- Standardize versioning
- Preserve compatibility
- Track production history
- Prevent accidental overwrites
- Support rollback
- Enable future automation

---

# Versioning Philosophy

Every production artifact is versioned.

Nothing important is overwritten.

History is always preserved.

---

# Version Scope

The following items require versioning:

- Character Bible
- Character Packs
- Prompt Recipes
- Prompt Engine
- Production Components
- Runtime Modules
- Assets
- Project Templates
- QA Reports
- Production Manifest
- Final Deliverables

---

# Version Format

Semantic Versioning

```
MAJOR.MINOR.PATCH
```

Example

```
1.0.0
2.3.1
4.1.12
```

---

# Version Meaning

## Major

Breaking changes

Examples

- Character redesign
- Prompt architecture redesign
- Runtime redesign

Example

```
2.0.0
```

---

## Minor

New features

Examples

- New Camera Profile
- New Prompt Recipe
- New QA Rules

Example

```
2.4.0
```

---

## Patch

Bug fixes

Examples

- Metadata correction
- Typo fixes
- Documentation improvements

Example

```
2.4.3
```

---

# Compatibility Rules

| Change | Compatibility |
|---------|---------------|
| Patch | Fully Compatible |
| Minor | Backward Compatible |
| Major | Compatibility Review Required |

---

# Version Lifecycle

Draft

↓

Review

↓

Approved

↓

Released

↓

Deprecated

↓

Archived

---

# Release Types

## Alpha

Internal testing.

---

## Beta

Limited production use.

---

## Stable

Approved for production.

---

## Long-Term Support (LTS)

Recommended for long-running productions.

---

# Version Registry

Each release records

- Version Number
- Release Date
- Owner
- Change Summary
- Compatibility Notes
- Approval Status

---

# Change Log

Every update includes

- Added
- Changed
- Fixed
- Deprecated
- Removed

Example

```
Version 2.1.0

Added

- Educational Camera Profile

Changed

- Lighting Library

Fixed

- Metadata validation

Deprecated

- Legacy Classroom Background
```

---

# Rollback Policy

Rollback is allowed when

- Critical production failure
- QA rejection
- Platform incompatibility
- Corrupted assets

Rollback must

- Preserve history
- Record reason
- Update Manifest
- Notify dependent modules

---

# Version Validation

Verify

✓ Correct version format

✓ Dependencies compatible

✓ Manifest updated

✓ Metadata synchronized

✓ QA completed

---

# Best Practices

- Never overwrite released versions.
- Use semantic versioning consistently.
- Keep detailed change logs.
- Archive deprecated versions.
- Validate compatibility before upgrading.

---

# Related Documents

- KIT-003 Metadata Template
- KIT-004 Production Manifest
- KIT-005 Asset Structure
- RT-001 Production Orchestrator
- KS-003 Version Control (Future)