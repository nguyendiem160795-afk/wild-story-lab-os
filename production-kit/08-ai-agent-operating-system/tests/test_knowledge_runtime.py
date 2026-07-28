"""
Wild Story Lab OS
Module 08 - Testing
test_knowledge_runtime.py
"""

from __future__ import annotations

import unittest

from runtime.knowledge.repository import KnowledgeRepository


class TestKnowledgeRuntime(unittest.TestCase):

    def test_repository(self):
        repo = KnowledgeRepository()
        repo.add("doc1", {"title": "Demo"})

        self.assertTrue(repo.exists("doc1"))
        self.assertEqual(repo.get("doc1")["title"], "Demo")


if __name__ == "__main__":
    unittest.main()
