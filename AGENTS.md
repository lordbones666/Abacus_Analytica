# AGENTS.md — AbacusAnalytica Repository Governance

This repository is an architecture-first forecasting engine for reproducible, evidence-driven probabilistic reasoning.

All AI agents, including Codex, must comply with the following rules.

---

# 1. Primary Directive

Do not replace architecture by default.

This repo is not a greenfield toy project.
It already has a coherent design:
- policy layer
- orchestration layer
- ledger/replay layer
- config/schema governance
- extension layer
- evaluation/calibration layer

Your default behavior is:

- preserve
- understand
- tighten
- extend carefully
- document
- test

Only replace a subsystem when explicitly instructed by the human operator.

---

# 2. Repo Identity

This repository is designed around:

- reproducibility
- deterministic policy updates
- append-only ledgers
- replayability
- config-driven logic
- evidence structuring
- calibration and scoring
- extension-friendly forecasting workflows
- compatibility with custom GPT / agent environments

Do not weaken those properties.

---

# 3. Architectural Map (authoritative mental model)

## Core stable zones
- `src/forecasting_engine/policies/*`
- `src/forecasting_engine/pipeline.py`
- `src/forecasting_engine/models.py`
- `src/forecasting_engine/validation.py`
- `src/forecasting_engine/ledger.py`
- `src/forecasting_engine/evaluation.py`

## Extension zone
- `src/forecasting_engine/extensions/*`

## Operational wrappers / adapters
- `pipeline/*`
- `ledger/*`
- `evaluation/*`

## Governance / contract layer
- `config/*`
- `schemas/*`
- `docs/*`
- `repo_manifest.json`
- `file_manifest.json`

Treat these boundaries as intentional.

---

# 4. Core Rule: Upgrade, Don’t Replace

Allowed by default:
- bug fixes
- tighter validation
- stricter typing
- replay hardening
- test additions
- docs improvements
- additive helper modules
- bounded refactors preserving public behavior
- config/schema consistency fixes
- better extension isolation

Disallowed by default:
- architecture rewrites
- replacing the pipeline model
- collapsing policy/orchestration boundaries
- changing contracts without preserving backward compatibility
- removing modules because they “look redundant”
- introducing opaque agentic logic into deterministic policy layers

---

# 5. Determinism and Replay Safety

This repo’s trust depends on deterministic behavior.

Protect:
- ledger append semantics
- replay reproducibility
- update ordering
- content hash usage
- timestamp assumptions
- config version references
- calibration reproducibility

Any change that may alter replayed outputs must be:
- explicitly documented
- tested
- framed as a controlled upgrade

---

# 6. Policy Layer Discipline

Files under `src/forecasting_engine/policies/*` should remain:

- deterministic
- side-effect-free where intended
- mathematically explicit
- contract-driven
- easy to replay and audit

Do not inject:
- ad hoc I/O
- hidden state
- external calls
- LLM behavior
- non-deterministic shortcuts

---

# 7. Orchestration Discipline

`src/forecasting_engine/pipeline.py` is orchestration, not policy math.

Preserve the split between:
- ingestion
- structuring
- dedupe
- routing
- update
- regime/MC
- persistence
- evaluation

Do not push too much logic down into orchestration or too much orchestration into policies.

---

# 8. Extension Layer Discipline

`src/forecasting_engine/extensions/*` is powerful but must remain controlled.

Rules:
- Extensions may add capability, not silently mutate baseline semantics.
- Extension contracts must be typed and documented.
- Core assumptions must not be redefined by extension side effects.
- If an extension depends on a baseline policy behavior, document it.

Add tests when extension behavior meaningfully affects:
- evidence mapping
- regime logic
- pricing/valuation logic
- question compilation
- surprise/misinfo handling
- source memory
- time-series conversion

---

# 9. Config / Schema Governance

This repo is config-heavy and schema-aware.

Protect:
- config loading correctness
- schema alignment
- algorithm config versioning
- change control assumptions
- route/category/base-rate integrity

Do not:
- hardcode values that belong in config
- bypass schema validation for convenience
- add silent fallback behavior unless explicitly documented

---

# 10. Docs Are Part of the Product

`docs/*` and `docs/specs/*` are not decorative.

They are part of the repo’s operating doctrine.

When code changes:
- check for doc drift
- update architecture references if needed
- preserve terminology continuity
- improve navigability for future AI agents

Especially protect:
- `docs/system_overview.md`
- `docs/architecture.md`
- `docs/source_policy.md`
- methodology specs in `docs/specs/*`

