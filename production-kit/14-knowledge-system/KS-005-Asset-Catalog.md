# KS-005 — Asset Catalog

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Asset Catalog defines the centralized indexing system for every production asset used throughout Wild Story Lab OS.

Unlike a traditional file directory, the Asset Catalog provides structured metadata, semantic relationships, usage history, quality status, and dependency information, allowing assets to be discovered, evaluated, and reused intelligently.

---

# Objectives

- Centralize asset discovery
- Eliminate duplicate assets
- Improve asset reuse
- Support AI retrieval
- Track asset lifecycle
- Enable production analytics

---

# Catalog Philosophy

Assets are Knowledge Objects.

Files are only one representation.

Every asset has identity, context, history, and relationships.

---

# Catalog Architecture

Asset Sources

↓

Metadata Extraction

↓

Asset Registration

↓

Knowledge Graph

↓

Asset Catalog

↓

Search

↓

AI Agents

↓

Production

---

# Asset Categories

## Character Assets

Includes

- Character Bible
- Character Pack
- Turnaround Sheets
- Expressions
- Outfit Library
- Accessories
- Voice Profiles

---

## Environment Assets

Includes

- Backgrounds
- Classroom Packs
- Kitchen Packs
- Forest Packs
- Lighting Profiles
- Camera Zones

---

## Prop Assets

Includes

- Educational Objects
- Toys
- Cooking Tools
- Seasonal Props
- Interactive Objects

---

## Audio Assets

Includes

- Narration
- Music
- Sound Effects
- Ambient Audio
- Character Voices

---

## Prompt Assets

Includes

- Prompt Recipes
- Prompt Blocks
- Platform Profiles
- Optimization Rules

---

## Branding Assets

Includes

- Logos
- Intro
- Outro
- Thumbnail Templates
- Brand Colors
- Typography

---

# Asset Metadata

Every asset records

- Asset ID
- Asset Name
- Category
- Subcategory
- Version
- Owner
- Status
- License
- Language
- Tags
- Creation Date
- Last Updated

---

# Asset Relationships

Each asset records

Uses

Referenced By

Depends On

Replaced By

Derived From

Compatible With

Used In Projects

Used In Stories

Used In Scenes

---

# Asset Quality Status

Draft

↓

Review

↓

Approved

↓

Production

↓

Golden Reference

↓

Deprecated

↓

Archived

---

# Usage Analytics

Track

- Number of Projects
- Number of Stories
- Number of Scenes
- AI Platforms Used
- Average QA Score
- Last Usage
- Reuse Frequency

---

# Search Filters

Search by

- Asset Type
- Character
- Environment
- Topic
- Educational Subject
- Platform
- Version
- Status
- Language
- Confidence Score

---

# Duplicate Detection

The catalog should identify

✓ Duplicate Assets

✓ Similar Assets

✓ Deprecated Assets

✓ Unused Assets

✓ Orphan Assets

---

# Validation Rules

Every asset must

✓ Have metadata

✓ Have unique ID

✓ Have version

✓ Be categorized

✓ Be searchable

✓ Be linked to the Knowledge Graph

---

# Best Practices

- Register every approved asset.
- Avoid duplicate uploads.
- Archive rather than delete.
- Track every dependency.
- Review asset quality regularly.

---

# Related Documents

- KS-001 Knowledge Graph
- KS-002 Taxonomy
- KS-004 Reference Library
- KIT-005 Asset Structure
- RT-003 Asset Resolver