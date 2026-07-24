# PB-025 --- Generate Metadata Package

> **Module:** 07-playbook-os\
> **Playbook ID:** PB-025\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Executive Summary

Generate a complete Metadata Package for publishing across supported
platforms. The package includes SEO metadata, discovery metadata,
platform-specific fields, and release information.

------------------------------------------------------------------------

# Purpose

Create standardized metadata that improves discoverability, consistency,
and publishing efficiency.

------------------------------------------------------------------------

# Business Value

-   Improve search visibility.
-   Standardize publishing metadata.
-   Support multi-platform distribution.
-   Reduce manual publishing work.

------------------------------------------------------------------------

# Prerequisites

-   PB-020 Validate Media Package approved.
-   PB-024 Validate Thumbnail Package approved.

------------------------------------------------------------------------

# Inputs

## Required

-   Approved Media Package
-   Approved Thumbnail Package
-   Content Blueprint
-   Story Package
-   Brand Guidelines

## Optional

-   SEO Keyword Research
-   Platform Publishing Rules
-   Localization Guidelines

------------------------------------------------------------------------

# Outputs

-   Metadata Package
-   Title Set
-   Description Set
-   Keyword Set
-   Hashtag Set
-   Publishing Metadata Report

------------------------------------------------------------------------

# Workflow

1.  Load approved production assets.
2.  Generate platform titles.
3.  Generate descriptions.
4.  Generate keywords and hashtags.
5.  Assign category, language, playlist, and audience settings.
6.  Link thumbnail and media references.
7.  Export Metadata Package.
8.  Archive generation report.

------------------------------------------------------------------------

# Metadata Package Structure

``` text
Metadata Package
├── Titles
├── Descriptions
├── Keywords
├── Hashtags
├── Platform Metadata
├── Publishing Settings
└── Generation Report
```

------------------------------------------------------------------------

# Decision Rules

  Condition                      Action
  ------------------------------ -------------------------
  Missing required metadata      Generate missing fields
  SEO conflict detected          Optimize metadata
  Platform requirement differs   Create platform variant
  Complete package               Export Metadata Package

------------------------------------------------------------------------

# Validation Checklist

-   [ ] Titles generated
-   [ ] Descriptions generated
-   [ ] Keywords included
-   [ ] Hashtags included
-   [ ] Platform settings completed
-   [ ] Thumbnail mapping verified
-   [ ] Naming conventions followed

------------------------------------------------------------------------

# Success Criteria

-   Metadata Package is complete.
-   SEO fields are populated.
-   Platform-specific requirements satisfied.
-   Ready for validation.

------------------------------------------------------------------------

# Deliverables

-   Metadata Package
-   SEO Metadata
-   Publishing Metadata Report

------------------------------------------------------------------------

# Best Practices

-   Keep titles concise and compelling.
-   Write natural descriptions.
-   Use relevant keywords only.
-   Maintain consistent branding.

------------------------------------------------------------------------

# Common Mistakes

-   Keyword stuffing.
-   Duplicate titles.
-   Missing publishing fields.
-   Incorrect platform mapping.

------------------------------------------------------------------------

# Related Playbooks

**Previous**

-   PB-024 Validate Thumbnail Package

**Next**

-   PB-026 Validate Metadata Package

------------------------------------------------------------------------

# Version History

  Version   Description
  --------- -----------------
  1.0.0     Initial Release

**End of Playbook**
