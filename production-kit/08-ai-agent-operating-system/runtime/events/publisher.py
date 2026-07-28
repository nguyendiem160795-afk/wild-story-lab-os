"""
Wild Story Lab OS
Module 08 - Event Bus
Publisher
"""

from __future__ import annotations

from .event import Event
from .event_bus import EventBus


class Publisher:
    """Publishes events to the runtime event bus."""

    def __init__(self, bus: EventBus):
        self.bus = bus

    def publish(self, event_type: str, payload: dict | None = None) -> Event:
        event = Event(
            event_type=event_type,
            payload=payload or {},
        )
        self.bus.publish(event)
        return event
