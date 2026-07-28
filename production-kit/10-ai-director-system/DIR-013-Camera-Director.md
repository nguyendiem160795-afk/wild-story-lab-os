# DIR-013 Camera Director

## Metadata

ID: DIR-013
Module: 10 AI Director System
Category: Cinematic Directing
Version: 1.0.0
Status: Active

## Purpose

Camera Director chịu trách nhiệm lựa chọn và điều phối ngôn ngữ máy quay (Camera Language) cho từng cảnh nhằm tối đa hóa hiệu quả kể chuyện bằng hình ảnh.

## Responsibilities

- Chọn Camera Shot
- Chọn Camera Movement
- Điều chỉnh Camera Height
- Quyết định Camera Angle
- Đồng bộ Camera với Emotion
- Đồng bộ Camera với Story Beat

## Inputs

- Scene Blueprint
- Story Beat
- Emotional Target
- Character Blocking

## Camera Decision Pipeline

Scene Analysis
→ Emotion Analysis
→ Camera Strategy
→ Shot Selection
→ Movement Selection
→ Validation
→ Camera Plan

## Camera Strategies

### Dialogue
- Medium Shot
- Over Shoulder
- Close-up

### Action
- Tracking Shot
- Crane Shot
- Orbit Shot

### Emotion
- Close-up
- Slow Push-in
- Static Frame

### Reveal
- Dolly In
- Wide Shot
- Bird's Eye View

## Outputs

- Camera Plan
- Shot List
- Camera Metadata
- Camera Prompt Block

## Validation Rules

- Camera phải hỗ trợ Story Goal.
- Không đổi góc máy vô lý.
- Chuyển động camera phải có chủ đích.
- Một cảnh có một chiến lược camera chính.

## Dependencies

- DIR-008 Scene Planner
- DIR-009 Story Beat Planner
- PCL-010 Shot Library
- PCL-012 Camera Movement Library

Status: Approved
