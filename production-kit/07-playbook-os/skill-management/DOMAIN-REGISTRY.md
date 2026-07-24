# DOMAIN-REGISTRY.md

> **Module:** 07 -- Playbook OS\
> **Document Type:** Registry\
> **Version:** 3.0.0-draft\
> **Status:** Draft

------------------------------------------------------------------------

# Purpose

This registry is the authoritative catalog of all Business Domains and
Operational Domains used by Playbook OS.

Every Capability MUST belong to exactly one Operational Domain.

Every Executable Skill MUST belong to exactly one Capability.

------------------------------------------------------------------------

# Architecture

``` text
Business Domain
    │
    ▼
Operational Domain
    │
    ▼
Capability
    │
    ▼
Executable Skill
```

------------------------------------------------------------------------

# Business Domains

  ID      Business Domain           Status
  ------- ------------------------- ---------
  BD-01   Enterprise Management     Planned
  BD-02   Content Production        Planned
  BD-03   AI Engineering            Planned
  BD-04   Creative Production       Planned
  BD-05   Distribution & Growth     Planned
  BD-06   Operations & Governance   Planned

------------------------------------------------------------------------

# Operational Domains (Initial)

## Enterprise Management

  ID       Operational Domain
  -------- ----------------------
  OD-001   Enterprise Assets
  OD-002   Knowledge Management
  OD-003   Governance
  OD-004   Risk & Compliance

## Content Production

  ID       Operational Domain
  -------- ----------------------
  OD-101   Story Engineering
  OD-102   Character Production
  OD-103   World Building
  OD-104   Prompt Engineering
  OD-105   Google Flow
  OD-106   Veo Production
  OD-107   Thumbnail Design

## Distribution & Growth

  ID       Operational Domain
  -------- --------------------
  OD-201   SEO
  OD-202   Publishing
  OD-203   Analytics

## AI Engineering

  ID       Operational Domain
  -------- --------------------
  OD-301   AI Agents
  OD-302   Automation
  OD-303   Runtime Engine

------------------------------------------------------------------------

# Governance Rules

1.  A Capability belongs to one Operational Domain.
2.  A Skill belongs to one Capability.
3.  Domains are stable identifiers and should rarely change.
4.  New Domains require architecture review.

------------------------------------------------------------------------

# Next Documents

1.  CAPABILITY-REGISTRY.md
2.  SKILL-REGISTRY.md
3.  MASTER-SKILL-INDEX.md (updated)

------------------------------------------------------------------------

**End of Document**
