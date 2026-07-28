"""
Wild Story Lab OS
Module 08 - Testing
test_telemetry.py
"""

from __future__ import annotations

import unittest

from runtime.telemetry.collector import MetricCollector
from runtime.telemetry.metric import Metric


class TestTelemetry(unittest.TestCase):

    def test_metric_collection(self):
        collector = MetricCollector()
        collector.record(Metric(name="latency", value=12.5, unit="ms"))

        self.assertEqual(len(collector.all()), 1)
        self.assertEqual(collector.latest().name, "latency")


if __name__ == "__main__":
    unittest.main()
