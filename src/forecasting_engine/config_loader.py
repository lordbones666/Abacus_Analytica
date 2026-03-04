from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return cast(dict[str, Any], json.load(f))


def load_config(config_dir: Path) -> dict[str, dict[str, Any]]:
    files = {
        "allowed_sources": "allowed_sources.json",
        "category_maps": "category_maps.json",
        "magnitude_tables": "magnitude_tables.json",
        "routing_maps": "routing_maps.json",
        "weights": "weight_tables.v1.json",
        "regime": "regime_params.v1.json",
        "change_control": "change_control.json",
        "base_rates": "base_rates.v1.json",
    }
    return {k: load_json(config_dir / v) for k, v in files.items()}


def validate_change_control(change: dict[str, Any]) -> None:
    required = [
        "component",
        "old_version",
        "new_version",
        "rationale",
        "expected_impact",
        "replay_diff",
    ]
    missing = [item for item in required if not change.get(item)]
    if missing:
        raise ValueError(f"Missing change control fields: {', '.join(missing)}")
    if change["old_version"] == change["new_version"]:
        raise ValueError("new_version must differ from old_version")
