# DIR-039 Manifest Generator

## Metadata

ID: DIR-039
Module: 10 AI Director System
Category: Packaging & Release
Version: 1.0.0
Status: Active

## Purpose

Manifest Generator tạo các tệp manifest chuẩn mô tả toàn bộ Production Package để hỗ trợ tự động hóa, kiểm tra tính toàn vẹn và tích hợp với GitHub CI/CD hoặc các AI Pipeline.

## Responsibilities

- Sinh manifest.json
- Sinh release-manifest.yaml
- Sinh asset-manifest.json
- Sinh prompt-manifest.json
- Sinh qa-manifest.json
- Gắn metadata phiên bản

## Inputs

- Production Package
- Prompt Package
- Asset Manifest
- QA Reports
- Release Metadata

## Generation Pipeline

Collect Metadata
→ Validate Resources
→ Build Manifest Objects
→ Cross-reference Assets
→ Export Manifest Files

## Manifest Sections

### Package
- Package ID
- Version
- Build
- Release Type

### Assets
- Characters
- Backgrounds
- Props
- Audio
- FX

### Production
- Scenes
- Shots
- Prompts
- QA

### Integrity
- File Count
- Checksums
- Build Timestamp

## Outputs

- manifest.json
- release-manifest.yaml
- asset-manifest.json
- prompt-manifest.json
- qa-manifest.json

## Acceptance Criteria

- Metadata đầy đủ
- Không có tham chiếu lỗi
- Manifest hợp lệ
- Sẵn sàng cho Deployment

## Dependencies

- DIR-038 Package Builder
- DIR-037 Release Manager

Status: Approved
