"""
Wild Story Lab OS
Module 08 - Knowledge Runtime
Knowledge Repository
"""

from __future__ import annotations

from typing import Any


class KnowledgeRepository:
    """Central repository for runtime knowledge assets."""

    def __init__(self) -> None:
        self._store: dict[str, Any] = {}

    def add(self, key: str, value: Any) -> None:
        self._store[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._store.get(key, default)

    def remove(self, key: str) -> None:
        self._store.pop(key, None)

    def exists(self, key: str) -> bool:
        return key in self._store

    def keys(self) -> list[str]:
        return sorted(self._store.keys())

    def clear(self) -> None:
        self._store.clear()
