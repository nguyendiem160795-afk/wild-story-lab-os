"""
Wild Story Lab OS
Module 08 - Testing
test_prompt_runtime.py
"""

from __future__ import annotations

import unittest

from runtime.prompts.renderer import PromptRenderer


class TestPromptRuntime(unittest.TestCase):

    def test_render(self):
        renderer = PromptRenderer()
        result = renderer.render(
            "Hello {{name}}!",
            {"name": "Wild Story Lab"},
        )

        self.assertEqual(result, "Hello Wild Story Lab!")


if __name__ == "__main__":
    unittest.main()
