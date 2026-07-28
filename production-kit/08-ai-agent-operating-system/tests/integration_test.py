"""
Wild Story Lab OS
Module 08 - Testing
integration_test.py
"""

from __future__ import annotations

import unittest

from runtime.registry.registry_manager import RegistryManager
from runtime.engine.execution_plan import ExecutionPlan, ExecutionStep
from runtime.prompts.renderer import PromptRenderer
from runtime.memory.session_memory import SessionMemory
from runtime.events.event import Event
from runtime.events.event_bus import EventBus


class TestIntegration(unittest.TestCase):

    def test_runtime_integration(self):
        registry = RegistryManager()
        memory = SessionMemory()

        renderer = PromptRenderer()
        rendered = renderer.render(
            "Hello {{user}}",
            {"user": "Wild Story Lab"},
        )
        self.assertEqual(rendered, "Hello Wild Story Lab")

        plan = ExecutionPlan("demo.workflow")
        plan.add_step(
            ExecutionStep(
                step_id="step1",
                agent="agent.demo",
            )
        )
        self.assertEqual(plan.total_steps(), 1)

        memory.set("status", "running")
        self.assertEqual(memory.get("status"), "running")

        bus = EventBus()
        events = []

        bus.subscribe(
            "workflow.started",
            lambda event: events.append(event.event_type),
        )

        bus.publish(Event(event_type="workflow.started"))

        self.assertEqual(events, ["workflow.started"])


if __name__ == "__main__":
    unittest.main()
