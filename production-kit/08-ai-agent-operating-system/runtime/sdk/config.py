"""
Wild Story Lab OS
Module 08 - SDK & CLI
Configuration
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Config:
    """Loads and stores SDK configuration."""

    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.data: dict[str, Any] = {}

    def load(self) -> dict[str, Any]:
        if self.path.exists():
            self.data = json.loads(self.path.read_text(encoding="utf-8"))
        return self.data

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
