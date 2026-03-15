
## 3) AGENTS.md

```md
# AGENTS.md

## Scope

This repo is being evolved toward a **Decision Lab seed** on top of the existing forecasting/simulation architecture.

Your scope is limited to:

- `config/**`
- `docs/**`
- `src/forecasting_engine/**`
- `tests/**`
- `README.md`
- this `AGENTS.md`

Do not rename, move, or delete major repo structure unless a ticket explicitly authorizes it.

---

## Mission

Preserve the existing architecture while adding the smallest possible scaffolding for:

- external self-model manifest
- callable world-model bridge over existing simulation/predictive modules
- uncertainty routing
- reproducible orchestration contracts

This repo is **not** to be turned into a generic platform or dashboard suite by default.

---

## Required workflow

Always work in this order:

1. **Plan**
2. **Implement**
3. **Verify**

Map first before changing anything.

---

## Non-negotiable rules

### 1) Preserve architecture
Preserve existing architecture unless the ticket explicitly authorizes structural changes.

### 2) No rewrites
Do not refactor everything.  
Do not perform sweeping renames.  
Do not reorganize directories unless requested.

### 3) Wrap, don’t rebuild
Prefer wrappers/adapters over new engines.  
Treat existing simulation/predictive modules as substrate.

### 4) No fake world model
Do not claim retrieval is the world model.  
Do not invent a general world model engine unless the ticket explicitly requires it.

### 5) Externalize the self-model
Do not rely on model introspection for tool/capability awareness.  
Use a manifest/config-based approach.

### 6) Keep the deterministic core clean
Do not inject opaque LLM logic into:
- core forecasting updates
- replay
- ledger semantics
- deterministic evaluation logic
- simulation math

LLMs may orchestrate, classify, summarize, and explain around the core.

### 7) Uncertainty is mandatory
If a bridge or simulation output may be out of domain, surface that explicitly.  
Prefer a visible `out_of_domain` or `partial` result over false confidence.

### 8) Every new file must justify itself
Each new file must solve a specific problem that could not be handled by editing an existing file.

### 9) Reference new files
Every new user-facing file must be referenced by `README.md` or the operator docs.

### 10) Stop on ambiguity
If the ticket is ambiguous about:
- which modules are canonical
- which simulation paths should be exposed
- contract semantics
- routing policy
- replay or ledger expectations

create `docs/questions.md` and stop. Do not guess.

---

## Style rules

- Keep docs short, operational, and enforceable.
- Prefer checklists and contracts over essays.
- Prefer typed/structured payloads over loose prose.
- Keep names literal and boring.
- Avoid platform language unless the ticket explicitly calls for it.

---

## Output discipline

When you finish a task:
- update README if user-facing behavior changed
- update or add tests
- include one end-to-end example if new behavior was introduced
- summarize what changed and why

---

## Approval gates

Ask before:
- deleting files
- renaming files
- moving directories
- changing package boundaries
- replacing an existing module with a new abstraction
- adding more files than the ticket authorizes

---

## Verification standard

A task is not done until:
- requested files exist
- contracts are clear
- tests pass
- examples or docs are updated
- no unrelated drift was introduced

---

## Build posture

Prefer:
- thin adapters
- typed contracts
- reusable loaders
- explicit failure states
- small additive changes

Avoid:
- framework sprawl
- giant schema factories
- dashboard-first work
- hidden behavior
- broad cleanup unrelated to the ticket
