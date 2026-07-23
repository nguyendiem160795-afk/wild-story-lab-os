---
document_id: DOC-012
module: 03-world-os
category: core-documentation
title: World Asset Registry
version: 1.0.0
status: Approved
classification: Public
owner: Wild Story Lab
created_date: 2026-07-23
last_updated: 2026-07-23
---

# World Asset Registry

> Official asset registration and management system for Wild Story Lab World OS.

---

# 1. Purpose

This document defines the World Asset Registry System.

The purpose is to create a centralized system for managing all assets related to worlds.

The registry ensures:

- Asset ownership.
- Asset identification.
- Asset tracking.
- Version management.
- Production reuse.
- World consistency.

---

# 2. Asset Registry Definition

World Asset Registry is the official database structure for tracking world-related assets.

It manages:

```
Environment Assets

+

Location Assets

+

Background Assets

+

Object Assets

+

Prompt Assets

+

Reference Assets
```

---

# 3. Asset Registry Architecture

The registry structure:

```
World

↓

Location

↓

Asset Category

↓

Asset ID

↓

Asset Version

↓

Production Usage
```

---

# 4. Asset Identification System

Every asset requires a unique ID.

Format:

```
[TYPE]-[CATEGORY]-[NUMBER]
```

---

Examples:

```
WORLD-001

ENV-BG-001

ENV-PROP-001

LOC-001

PROMPT-WORLD-001
```

---

# 5. Asset Categories

World assets are classified into:

---

# 5.1 Location Assets

Purpose:

Manage location-specific assets.

Examples:

```
Classroom

Forest

City

Island
```

---

# 5.2 Environment Assets

Purpose:

Manage environmental components.

Examples:

```
Background

Architecture

Nature

Lighting
```

---

# 5.3 Object Assets

Purpose:

Manage interactive objects.

Examples:

```
Books

Tools

Learning Objects

Special Items
```

---

# 5.4 Prompt Assets

Purpose:

Manage AI generation instructions.

Examples:

```
World Prompt

Location Prompt

Scene Prompt
```

---

# 6. Asset Metadata Standard

Every asset requires:

```
Asset ID

Asset Name

Category

World ID

Location ID

Version

Status

Owner

Creation Date

Usage
```

---

# 7. Asset Status System

Every asset must have a status:

```
Draft

Review

Approved

Canonical

Deprecated
```

---

# 8. Canonical Asset System

Canonical assets are official references.

Rules:

- Cannot be replaced without review.
- Must preserve original identity.
- Must maintain version history.
- Must be used for consistency checks.

---

Example:

```
ENV-BG-001

Daily Learning Classroom Background

Status:

Canonical
```

---

# 9. Asset Relationship System

Assets must maintain relationships.

Structure:

```
World

↓

Location

↓

Asset

↓

Scene
```

---

Example:

```
WORLD-001

↓

LOCATION-001

↓

ENV-PROP-001 Learning Board

↓

Episode Scene
```

---

# 10. Asset Version Control

Every asset follows:

```
Creation

↓

Review

↓

Approval

↓

Release

↓

Update
```

---

Version format:

```
v1.0.0
```

---

# 11. Asset Change Rules

Changes require:

```
Change Request

↓

Impact Review

↓

Approval

↓

Version Update
```

---

Changes include:

```
Visual Update

Function Update

Style Update

Replacement
```

---

# 12. AI Production Asset Usage

AI production requires:

```
Approved Asset

+

Correct Version

+

World Reference

+

Usage Context
```

---

AI should not use:

```
Unknown Assets

Deprecated Assets

Wrong World Assets
```

---

# 13. Asset Search System

Assets should be searchable by:

```
Asset ID

World

Location

Category

Version

Status
```

---

# 14. Asset Registry Example

Canonical World:

```
WORLD-001

Mochi Learning Universe
```

Registry:

```
LOC-001

Daily Learning Classroom


ENV-BG-001

Classroom Background


ENV-PROP-001

Learning Board


PROMPT-WORLD-001

Classroom Generation Prompt
```

---

# 15. Asset Quality Checklist

| Requirement | Status |
|---|---|
| Asset ID assigned | Required |
| Metadata complete | Required |
| Version recorded | Required |
| World relationship defined | Required |
| Quality approved | Required |
| Production tested | Required |

---

# 16. Asset Governance Rules

All assets must:

1. Have a registered identity.
2. Belong to an approved world.
3. Maintain version history.
4. Have documented usage.
5. Pass quality validation.

---

# 17. Future Asset Expansion

Future versions may support:

```
AI Asset Generation

Automatic Asset Tagging

Asset Recommendation System

Asset Intelligence Layer
```

---

# 18. References

Related Documents:

- DOC-005 Environment Asset Pack
- DOC-010 World Prompt Standard
- DOC-011 World Production Workflow
- DOC-013 World Consistency System
- DOC-014 World Version Control

Related Modules:

- 02-character-os
- 11-production-runtime
- 14-knowledge-system
- 15-ai-agent-framework

---

# 19. Revision History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-07-23 | Initial World Asset Registry |

---

# End of Document