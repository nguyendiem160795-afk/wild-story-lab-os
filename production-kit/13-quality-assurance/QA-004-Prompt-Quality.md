# QA-004 — Prompt Quality

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Prompt Quality defines the validation standards for every prompt generated within Wild Story Lab OS.

The objective is to ensure prompts are complete, deterministic, platform-optimized, reusable, and capable of producing consistent AI-generated outputs.

---

# Objectives

- Improve prompt reliability
- Reduce AI ambiguity
- Ensure platform compatibility
- Preserve character consistency
- Increase generation success rate
- Support automated prompt evaluation

---

# Validation Workflow

Prompt Recipe

↓

Prompt Builder

↓

Prompt Validation

↓

Platform Validation

↓

Optimization

↓

Approval

↓

Production

---

# Prompt Architecture Validation

Every prompt should include

✓ Subject

✓ Character

✓ Environment

✓ Action

✓ Camera

✓ Lighting

✓ Motion

✓ Style

✓ Mood

✓ Output Constraints

---

# Character Validation

Verify

✓ Correct Character Bible

✓ Character Pack Version

✓ Appearance Description

✓ Clothing

✓ Expressions

✓ Accessories

✓ Personality

---

# Environment Validation

Verify

✓ Environment Profile

✓ Time of Day

✓ Lighting Profile

✓ Background Consistency

✓ Props

✓ Atmosphere

---

# Camera Validation

Verify

✓ Shot Type

✓ Camera Angle

✓ Camera Movement

✓ Framing

✓ Focus

---

# Motion Validation

Verify

✓ Character Motion

✓ Secondary Motion

✓ Environmental Motion

✓ Motion Continuity

---

# Lighting Validation

Verify

✓ Lighting Style

✓ Shadow Consistency

✓ Color Temperature

✓ Exposure

---

# Style Validation

Verify

✓ Pixar Style

✓ Visual Quality

✓ Color Palette

✓ Material Definition

✓ Rendering Style

---

# Platform Validation

Supported Platforms

- Google Flow
- Veo
- Runway
- Sora
- Kling
- Pika

Verify

✓ Platform Profile

✓ Supported Parameters

✓ Compatible Syntax

✓ Platform Constraints

---

# Prompt Safety Validation

Verify

✓ Child-safe language

✓ No prohibited content

✓ Positive educational tone

✓ Appropriate emotional intensity

---

# Prompt Consistency

Verify

✓ Character consistency

✓ Story consistency

✓ Visual consistency

✓ Prompt Recipe consistency

---

# Common Issues

Critical

- Missing character definition
- Missing environment
- Conflicting instructions
- Unsupported platform syntax

Major

- Weak camera description
- Incomplete motion
- Missing lighting

Minor

- Redundant wording
- Minor grammar issues
- Excessive adjectives

---

# Prompt Quality Score

| Category | Weight |
|----------|-------:|
| Structure | 20% |
| Character | 20% |
| Environment | 15% |
| Camera | 10% |
| Motion | 10% |
| Lighting | 10% |
| Platform Compatibility | 10% |
| Safety | 5% |

Passing Score

≥96%

---

# QA Checklist

Before approval verify

✓ Prompt Recipe applied

✓ Character Pack correct

✓ Environment Profile correct

✓ Platform Profile selected

✓ Prompt optimized

✓ Quality score ≥96%

---

# Best Practices

- Keep prompts deterministic.
- Avoid contradictory instructions.
- Use approved Prompt Recipes.
- Match the target platform profile.
- Validate prompts before rendering.

---

# Related Documents

- 10-prompt-engine
- RT-003 Asset Resolver
- RT-004 Consistency Manager
- QA-002 Character Consistency
- QA-003 Story Validation