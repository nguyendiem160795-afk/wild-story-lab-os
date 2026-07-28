"""
Wild Story Lab OS
Module 08 - Testing
test_registry.py
"""

from __future__ import annotations

import unittest

from runtime.registry.registry_manager import RegistryManager


class TestRegistryManager(unittest.TestCase):

    def test_registry_summary(self):
        manager = RegistryManager()
        summary = manager.summary()

        self.assertEqual(summary["agents"], 0)
        self.assertEqual(summary["workflows"], 0)
        self.assertEqual(summary["prompts"], 0)
        self.assertEqual(summary["knowledge"], 0)
        self.assertEqual(summary["memory"], 0)


if __name__ == "__main__":
    unittest.main()
