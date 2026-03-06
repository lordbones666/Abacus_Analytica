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
