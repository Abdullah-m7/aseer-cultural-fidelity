# Aseer Cultural Fidelity

**A source-anchored benchmark for measuring cultural distortion in AI-mediated tourism and hospitality.**

This project asks a narrower question than conventional cultural-knowledge benchmarks:

> When a generative AI system *transforms* a local culture for a new audience or operational context, what does it preserve, what does it silently replace, and what does it invent?

Aseer (Asir), Saudi Arabia is the first testbed. The initial focus is culinary heritage and hospitality because the domain combines place-based identity, translation, commercial adaptation, tourism, and real deployment pressure.

## Why this is not another Saudi culture Q&A benchmark

Existing work already evaluates whether models know Saudi facts, norms, or regional culture. This repository targets **transformation fidelity** instead: the drift that can happen when a model is asked to translate, upscale, market, summarize, recommend, or modernize culturally grounded material.

The benchmark therefore separates:

- **source-grounded hard invariants** — claims that must not be contradicted or silently replaced;
- **allowed adaptation space** — wording, presentation, creativity, and localization that may change;
- **critical distortion** — contradiction, origin reassignment, fabricated provenance, or omission of an invariant explicitly required by the task;
- **non-critical loss** — omission that reduces richness but does not falsify the cultural object;
- **unsupported cultural additions** — culturally specific claims introduced without source support;
- **adaptation transparency** — whether a substantial reinterpretation is presented honestly as an adaptation rather than as tradition.

## Stage 001

Stage 001 establishes a source-anchored pilot rather than making a premature novelty claim. It includes:

- a research charter and explicit gap hypothesis;
- a literature map covering global, MENA, Saudi, and tourism/gastronomy-adjacent work;
- a measurement protocol centered on **Critical Cultural Distortion Rate (CCDR)**;
- a machine-readable case schema;
- an initial Aseer culinary/hospitality pilot;
- deterministic validation and scoring utilities with tests.

See [`docs/STAGE_001_REPORT.md`](docs/STAGE_001_REPORT.md).

## Working research questions

1. How often do LLMs introduce critical cultural distortion when adapting source-grounded Aseer heritage for tourism and hospitality tasks?
2. Which transformation tasks produce the most drift: translation, luxury adaptation, global marketing, concierge synthesis, or modernization?
3. Does an explicit cultural-fidelity instruction reduce distortion without collapsing usefulness or creativity?
4. Does prompt/output language change the probability or type of distortion?
5. Are cultural errors primarily omissions, substitutions, false provenance, or stereotype-driven additions?

## Stage 002 exploratory result

A first English-language 2×2 pilot separated **source grounding** from a generic **cultural-fidelity instruction** using `llama3.2:latest` and 10 paired Aseer cases per condition. In a unified blinded AI-assisted annotation pass, strict CCDR was:

- neutral: **1.00 (10/10)**
- fidelity instruction only: **1.00 (10/10)**
- source grounding only: **0.50 (5/10)**
- grounding + fidelity instruction: **0.20 (2/10)**

The adaptive result suggests a mechanistic hypothesis: a model cannot reliably “preserve” local culture from a generic instruction when its underlying local prior is wrong; short authoritative grounding may be the necessary first control. These are **exploratory, not expert-validated effect estimates**. Unsupported cultural embellishment also remained common even after grounding.

See `docs/STAGE_002_FACTORIAL_RESULTS.md` and `docs/STAGE_002B_MANUAL_AUDIT.md`.

## Repository map

```text
benchmark/
  pilot/        Source-anchored pilot cases
  schema/       Machine-readable benchmark contracts
docs/
  LITERATURE_MAP.md
  MEASUREMENT_PROTOCOL.md
  RESEARCH_CHARTER.md
  STAGE_001_REPORT.md
  STAGE_002A_MANUAL_AUDIT.md
  STAGE_002B_PROTOCOL.md
  STAGE_002_FACTORIAL_RESULTS.md
  STAGE_002B_MANUAL_AUDIT.md
references/
  sources.yaml
scripts/
  validate_pilot.py
  run_stage_002_pilot.py
  annotate_stage_002_claude.py
  analyze_stage_002.py
  validate_stage_002_factorial.py
src/acf/
  experiment.py
  scoring.py
tests/
  test_experiment.py
  test_scoring.py
```

## Scientific posture

The repository deliberately distinguishes a **working gap hypothesis** from a proven novelty claim. The current hypothesis is that existing benchmarks largely test static cultural knowledge, values, or norms, while applied generative systems also need evaluation for **source-anchored cultural transformation drift**. That claim will be tightened only after a systematic literature review.

## Collaboration direction

The testbed is intentionally designed so domain experts in Aseer culture, culinary arts, tourism, and hospitality can contribute at high leverage: validating invariants, identifying unacceptable transformations, and distinguishing legitimate innovation from misrepresentation.

## Status

**Stage 002 — exploratory factorial pilot complete on the research branch; expert calibration is the next scientific gate.**
