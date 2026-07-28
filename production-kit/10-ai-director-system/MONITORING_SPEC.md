# MONITORING_SPEC.md

# AI Director Monitoring Specification

Version: 2.0 Vision
Status: Draft

## Purpose

Định nghĩa hệ thống giám sát (Monitoring) của AI Director System nhằm theo dõi trạng thái hoạt động, hiệu năng, chất lượng và mức độ ổn định của toàn bộ pipeline sản xuất.

---

# Monitoring Architecture

AI Director
↓
Monitoring Manager
├── Health Monitor
├── Performance Monitor
├── Workflow Monitor
├── Resource Monitor
├── QA Monitor
└── Alert Manager

---

# Monitoring Scope

## System Health

Theo dõi:

- System Status
- Service Availability
- Error Rate
- Uptime

---

## Workflow Monitoring

Theo dõi:

- Active Workflow
- Completed Workflow
- Failed Workflow
- Retry Count
- Average Completion Time

---

## Task Monitoring

Theo dõi:

- Pending Tasks
- Running Tasks
- Completed Tasks
- Failed Tasks
- Queue Length

---

## Resource Monitoring

Theo dõi:

- CPU Usage
- GPU Usage
- Memory Usage
- Storage Usage
- Network Latency

---

## QA Monitoring

Theo dõi:

- Story QA Score
- Visual QA Score
- Prompt QA Score
- Continuity QA Score
- Release QA Score

---

# Alert Levels

INFO
- Chỉ ghi log

WARNING
- Cần theo dõi

ERROR
- Cần xử lý

CRITICAL
- Dừng Pipeline và thông báo AI Director

---

# Monitoring Interval

- Health Check: 30 giây
- Workflow Check: 10 giây
- Resource Check: 15 giây
- QA Summary: Sau mỗi Project

---

# Dashboard Metrics

- Success Rate
- Failure Rate
- Throughput
- Average Runtime
- Active Agents
- Queue Size
- System Health Score

---

# Outputs

- Monitoring Report
- Health Dashboard
- Alert Log
- Performance Summary

Status: Draft
