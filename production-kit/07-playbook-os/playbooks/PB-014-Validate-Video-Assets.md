# PB-014 --- Validate Video Assets

> **Module:** 07-playbook-os\
> **Playbook ID:** PB-014\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Executive Summary

Validate all generated video assets to ensure they satisfy creative,
technical, and production quality standards before progressing to audio
production and final assembly.

------------------------------------------------------------------------

# Purpose

Verify that every generated video scene is visually consistent,
technically correct, and aligned with the approved Story Package,
Character Package, Prompt Package, and Production Plan.

------------------------------------------------------------------------

# Business Value

-   Prevent defective video assets from entering post-production.
-   Preserve character, environment, and motion consistency.
-   Reduce downstream editing and regeneration costs.
-   Increase production reliability.

------------------------------------------------------------------------

# Prerequisites

-   PB-013 Generate Video Assets completed.

------------------------------------------------------------------------

# Inputs

Required

-   Video Asset Package
-   Production Plan
-   Approved Story Package
-   Approved Character Package
-   Approved Prompt Package

Optional

-   Motion Style Guide
-   Camera Language Guide
-   Brand Guidelines

------------------------------------------------------------------------

# Outputs

-   Approved Video Asset Package
-   Video Validation Report
-   Regeneration Request (if required)
-   Issue Log

------------------------------------------------------------------------

# Workflow

1.  Load Video Asset Package.
2.  Verify scene completeness.
3.  Review visual continuity.
4.  Validate character consistency.
5.  Validate camera movement and composition.
6.  Validate animation quality.
7.  Review technical specifications.
8.  Approve or reject assets.

------------------------------------------------------------------------

# Validation Checklist

-   [ ] All planned scenes are present.
-   [ ] Character identity is consistent.
-   [ ] Camera language follows storyboard.
-   [ ] Motion is smooth and natural.
-   [ ] Scene transitions are coherent.
-   [ ] Visual style is consistent.
-   [ ] Resolution and frame rate meet project standards.
-   [ ] No rendering artifacts detected.
-   [ ] File naming follows project convention.

------------------------------------------------------------------------

# Decision Rules

  Validation Result   Action
  ------------------- ----------------------------
  All checks passed   Approve Video Assets
  Minor issues        Regenerate affected scenes
  Critical issues     Reject Video Asset Package

------------------------------------------------------------------------

# Success Criteria

-   Every scene passes validation.
-   Character continuity is preserved.
-   Technical quality meets production standards.
-   Assets are ready for audio production.

------------------------------------------------------------------------

# Deliverables

-   Approved Video Asset Package
-   Video Validation Report
-   Issue Log
-   Validation Checklist

------------------------------------------------------------------------

# Best Practices

-   Review videos scene-by-scene.
-   Compare against approved storyboard.
-   Validate motion before visual effects.
-   Archive approved asset versions.

------------------------------------------------------------------------

# Common Mistakes

-   Character appearance changes between scenes.
-   Inconsistent camera language.
-   Abrupt or unrealistic motion.
-   Accepting videos with rendering defects.

------------------------------------------------------------------------

# Related Playbooks

**Previous**

-   PB-013 Generate Video Assets

**Next**

-   PB-015 Generate Audio Assets

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**
