"""
Wild Story Lab OS
Module 08 - Testing
test_memory_runtime.py
"""

from __future__ import annotations

import unittest

from runtime.memory.session_memory import SessionMemory


class TestMemoryRuntime(unittest.TestCase):

    def test_session_memory(self):
        memory = SessionMemory()
        memory.set("user", "demo")

        self.assertEqual(memory.get("user"), "demo")
        self.assertEqual(memory.snapshot()["user"], "demo")


if __name__ == "__main__":
    unittest.main()
