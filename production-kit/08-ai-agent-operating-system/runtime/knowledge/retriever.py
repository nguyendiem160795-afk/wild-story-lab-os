"""
Wild Story Lab OS
Module 08 - Knowledge Runtime
Knowledge Retriever
"""

from __future__ import annotations

from typing import Any

from .index import KnowledgeIndex
from .repository import KnowledgeRepository


class KnowledgeRetriever:
    """Retrieves knowledge assets using the index and repository."""

    def __init__(
        self,
        repository: KnowledgeRepository,
        index: KnowledgeIndex,
    ) -> None:
        self.repository = repository
        self.index = index

    def retrieve(self, term: str) -> list[Any]:
        document_ids = self.index.search(term)
        results = []
        for document_id in document_ids:
            item = self.repository.get(document_id)
            if item is not None:
                results.append(item)
        return results

    def retrieve_one(self, term: str) -> Any | None:
        results = self.retrieve(term)
        return results[0] if results else None
