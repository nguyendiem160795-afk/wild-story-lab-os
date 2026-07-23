# MPP-006 — Version Management

Version: 1.0.0

Status: Active

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

This document defines the versioning strategy used across the entire Wild Story Lab OS.

A consistent versioning system improves project tracking, collaboration, documentation quality, and release management.

---

# Versioning Standard

Wild Story Lab uses Semantic Versioning.

Format:

MAJOR.MINOR.PATCH

Example:

1.0.0

---

# Version Rules

## MAJOR

Increase when:

- Major architecture changes
- Breaking workflow changes
- Large Production Kit redesign
- New production generation

Examples

1.0.0 → 2.0.0

---

## MINOR

Increase when:

- New module
- New Playbook
- New Character OS component
- New Prompt Library
- New Environment

Examples

1.1.0

1.2.0

1.3.0

---

## PATCH

Increase when:

- Typo fixes
- Documentation improvements
- Small workflow updates
- Template refinement
- Metadata updates

Examples

1.0.1

1.0.2

1.0.3

---

# Status Definitions

Draft

Document is under development.

---

Review

Waiting for approval.

---

Approved

Reviewed and accepted.

---

Production

Official production document.

---

Archived

Deprecated but preserved.

---

# Release Naming

Examples

Foundation v1.0

Character OS v1.0

Environment OS v1.0

Production Kit v2.0

---

# Repository Version

Every GitHub Release should include:

Release Name

Version

Summary

Major Changes

Known Issues

---

# Document Header Standard

Every Markdown document should contain:

Document ID

Version

Status

Owner

Created Date

Last Updated

Purpose

Related Documents

---

# Folder Versioning

Folders do not have versions.

Only documents are versioned.

---

# Production Kit Version

The Production Kit version reflects the overall repository maturity.

Example

Production Kit v1.0

↓

v1.1

↓

v1.2

↓

v2.0

---

# Best Practices

- Keep version history clear.
- Avoid unnecessary major releases.
- Update CHANGELOG before publishing.
- Maintain backward compatibility whenever possible.
- Version every production-ready document.

---

# Related Documents

MPP-001 Master Production Pipeline

MPP-002 Project Index

MPP-003 Roadmap

MPP-005 Changelog

MPP-004 Backlog