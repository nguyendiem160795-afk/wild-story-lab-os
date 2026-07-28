"""
Wild Story Lab OS
Module 08 - Testing
test_workflow.py
"""

from __future__ import annotations

import unittest

from runtime.engine.execution_plan import ExecutionPlan, ExecutionStep


class TestWorkflow(unittest.TestCase):

    def test_execution_plan(self):
        plan = ExecutionPlan(workflow_id="wf.demo")
        plan.add_step(ExecutionStep(step_id="step1", agent="agent.demo"))

        self.assertEqual(plan.total_steps(), 1)
        self.assertEqual(plan.ordered_steps()[0].step_id, "step1")


if __name__ == "__main__":
    unittest.main()
