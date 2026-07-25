## Execution Contract
- ID: PB-012-Validate-Image-Assets (1)
- Version: 1.0
- Status: Executable Draft

## Objective

## Inputs

## Outputs

## Validation

---

# PB-012 --- Validate Image Assets

> **Module:** 07-playbook-os\
> **Playbook ID:** PB-012\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Executive Summary

Validate all generated image assets to ensure they meet Wild Story Lab
quality standards before entering AI video production.

------------------------------------------------------------------------

# Purpose

Verify that image assets are complete, visually consistent, technically
compliant, and ready for downstream production.

------------------------------------------------------------------------

# Business Value

-   Prevent low-quality assets from entering production.
-   Protect character and brand consistency.
-   Reduce expensive regeneration during video production.
-   Increase first-pass production success.

------------------------------------------------------------------------

# Prerequisites

-   PB-011 Generate Image Assets completed.

------------------------------------------------------------------------

# Inputs

Required

-   Image Asset Package
-   Character Package
-   Story Package
-   Prompt Package

Optional

-   Brand Guidelines
-   Reference Images

------------------------------------------------------------------------

# Outputs

-   Approved Image Asset Package
-   Image Validation Report
-   Regeneration Request (if required)

------------------------------------------------------------------------

# Workflow

1.  Load Image Asset Package.
2.  Verify asset completeness.
3.  Validate character consistency.
4.  Validate environments and props.
5.  Review technical quality.
6.  Record issues.
7.  Approve or reject assets.
8.  Archive validation results.

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Character appearance is consistent.
-   [ ] Facial features match approved package.
-   [ ] Clothing and accessories are correct.
-   [ ] Environment matches story.
-   [ ] Style is consistent across all images.
-   [ ] Resolution meets project standard.
-   [ ] File naming follows convention.
-   [ ] Required assets are complete.

------------------------------------------------------------------------

# Decision Rules

  Validation Result   Action
  ------------------- ----------------------------
  All checks passed   Approve Image Assets
  Minor issues        Regenerate affected assets
  Critical issues     Reject Image Asset Package

------------------------------------------------------------------------

# Success Criteria

-   Image package is production-ready.
-   Character identity remains unchanged.
-   All required scenes are supported.
-   No critical quality defects remain.

------------------------------------------------------------------------

# Deliverables

-   Approved Image Asset Package
-   Image Validation Report
-   Asset Issue Log

------------------------------------------------------------------------

# Best Practices

-   Compare against approved Character Package.
-   Review assets scene-by-scene.
-   Validate before video generation.
-   Archive approved versions.

------------------------------------------------------------------------

# Common Mistakes

-   Inconsistent character design.
-   Missing props.
-   Mixed artistic styles.
-   Incorrect aspect ratio or resolution.

------------------------------------------------------------------------

# Related Playbooks

Previous: - PB-011 Generate Image Assets

Next: - PB-013 Generate Video Assets

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**


## Decision Points

## Validation Checklist
- [ ] Inputs verified
- [ ] Outputs validated
- [ ] Quality gate passed

## Related Capability

## Related Skill

## Automation Hooks
- Trigger:
- Inputs:
- Outputs:
