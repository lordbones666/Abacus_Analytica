from __future__ import annotations

from forecasting_engine.ledger import JsonlLedger
from forecasting_engine.simulation.contracts import SimulationOutput


class SimulationLedger(JsonlLedger):
    def append_simulation(self, output: SimulationOutput) -> None:
        payload = {
            "simulator": output.simulator,
            "scenario_id": output.context.scenario_id,
            "as_of": output.context.as_of,
            "horizon_steps": output.context.horizon_steps,
            "seed": output.context.seed,
            "config_version": output.context.config_version,
            "state": output.state,
            "metrics": output.metrics,
            "assumptions": output.assumptions,
            "artifacts": output.artifacts,
        }
        self.append(payload)
