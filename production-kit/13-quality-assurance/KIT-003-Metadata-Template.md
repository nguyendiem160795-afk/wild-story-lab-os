# KIT-003 — Metadata Template

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Metadata Template defines the standard metadata model for every production project, scene, asset, prompt, render, and published deliverable within Wild Story Lab OS.

Metadata enables traceability, automation, analytics, search, and version control.

---

# Objectives

- Standardize metadata
- Improve discoverability
- Support automation
- Track production history
- Enable analytics
- Maintain data consistency

---

# Metadata Hierarchy

Project

↓

Scene

↓

Asset

↓

Prompt

↓

Render

↓

Publication

---

# Project Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Project ID | Unique project identifier |
| Project Name | Human-readable project name |
| Series | Series identifier |
| Episode | Episode number |
| Language | Primary language |
| Target Audience | Intended viewers |
| Recipe | Prompt Recipe used |
| Platform | Target AI platform |
| Runtime Version | Production Runtime version |
| Status | Current production status |
| Created Date | Project creation date |
| Updated Date | Last modification date |

---

# Scene Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Scene ID | Unique scene identifier |
| Scene Number | Scene order |
| Scene Name | Scene title |
| Duration | Estimated duration |
| Story Purpose | Narrative objective |
| Learning Objective | Educational objective |
| Characters | Characters used |
| Environment | Environment profile |
| Prompt Version | Prompt reference |
| Render Status | Current render state |

---

# Asset Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Asset ID | Unique asset identifier |
| Asset Type | Character, Environment, Prop, Audio |
| Name | Asset name |
| Version | Asset version |
| Owner | Responsible creator |
| Status | Draft, Approved, Archived |
| Source | Origin of asset |
| License | Usage rights |
| Tags | Search keywords |

---

# Prompt Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Prompt ID | Unique prompt identifier |
| Recipe | Prompt Recipe |
| Platform Profile | Target platform |
| Prompt Version | Prompt version |
| Validator Score | Validation score |
| Optimizer Version | Optimizer version |
| Generation Date | Creation date |

---

# Render Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Render ID | Unique render identifier |
| Platform | AI platform |
| Resolution | Output resolution |
| Aspect Ratio | Output ratio |
| Frame Rate | FPS |
| Render Profile | Draft, Production, Studio |
| Render Time | Generation duration |
| File Size | Output size |

---

# Publication Metadata

Required Fields

| Field | Description |
|---------|-------------|
| Platform | YouTube, TikTok, etc. |
| Title | Published title |
| Description | Published description |
| Thumbnail | Thumbnail reference |
| Keywords | SEO keywords |
| Hashtags | Publishing hashtags |
| Publish Date | Release date |

---

# Metadata Standards

Every metadata record must be:

✓ Complete

✓ Accurate

✓ Versioned

✓ Searchable

✓ Machine-readable

---

# Metadata Formats

Supported formats

- JSON
- YAML
- CSV
- Markdown

---

# Example Metadata (YAML)

```yaml
project:
  id: ENG-001
  name: Alphabet Letter A
  series: English Basics
  episode: 1
  language: English
  audience: Children 3–8
  recipe: Alphabet Lesson
  platform: Google Flow
  runtime: 1.0.0
  status: Production

scene:
  id: SC-001
  duration: 8s
  environment: Daily Learning Classroom

character:
  primary: Mochi

render:
  profile: Production
  resolution: 1080p
```

---

# Validation Rules

Metadata must

✓ Match project version

✓ Reference existing assets

✓ Follow naming conventions

✓ Include required fields

---

# Best Practices

- Update metadata immediately after major production steps.
- Never remove historical metadata.
- Keep metadata synchronized with assets.
- Store metadata alongside project files.

---

# Related Documents

- KIT-001 Project Folder Template
- KIT-002 Naming Convention
- KIT-004 Production Manifest
- KIT-006 Versioning Guide
- RT-001 Production Orchestrator
- RT-003 Asset Resolver