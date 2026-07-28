"""
Wild Story Lab OS
Module 08 - Prompt Runtime
Prompt Cache
"""

from __future__ import annotations

from collections import OrderedDict


class PromptCache:
    """Simple in-memory LRU cache for rendered prompts."""

    def __init__(self, capacity: int = 100) -> None:
        self.capacity = capacity
        self._cache: OrderedDict[str, str] = OrderedDict()

    def get(self, key: str) -> str | None:
        if key not in self._cache:
            return None
        self._cache.move_to_end(key)
        return self._cache[key]

    def set(self, key: str, value: str) -> None:
        self._cache[key] = value
        self._cache.move_to_end(key)
        if len(self._cache) > self.capacity:
            self._cache.popitem(last=False)

    def clear(self) -> None:
        self._cache.clear()

    def size(self) -> int:
        return len(self._cache)
