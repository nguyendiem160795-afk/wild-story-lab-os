"""
Wild Story Lab OS
Module 08 - Event Bus
Hooks
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable


class HookManager:
    """Registers and executes named runtime hooks."""

    def __init__(self) -> None:
        self._hooks: dict[str, list[Callable[..., Any]]] = defaultdict(list)

    def register(self, name: str, callback: Callable[..., Any]) -> None:
        self._hooks[name].append(callback)

    def run(self, name: str, *args: Any, **kwargs: Any) -> list[Any]:
        results = []
        for callback in self._hooks.get(name, []):
            results.append(callback(*args, **kwargs))
        return results

    def clear(self) -> None:
        self._hooks.clear()
