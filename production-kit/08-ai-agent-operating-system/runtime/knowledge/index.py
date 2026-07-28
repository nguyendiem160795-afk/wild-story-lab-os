"""
Wild Story Lab OS
Module 08 - Knowledge Runtime
Knowledge Index
"""

from __future__ import annotations

from collections import defaultdict


class KnowledgeIndex:
    """Maintains an inverted index for knowledge lookup."""

    def __init__(self) -> None:
        self._index: dict[str, set[str]] = defaultdict(set)

    def add(self, document_id: str, terms: list[str]) -> None:
        for term in terms:
            self._index[term.lower()].add(document_id)

    def search(self, term: str) -> list[str]:
        return sorted(self._index.get(term.lower(), set()))

    def remove(self, document_id: str) -> None:
        for term in list(self._index.keys()):
            self._index[term].discard(document_id)
            if not self._index[term]:
                del self._index[term]

    def clear(self) -> None:
        self._index.clear()
