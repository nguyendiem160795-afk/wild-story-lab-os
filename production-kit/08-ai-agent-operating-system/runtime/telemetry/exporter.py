"""
Wild Story Lab OS
Module 08 - Telemetry
Exporter
"""

from __future__ import annotations

import json
from pathlib import Path

from .collector import MetricCollector


class MetricExporter:
    """Exports collected metrics to JSON."""

    def export_json(self, collector: MetricCollector, output: str | Path) -> Path:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)

        data = [metric.to_dict() for metric in collector.all()]

        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return path
