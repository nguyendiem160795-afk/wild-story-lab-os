# DIR-026 Prompt Validator

## Metadata

ID: DIR-026
Module: 10 AI Director System
Category: Prompt Orchestrator
Version: 1.0.0
Status: Active

## Purpose

Prompt Validator kiểm tra tính đầy đủ, nhất quán và khả năng thực thi của Prompt trước khi gửi sang các nền tảng AI Video.

## Responsibilities

- Kiểm tra cấu trúc Prompt
- Phát hiện Prompt Block bị thiếu
- Phát hiện xung đột giữa các thành phần
- Kiểm tra Character Consistency
- Kiểm tra Story Consistency
- Kiểm tra Platform Compatibility

## Inputs

- Master Prompt
- Scene Prompt
- Prompt Metadata
- Platform Profile

## Validation Pipeline

Load Prompt
→ Structure Validation
→ Dependency Validation
→ Consistency Check
→ Platform Check
→ Quality Score
→ Validation Report

## Validation Rules

### Structure
- Đủ tất cả Prompt Blocks
- Thứ tự hợp lệ
- Không trùng lặp

### Story
- Hook nhất quán
- Scene đúng Story Beat
- Ending hợp lý

### Character
- Character DNA đúng
- Emotion đúng
- Acting đúng

### Cinematic
- Camera hợp lệ
- Lens hợp lệ
- Lighting hợp lệ
- FX hợp lệ

## Outputs

- Validation Report
- Error List
- Warning List
- Validation Score
- Ready for Optimization Flag

## Dependencies

- DIR-025 Prompt Composer
- Module 09 Prompt Components
- Platform Adapter

Status: Approved
