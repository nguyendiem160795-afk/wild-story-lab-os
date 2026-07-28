"""
Wild Story Lab OS
Module 08 - Event Bus
Dispatcher
"""

from __future__ import annotations

from collections import deque

from .event import Event
from .event_bus import EventBus


class EventDispatcher:
    """Dispatches queued events through the EventBus."""

    def __init__(self, bus: EventBus):
        self.bus = bus
        self._queue: deque[Event] = deque()

    def enqueue(self, event: Event) -> None:
        self._queue.append(event)

    def dispatch(self) -> int:
        count = 0
        while self._queue:
            self.bus.publish(self._queue.popleft())
            count += 1
        return count

    def pending(self) -> int:
        return len(self._queue)
