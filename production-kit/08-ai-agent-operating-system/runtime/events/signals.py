"""
Wild Story Lab OS
Module 08 - Event Bus
Signals
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Signal:
    """Represents a lightweight runtime signal."""

    name: str
    source: str
    payload: dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)


class SignalRegistry:
    """Stores and dispatches runtime signals."""

    def __init__(self) -> None:
        self._signals: list[Signal] = []

    def emit(self, signal: Signal) -> None:
        self._signals.append(signal)

    def latest(self) -> Signal | None:
        return self._signals[-1] if self._signals else None

    def history(self) -> list[Signal]:
        return list(self._signals)

    def clear(self) -> None:
        self._signals.clear()
