# Assets

> Module 08 — AI Agent Operating System

Version: **0.1.0**

---

# Purpose

The `assets` directory contains all reusable non-source-code resources used throughout the AI Agent Operating System.

Assets improve consistency across documentation, presentations, workflows, and future implementations.

Unlike documentation, assets are primarily visual or binary resources intended to support communication rather than define system behavior.

---

# Objectives

The asset library exists to:

- Centralize reusable visual resources
- Eliminate duplicated files
- Maintain visual consistency
- Support documentation
- Support presentations
- Support training materials

---

# Asset Categories

## Architecture

Architecture diagrams describing the operating system.

Examples:

- System Architecture
- Layered Architecture
- Workflow Architecture
- Knowledge Architecture

Recommended location:

```text
assets/
└── architecture/
```

---

## Diagrams

General-purpose engineering diagrams.

Examples:

- Sequence Diagrams
- Component Diagrams
- Flowcharts
- State Machines

Recommended location:

```text
assets/
└── diagrams/
```

---

## Branding

Official branding resources.

Examples:

- Logos
- Color Palette
- Icons
- Typography

Recommended location:

```text
assets/
└── branding/
```

---

## Illustrations

Images used inside documentation.

Examples:

- Architecture illustrations
- Workflow illustrations
- Agent illustrations

Recommended location:

```text
assets/
└── illustrations/
```

---

## Icons

Reusable SVG or PNG icons.

Examples:

- Agent
- Workflow
- Memory
- Knowledge
- Prompt
- Automation

Recommended location:

```text
assets/
└── icons/
```

---

## Screenshots

Reference screenshots.

Examples:

- GitHub
- Google Flow
- OpenAI
- Runway
- Veo

Recommended location:

```text
assets/
└── screenshots/
```

---

# Recommended Structure

```text
assets/
│
├── README.md
├── architecture/
├── branding/
├── diagrams/
├── icons/
├── illustrations/
├── screenshots/
└── references/
```

---

# Supported Formats

Preferred image formats:

- SVG
- PNG
- WebP

Preferred document formats:

- PDF

Preferred diagram formats:

- Mermaid
- Draw.io
- SVG

Avoid proprietary formats whenever possible.

---

# Naming Convention

Use lowercase kebab-case.

Examples:

```
system-architecture.svg

workflow-engine.png

knowledge-graph.drawio

agent-lifecycle.pdf
```

Avoid:

```
Architecture.png

Image Final.png

diagram1.svg
```

---

# Versioning

Important assets should be versioned.

Example:

```
system-architecture-v1.svg

system-architecture-v2.svg
```

Do not overwrite historical production assets.

---

# Documentation References

Assets should never exist without documentation.

Whenever an asset is introduced:

- Explain its purpose.
- Reference it from documentation.
- Record significant updates.

---

# Optimization Guidelines

Assets should be:

- High quality
- Lightweight
- Reusable
- Clearly named
- Easy to locate

Avoid storing duplicate images.

---

# Repository Rules

Do not store:

- Temporary exports
- Working files
- Personal assets
- Unused graphics

Store only production-ready assets.

---

# Future Expansion

Future versions may include:

```text
assets/
├── animations/
├── videos/
├── audio/
├── mockups/
├── ui/
└── presentations/
```

---

# Related Documents

- DIRECTORY_STRUCTURE.md
- ARCHITECTURE.md
- docs/README.md

---

# Summary

The `assets` directory is the central repository for reusable visual resources used by the AI Agent Operating System.

A well-organized asset library improves documentation quality, strengthens visual consistency, and reduces duplication across the Wild Story Lab ecosystem.