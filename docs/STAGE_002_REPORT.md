# Stage 002 Report — Instruction × Grounding Exploratory Pilot

## Controller decision

**PASS** for an exploratory mechanistic signal.  
**HOLD** for publication-level effect-size or expert-validity claims.

## Design frozen and executed

Stage 002 used 10 source-anchored Aseer transformation cases with `llama3.2:latest` (`a80c4f17acd5`), English outputs, temperature 0.2, seed 20260828, one generation per cell, and a 512-token ceiling.

The final adaptive 2×2 design separated:

1. no grounding / no fidelity instruction (`neutral`);
2. no grounding / fidelity instruction (`fidelity-aware`);
3. source grounding / no fidelity instruction (`grounded-neutral`);
4. source grounding / fidelity instruction (`grounded-fidelity`).

Stage 002B was explicitly specified after the Stage 002A ceiling result and is therefore hypothesis-generating rather than preregistered confirmatory evidence.

## Primary exploratory result

Under the unified randomized blinded factorial annotation pass:

| Regime | Critical / n | CCDR |
|---|---:|---:|
| neutral | 10 / 10 | 1.00 |
| fidelity-aware | 10 / 10 | 1.00 |
| grounded-neutral | 5 / 10 | 0.50 |
| grounded-fidelity | 2 / 10 | 0.20 |

The planned `fidelity-aware → grounded-fidelity` paired contrast had 8 critical→clean transitions, 0 clean→critical transitions, and an exploratory exact two-sided p-value of 0.0078125. The instruction-only contrast produced no CCDR change. Under grounding, adding the fidelity instruction reduced CCDR by a further 0.30, but the paired p-value was 0.25 at n=10.

## Mechanistic interpretation

The strongest supported hypothesis is not that generic fidelity prompting is sufficient. Stage 002 suggests the opposite failure mode:

> A model cannot reliably preserve a local cultural identity that it does not correctly know. A generic preservation instruction may simply reinforce an incorrect cultural prior. Short authoritative grounding appears to supply the missing factual substrate; the fidelity instruction may then add incremental value.

This interpretation is consistent with visible ungrounded failures such as reassigning Haneeth to Oman, Areeka to Ethiopia, Al-Radifah to Yemen/Morocco, and treating Al-Mashghoutha as a town rather than a dish.

## What grounding did not solve

Grounded-fidelity outputs still contained 14 unsupported cultural claims among 41 counted cultural claims, and 8/10 outputs contained at least one unsupported claim under the exploratory judge. Thus reduction in **critical identity distortion** did not eliminate decorative or provenance-adjacent hallucination.

This is an important measurement result: CCDR should not replace the secondary unsupported-claim measures.

## Annotation uncertainty

All factorial labels are AI-assisted and source-grounded, not expert ground truth. Controller audit identified rubric-sensitive examples:

- transparent vegan adaptation was once labeled as `replaced` despite explicit disclosure;
- one grounded Haneeth output was critical solely because of the separate `fabricated_provenance` flag, with no hard-invariant violation;
- some outputs classified non-critical still contained unsupported “ancient,” ingredient, or generational-tradition embellishments.

Accordingly, the exact 0.50 and 0.20 CCDR estimates must not be treated as final effect sizes.

## Reproducibility gates

- final generations: 40/40 unique response IDs;
- condition balance: 10 per factorial cell;
- termination: 40/40 `done_reason=stop`;
- generator digest: `a80c4f17acd5` for all 40;
- unified factorial annotations: 40/40;
- model/regime metadata fields in annotation rows: none;
- model/regime strings found in stored factorial judge outputs: none;
- benchmark validator: PASS, 10/10 cases;
- factorial artifact integrity gate: PASS, 40 generations / 40 annotations / 10 per cell / 4 raw blind batches;
- repeat blind-pass case-level critical status agreement on the original Stage 002A outputs: 20/20 (same judge family; not human inter-rater reliability);
- unit tests: PASS, 11/11;
- `git diff --check`: PASS.

Frozen artifact SHA-256 values:

- `results/stage_002/generations.jsonl`: `3e26445b1a958a498b0c611a3f8ac3e554a517a71a296cc74e2b36ccf1aa47ae`
- `results/stage_002/annotations_factorial_blinded.jsonl`: `803f545fb8a05a4173fd41b3b7a2eb4687d88a7de08305d748bb51670d9dd71d`
- `results/stage_002/summary_factorial.json`: `1d871e7318f30a94cab8507af4317f15c73226dd7b776b136fcb48d25342b7aa`

## Next scientific gate

Do **not** scale to many models yet. The highest-value next step is expert calibration of invariants and annotation boundaries on the existing cases, followed by a held-out Aseer case set and replication of the grounding effect. Only after that should the benchmark expand across models, Arabic outputs, and additional hospitality/tourism domains.
