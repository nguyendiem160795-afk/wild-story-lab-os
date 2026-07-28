"""
Wild Story Lab OS
Module 08 - Telemetry
Collector
"""

from __future__ import annotations

from .metric import Metric


class MetricCollector:
    """Collects runtime metrics."""

    def __init__(self) -> None:
        self._metrics: list[Metric] = []

    def record(self, metric: Metric) -> None:
        self._metrics.append(metric)

    def all(self) -> list[Metric]:
        return list(self._metrics)

    def latest(self) -> Metric | None:
        return self._metrics[-1] if self._metrics else None

    def clear(self) -> None:
        self._metrics.clear()
