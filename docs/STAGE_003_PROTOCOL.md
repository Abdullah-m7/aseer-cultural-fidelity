# Stage 003 — Expert Calibration + Held-Out Freeze

## Status

**PRE-EXPERT / PRE-GENERATION FREEZE**

Stage 003 is split into two gates:

- **003A — construct calibration:** a domain expert reviews a small, outcome-blinded subset of source anchors, hard invariants, `must_surface` decisions, and adaptation boundaries.
- **003B — held-out replication:** only after the calibration decisions are frozen do we generate model outputs on new held-out Aseer cases.

## Why this stage exists

Stage 002 produced an exploratory mechanistic signal: short source grounding substantially reduced critical cultural distortion for one local model, while instruction-only prompting did not. Those annotations remain AI-assisted rather than expert ground truth.

The next risk is therefore **construct validity**, not more compute. If an invariant is too strict, locally incomplete, or treats legitimate adaptation as replacement, scaling the experiment would only reproduce a bad measurement decision.

## 003A expert-calibration design

The expert sees no model outputs and no Stage 002 cell results.

Five cases / fifteen invariants are frozen in `expert_review/calibration_worksheet_v0.1.csv`.

The review asks for:

- source adequacy;
- invariant validity;
- whether omission should count as misleading in the stated task;
- severity if the invariant is violated;
- missing local nuance.

The first pass is methodological consultation, not publication data collection. Any later use of identifiable expert responses as research data requires an appropriate ethics determination.

## 003B held-out set

Six new cases are frozen in `benchmark/heldout/aseer_heldout_v0.1.jsonl`:

1. Al-Qatt Al-Asiri in a luxury-hotel interior;
2. Aseeri honey as a modern hospitality product;
3. a resort inspired by Aseer heritage-village architecture;
4. an AI concierge explanation of Al-Quriyyah village;
5. international destination marketing tied to the official Aseer strategy;
6. an explanation of Aseer authenticity spanning tangible and intangible heritage.

These cases extend the construct beyond gastronomy while remaining directly relevant to tourism and hospitality.

## Anti-leakage rule

No model generation, AI annotation, result table, or exploratory scoring is allowed on the held-out set until the expert-calibration decisions are frozen in a new versioned artifact.

If the expert changes an invariant, source anchor, `must_surface` decision, or prompt, the change is applied **before** any held-out generation and logged explicitly.

## Planned post-calibration replication

The default replication design is the same four conditions used in Stage 002:

- neutral;
- fidelity-aware;
- grounded-neutral;
- grounded-fidelity.

The number of repeats and languages will be fixed only after expert calibration and before generation. Stage 003B should not use the Stage 002 cases for confirmatory inference.

## Decision gate

Stage 003A is **PASS** only if:

- the held-out set is source-anchored and structurally valid;
- the expert worksheet is frozen before feedback;
- no held-out generations exist;
- external feedback is versioned rather than silently overwriting the pre-review instrument.
