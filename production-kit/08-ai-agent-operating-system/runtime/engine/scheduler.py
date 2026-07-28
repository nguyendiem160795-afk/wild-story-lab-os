"""
Wild Story Lab OS
Module 08 - Workflow Engine
Workflow Scheduler
"""

from __future__ import annotations

from collections import deque
from typing import Any


class WorkflowScheduler:
    """Schedules workflow execution order."""

    def __init__(self) -> None:
        self._queue: deque[dict[str, Any]] = deque()

    def enqueue(self, step: dict[str, Any]) -> None:
        self._queue.append(step)

    def dequeue(self) -> dict[str, Any] | None:
        if not self._queue:
            return None
        return self._queue.popleft()

    def has_pending(self) -> bool:
        return len(self._queue) > 0

    def size(self) -> int:
        return len(self._queue)

    def clear(self) -> None:
        self._queue.clear()
