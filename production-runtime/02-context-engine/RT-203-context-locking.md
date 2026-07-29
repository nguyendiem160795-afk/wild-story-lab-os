# RT-203 Context Locking

**Module:** 02-context-engine\
**Version:** 1.0.0

## Purpose

Ngăn ghi đè dữ liệu trong quá trình Runtime.

## Lock Levels

-   Global Lock
-   Project Lock
-   Episode Lock
-   Scene Lock

## Rules

-   Chỉ Runtime Core được mở khóa.
-   Scene không được sửa Global Context.
-   Lock được ghi vào Runtime Log.
