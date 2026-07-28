"""
Wild Story Lab OS
Module 08 - Registry Engine
Knowledge Registry
"""

from __future__ import annotations

from typing import Any


class KnowledgeRegistry:
    """Registry responsible for runtime knowledge assets."""

    def __init__(self) -> None:
        self._knowledge: dict[str, Any] = {}

    def register(self, knowledge_id: str, knowledge: Any) -> None:
        if knowledge_id in self._knowledge:
            raise ValueError(f"Knowledge '{knowledge_id}' is already registered.")
        self._knowledge[knowledge_id] = knowledge

    def unregister(self, knowledge_id: str) -> None:
        self._knowledge.pop(knowledge_id, None)

    def resolve(self, knowledge_id: str) -> Any:
        return self._knowledge.get(knowledge_id)

    def exists(self, knowledge_id: str) -> bool:
        return knowledge_id in self._knowledge

    def all(self) -> dict[str, Any]:
        return dict(self._knowledge)

    def clear(self) -> None:
        self._knowledge.clear()