---

# 11. Tests Are Contract Surface

Do not treat tests as cleanup targets.

Tests in this repo express:
- determinism expectations
- replay assumptions
- policy invariants
- integration assumptions
- extension safety

When changing behavior:
- add or update tests intentionally
- explain why the contract change is valid
- prefer more explicit tests over fewer tests

High-priority test surfaces:
- replay determinism
- policy metamorphic invariants
- config/schema validation
- extension integration
- pipeline correctness

---

# 12. Custom GPT / Agent Environment Fitness

This repo is intended to work well inside a custom GPT / agent environment with web access.

Optimize for:
- clear entry points
- explicit contracts
- machine-readable manifests
- schema-safe evidence objects
- audit-friendly logs and ledgers
- predictable data flow
- safe navigation for GPT-class tooling

Good upgrades include:
- improving manifests
- documenting extension points
- clarifying source/evidence object expectations
- making boundary contracts easier for agents to inspect

Do not “AI-ify” the core engine in a way that reduces determinism.

---

# 13. Web Access Use Policy

Codex may use web access to:
- verify implementation patterns
- confirm library behavior
- compare forecasting/evaluation best practices
- validate ecosystem assumptions

Codex may not use web access as justification to:
- import alien architecture wholesale
- replace local repo doctrine
- overfit design to external frameworks

External research should inform upgrades, not override repo identity.

---

# 14. Change Framing Requirements

For every meaningful modification, explain:

- what was wrong or weak
- why it mattered
- what changed
- why the change preserves repo architecture
- what tests protect it
- whether it affects replay/determinism/contracts

If you cannot explain that, do not make the change.

---

# 15. Zero Hallucination Policy

If a symbol, contract, assumption, or architectural intent is unclear:

- do not invent
- do not guess
- inspect more files
- infer conservatively
- document uncertainty
- propose instead of silently rewriting

This applies to:
- policy logic
- extension interactions
- config meaning
- source/evidence semantics
- test intent

---

# 16. Preferred Operating Style

Prefer:
- small precise improvements
- explicitness
- additive compatibility
- strong comments on trust-critical logic
- code/docs/tests staying in sync
- repo-specific judgment over generic cleanup culture

Avoid:
- broad rewrites
- cosmetic churn
- renaming cascades
- abstraction inflation
- replacing existing patterns with fashionable ones

---

# 17. End State Objective

This repository should become:

- more coherent
- more durable
- easier to audit
- easier for AI agents/Gpts to navigate safely
- more deterministic
- more replay-safe
- more tightly aligned across code, config, schemas, docs, and tests

without sacrificing the architecture that already gives it strength.

# AGENTS.md ADDENDUM — Decision Lab Build Discipline

This addendum applies specifically to Decision Lab expansion work.

It supplements, not replaces, the existing AGENTS.md rules.

---

# 1. Primary Rule for Decision Lab Work

Build the Decision Lab **in phases**.
Do not overbuild.
Do not front-load dashboards, automation, or speculative abstractions before the trust spine exists.

The trust spine is:

1. contracts
2. ledgers
3. reproducible simulation runs
4. config/schema integrity
5. tests
6. docs

If these are weak, the Decision Lab is fake.

---

# 2. Mandatory Build Order

Codex must follow this order:

## Phase 1 — Mapping and reuse analysis
- map the repo
- identify reusable modules
- identify simulation-capable code
- identify replay-critical surfaces
- identify config/schema dependencies
- identify doc/code drift

No major coding before this is done.

## Phase 2 — Core foundations
Build only:
- simulation contracts
- scenario contracts/compiler
- Bayesian core
- Markov core
- Monte Carlo core
- simulation run manager/orchestrator

Do not build dashboards first.
Do not build broad automation first.

## Phase 3 — Ledgers and provenance
Add:
- scenario ledger
- simulation run ledger
- portfolio ledger (if portfolio exists)
- provenance capture for runs/config/seeds/evidence snapshots

No simulator is “done” unless it is provenance-safe.

## Phase 4 — Tier A domain simulators
Only after phases 1–3 are stable.

Priority:
- macro system
- conflict escalation
- crisis cascade
- financial contagion
- supply chain

Keep them interpretable and bounded.

## Phase 5 — Portfolio and regime surfaces
Build:
- forecast portfolio
- exposure / correlation surfaces
- regime dashboard summaries

Only after simulators and ledgers are working.

## Phase 6 — Automation
Build:
- diff detection
- refresh jobs
- rerun triage

Only after:
- scenarios are formalized
- simulation orchestration exists
- ledgers are stable

