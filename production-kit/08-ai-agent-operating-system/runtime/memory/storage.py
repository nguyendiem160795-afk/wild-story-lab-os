"""
Wild Story Lab OS
Module 08 - Memory Runtime
Storage Backend
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .persistent_memory import PersistentMemory


class MemoryStorage:
    """High-level storage backend for runtime memory."""

    def __init__(self, root: str | Path):
        self.root = Path(root)

    def open(self, name: str) -> PersistentMemory:
        return PersistentMemory(self.root / name)

    def save(self, name: str, data: dict[str, Any]) -> None:
        self.open(name).save(data)

    def load(self, name: str) -> dict[str, Any]:
        return self.open(name).load()

    def exists(self, name: str) -> bool:
        return self.open(name).exists()
