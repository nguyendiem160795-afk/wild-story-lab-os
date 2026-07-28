# DIR-034 Continuity QA

## Metadata

ID: DIR-034
Module: 10 AI Director System
Category: Quality Intelligence
Version: 1.0.0
Status: Active

## Purpose

Continuity QA đảm bảo tính liên tục giữa các Scene, Shot và Sequence để tránh lỗi về nhân vật, bối cảnh, đạo cụ, ánh sáng, thời gian và chuyển động.

## Responsibilities

- Kiểm tra Character Continuity
- Kiểm tra Costume & Props
- Kiểm tra Camera Continuity
- Kiểm tra Lighting Continuity
- Kiểm tra Timeline
- Kiểm tra Spatial Continuity

## Inputs

- Scene Blueprint
- Shot List
- Character Map
- Camera Plan
- Lighting Plan
- Timeline

## QA Workflow

Load Sequence
→ Compare Adjacent Scenes
→ Detect Continuity Issues
→ Classify Issues
→ Generate QA Report

## Validation Categories

### Character
- Appearance
- Outfit
- Scale
- Position

### Environment
- Background
- Weather
- Time of Day
- Props

### Cinematic
- Camera Direction
- Screen Direction
- Lighting
- Motion

### Timeline
- Action Order
- Scene Order
- Time Consistency

## Outputs

- Continuity QA Report
- Issue List
- Severity Classification
- Continuity Score

## Acceptance Criteria

- No Critical Continuity Errors
- Character Continuity PASS
- Timeline PASS
- Visual Continuity PASS
- Ready for Production

## Dependencies

- DIR-031 Visual QA
- DIR-032 Story QA
- DIR-033 Prompt QA

Status: Approved
