# QA-005 — Render Validation

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Render Validation defines the quality standards for evaluating AI-generated visual outputs before approval and publication.

It ensures that every rendered scene meets technical, artistic, and educational requirements while remaining consistent with the approved production specifications.

---

# Objectives

- Validate render quality
- Ensure visual consistency
- Detect rendering artifacts
- Verify technical specifications
- Improve production reliability
- Support automated render assessment

---

# Validation Workflow

Prompt Approved

↓

AI Rendering

↓

Technical Validation

↓

Visual Validation

↓

Consistency Validation

↓

QA Approval

↓

Production Release

---

# Technical Validation

Verify

✓ Resolution

✓ Aspect Ratio

✓ Frame Rate

✓ Video Duration

✓ Encoding Format

✓ Bitrate

✓ File Integrity

---

# Image Quality

Verify

✓ Sharpness

✓ Detail Preservation

✓ Noise Level

✓ Compression Artifacts

✓ Edge Quality

✓ Texture Quality

✓ Material Definition

---

# Character Validation

Verify

✓ Character Identity

✓ Facial Accuracy

✓ Body Proportions

✓ Clothing

✓ Accessories

✓ Expressions

✓ Animation Consistency

---

# Environment Validation

Verify

✓ Background Quality

✓ Lighting

✓ Props

✓ Environmental Details

✓ Spatial Consistency

✓ Depth

---

# Camera Validation

Verify

✓ Framing

✓ Camera Angle

✓ Camera Movement

✓ Focus

✓ Stability

✓ Composition

---

# Motion Validation

Verify

✓ Character Animation

✓ Secondary Motion

✓ Object Motion

✓ Motion Blur

✓ Animation Smoothness

✓ Frame Continuity

---

# Lighting Validation

Verify

✓ Exposure

✓ Shadow Quality

✓ Highlight Control

✓ Global Illumination

✓ Color Consistency

✓ White Balance

---

# Color Validation

Verify

✓ Brand Palette

✓ Saturation

✓ Contrast

✓ Color Harmony

✓ Skin/Fur Accuracy

✓ Background Balance

---

# Audio Synchronization

Verify

✓ Lip Sync

✓ Sound Effects Timing

✓ Background Music

✓ Voice Synchronization

✓ Audio Balance

---

# Platform Validation

Verify

✓ Google Flow Profile

✓ Veo Profile

✓ Runway Profile

✓ Sora Profile

✓ Platform Constraints

---

# Render Defects

Critical

- Broken frames
- Missing character
- Corrupted output
- Severe flickering
- Major geometry distortion

Major

- Lighting inconsistency
- Camera instability
- Animation glitches
- Incorrect shadows

Minor

- Slight noise
- Minor texture issues
- Small lighting variation

---

# Render Quality Score

| Category | Weight |
|----------|-------:|
| Technical | 15% |
| Image Quality | 15% |
| Character | 20% |
| Environment | 10% |
| Camera | 10% |
| Motion | 10% |
| Lighting | 10% |
| Color | 5% |
| Audio | 5% |

Passing Score

≥96%

---

# QA Checklist

Before approval verify

✓ Render profile correct

✓ Character validated

✓ Environment validated

✓ Camera approved

✓ Motion smooth

✓ Lighting approved

✓ Resolution verified

✓ Audio synchronized

✓ Render score ≥96%

---

# Best Practices

- Validate every render independently.
- Compare renders against Golden References.
- Review renders on multiple display sizes.
- Archive approved renders.
- Re-render scenes that fail critical validation.

---

# Related Documents

- QA-002 Character Consistency
- QA-003 Story Validation
- QA-004 Prompt Quality
- RT-005 Render Pipeline
- RT-006 Production Checklist