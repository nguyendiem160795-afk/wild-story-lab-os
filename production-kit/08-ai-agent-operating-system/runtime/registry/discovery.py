"""
Wild Story Lab OS
Module 08 - Registry Engine
Component Discovery
"""

from __future__ import annotations

from pathlib import Path


class ComponentDiscovery:
    """Discovers runtime components from the filesystem."""

    def __init__(self, root: str | Path):
        self.root = Path(root)

    def discover(self, pattern: str = "*.py") -> list[Path]:
        """Return matching component files."""
        return sorted(
            p for p in self.root.rglob(pattern)
            if p.is_file() and not p.name.startswith("__")
        )

    def exists(self) -> bool:
        return self.root.exists()

    def count(self, pattern: str = "*.py") -> int:
        return len(self.discover(pattern))
