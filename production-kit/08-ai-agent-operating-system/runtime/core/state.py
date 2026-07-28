"""
Wild Story Lab OS
Module 08 - Runtime State
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from typing import Any


class RuntimeStatus(str, Enum):
    IDLE = "idle"
    INITIALIZING = "initializing"
    READY = "ready"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"
    SHUTDOWN = "shutdown"


@dataclass
class RuntimeState:
    """Represents the current state of the runtime."""

    status: RuntimeStatus = RuntimeStatus.IDLE
    started_at: datetime | None = None
    ended_at: datetime | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def start(self) -> None:
        self.status = RuntimeStatus.RUNNING
        self.started_at = datetime.utcnow()

    def stop(self) -> None:
        self.status = RuntimeStatus.COMPLETED
        self.ended_at = datetime.utcnow()

    def fail(self, reason: str) -> None:
        self.status = RuntimeStatus.FAILED
        self.metadata["failure_reason"] = reason
        self.ended_at = datetime.utcnow()

    @property
    def is_active(self) -> bool:
        return self.status == RuntimeStatus.RUNNING
