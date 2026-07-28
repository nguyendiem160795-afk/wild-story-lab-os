"""
Wild Story Lab OS
Module 08 - Testing
test_event_bus.py
"""

from __future__ import annotations

import unittest

from runtime.events.event import Event
from runtime.events.event_bus import EventBus


class TestEventBus(unittest.TestCase):

    def test_publish(self):
        bus = EventBus()
        received = []

        bus.subscribe("demo", lambda e: received.append(e.event_type))
        bus.publish(Event(event_type="demo"))

        self.assertEqual(received, ["demo"])


if __name__ == "__main__":
    unittest.main()
