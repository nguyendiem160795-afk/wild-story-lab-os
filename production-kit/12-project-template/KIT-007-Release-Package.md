# KIT-007 — Release Package

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Release Package defines the official deliverables required before a Wild Story Lab project is considered complete and ready for publishing.

It standardizes the packaging of videos, metadata, prompts, assets, reports, and documentation to ensure every release is reproducible, reviewable, and archive-ready.

---

# Objectives

- Standardize project deliverables
- Simplify publishing
- Support long-term maintenance
- Enable reproducibility
- Improve collaboration
- Preserve production history

---

# Release Workflow

Production Complete

↓

Quality Assurance Passed

↓

Generate Release Package

↓

Validate Package

↓

Publish

↓

Archive

---

# Package Structure

```text
release/
│
├── video/
│   ├── final.mp4
│   ├── preview.mp4
│   └── trailer.mp4
│
├── thumbnails/
│
├── prompts/
│
├── metadata/
│
├── reports/
│
├── manifest/
│
├── assets/
│
└── documentation/
```

---

# Required Deliverables

## Final Video

Requirements

- Production approved
- Correct duration
- Correct resolution
- Final render profile

---

## Thumbnail

Requirements

- Approved design
- Correct aspect ratio
- Branding applied

---

## Prompt Package

Include

- Final Prompt
- Prompt Version
- Recipe Reference
- Platform Profile

---

## Metadata Package

Include

- Project Metadata
- Scene Metadata
- Asset Metadata
- Render Metadata
- Publication Metadata

---

## Production Reports

Include

- Runtime Report
- QA Report
- Render Report
- Validation Report

---

## Production Manifest

Include

- Final Manifest
- Version History
- Dependency Summary

---

## Asset Package

Include

- Character Pack
- Environment Pack
- Prop Pack
- Audio Pack
- Branding Assets

---

## Documentation

Include

- Release Notes
- Change Log
- Known Limitations
- Production Summary

---

# Release Validation

Every Release Package must contain

✓ Final Video

✓ Thumbnail

✓ Prompt Package

✓ Metadata

✓ QA Report

✓ Production Manifest

✓ Release Notes

---

# Release Levels

## Draft

Internal review only.

---

## Production

Approved for publishing.

---

## Studio Master

Official archival release.

---

# Release Notes

Each release includes

- Version
- Summary
- New Features
- Improvements
- Bug Fixes
- Known Issues

---

# Naming Convention

```
release-<project>-v<version>
```

Example

```
release-eng001-v1.0.0
```

---

# Validation Checklist

Verify

✓ All required files included

✓ Metadata synchronized

✓ Manifest updated

✓ QA passed

✓ Version numbers match

✓ Assets complete

---

# Best Practices

- Generate one Release Package per approved version.
- Never modify archived releases.
- Store release packages separately from working files.
- Keep documentation synchronized with released assets.
- Validate the package before publication.

---

# Related Documents

- KIT-004 Production Manifest
- KIT-005 Asset Structure
- KIT-006 Versioning Guide
- QA-001 Final Video Checklist
- RT-006 Production Checklist