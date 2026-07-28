"""
Wild Story Lab OS
Module 08 - Testing
test_runtime.py
"""

from __future__ import annotations

import unittest

from runtime.registry.agent_registry import AgentRegistry


class TestAgentRegistry(unittest.TestCase):

    def test_register_and_resolve(self):
        registry = AgentRegistry()
        agent = object()

        registry.register("agent.demo", agent)

        self.assertTrue(registry.exists("agent.demo"))
        self.assertIs(registry.resolve("agent.demo"), agent)


if __name__ == "__main__":
    unittest.main()
