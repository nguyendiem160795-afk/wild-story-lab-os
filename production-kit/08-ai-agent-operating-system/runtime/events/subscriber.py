"""
Wild Story Lab OS
Module 08 - Event Bus
Subscriber
"""

from __future__ import annotations

from typing import Callable

from .event import Event


class Subscriber:
    """Registers callbacks for runtime events."""

    def __init__(self, event_type: str, callback: Callable[[Event], None]):
        self.event_type = event_type
        self.callback = callback

    def notify(self, event: Event) -> None:
        if event.event_type == self.event_type:
            self.callback(event)
