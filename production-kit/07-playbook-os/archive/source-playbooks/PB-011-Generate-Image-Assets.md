# PB-011 --- Generate Image Assets

> **Module:** 07-playbook-os\
> **Playbook ID:** PB-011\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Executive Summary

Generate all required image assets from approved production inputs while
maintaining character, world, visual style, and brand consistency.

------------------------------------------------------------------------

# Purpose

Produce production-ready image assets that become the visual foundation
for AI video generation.

------------------------------------------------------------------------

# Business Value

-   Standardize image generation.
-   Maintain visual consistency.
-   Reduce regeneration costs.
-   Create reusable visual assets.

------------------------------------------------------------------------

# Prerequisites

-   PB-010 Production Readiness Review approved.

------------------------------------------------------------------------

# Inputs

Required

-   Approved Character Package
-   Approved Story Package
-   Approved Prompt Package
-   Production Plan

Optional

-   Reference Images
-   Brand Guidelines

------------------------------------------------------------------------

# Outputs

-   Master Character Images
-   Scene Images
-   Environment Images
-   Props & Object Images
-   Image Generation Report

------------------------------------------------------------------------

# Workflow

1.  Load approved production assets.
2.  Select target AI image platform.
3.  Generate character images.
4.  Generate environment images.
5.  Generate scene assets.
6.  Perform first-pass quality check.
7.  Organize assets by scene.
8.  Export Image Asset Package.

------------------------------------------------------------------------

# Image Asset Package

``` text
Image Assets
├── Characters
├── Environments
├── Props
├── Scene Images
├── Reference Images
└── Generation Report
```

------------------------------------------------------------------------

# Decision Rules

  Condition                 Action
  ------------------------- -------------------------------
  Character inconsistency   Regenerate character images
  Style mismatch            Adjust prompts and regenerate
  Missing scene asset       Generate required asset
  Approved output           Export package

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Character appearance matches package
-   [ ] Environment matches story
-   [ ] Visual style is consistent
-   [ ] Resolution meets project standard
-   [ ] All required assets generated
-   [ ] Assets organized correctly

------------------------------------------------------------------------

# Success Criteria

-   Every required image exists.
-   Character identity remains consistent.
-   Images are ready for video generation.
-   No blocking visual issues remain.

------------------------------------------------------------------------

# Deliverables

-   Image Asset Package
-   Generation Report
-   Asset Inventory

------------------------------------------------------------------------

# Best Practices

-   Lock character prompts before scene generation.
-   Reuse approved reference assets.
-   Batch similar scenes together.
-   Archive every approved generation.

------------------------------------------------------------------------

# Common Mistakes

-   Changing character appearance between scenes.
-   Mixing artistic styles.
-   Using low-resolution outputs.
-   Skipping quality checks.

------------------------------------------------------------------------

# Related Playbooks

**Previous**

-   PB-010 Production Readiness Review

**Next**

-   PB-012 Validate Image Assets

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**
