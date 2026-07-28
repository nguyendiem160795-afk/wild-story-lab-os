# MANIFEST_SPEC.md

# AI Director Manifest Specification

Version: 1.0.0
Status: Stable

## Purpose

MANIFEST_SPEC định nghĩa cấu trúc chuẩn của các tệp manifest được sử dụng trong Module 10 AI Director System để quản lý Production Package, Release Package và Metadata.

---

# Manifest Hierarchy

Root Manifest
├── module.json
├── manifest.json
├── release.json
├── build-info.json
└── qa-manifest.json

---

# module.json

Purpose:
Mô tả thông tin cơ bản của Module.

Fields

- module_id
- module_name
- version
- status
- owner
- dependencies
- document_count

---

# manifest.json

Purpose:
Liệt kê toàn bộ nội dung của Production Package.

Fields

- package_id
- version
- build
- prompts
- scenes
- shots
- assets
- qa_reports

---

# release.json

Purpose:
Thông tin của bản phát hành.

Fields

- release_id
- version
- release_type
- release_date
- compatibility
- notes

---

# build-info.json

Purpose:
Theo dõi thông tin build.

Fields

- build_number
- build_time
- git_commit
- builder
- target_platforms

---

# qa-manifest.json

Purpose:
Tổng hợp kết quả QA.

Fields

- story_score
- visual_score
- prompt_score
- continuity_score
- release_score
- approval_status

---

# Validation Rules

- Tất cả manifest phải có version.
- Không được thiếu package_id.
- QA phải PASS trước khi Release.
- Metadata phải nhất quán giữa các manifest.

---

# Outputs

- Production Manifest
- Release Manifest
- Build Metadata
- QA Manifest

Status: Approved
