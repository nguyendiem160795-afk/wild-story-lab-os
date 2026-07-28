"""
Wild Story Lab OS
Module 08 - Event Bus
Event Bus
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

from .event import Event


class EventBus:
    """Central event bus for publishing and subscribing runtime events."""

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Event], None]]] = defaultdict(list)

    def subscribe(self, event_type: str, callback: Callable[[Event], None]) -> None:
        self._subscribers[event_type].append(callback)

    def publish(self, event: Event) -> None:
        for callback in self._subscribers.get(event.event_type, []):
            callback(event)

    def clear(self) -> None:
        self._subscribers.clear()
