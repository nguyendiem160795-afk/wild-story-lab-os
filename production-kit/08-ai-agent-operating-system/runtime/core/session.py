"""
Wild Story Lab OS
Module 08 - Runtime Core Session
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import uuid4


class SessionStatus(str, Enum):
    CREATED = "created"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class RuntimeSession:
    """Represents a runtime execution session."""

    workflow_id: str
    session_id: str = field(default_factory=lambda: str(uuid4()))
    status: SessionStatus = SessionStatus.CREATED
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def start(self) -> None:
        self.status = SessionStatus.RUNNING
        self.updated_at = datetime.utcnow()

    def pause(self) -> None:
        self.status = SessionStatus.PAUSED
        self.updated_at = datetime.utcnow()

    def complete(self) -> None:
        self.status = SessionStatus.COMPLETED
        self.updated_at = datetime.utcnow()

    def fail(self) -> None:
        self.status = SessionStatus.FAILED
        self.updated_at = datetime.utcnow()
