# DIR-025 Prompt Composer

## Metadata

ID: DIR-025
Module: 10 AI Director System
Category: Prompt Orchestrator
Version: 1.0.0
Status: Active

## Purpose

Prompt Composer là thành phần trung tâm của AI Director, chịu trách nhiệm tổng hợp mọi quyết định đạo diễn thành Prompt AI Video hoàn chỉnh, nhất quán và tối ưu cho từng nền tảng.

## Responsibilities

- Thu thập dữ liệu từ các Director
- Ghép Prompt Blocks
- Chuẩn hóa Prompt Structure
- Đồng bộ Story, Character và Cinematic Language
- Chuẩn bị Prompt cho Platform Adapter

## Inputs

- Story Blueprint
- Scene Blueprint
- Camera Plan
- Lens Plan
- Lighting Plan
- Composition Plan
- Acting Plan
- FX Plan
- Audio Plan

## Prompt Structure

1. Subject
2. Environment
3. Camera
4. Lens
5. Composition
6. Lighting
7. Motion
8. Acting
9. FX
10. Audio
11. Style
12. Rendering Quality

## Assembly Workflow

Collect Director Outputs
→ Normalize Data
→ Merge Prompt Blocks
→ Resolve Conflicts
→ Validate Structure
→ Generate Master Prompt

## Outputs

- Master Prompt
- Scene Prompt
- Prompt Metadata
- Prompt Package

## Validation Rules

- Không thiếu Prompt Block bắt buộc.
- Không có thông tin mâu thuẫn.
- Đảm bảo Character Consistency.
- Đảm bảo Story Consistency.
- Prompt có thể chuyển sang Platform Adapter.

## Dependencies

- DIR-013 → DIR-024
- Module 09 Production Components
- Prompt Component Library

Status: Approved