---

# 3. Anti-Overbuilding Rule

Do not overbuild any of the following in early passes:

- dashboards
- UI surfaces
- automation workers
- HMM sophistication
- advanced portfolio optimization
- “intelligent” scenario generation
- black-box ML wrappers

Start with:
- explicit contracts
- reproducible runs
- interpretable simulators
- stable ledgers
- testable outputs

Sophistication comes later.

---

# 4. Reuse Before Invention

Before adding any new Decision Lab module, inspect whether the repo already contains usable substrate.

Likely reuse candidates include:
- `policies/market_path.py`
- `extensions/regime_detector.py`
- `extensions/market_macro.py`
- `extensions/dependency_graph.py`
- `extensions/event_network.py`
- `extensions/numeric_thresholds.py`
- `extensions/range_forecaster.py`
- `extensions/backtest_harness.py`
- `evaluation/*`

Do not duplicate existing functionality just to fit the new package layout.
Wrap, bridge, or adapt it.

---

# 5. Domain Simulator Discipline

Domain simulators must remain:

- interpretable
- parameter-explicit
- config-driven
- assumption-documented
- reproducible by seed
- bounded in claims

Do not fake realism.
Do not simulate more than the model can justify.
If a simulator is scaffolded, say so explicitly.

Each domain simulator must define:
- state variables
- transition rules
- shock inputs
- output objects
- assumptions
- known limitations

---

# 6. Scenario Discipline

Scenario generation must not become narrative sludge.

Scenario objects must contain:
- scenario id
- trigger set
- horizon
- linked evidence ids
- state assumptions
- simulator applicability
- explicit confidence / uncertainty metadata

Scenarios must be:
- structured
- replayable
- inspectable
- tied to evidence

No freeform “scenario vibes.”

---

# 7. Simulation Run Discipline

Every simulation run must capture:
- simulator id
- scenario id
- config version
- seed
- timestamp
- evidence snapshot hash
- regime snapshot
- output summary
- failure mode if run fails

If this is missing, the run is not trustworthy.

---

# 8. Portfolio Discipline

Forecast portfolios are not just groups of questions.

They must expose:
- concentration
- scenario overlap
- correlated exposure
- regime sensitivity
- failure clustering

Do not build portfolio UI or optimization layers until the core portfolio object and ledger exist.

---

# 9. Dashboard Discipline

Dashboard work must be summary-first, not frontend-first.

Acceptable early dashboard outputs:
- Python summaries
- structured state objects
- markdown artifacts
- JSON summaries

Do not turn early Decision Lab work into a UI project.

---

# 10. Automation Discipline

Automation must only act on explicit rerun rules.

Add triage categories such as:
- informational
- evidence-only
- scenario-affecting
- rerun-required
- operator-review-required

Do not rerun the whole lab whenever any new evidence appears.

---

# 11. Config / Schema First Rule

Every major Decision Lab object must have:
- config support
- schema support
- validation path

This applies to:
- scenarios
- simulation runs
- portfolios
- automation rules
- dashboard state objects

Do not hide assumptions in code when they belong in config/schema.

---

# 12. Documentation Is Part of the Build

Every major Decision Lab layer must be documented when introduced.

At minimum, update:
- architecture docs
- system overview
- simulation overview
- scenario spec
- orchestration spec

If code is added without corresponding architecture explanation, the build is incomplete.

---

# 13. Test Discipline

Every Decision Lab phase must land with tests.

Minimum required per phase:
- contract/schema tests
- deterministic seed tests
- provenance tests
- integration path tests
- domain simulator sanity tests

Do not postpone tests until “after the architecture is done.”

---

# 14. No Black-Box Drift

Do not inject opaque ML or LLM behavior into:

- Bayesian core
- Markov core
- Monte Carlo core
- simulation run manager
- ledgers
- scoring

LLMs may support evidence structuring and scenario suggestion outside the deterministic core, but they do not replace the core simulation logic.

---

# 15. Stop Conditions

If Codex encounters ambiguity around:
- contract intent
- replay semantics
- ledger expectations
- extension reuse
- config meaning

then stop, document uncertainty, and propose options.

Do not “solve” ambiguity by silent structural rewrites.

---

# 16. End State Objective

The Decision Lab must emerge as:

- architecture-preserving
- evidence-linked
- simulation-capable
- reproducible
- portfolio-aware
- regime-visible
- automation-ready
- usable by future Codex / GPT agents without confusion

without becoming bloated, opaque, or detached from the repo’s original forecasting identity.
