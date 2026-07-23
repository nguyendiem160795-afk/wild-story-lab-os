# RT-004 — Consistency Manager

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Consistency Manager ensures that every scene within a production maintains visual, narrative, and technical consistency.

It continuously compares scene outputs against the project standards defined by Character OS, Production Components, and Prompt Engine.

---

# Objectives

- Maintain character consistency
- Maintain environment consistency
- Maintain visual identity
- Maintain educational continuity
- Detect production conflicts
- Prevent quality degradation

---

# Consistency Workflow

Production Context

↓

Load Standards

↓

Compare Scene

↓

Detect Differences

↓

Evaluate Severity

↓

Apply Corrections

↓

Approve Scene

---

# Consistency Domains

## Character Consistency

Checks

- Face
- Body proportions
- Fur / Skin color
- Hair
- Outfit
- Accessories
- Personality
- Signature pose
- Signature expressions

Reference

Character Bible

---

## Environment Consistency

Checks

- Environment profile
- Layout
- Colors
- Props
- Decorative elements
- Time of day

Reference

Environment Library

---

## Camera Consistency

Checks

- Camera profile
- Lens style
- Camera movement
- Shot progression

Reference

Camera Library

---

## Motion Consistency

Checks

- Animation style
- Walking cycle
- Gestures
- Speed
- Interaction quality

Reference

Motion Library

---

## Expression Consistency

Checks

- Emotional progression
- Facial expressions
- Eye direction
- Mouth movement

Reference

Expression Library

---

## Lighting Consistency

Checks

- Light direction
- Color temperature
- Brightness
- Shadow quality

Reference

Lighting Library

---

## Audio Consistency

Checks

- Music profile
- Ambient sound
- Voice profile
- Sound effects

Reference

Audio Library

---

## Story Consistency

Checks

- Story progression
- Learning objective
- Character knowledge
- Scene transitions
- Emotional flow

---

# Validation Levels

## Scene Level

Validate one scene.

---

## Sequence Level

Validate a group of related scenes.

---

## Project Level

Validate the entire production.

---

# Conflict Types

## Minor

Examples

- Slight lighting variation
- Small prop position changes

Action

Accept automatically.

---

## Moderate

Examples

- Different outfit
- Different background layout
- Camera inconsistency

Action

Recommend correction.

---

## Critical

Examples

- Different character design
- Wrong Character Bible version
- Missing educational objective
- Incorrect platform profile

Action

Reject scene.

---

# Consistency Report

Each validation generates:

- Scene ID
- Validation Time
- Checked Domains
- Issues Found
- Severity
- Suggested Fixes
- Overall Score

---

# Consistency Score

| Score | Status |
|--------|--------|
| 98–100 | Perfect |
| 90–97 | Excellent |
| 80–89 | Acceptable |
| Below 80 | Needs Revision |

---

# Automatic Corrections

Supported automatic fixes

- Standardize terminology
- Restore Character Bible references
- Replace outdated profiles
- Update asset versions
- Normalize metadata

---

# Human Review Required

Required when:

- Character redesign detected
- Story conflict detected
- Major environment changes
- Educational objective mismatch

---

# Best Practices

- Validate after every generated scene.
- Use the latest approved Character Bible.
- Lock production profiles after approval.
- Review critical issues before rendering.
- Archive validation reports.

---

# Related Documents

- RT-001 Production Orchestrator
- RT-002 Scene Planner
- RT-003 Asset Resolver
- RT-005 Render Pipeline
- PE-004 Prompt Validator
- DOC-003 Character Bible
- PCL-001 → PCL-009