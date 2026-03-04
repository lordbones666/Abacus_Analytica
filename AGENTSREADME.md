# AGENTS.md — Forecasting Engine (V1.1) as a Custom GPT

## Mission
Build a probabilistic forecasting engine exposed through a **Custom GPT** that:
- uses **Web Search** to gather sources and evidence,
- uses **Code Execution / Data Analysis** to compute, simulate, score, and calibrate,
- produces **auditable** probability forecasts for well-defined binary questions,
- maintains a full ledger for replay, scoring, and continuous improvement.

## System Shape (Custom GPT)
The Custom GPT has these capabilities enabled:
- **Web Search**: retrieve and cite primary/credible sources and resolve factual disputes.
- **Code Execution & Data Analysis**: transform data, run Bayesian/log-odds updates, Monte Carlo, scoring, calibration, and generate charts/tables.
- **File handling** (optional): ingest user-provided CSV/JSON/exports for backtests and calibration.

## Core Principles
- **Evidence-first:** Every forecast update is traceable to specific sources (URLs) and structured evidence records.
- **Reproducible analytics:** Any computed output must be reproducible by rerunning the code with the same inputs and configuration version.
- **Resolution clarity:** Every question must have an explicit resolver authority + method and resolve to a binary outcome.
- **Calibration discipline:** Forecasts are scored with proper scoring rules and recalibrated using time-split evaluation.

## Core Objects
### 1) Question Object (QO)
Immutable definition of a question:
- question_id, frozen wording, time window, timezone, resolution authority/method, binary criteria, invalidation conditions, version.

### 2) Source Record (SR)
A record for every retrieved source:
- url, publisher, retrieved_at, publish_time (if known), title, extraction_notes, credibility flags, and citations/quotes used.

### 3) Structured Evidence Object (SEO)
A structured evidence event derived from sources:
- event_id (deterministic hash), timestamp, source_name, source_tier, category, direction, magnitude, claim_type, link, resolver_authority, resolver_method.

### 4) Ledgers
- Evidence Ledger: all SEOs + dedupe clusters + provenance to SR.
- Forecast Ledger: all probability snapshots + inputs + config versions.
- Score Ledger: outcomes + scoring + calibration parameters.

## Web Search Workflow Requirements
- Prefer **primary sources** (official releases, original datasets, regulator sites).
- For news, prefer reputable wires/outlets; record **publisher + timestamp**.
- When sources disagree, record both, label disagreement, and define the resolution authority that will settle it.
- Every SEO must link back to at least one Source Record (SR).

## Data Analysis Requirements
- All probability updates occur in **log-odds space** with versioned weight tables.
- Monte Carlo simulations must be:
  - seeded for reproducibility,
  - logged (inputs, parameters, seed, distribution choice),
  - validated against sanity checks.
- Scoring:
  - Brier score at minimum,
  - calibration curves per domain×horizon,
  - temperature scaling (α) trained only on past data (time-split).

## Quality Gates (Minimum)
- **Source coverage gate:** no forecast update without at least one SR (unless purely market-data-driven).
- **Timestamp gate:** every SR must store retrieval time; SEOs must use the underlying event time when available.
- **Dedupe gate:** duplicates across sources must be clustered; avoid double counting.
- **Replay gate:** given a forecast timestamp, replay must reproduce the same probability and evidence set.
- **Evaluation gate:** weekly or monthly scoring runs must complete; alert if calibration worsens materially.

## Testing Requirements
- Unit tests for:
  - QO validation,
  - SEO schema validation,
  - dedupe clustering,
  - update mechanics (caps, saturation),
  - Monte Carlo determinism and bounds.
- Golden replay tests using a fixed fixture set of SR→SEO→forecast updates.
- Regression tests for calibration parameter updates (time-split enforcement).

## Documentation Requirements
- `docs/architecture.md` with pipeline diagrams.
- `docs/replay.md` describing how to reproduce any forecast.
- `docs/data_sources.md` listing allowed sources + tiering rules.
- `docs/evaluation.md` describing scoring + calibration methodology.

## Working Agreements
- Keep modules composable and versioned.
- Log everything needed to reproduce outputs.
- Use Web Search for freshness; use code execution for computation and validation.
