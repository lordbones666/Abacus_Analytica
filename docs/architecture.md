# Forecasting Engine V1.1 Architecture

Pipeline: `question_gate -> SR ingest+snapshot -> SEO extraction -> dedupe cluster -> route -> log-odds update -> optional regime/MC ablations -> ledgers -> scoring/calibration -> monitoring/freeze`.

Layer split:
- `policies/*`: pure, side-effect-free algorithm modules (deterministic math/decision logic).
- `pipeline.py`: orchestration and data-flow wiring.
- `ledger.py`: append-only persistence and replay.

Core stores:
- Evidence ledger (SEO + provenance + correction links)
- Forecast ledger (pre/post log-odds + config versions + reversal metadata + artifacts)
- Score ledger (outcomes, Brier, calibration params)

Replay uses timestamped ledger rows plus source snapshots (`content_hash`, `excerpt`, optional `archive_pointer`) to produce audit-ready reconstruction.

Governance:
- Config change control requires version bump + rationale + expected impact + replay diff.
- Drift monitoring can trigger freeze protocol and aggressiveness reduction.
