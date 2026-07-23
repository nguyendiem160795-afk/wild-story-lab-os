# AG-002 — Agent Roles

Version: 1.0.0

Status: Production

Owner: Wild Story Lab

Last Updated: 2026-07-23

---

# Purpose

Agent Roles defines the responsibilities, boundaries, authority, collaboration model, and expected outputs for every AI Agent operating within Wild Story Lab OS.

Each agent has a clearly defined specialization, minimizing overlap and maximizing production efficiency.

---

# Objectives

- Define clear responsibilities
- Prevent role conflicts
- Improve collaboration
- Enable scalable expansion
- Standardize outputs
- Simplify orchestration

---

# Role Philosophy

One Agent

↓

One Primary Responsibility

↓

Many Supporting Capabilities

No agent should attempt to perform every task.

---

# Agent Hierarchy

Executive Layer

↓

Orchestrator Layer

↓

Domain Agents

↓

Utility Agents

↓

Infrastructure Agents

---

# Executive Layer

## Human Director

Responsibilities

- Define production goals
- Approve final releases
- Set creative direction
- Resolve conflicts

Authority

Highest

---

# Orchestrator Layer

## Orchestrator Agent

Responsibilities

- Analyze requests
- Break work into tasks
- Assign agents
- Monitor execution
- Consolidate outputs

Inputs

Human requests

Outputs

Execution plans

Dependencies

All agents

---

# Creative Domain

## Story Agent

Responsibilities

- Story structure
- Educational flow
- Emotional curve
- Hooks
- Scene sequencing

Produces

- Story Outline
- Story Script
- Story QA Notes

---

## Character Agent

Responsibilities

- Character Bible
- Expressions
- Personality
- Motion consistency
- Dialogue style

Produces

- Character Profile
- Character Validation
- Expression Guide

---

## Prompt Agent

Responsibilities

- Prompt Engineering
- Prompt Optimization
- Platform Adaptation
- Prompt Testing

Supports

- Google Flow
- Veo
- Runway
- Sora
- Kling

Produces

- Production Prompt
- Prompt Recipe
- Optimization Report

---

## Visual Director Agent

Responsibilities

- Camera Language
- Composition
- Lighting
- Color Palette
- Cinematic Style

Produces

- Visual Plan
- Camera Plan
- Lighting Plan

---

# Production Domain

## Asset Agent

Responsibilities

- Asset Discovery
- Asset Selection
- Asset Validation
- Asset Reuse

Produces

- Asset Package
- Dependency Report

---

## Runtime Agent

Responsibilities

- Production Execution
- Workflow Control
- Scene Pipeline
- Runtime Monitoring

Produces

- Runtime Report
- Production Status

---

## Render Agent

Responsibilities

- Render Planning
- Platform Configuration
- Render Validation
- Render Optimization

Produces

- Render Package
- Render Metrics

---

## Publisher Agent

Responsibilities

- SEO
- Metadata
- Thumbnail
- Scheduling
- Platform Packaging

Produces

- Publishing Package
- SEO Report

---

# Knowledge Domain

## Knowledge Agent

Responsibilities

- Knowledge Graph
- Search
- References
- Taxonomy
- Version Retrieval

Produces

- Knowledge Report
- Search Results

---

# Quality Domain

## QA Agent

Responsibilities

- Character QA
- Story QA
- Prompt QA
- Render QA
- Publishing QA

Produces

- QA Report
- Quality Score
- Improvement Suggestions

---

# Governance Domain

## Governance Agent

Responsibilities

- Policy Validation
- Version Compliance
- Audit Support
- Lifecycle Management

Produces

- Compliance Report
- Governance Status

---

# Analytics Domain

## Analytics Agent

Responsibilities

- Production Analytics
- Performance Metrics
- Trend Detection
- Recommendation Generation

Produces

- KPI Dashboard
- Performance Report

---

# Collaboration Rules

Every agent

✓ Owns one primary domain

✓ May request assistance

✓ Cannot bypass governance

✓ Reports execution status

✓ Shares knowledge

---

# Escalation Rules

Agent

↓

Orchestrator

↓

Human Director

---

# Authority Matrix

| Agent | Create | Modify | Approve | Publish |
|---------|:------:|:------:|:-------:|:-------:|
| Story | ✓ | ✓ | ✗ | ✗ |
| Character | ✓ | ✓ | ✗ | ✗ |
| Prompt | ✓ | ✓ | ✗ | ✗ |
| Asset | ✓ | ✓ | ✗ | ✗ |
| Runtime | ✓ | ✓ | ✗ | ✗ |
| QA | ✗ | ✗ | ✓ | ✗ |
| Governance | ✗ | ✗ | ✓ | ✗ |
| Publisher | ✗ | ✓ | ✗ | ✓ |
| Human Director | ✓ | ✓ | ✓ | ✓ |

---

# Performance Indicators

Evaluate agents using

- Task Success Rate
- Average Execution Time
- QA Pass Rate
- Knowledge Reuse
- Error Recovery
- Collaboration Efficiency

---

# Best Practices

- Keep responsibilities focused.
- Avoid overlapping ownership.
- Prefer collaboration over duplication.
- Escalate unresolved conflicts.
- Continuously improve through analytics.

---

# Related Documents

- AG-001 Agent Architecture
- AG-003 Agent Communication
- KS-001 Knowledge Graph
- RT-001 Production Orchestrator