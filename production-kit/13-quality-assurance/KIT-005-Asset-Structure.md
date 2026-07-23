# KIT-005 — Asset Structure

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Asset Structure defines the standard organization of every production asset used within Wild Story Lab OS.

It ensures that characters, environments, props, audio, prompts, renders, and supporting files are stored consistently across all projects.

---

# Objectives

- Standardize asset organization
- Improve asset discoverability
- Enable automation
- Support asset reuse
- Simplify maintenance
- Improve production scalability

---

# Asset Hierarchy

Project

↓

Assets

├── Characters

├── Environments

├── Props

├── Audio

├── Visual Effects

├── Fonts

├── References

└── Branding

---

# Standard Folder Structure

```text
assets/
│
├── characters/
│   ├── mochi/
│   ├── ollie/
│   └── shared/
│
├── environments/
│   ├── classroom/
│   ├── kitchen/
│   ├── playground/
│   └── forest/
│
├── props/
│   ├── education/
│   ├── cooking/
│   ├── toys/
│   └── seasonal/
│
├── audio/
│   ├── music/
│   ├── sfx/
│   ├── ambience/
│   └── voice/
│
├── vfx/
│
├── fonts/
│
├── references/
│
└── branding/
```

---

# Character Assets

Each character folder contains

- Character Bible
- Turnaround Images
- Expressions
- Outfit Library
- Accessories
- Voice Profile
- Metadata

Example

```text
characters/mochi/

character-bible.md

turnaround/

expressions/

outfits/

accessories/

voice/

metadata.yaml
```

---

# Environment Assets

Each environment includes

- Master Background
- Layout
- Lighting Variants
- Props
- Ambient Audio
- Metadata

---

# Prop Assets

Each prop contains

- Master Image
- Variations
- Animation Notes
- Metadata

---

# Audio Assets

Categories

- Background Music
- Sound Effects
- Ambient Audio
- Character Voices

Each audio asset records

- Duration
- Format
- License
- Loudness
- Loop Support

---

# Branding Assets

Include

- Logos
- Intro
- Outro
- Watermarks
- Thumbnail Templates
- Brand Colors

---

# Reference Assets

Reference folder stores

- Mood Boards
- Color References
- Style Frames
- Camera References
- Inspiration Images

---

# Asset Packaging

Every project produces an Asset Package.

Contents

- Character Pack
- Environment Pack
- Prop Pack
- Audio Pack
- Branding Pack
- Metadata

---

# Asset Validation

Every asset must

✓ Have metadata

✓ Follow naming convention

✓ Have version information

✓ Pass QA

✓ Match project style

---

# Asset Lifecycle

Draft

↓

Review

↓

Approved

↓

Production

↓

Archived

---

# Storage Guidelines

Active Assets

Used in current productions.

Shared Assets

Reusable across projects.

Archived Assets

Read-only historical versions.

Deprecated Assets

Retained for compatibility only.

---

# Best Practices

- Store one asset in one canonical location.
- Avoid duplicate copies.
- Update metadata after every revision.
- Archive instead of deleting.
- Reuse approved assets whenever possible.

---

# Related Documents

- KIT-002 Naming Convention
- KIT-003 Metadata Template
- KIT-004 Production Manifest
- KIT-006 Versioning Guide
- RT-003 Asset Resolver
- AS-001 Asset Standards (Future)