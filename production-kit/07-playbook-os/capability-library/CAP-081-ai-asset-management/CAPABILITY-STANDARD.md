# CAPABILITY-STANDARD

> **Module:** 07 -- Playbook OS\
> **Document:** CAPABILITY-STANDARD.md\
> **Version:** 1.0.0\
> **Status:** Stable

------------------------------------------------------------------------

# Purpose

This document defines the mandatory standard for every Capability Pack
in Playbook OS.

All Capability Packs MUST comply with this specification.

------------------------------------------------------------------------

# Standard Folder Structure

``` text
CAP-XXX-capability-name/
│
├── README.md
├── CAPABILITY.md
├── SKILLS.md
├── EXAMPLES.md
├── CHANGELOG.md      (optional)
└── RELEASE.md        (optional)
```

------------------------------------------------------------------------

# Required Documents

  Document        Required   Purpose
  --------------- ---------- -----------------------------------
  README.md       Yes        Entry point and overview
  CAPABILITY.md   Yes        Business capability specification
  SKILLS.md       Yes        Executable Skill catalog
  EXAMPLES.md     Yes        Reference execution examples
  CHANGELOG.md    Optional   Version history
  RELEASE.md      Optional   Release information

------------------------------------------------------------------------

# Mandatory Metadata

Every Capability Pack must define:

-   Capability ID
-   Capability Name
-   Business Domain
-   Operational Domain
-   Version
-   Status
-   Owner
-   Last Updated

------------------------------------------------------------------------

# Naming Convention

-   Capability IDs use the format `CAP-XXX`.
-   Folder names use lowercase kebab-case.
-   Skill IDs remain immutable.
-   Document names are fixed by this standard.

------------------------------------------------------------------------

# Skill Requirements

Every Skill must:

1.  Have a unique Skill ID.
2.  Define clear inputs and outputs.
3.  Include validation rules.
4.  Support automation where applicable.
5.  Be traceable to its Capability.

------------------------------------------------------------------------

# Versioning

Semantic Versioning is recommended:

``` text
MAJOR.MINOR.PATCH
```

Example:

-   1.0.0 Initial Release
-   1.1.0 New Skills
-   1.1.1 Documentation Fix

------------------------------------------------------------------------

# Review Checklist

Before release verify:

-   Folder structure is correct.
-   Required documents exist.
-   Metadata is complete.
-   Skills are registered.
-   Examples are valid.
-   Internal links work.

------------------------------------------------------------------------

# Compliance

A Capability Pack is considered compliant only if it satisfies every
requirement in this standard.

------------------------------------------------------------------------

# Related Documents

-   skill-management/CAPABILITY-TEMPLATE.md
-   skill-management/SKILL-TEMPLATE.md
-   skill-management/GOVERNANCE.md

------------------------------------------------------------------------

**End of Document**
