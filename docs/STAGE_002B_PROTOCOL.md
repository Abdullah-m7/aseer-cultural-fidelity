# Stage 002B Protocol — Adaptive Grounding Factor

## Status
Adaptive follow-up specified **after** Stage 002A was frozen, annotated, analyzed, manually audited, committed, and pushed. Stage 002B is therefore not presented as preregistered with Stage 002A.

## Why this follow-up exists
Stage 002A produced a ceiling: 10/10 neutral and 10/10 fidelity-aware outputs were classified critical by the blinded exploratory judge. Manual audit confirmed multiple explicit cultural-identity substitutions. A generic fidelity instruction therefore could not be meaningfully distinguished from neutral generation under the ungrounded setup.

The mechanistic hypothesis suggested by those failures is:

> Fidelity instructions cannot preserve source culture when the model's local prior is wrong; source grounding may be the missing intervention.

## Factorial design
Stage 002B completes a 2 × 2 design using the same 10 cases, model, English language, temperature, seed, and single repeat:

| Source grounding | Fidelity instruction | Regime |
|---|---|---|
| No | No | `neutral` (Stage 002A) |
| No | Yes | `fidelity-aware` (Stage 002A) |
| Yes | No | `grounded-neutral` (Stage 002B) |
| Yes | Yes | `grounded-fidelity` (Stage 002B) |

Grounding consists of the case's short `source_anchor` plus source title/authority supplied as reference context. Hard-invariant labels are **not** given to the generator.

## Outcomes
Primary endpoint remains CCDR without modification. Secondary metrics remain unchanged.

## Blinding
New outputs are added to the same anonymous response-ID pool and annotated using the same source-grounded Claude CLI protocol. The annotation assistant does not receive regime or model metadata.

## Planned descriptive contrasts
1. Fidelity instruction effect without grounding: `neutral` vs `fidelity-aware`.
2. Grounding effect without fidelity instruction: `neutral` vs `grounded-neutral`.
3. Grounding effect with fidelity instruction: `fidelity-aware` vs `grounded-fidelity`.
4. Fidelity instruction effect under grounding: `grounded-neutral` vs `grounded-fidelity`.

For each contrast, report paired critical-status transitions, CCDR difference, and exact two-sided McNemar/sign-test p-value as exploratory statistics.

## Interpretation boundary
Because Stage 002B is motivated by Stage 002A results, its evidence is hypothesis-generating. A strong grounding effect should be replicated later on a held-out case set and expert-validated annotations.
