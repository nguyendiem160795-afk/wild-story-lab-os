"""
Wild Story Lab OS
Module 08 - Memory Runtime
Session Memory
"""

from __future__ import annotations

from typing import Any


class SessionMemory:
    """Stores temporary runtime data for a single execution session."""

    def __init__(self) -> None:
        self._memory: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._memory[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._memory.get(key, default)

    def delete(self, key: str) -> None:
        self._memory.pop(key, None)

    def snapshot(self) -> dict[str, Any]:
        return dict(self._memory)

    def clear(self) -> None:
        self._memory.clear()
