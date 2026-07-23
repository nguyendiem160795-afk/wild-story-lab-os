---
document_id: DOC-010
module: 03-world-os
category: core-documentation
title: World Prompt Standard
version: 1.0.0
status: Approved
classification: Public
owner: Wild Story Lab
created_date: 2026-07-23
last_updated: 2026-07-23
---

# World Prompt Standard

> Official prompt engineering standard for generating consistent worlds inside Wild Story Lab.

---

# 1. Purpose

This document defines the World Prompt Standard.

The purpose is to transform approved World OS data into structured AI prompts for:

- Image generation.
- Video generation.
- Environment creation.
- Location visualization.
- Cinematic scene production.

---

# 2. Prompt Philosophy

A world prompt is not only a visual description.

A world prompt contains:

```
World Identity

+

Location Context

+

Visual Language

+

Environment Details

+

Camera Direction

+

Production Intent
```

---

# 3. World Prompt Architecture

The standard structure:

```
World Reference

↓

Location Reference

↓

Environment Description

↓

Visual Style

↓

Camera

↓

Lighting

↓

Atmosphere

↓

Motion / Usage
```

---

# 4. World Reference Layer

## Purpose

Defines the universe identity.

Required:

```
World Name

World Theme

World Style

World Personality
```

---

Example:

```
WORLD-001

Mochi Learning Universe

A joyful educational 3D animated world,
full of curiosity, friendship, and discovery.
```

---

# 5. Location Reference Layer

## Purpose

Defines where the scene happens.

Required:

```
Location Name

Location Purpose

Location Features

Story Function
```

---

Example:

```
Location:

Daily Learning Classroom

Purpose:

Main educational interaction space

Features:

Bookshelves, learning boards, colorful furniture
```

---

# 6. Environment Description Layer

Defines the physical environment.

Include:

```
Architecture

Objects

Nature Elements

Materials

Atmosphere
```

---

Example:

```
A bright modern classroom with rounded furniture,
large windows, colorful learning objects,
warm educational atmosphere.
```

---

# 7. Visual Style Layer

Every prompt must include approved visual identity.

Required:

```
Art Style

Rendering Style

Shape Language

Color Language
```

---

Example:

```
Premium 3D animated style,
soft rounded shapes,
bright colors,
cinematic kids animation quality.
```

---

# 8. Camera Prompt System

Camera description must define:

```
Shot Type

Camera Angle

Camera Movement

Composition
```

---

## Camera Examples

Wide Shot:

```
Wide cinematic establishing shot,
showing the entire environment.
```

---

Medium Shot:

```
Medium shot focusing on character interaction.
```

---

Close Shot:

```
Close-up emotional character moment.
```

---

# 9. Lighting Prompt System

Lighting must match World Identity.

Required:

```
Light Source

Mood

Time

Atmosphere
```

---

Examples:

```
Soft morning sunlight,
warm cinematic lighting,
peaceful and joyful atmosphere.
```

---

# 10. Atmosphere Layer

Defines emotional environment.

Examples:

```
Magical

Friendly

Educational

Adventure

Peaceful
```

---

# 11. Motion Prompt System

For AI video generation.

Include:

```
Character Motion

Environment Motion

Camera Motion

Speed
```

---

Example:

```
Characters move naturally,
objects gently animate,
slow cinematic camera movement.
```

---

# 12. World Consistency Prompt Rules

Every prompt must preserve:

```
World Identity

+

Location Identity

+

Visual Style

+

Rule System
```

---

AI must not:

```
Change art style.

Change environment identity.

Create unrelated objects.

Break world logic.
```

---

# 13. Prompt Template

Official format:

```
[Camera Shot + Camera Movement]

+

[World Reference]

+

[Location Description]

+

[Environment Details]

+

[Visual Style]

+

[Lighting]

+

[Atmosphere]

+

[Motion]
```

---

# 14. Image Prompt Template

Example:

```
Wide cinematic shot of WORLD-001 Mochi Learning Universe,
inside Daily Learning Classroom,
bright colorful educational environment,
premium 3D animated style,
soft cinematic lighting,
friendly magical atmosphere.
```

---

# 15. Video Prompt Template

Example:

```
Medium tracking shot inside WORLD-001 Mochi Learning Universe,
Mochi walking through Daily Learning Classroom,
bright educational environment,
premium 3D animation style,
warm cinematic lighting,
smooth character movement,
gentle camera motion.
```

---

# 16. Prompt Version Control

Every production prompt requires:

```
Prompt ID

World Reference

Version

Purpose

Usage
```

---

Example:

```
PROMPT-WORLD-001

Version:

v1.0.0

Purpose:

Classroom environment generation
```

---

# 17. Prompt Validation Checklist

| Requirement | Status |
|---|---|
| World reference included | Required |
| Location reference included | Required |
| Style defined | Required |
| Camera defined | Required |
| Lighting defined | Required |
| Motion defined | Required |

---

# 18. Canonical Example

World:

```
WORLD-001

Mochi Learning Universe
```

Prompt Identity:

```
Friendly

Educational

Magical

Premium 3D Animation
```

---

# 19. References

Related Documents:

- DOC-003 World Identity System
- DOC-005 Environment Asset Pack
- DOC-006 Background Design Standard
- DOC-007 World Rules Framework
- DOC-011 World Production Workflow

Related Modules:

- 02-character-os
- 11-production-runtime
- 14-knowledge-system
- 15-ai-agent-framework

---

# 20. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial World Prompt Standard |

---

# End of Document