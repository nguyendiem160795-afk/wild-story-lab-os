"""
Wild Story Lab OS
Module 08 - Telemetry
Logger
"""

from __future__ import annotations

from datetime import datetime
from typing import Any


class Logger:
    """Simple runtime logger."""

    def __init__(self) -> None:
        self._entries: list[dict[str, Any]] = []

    def log(self, level: str, message: str) -> None:
        self._entries.append({
            "timestamp": datetime.utcnow().isoformat(),
            "level": level.upper(),
            "message": message,
        })

    def entries(self) -> list[dict[str, Any]]:
        return list(self._entries)

    def clear(self) -> None:
        self._entries.clear()
