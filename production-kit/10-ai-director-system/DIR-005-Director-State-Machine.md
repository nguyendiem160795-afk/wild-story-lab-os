# DIR-005 Director State Machine

## Metadata

ID: DIR-005
Module: 10 AI Director System
Category: Director Core
Version: 1.0.0
Status: Active

## Purpose

Định nghĩa vòng đời hoạt động của AI Director và các trạng thái xử lý từ lúc nhận yêu cầu đến khi xuất gói Prompt.

## States

1. Idle
2. Receive Story
3. Analyze Story
4. Plan Scenes
5. Direct Production
6. Assemble Prompts
7. Validate Quality
8. Export Package
9. Complete
10. Error Recovery

## State Transitions

Idle
→ Receive Story
→ Analyze Story
→ Plan Scenes
→ Direct Production
→ Assemble Prompts
→ Validate Quality
→ Export Package
→ Complete

Nếu Validation thất bại:
Validate Quality → Error Recovery → Validate Quality

## Entry Conditions

- Story hợp lệ
- Character Bible sẵn sàng
- Production Components khả dụng

## Exit Conditions

- Prompt Package hoàn chỉnh
- QA đạt yêu cầu
- Báo cáo sản xuất được tạo

## Dependencies

- DIR-002 Director Workflow
- DIR-003 Director Decision Engine
- DIR-004 Director Rules

Status: Approved
