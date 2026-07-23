# RT-003 — Asset Resolver

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Asset Resolver is responsible for collecting, validating, and resolving every production asset required before prompt generation.

It guarantees that each scene references the correct characters, environments, props, audio profiles, lighting profiles, and production components.

Asset Resolver acts as the bridge between planning and prompt generation.

---

# Objectives

- Resolve production assets
- Validate asset availability
- Eliminate missing references
- Maintain asset consistency
- Optimize asset reuse
- Support version-controlled assets

---

# Asset Resolution Pipeline

Scene Plan

↓

Load Character Assets

↓

Load Environment Assets

↓

Load Production Components

↓

Resolve Dependencies

↓

Validate Assets

↓

Build Asset Package

↓

Ready for Prompt Generation

---

# Asset Categories

## Character Assets

Examples

- Character Bible
- Character Profile
- Character Images
- Expressions
- Outfits
- Accessories

Reference

Character OS

---

## Environment Assets

Examples

- Classroom
- Kitchen
- Forest
- Playground
- Bedroom
- City

Reference

Environment Library

---

## Prop Assets

Examples

- Books
- Toys
- Alphabet Board
- Fruits
- Cooking Tools
- Vehicles

---

## Camera Assets

Examples

- Camera Profiles
- Camera Angles
- Camera Motion

Reference

Camera Library

---

## Motion Assets

Examples

- Walking
- Running
- Jumping
- Teaching
- Dancing
- Cooking

Reference

Motion Library

---

## Expression Assets

Examples

- Happy
- Curious
- Excited
- Surprised
- Thinking
- Celebrating

Reference

Expression Library

---

## Lighting Assets

Examples

- Warm Morning
- Sunset
- Indoor Studio
- Fantasy Glow

Reference

Lighting Library

---

## Audio Assets

Examples

- Background Music
- Sound Effects
- Ambient Sound
- Voice Profile

Reference

Audio Library

---

# Asset Resolution Rules

Every asset must:

✓ Exist

✓ Match version requirements

✓ Match project style

✓ Match platform compatibility

✓ Match Character Bible

---

# Dependency Resolution

Character

↓

Outfit

↓

Accessories

↓

Environment

↓

Props

↓

Camera

↓

Lighting

↓

Audio

---

# Asset Package

Each scene produces a standardized Asset Package.

Contents

- Scene ID
- Character Version
- Environment Version
- Prop List
- Camera Profile
- Motion Profile
- Expression Profile
- Lighting Profile
- Audio Profile
- Platform Profile

---

# Missing Asset Handling

## Missing Asset

Action

Search Asset Library

↓

Find Compatible Alternative

↓

Flag Replacement

↓

Continue

---

## Critical Asset Missing

Examples

- Character Bible
- Primary Character
- Required Environment

Action

Stop production

Return detailed error report

---

# Asset Validation

Check

- Version compatibility
- Duplicate assets
- Naming consistency
- Platform compatibility
- Licensing status
- Resolution quality

---

# Asset Cache

Frequently used assets should be cached.

Examples

- Mochi Character Pack
- Daily Learning Classroom
- Warm Morning Lighting
- Educational Camera Profile

Benefits

- Faster production
- Consistent outputs
- Reduced loading time

---

# Performance Metrics

| Metric | Description |
|---------|-------------|
| Assets Loaded | Total assets resolved |
| Cache Hit Rate | Assets loaded from cache |
| Missing Assets | Assets requiring replacement |
| Validation Errors | Asset validation failures |
| Resolution Time | Total asset loading duration |

---

# Best Practices

- Reuse standardized assets whenever possible.
- Keep asset versions synchronized.
- Resolve all assets before prompt generation.
- Validate compatibility before rendering.
- Maintain a clean asset naming convention.

---

# Related Documents

- RT-001 Production Orchestrator
- RT-002 Scene Planner
- RT-004 Consistency Manager
- PE-007 Prompt Recipes
- PCL-001 → PCL-009
- DOC-003 Character Bible