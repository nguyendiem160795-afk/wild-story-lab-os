# MASTER-SKILL-INDEX.md

> **Module:** 07 -- Playbook OS\
> **Document Type:** AI Routing Index\
> **Version:** 3.0.0-draft\
> **Status:** Draft

------------------------------------------------------------------------

# Purpose

MASTER-SKILL-INDEX is the primary routing document for Playbook OS.

It is not merely a list of Skills.

Its responsibility is to route every user request to the correct:

-   Business Domain
-   Operational Domain
-   Capability
-   Executable Skill

before execution begins.

This document acts as the entry point for AI Directors, AI Agents,
Runtime Engines, and future automation systems.

------------------------------------------------------------------------

# AI Routing Pipeline

``` text
User Request
      │
      ▼
Intent Analysis
      │
      ▼
Business Domain Detection
      │
      ▼
Operational Domain Selection
      │
      ▼
Capability Selection
      │
      ▼
Skill Selection
      │
      ▼
Execution
      │
      ▼
Validation
      │
      ▼
Result
```

------------------------------------------------------------------------

# Routing Sources

MASTER-SKILL-INDEX does not duplicate information.

Instead, it references the authoritative registries.

  Registry              Responsibility
  --------------------- --------------------------------
  DOMAIN-REGISTRY       Business & Operational Domains
  CAPABILITY-REGISTRY   Capability catalog
  SKILL-REGISTRY        Executable Skills

------------------------------------------------------------------------

# Routing Algorithm

## Step 1

Determine the user's business objective.

↓

## Step 2

Identify the appropriate Business Domain.

↓

## Step 3

Locate the Operational Domain.

↓

## Step 4

Select the correct Capability.

↓

## Step 5

Locate the required Executable Skill.

↓

## Step 6

Execute the Skill.

↓

## Step 7

Validate the output.

------------------------------------------------------------------------

# Example Routing

## Example 1

User Goal

Register a new AI Asset

Routing

``` text
Enterprise Management
        │
        ▼
Enterprise Assets
        │
        ▼
CAP-081 AI Asset Management
        │
        ▼
PB-091 Register AI Asset
```

------------------------------------------------------------------------

## Example 2

User Goal

Create a Google Flow project

Routing

``` text
Content Production
        │
        ▼
Google Flow
        │
        ▼
CAP-104 Google Flow Production
        │
        ▼
PB-231 (future)
```

------------------------------------------------------------------------

# Routing Principles

-   Never bypass Capability selection.
-   Never execute an undefined Skill.
-   Every Skill must exist in SKILL-REGISTRY.
-   Every Capability must exist in CAPABILITY-REGISTRY.
-   Every Domain must exist in DOMAIN-REGISTRY.

------------------------------------------------------------------------

# AI Director Responsibilities

The AI Director shall:

1.  Analyze intent.
2.  Route requests.
3.  Select Capability.
4.  Execute Skill.
5.  Validate output.
6.  Record execution.

------------------------------------------------------------------------

# Related Documents

-   DOMAIN-REGISTRY.md
-   CAPABILITY-REGISTRY.md
-   SKILL-REGISTRY.md
-   SKILL-GRAPH.md

------------------------------------------------------------------------

# Next Milestone

Capability Packs (CAP-XXX)

------------------------------------------------------------------------

**End of Document**
