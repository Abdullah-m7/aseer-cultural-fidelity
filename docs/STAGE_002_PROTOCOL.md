# Stage 002 Protocol — Neutral vs Fidelity-Aware Pilot

## Status
Protocol frozen before annotation and aggregate analysis of Stage 002A.

## Objective
Test whether a minimal cultural-fidelity instruction changes the rate of source-grounded critical cultural distortion during transformation tasks.

## Stage 002A design
- Cases: all 10 Stage 001 pilot cases.
- Generator: `llama3.2:latest` via local Ollama.
- Language: English.
- Conditions: neutral vs fidelity-aware.
- Repeats: 1 per case-condition pair.
- Temperature: 0.2.
- Seed: 20260828.
- Maximum generation budget: 512 tokens.
- Pairing unit: benchmark case.

The fidelity-aware instruction is exactly the intervention frozen in `src/acf/experiment.py`. The neutral condition receives no cultural-fidelity system instruction.

## Primary endpoint
Critical Cultural Distortion Rate (CCDR), as defined in `docs/MEASUREMENT_PROTOCOL.md`.

## Secondary endpoints
- invariant preservation rate;
- required-invariant omission rate;
- unsupported cultural-claim rate;
- adaptation transparency when material adaptation occurs.

## Exploratory annotation
Stage 002A uses Claude CLI as a blinded, source-grounded annotation assistant. The judge sees the source anchor, invariants, original task, anonymous response ID, and generated output. It does **not** see generator identity or prompt regime.

These annotations are explicitly **not expert validation** and must not be presented as final human ground truth. Their purpose is instrument stress-testing and candidate-case discovery before domain-expert review.

## Paired analysis
For each case, compare neutral and fidelity-aware critical-distortion status. Report raw paired transitions and an exact two-sided McNemar/sign-test p-value only as descriptive exploratory evidence; the sample is too small for strong inferential claims.

## Pre-analysis generation correction
An initial 220-token preflight was completed before any annotation or semantic outcome analysis. Seventeen of 20 outputs ended with `done_reason=length`, creating a direct omission confound. Those raw generations are retained under `results/stage_002/preflight/` and excluded. The generation ceiling was therefore raised to 512 tokens before the analysis set was produced. This correction was based only on termination metadata, not cultural-fidelity labels.

## Pre-analysis exclusion
`qwen3:4b` was probed before Stage 002A. In the available local inference configuration it consumed the output budget with visible reasoning text and repeatedly failed to reach the requested final answer, including after a no-think probe. It is excluded from Stage 002A because this is an inference-contract failure that would confound cultural-fidelity measurement. It may be reintroduced after its serving configuration is repaired.

## Interpretation rule
A lower CCDR under the fidelity-aware condition is evidence that the intervention is worth studying further, not proof of general effectiveness. A null or adverse result is equally informative and should trigger case-level inspection rather than metric redesign after the fact.
