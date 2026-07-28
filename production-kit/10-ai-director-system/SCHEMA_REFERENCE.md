# SCHEMA_REFERENCE.md

# AI Director System Schema Reference

Version: 1.0.0
Status: Stable

## Purpose

Định nghĩa các schema dữ liệu chuẩn dùng trong Module 10 AI Director System.

---

# Core Schemas

## Story Schema

Fields

- story_id
- title
- genre
- audience
- story_goal
- story_beats
- ending

---

## Character Schema

Fields

- character_id
- name
- dna
- appearance
- personality
- voice
- animation_profile

---

## Prompt Schema

Fields

- subject
- action
- environment
- camera
- lens
- composition
- lighting
- motion
- emotion
- fx
- style
- quality

---

## Scene Schema

Fields

- scene_id
- story_beat
- duration
- location
- characters
- camera_plan

---

## Shot Schema

Fields

- shot_id
- scene_id
- shot_type
- lens
- movement
- framing

---

## Production Schema

Fields

- production_id
- scenes
- shots
- prompts
- assets
- render_queue

---

## Release Schema

Fields

- version
- build
- manifest
- qa_reports
- release_notes

---

## Validation Rules

- Required fields must exist.
- IDs must be unique.
- Character DNA immutable.
- Prompt must pass QA.
- Release must include manifest.

---

## Outputs

- JSON Objects
- Manifest Files
- Production Package
- Release Package

Status: Approved
