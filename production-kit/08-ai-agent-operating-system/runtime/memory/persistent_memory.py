"""
Wild Story Lab OS
Module 08 - Memory Runtime
Persistent Memory
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class PersistentMemory:
    """Persists runtime memory to disk."""

    def __init__(self, storage_path: str | Path):
        self.storage_path = Path(storage_path)

    def save(self, data: dict[str, Any]) -> None:
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with self.storage_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self) -> dict[str, Any]:
        if not self.storage_path.exists():
            return {}
        with self.storage_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def exists(self) -> bool:
        return self.storage_path.exists()
