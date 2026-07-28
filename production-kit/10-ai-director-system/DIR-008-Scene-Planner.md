# DIR-008 Scene Planner

## Metadata

ID: DIR-008
Module: 10 AI Director System
Category: Story Directing
Version: 1.0.0
Status: Active

## Purpose

Scene Planner chịu trách nhiệm chuyển Story Blueprint thành danh sách Scene có cấu trúc rõ ràng, phục vụ cho toàn bộ pipeline đạo diễn.

## Responsibilities

- Chia Story thành các Scene
- Xác định mục tiêu từng Scene
- Phân bổ thời lượng
- Xác định Story Beat
- Gán Emotional Target
- Gán Production Priority

## Inputs

- Story Blueprint
- Story Beats
- Emotional Arc
- Target Duration

## Outputs

- Scene List
- Scene Metadata
- Scene Timeline
- Scene Objectives

## Scene Blueprint Schema

### Scene ID
### Scene Goal
### Story Beat
### Characters
### Location
### Duration
### Emotion
### WOW Opportunity
### Transition Type

## Planning Workflow

Story Blueprint
→ Segment Story
→ Define Scene Goals
→ Allocate Duration
→ Validate Story Flow
→ Export Scene Plan

## Validation Rules

- Mỗi Scene chỉ có một mục tiêu chính.
- Scene phải đẩy Story tiến lên.
- Có sự leo thang cảm xúc giữa các Scene.
- Không có Scene dư thừa.
- Tổng thời lượng khớp với thời lượng video mục tiêu.

## Dependencies

- DIR-007 Story Analyzer
- DIR-003 Director Decision Engine
- Module 05 Story Engine

Status: Approved
