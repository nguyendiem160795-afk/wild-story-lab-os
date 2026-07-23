# PE-002 — Prompt Blocks

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

This document defines the standardized prompt blocks used by the Wild Story Lab Prompt Engine.

Each block represents a reusable unit of creative intent. By combining these blocks, creators can rapidly assemble consistent, production-ready prompts.

---

# Block Design Principles

Every Prompt Block must:

- Have a single responsibility.
- Be reusable across projects.
- Be platform independent.
- Support version control.
- Be human-readable.
- Be machine-friendly.

---

# Block Catalog

| ID | Block | Required | Source |
|----|-------|----------|--------|
| PB-01 | Story | Yes | Story Framework |
| PB-02 | Character | Yes | Character OS |
| PB-03 | Camera | Yes | PCL-001 |
| PB-04 | Motion | Yes | PCL-002 |
| PB-05 | Expression | Yes | PCL-003 |
| PB-06 | Environment | Yes | PCL-005 |
| PB-07 | Lighting | Yes | PCL-004 |
| PB-08 | Audio | Optional | PCL-006 |
| PB-09 | Composition | Yes | PCL-008 |
| PB-10 | Color | Yes | PCL-009 |
| PB-11 | Style | Yes | Character OS |
| PB-12 | Technical | Yes | Prompt Engine |
| PB-13 | Platform | Yes | Platform Profile |

---

# Block Specification

Each Prompt Block must include:

## Name

Unique block identifier.

---

## Purpose

Describe why the block exists.

---

## Inputs

Required information received from previous modules.

---

## Outputs

Standardized prompt fragment.

---

## Dependencies

Referenced documents.

---

## Validation Rules

Rules that determine whether the block is complete.

---

## Example

Example implementation.

---

# Standard Block Template

## Block Name

Purpose

Inputs

Outputs

Dependencies

Validation

Prompt Fragment

Example

---

# Prompt Assembly Order

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

Composition

↓

Color

↓

Style

↓

Technical

↓

Platform

---

# Dependency Map

Story
↓

Character
↓

Production Components
↓

Prompt Blocks
↓

Prompt Assembler
↓

Prompt Validator
↓

Final Prompt

---

# Versioning Rules

Every Prompt Block must contain:

- Version
- Status
- Last Updated
- Dependencies
- Compatible Platforms

---

# Block Validation Checklist

□ Purpose defined

□ Inputs documented

□ Outputs documented

□ Dependencies listed

□ Validation rules completed

□ Example included

□ Compatible with Prompt Architecture

---

# Example Block

Name

Camera Block

Purpose

Define cinematic viewpoint.

Input

Camera Library

Output

Camera prompt fragment

Dependency

PCL-001

Validation

Camera movement must match scene intent.

Prompt Fragment

Medium shot with slow dolly in.

---

# Related Documents

- PE-001 Prompt Architecture
- PCL-001 → PCL-009
- DOC-006 Prompt Engineering Standard
- QA-001 Final Video Checklist