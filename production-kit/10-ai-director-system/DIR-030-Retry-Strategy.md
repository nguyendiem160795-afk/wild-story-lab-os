# DIR-030 Retry Strategy

## Metadata

ID: DIR-030
Module: 10 AI Director System
Category: Prompt Orchestrator
Version: 1.0.0
Status: Active

## Purpose

Retry Strategy định nghĩa cơ chế AI Director tự động sửa lỗi, tối ưu và tạo lại Prompt khi chất lượng chưa đạt ngưỡng yêu cầu.

## Objectives

- Tự động phát hiện lỗi
- Xác định nguyên nhân
- Chọn chiến lược sửa lỗi
- Sinh Prompt mới
- Đánh giá lại chất lượng
- Lặp cho đến khi đạt ngưỡng hoặc hết số lần thử

## Retry Triggers

- Quality Score < 85
- Character inconsistency
- Story inconsistency
- Platform validation failed
- Missing prompt blocks
- Technical validation failed

## Retry Workflow

Quality Report
→ Error Classification
→ Root Cause Analysis
→ Retry Strategy Selection
→ Prompt Regeneration
→ Validation
→ Quality Scoring

## Retry Strategies

### Level 1
- Remove redundancy
- Improve clarity
- Fix formatting

### Level 2
- Rebuild prompt blocks
- Adjust cinematic language
- Reorder prompt structure

### Level 3
- Recompose prompt from Director outputs
- Re-run Platform Adapter
- Full validation

## Retry Limits

- Maximum retries: 3
- Escalate to manual review after final failure

## Outputs

- Retry Report
- Updated Prompt
- Retry History
- Final Decision

## Dependencies

- DIR-026 Prompt Validator
- DIR-027 Prompt Optimizer
- DIR-028 Platform Adapter
- DIR-029 Quality Scoring

Status: Approved
