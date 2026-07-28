"""
Wild Story Lab OS
Module 08 - Event Bus
Event
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """Represents a runtime event."""

    event_type: str
    payload: dict[str, Any] = field(default_factory=dict)
    event_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "event_type": self.event_type,
            "payload": self.payload,
            "timestamp": self.timestamp.isoformat(),
        }
