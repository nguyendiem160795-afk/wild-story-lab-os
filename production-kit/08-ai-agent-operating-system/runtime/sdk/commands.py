"""
Wild Story Lab OS
Module 08 - SDK & CLI
Commands
"""

from __future__ import annotations

from typing import Callable


class CommandRegistry:
    """Registers and executes CLI commands."""

    def __init__(self) -> None:
        self._commands: dict[str, Callable[[], int]] = {}

    def register(self, name: str, command: Callable[[], int]) -> None:
        self._commands[name] = command

    def execute(self, name: str) -> int:
        if name not in self._commands:
            raise KeyError(f"Unknown command: {name}")
        return self._commands[name]()

    def list(self) -> list[str]:
        return sorted(self._commands.keys())
