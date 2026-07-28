"""
Wild Story Lab OS
Module 08 - Telemetry
Monitor
"""

from __future__ import annotations

from .collector import MetricCollector
from .metric import Metric


class RuntimeMonitor:
    """Monitors runtime metrics against thresholds."""

    def __init__(self, collector: MetricCollector):
        self.collector = collector

    def record(self, name: str, value: float, unit: str = "") -> None:
        self.collector.record(Metric(name=name, value=value, unit=unit))

    def latest(self) -> Metric | None:
        return self.collector.latest()

    def exceeds(self, threshold: float) -> bool:
        metric = self.latest()
        return metric is not None and metric.value > threshold
