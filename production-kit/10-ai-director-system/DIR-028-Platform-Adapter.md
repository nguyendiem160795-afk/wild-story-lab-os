# DIR-028 Platform Adapter

## Metadata

ID: DIR-028
Module: 10 AI Director System
Category: Prompt Orchestrator
Version: 1.0.0
Status: Active

## Purpose

Platform Adapter chuyển đổi Prompt chuẩn của AI Director thành định dạng tối ưu cho từng nền tảng AI Video mà vẫn giữ nguyên ý đồ đạo diễn.

## Responsibilities

- Chuyển đổi Prompt theo nền tảng
- Áp dụng quy tắc riêng của từng Platform
- Kiểm tra giới hạn Prompt
- Chuẩn hóa định dạng đầu ra
- Gắn Platform Metadata

## Supported Platforms

### Google Flow
- Scene-first Prompt
- Character Consistency
- Camera-first Syntax

### Veo
- Cinematic Prompt
- Motion-rich Description
- Natural Language Optimization

### Runway
- Camera-centric Prompt
- Style-aware Formatting

### Sora
- Long-form Narrative Prompt
- Physical Consistency
- Temporal Continuity

### Luma
- Dynamic Motion Prompt
- Environment-aware Prompt

## Adaptation Pipeline

Optimized Prompt
→ Detect Target Platform
→ Apply Platform Rules
→ Convert Syntax
→ Validate Output
→ Export Platform Prompt

## Outputs

- Google Flow Prompt
- Veo Prompt
- Runway Prompt
- Sora Prompt
- Luma Prompt

## Validation Rules

- Không thay đổi Story Goal.
- Không thay đổi Character DNA.
- Tuân thủ giới hạn của từng nền tảng.
- Giữ nguyên ngôn ngữ điện ảnh.
- Prompt sẵn sàng để sử dụng trực tiếp.

## Dependencies

- DIR-027 Prompt Optimizer
- Module 09 Prompt Components
- Platform Profiles

Status: Approved
