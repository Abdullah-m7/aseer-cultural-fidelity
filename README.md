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

## Proposed first experiment

The pilot is designed for a compact factorial study:

- source-grounded Aseer cases;
- multiple applied transformation tasks;
- Arabic and English conditions;
- neutral vs fidelity-preserving prompt regimes;
- repeated generations per condition;
- blinded annotation at the invariant level.

The primary endpoint is **CCDR**, not a subjective single-score notion of “authenticity.” Secondary measures retain the structure of the error rather than hiding it in one composite score.

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
references/
  sources.yaml
scripts/
  validate_pilot.py
src/acf/
  scoring.py
tests/
  test_scoring.py
```

## Scientific posture

The repository deliberately distinguishes a **working gap hypothesis** from a proven novelty claim. The current hypothesis is that existing benchmarks largely test static cultural knowledge, values, or norms, while applied generative systems also need evaluation for **source-anchored cultural transformation drift**. That claim will be tightened only after a systematic literature review.

## Collaboration direction

The testbed is intentionally designed so domain experts in Aseer culture, culinary arts, tourism, and hospitality can contribute at high leverage: validating invariants, identifying unacceptable transformations, and distinguishing legitimate innovation from misrepresentation.

## Status

**Stage 001 — active.** Foundation and pilot are being built on `research/stage-001-source-anchored-pilot`.
