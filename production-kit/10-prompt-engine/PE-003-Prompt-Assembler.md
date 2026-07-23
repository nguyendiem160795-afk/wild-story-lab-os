# PE-003 — Prompt Assembler

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Prompt Assembler is responsible for transforming standardized Prompt Blocks into complete, production-ready prompts.

The assembler ensures that every generated prompt follows the Prompt Architecture while maintaining consistency across projects and AI platforms.

---

# Responsibilities

The Prompt Assembler shall:

- Load Prompt Blocks
- Resolve dependencies
- Validate required blocks
- Assemble prompt fragments
- Optimize output order
- Produce platform-ready prompts

---

# Assembly Pipeline

Idea

↓

Story Selection

↓

Character Selection

↓

Production Component Selection

↓

Prompt Block Generation

↓

Prompt Assembly

↓

Validation

↓

Platform Optimization

↓

Final Prompt

---

# Assembly Inputs

## Story

Source

Story Framework

Examples

- Alphabet Lesson
- Cooking Story
- Adventure

---

## Character

Source

Character OS

Examples

- Mochi
- Ollie

---

## Production Components

Source

PCL Library

Includes

- Camera
- Motion
- Expression
- Environment
- Lighting
- Audio
- Composition
- Color

---

## Technical Settings

Examples

- 16:9
- 9:16
- 4K
- 60 FPS
- 8 Seconds

---

## Platform Profile

Examples

- Google Flow
- Veo
- Runway
- Sora

---

# Assembly Workflow

Step 1

Validate Story Block

↓

Step 2

Load Character Block

↓

Step 3

Insert Production Components

↓

Step 4

Apply Style Block

↓

Step 5

Append Technical Block

↓

Step 6

Apply Platform Profile

↓

Step 7

Generate Final Prompt

---

# Conflict Resolution

When two blocks contain conflicting information:

Priority Order

1. Character Bible
2. Story Block
3. Production Components
4. Style Block
5. Technical Block
6. Platform Profile

Higher priority always overrides lower priority.

---

# Dependency Resolution

Prompt Assembler checks:

✓ Required blocks exist

✓ Version compatibility

✓ Character consistency

✓ Platform compatibility

✓ Missing dependencies

---

# Output Formats

## Basic

Fast draft.

---

## Production

Optimized prompt.

---

## Studio

Maximum quality.

Includes every available block.

---

# Error Handling

If a required block is missing:

- Stop assembly
- Report missing dependency
- Suggest replacement

If incompatible versions are detected:

- Display warning
- Recommend supported version

---

# Performance Goals

Prompt assembly should:

- Minimize duplication
- Maximize reuse
- Preserve consistency
- Reduce manual editing

---

# Example Assembly

Input

Story:
Cooking Lesson

Character:
Mochi

Camera:
Medium Shot

Motion:
Stirring

Expression:
Happy

Environment:
Kitchen

Lighting:
Warm Morning

Audio:
Cooking Profile

↓

Output

A production-ready prompt assembled from validated Story, Character, Camera, Motion, Expression, Environment, Lighting, Audio, Style, Technical, and Platform Blocks.

---

# Assembly Checklist

□ Story selected

□ Character selected

□ Required blocks loaded

□ Dependencies validated

□ Prompt assembled

□ Platform optimized

□ Validation completed

---

# Related Documents

- PE-001 Prompt Architecture
- PE-002 Prompt Blocks
- PCL-001 → PCL-009
- DOC-006 Prompt Engineering Standard
- QA-001 Final Video Checklist