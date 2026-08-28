# Stage 002A Results — Exploratory AI-Assisted Pilot

> **Evidence status:** exploratory only. Annotations are blinded and source-grounded but AI-assisted; no domain expert has validated these labels yet.

Total generated outputs: **20**.

## Aggregate CCDR

| Model | Regime | Critical / n | CCDR |
|---|---|---:|---:|
| llama3.2:latest | fidelity-aware | 10 / 10 | 1.000 |
| llama3.2:latest | neutral | 10 / 10 | 1.000 |

## Paired transition analysis

### llama3.2:latest
- Neutral critical → fidelity-aware clean: **0**
- Neutral clean → fidelity-aware critical: **0**
- Both critical: **10**
- Neither critical: **0**
- CCDR difference (fidelity − neutral): **+0.000**
- Exact paired p-value: **None**

## Interpretation boundary

This stage tests whether the instrument and intervention produce a plausible signal. It is not a paper-level effectiveness estimate. The next scientific gate is manual case inspection followed by domain-expert validation of the invariants and disputed labels.

## Controller case-level audit

A post-analysis manual audit found that the ceiling result is supported by multiple explicit identity substitutions rather than only by omission-sensitive labels. Examples include Haneeth → Omani, Areeka → Ethiopian, Al-Radifah → Yemeni/Moroccan, and Al-Mashghoutha → a fictitious town. `ACF-FOOD-004` is retained as an expert-sensitive disputed item because its critical status depends heavily on whether regional association must surface in that adaptation task.

The resulting Stage 002A hypothesis is therefore narrower than “fidelity prompting does not work”: **instruction without reliable local evidence may preserve a model's incorrect cultural prior rather than the target culture.** Stage 002B tests this adaptively by adding source grounding as an orthogonal factor.
