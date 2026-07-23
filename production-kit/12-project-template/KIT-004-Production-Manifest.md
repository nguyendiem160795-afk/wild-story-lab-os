# KIT-004 — Production Manifest

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Production Manifest is the master configuration document for every Wild Story Lab production.

It records all production settings, dependencies, versions, assets, recipes, runtime configuration, and publishing targets required to reproduce a project.

The Manifest acts as the single source of truth for the entire production lifecycle.

---

# Objectives

- Centralize project configuration
- Track production dependencies
- Improve reproducibility
- Enable automation
- Simplify project auditing
- Support long-term maintenance

---

# Manifest Architecture

Project

↓

Production Configuration

↓

Assets

↓

Story

↓

Runtime

↓

Rendering

↓

Publishing

↓

Archive

---

# Manifest Sections

## Project Information

Fields

- Project ID
- Project Name
- Series
- Episode
- Owner
- Team
- Status
- Created Date
- Updated Date

---

## Story Configuration

Fields

- Story Framework
- Prompt Recipe
- Target Audience
- Language
- Educational Objective
- Video Duration
- Scene Count

---

## Character Configuration

Fields

- Character Bible Version
- Character Pack
- Character Profiles
- Outfit Set
- Expression Pack

---

## Environment Configuration

Fields

- Environment Profile
- Lighting Profile
- Audio Profile
- Camera Profile
- Motion Profile
- Color Profile

---

## Asset Configuration

Fields

- Asset Manifest Version
- Asset Package
- Prop List
- Audio Assets
- Thumbnail Assets

---

## Prompt Configuration

Fields

- Prompt Architecture Version
- Prompt Block Version
- Validator Version
- Optimizer Version
- Platform Profile

---

## Runtime Configuration

Fields

- Runtime Version
- Scene Planner Version
- Asset Resolver Version
- Consistency Manager Version
- Render Pipeline Version

---

## Rendering Configuration

Fields

- AI Platform
- Render Profile
- Resolution
- Aspect Ratio
- Frame Rate
- Output Format

---

## QA Configuration

Fields

- QA Version
- Validation Status
- Production Score
- Approval Status

---

## Publishing Configuration

Fields

- Platform
- Title
- Description
- Keywords
- Hashtags
- Thumbnail
- Release Date

---

# Manifest Lifecycle

Draft

↓

Planning

↓

Production

↓

Rendering

↓

QA

↓

Approved

↓

Published

↓

Archived

---

# Example Manifest (YAML)

```yaml
project:
  id: ENG-001
  name: Alphabet Letter A

story:
  recipe: Alphabet Lesson
  duration: 60s

character:
  bible: DOC-003
  pack: Mochi-v2.3

environment:
  profile: Daily Learning Classroom

prompt:
  architecture: PE-001
  validator: PE-004

runtime:
  orchestrator: RT-001

render:
  platform: Google Flow
  profile: Production

qa:
  status: Passed

publish:
  platform: YouTube
```

---

# Validation Rules

Every Manifest must

✓ Reference valid assets

✓ Reference approved recipes

✓ Include runtime version

✓ Include QA status

✓ Include publishing information

---

# Best Practices

- Update the Manifest whenever project settings change.
- Store one Manifest per project.
- Never edit archived Manifests.
- Keep all version references synchronized.
- Validate the Manifest before rendering.

---

# Related Documents

- KIT-001 Project Folder Template
- KIT-002 Naming Convention
- KIT-003 Metadata Template
- KIT-005 Asset Structure
- RT-001 Production Orchestrator
- RT-003 Asset Resolver