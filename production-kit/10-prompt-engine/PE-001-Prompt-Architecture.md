# PE-001 — Prompt Architecture

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

This document defines the standard architecture for AI prompts used throughout Wild Story Lab OS.

Every production-ready prompt should follow this architecture to ensure consistency, scalability, readability, and compatibility across multiple AI video generation platforms.

---

# Prompt Philosophy

A prompt is not a paragraph.

A prompt is a structured system composed of reusable building blocks.

Each block has a single responsibility.

Together, these blocks describe the complete creative intent of a scene.

---

# Prompt Architecture

```
Prompt
│
├── Story Block
├── Character Block
├── Camera Block
├── Motion Block
├── Expression Block
├── Environment Block
├── Lighting Block
├── Audio Block
├── Style Block
├── Technical Block
└── Platform Block
```

---

# Core Blocks

## Story Block

Defines:

- Scene objective
- Narrative context
- Emotional goal

Required

YES

---

## Character Block

Defines:

- Character
- Appearance
- Outfit
- Personality
- Consistency Rules

Required

YES

---

## Camera Block

Defines

- Shot Type
- Camera Movement
- Camera Angle

Required

YES

Reference

PCL-001

---

## Motion Block

Defines

- Primary Action
- Secondary Action
- Motion Intensity

Required

YES

Reference

PCL-002

---

## Expression Block

Defines

- Emotion
- Facial Expression
- Eye Contact
- Gesture

Required

YES

Reference

PCL-003

---

## Environment Block

Defines

- Location
- Time
- Weather
- Props

Required

YES

Reference

PCL-005

---

## Lighting Block

Defines

- Lighting Style
- Color Temperature
- Mood

Required

YES

Reference

PCL-004

---

## Audio Block

Defines

- Music
- Ambient Sound
- Sound Effects
- Voice Style

Optional

YES

Reference

PCL-006

---

## Style Block

Defines

- Visual Style
- Animation Style
- Rendering Quality

Required

YES

Examples

- Pixar
- Disney
- Stylized 3D
- Storybook

---

## Technical Block

Defines

- Aspect Ratio
- Resolution
- Duration
- Frame Rate
- Output Quality

Required

YES

---

## Platform Block

Defines

Platform-specific optimization.

Examples

- Google Flow
- Veo
- Runway
- Sora

Required

YES

---

# Block Order

Always use the following order.

1 Story

2 Character

3 Camera

4 Motion

5 Expression

6 Environment

7 Lighting

8 Audio

9 Style

10 Technical

11 Platform

---

# Required Blocks

| Block | Required |
|--------|----------|
| Story | Yes |
| Character | Yes |
| Camera | Yes |
| Motion | Yes |
| Expression | Yes |
| Environment | Yes |
| Lighting | Yes |
| Audio | Optional |
| Style | Yes |
| Technical | Yes |
| Platform | Yes |

---

# Prompt Levels

## Level 1

Basic

Fast idea generation.

---

## Level 2

Production

Optimized for YouTube production.

---

## Level 3

Studio

Maximum detail.

Supports long-form production.

---

# Assembly Rules

Always

- One responsibility per block.
- Keep block order consistent.
- Reuse standardized terminology.
- Reference Production Components whenever possible.
- Preserve Character Bible consistency.

Never

- Duplicate information across blocks.
- Mix technical settings with story content.
- Skip required blocks.
- Use conflicting instructions.

---

# Validation Checklist

Before a prompt is approved:

□ Story objective is clear

□ Character matches Character Bible

□ Camera follows PCL-001

□ Motion follows PCL-002

□ Expression follows PCL-003

□ Environment follows PCL-005

□ Lighting follows PCL-004

□ Style is defined

□ Technical settings are complete

□ Platform target is specified

---

# Example Structure

Story
↓

Character
↓

Camera
↓

Motion
↓

Expression
↓

Environment
↓

Lighting
↓

Audio
↓

Style
↓

Technical
↓

Platform

---

# Related Documents

- README.md
- PCL-001 → PCL-009
- DOC-003 Mochi Character Bible
- DOC-006 Prompt Engineering Standard
- QA-001 Final Video Checklist