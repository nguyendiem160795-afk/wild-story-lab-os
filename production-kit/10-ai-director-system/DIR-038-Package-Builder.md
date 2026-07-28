# DIR-038 Package Builder

## Metadata

ID: DIR-038
Module: 10 AI Director System
Category: Packaging & Release
Version: 1.0.0
Status: Active

## Purpose

Package Builder chịu trách nhiệm tập hợp toàn bộ tài sản (artifacts) do AI Director tạo ra và xây dựng thành Production Package thống nhất, sẵn sàng phát hành hoặc tích hợp vào pipeline tự động.

## Responsibilities

- Thu thập toàn bộ Output
- Xây dựng cấu trúc thư mục chuẩn
- Đóng gói Prompt Package
- Đóng gói QA Reports
- Đóng gói Production Manifest
- Kiểm tra tính đầy đủ trước khi phát hành

## Inputs

- Prompt Package
- Production Plan
- QA Reports
- Asset Manifest
- Release Metadata

## Build Pipeline

Collect Outputs
→ Verify Files
→ Generate Folder Structure
→ Build Package
→ Integrity Check
→ Package Ready

## Standard Package Structure

production-package/
├── prompts/
├── scenes/
├── shots/
├── manifests/
├── qa/
├── assets/
├── release/
└── docs/

## Outputs

- Production Package
- Package Manifest
- Integrity Report
- Package Summary

## Acceptance Criteria

- Không thiếu file bắt buộc
- Cấu trúc thư mục đúng chuẩn
- Manifest khớp với nội dung
- QA Reports đầy đủ
- Package sẵn sàng phát hành

## Dependencies

- DIR-036 Export Manager
- DIR-037 Release Manager

Status: Approved
