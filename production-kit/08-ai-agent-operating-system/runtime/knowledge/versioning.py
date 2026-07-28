"""
Wild Story Lab OS
Module 08 - Knowledge Runtime
Knowledge Versioning
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class KnowledgeVersion:
    """Represents a version of a knowledge asset."""

    asset_id: str
    version: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    author: str | None = None
    description: str = ""


class VersionManager:
    """Tracks versions of knowledge assets."""

    def __init__(self) -> None:
        self._versions: dict[str, list[KnowledgeVersion]] = {}

    def add(self, version: KnowledgeVersion) -> None:
        self._versions.setdefault(version.asset_id, []).append(version)

    def latest(self, asset_id: str) -> KnowledgeVersion | None:
        versions = self._versions.get(asset_id, [])
        return versions[-1] if versions else None

    def history(self, asset_id: str) -> list[KnowledgeVersion]:
        return list(self._versions.get(asset_id, []))

    def clear(self) -> None:
        self._versions.clear()
