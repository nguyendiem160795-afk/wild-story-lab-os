# Source Playbooks Archive

> **Module:** 07 -- Playbook OS\
> **Folder:** `archive/source-playbooks/`\
> **Document:** README.md\
> **Version:** 1.0.0\
> **Status:** Archived

------------------------------------------------------------------------

# Purpose

This directory preserves the original Playbook documents (PB-001 →
PB-100) created before the introduction of the Capability Pack
architecture.

These documents are retained for historical reference, migration
verification, and traceability.

They are **not** the authoritative implementation of Playbook OS.

------------------------------------------------------------------------

# Archive Status

This archive is considered **frozen**.

-   No new Playbooks should be added.
-   Existing Playbooks should not be modified except to correct critical
    historical errors.
-   Development has officially moved to the Capability Library.

------------------------------------------------------------------------

# Migration

Original Architecture

``` text
Playbook
    └── PB-001.md
    └── PB-002.md
    └── ...
```

Current Architecture

``` text
Capability Pack
│
├── CAPABILITY.md
├── SKILLS.md
└── EXAMPLES.md
```

Each Capability Pack now contains multiple Skill Objects instead of one
markdown file per Skill.

------------------------------------------------------------------------

# Repository Policy

The authoritative sources are now:

1.  skill-management/
2.  capability-library/

This archive exists only for:

-   Historical reference
-   Migration auditing
-   Version comparison
-   Recovery if needed

------------------------------------------------------------------------

# Future Work

Migration progress will be documented in:

``` text
archive/
└── migration/
    └── MIGRATION-GUIDE.md
```

------------------------------------------------------------------------

# Related Documents

-   PLAYBOOK-SPECIFICATION.md
-   MASTER-SKILL-INDEX.md
-   CAPABILITY-REGISTRY.md
-   SKILL-REGISTRY.md

------------------------------------------------------------------------

**End of Document**
