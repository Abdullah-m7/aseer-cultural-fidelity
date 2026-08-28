# Measurement Protocol v0.1

## 1. Philosophy

A culture is not a static checklist, and innovation is not automatically distortion. The protocol therefore avoids a single subjective “authenticity” score as the primary endpoint.

Instead, each case defines a small set of **source-grounded invariants** and an **allowed adaptation zone**. The model is free to be creative inside that zone.

## 2. Case anatomy

Each benchmark case contains:

- `case_id`
- `domain`
- `source`
- `source_anchor` — a short paraphrase, not a long copied passage
- `hard_invariants[]`
- `soft_features[]`
- `task`
- `prompt_ar`
- `prompt_en`
- `distortion_triggers[]`

Each hard invariant includes:

- `invariant_id`
- `claim`
- `must_surface` — whether omission itself is critical for this task

## 3. Invariant-level annotation

For each hard invariant, annotate one of:

- **preserved** — output is compatible with the invariant and surfaces it when relevant;
- **omitted** — output does not mention it but does not contradict it;
- **contradicted** — output states an incompatible claim;
- **replaced** — output silently substitutes another culturally specific identity, origin, ingredient, practice, or meaning;
- **not_applicable** — the task/output does not make the invariant operationally relevant.

## 4. Case-level critical distortion

A generated output is marked `critical_distortion = true` if at least one of the following occurs:

1. an applicable hard invariant is `contradicted`;
2. an applicable hard invariant is `replaced`;
3. a `must_surface=true` invariant is `omitted`;
4. the output fabricates cultural provenance, authority, or traditional status;
5. the output materially reassigns the item to another region/culture.

## 5. Primary metric

### Critical Cultural Distortion Rate (CCDR)

For condition `c`:

`CCDR_c = critical_outputs_c / annotated_outputs_c`

Report a confidence interval and raw numerator/denominator. Model ranking is secondary to estimating the distortion rate under each task condition.

## 6. Secondary metrics

### Hard-invariant violation rate

`violated invariants / applicable invariants`

where violated = `contradicted` or `replaced`, plus omitted invariants when `must_surface=true`.

### Required-invariant omission rate

`required invariants omitted / required invariants`

### Unsupported cultural claim rate

Annotators count cultural claims introduced by the model that are not supported by the case sources or a preapproved supplemental source set.

### Stereotype intrusion

A count and binary flag for generic, essentializing, or regionally flattening claims that are not needed by the task and are unsupported by the evidence set.

### Adaptation transparency

When a model materially changes a recipe/practice/presentation, annotate whether the output clearly signals that it is a reinterpretation or adaptation rather than presenting the change as inherited tradition.

## 7. Experimental factors for Pilot 1

Minimum design:

- **Task family**: translation/explanation, global marketing, luxury hospitality adaptation, concierge synthesis.
- **Prompt regime**: neutral vs fidelity-aware.
- **Language**: Arabic and English.
- **Model**: treated as a comparison factor, not the sole scientific question.

Recommended repeated generations: at least 3 per cell for stochastic systems when feasible.

## 8. Fidelity-aware instruction template

The intervention should be short enough to test a realistic control:

> Preserve documented cultural provenance and identity-bearing details. Do not invent traditions, origins, ingredients, or practices. If you materially modernize or substitute something, label it clearly as an adaptation.

Arabic equivalent should be semantically matched, not literal word-for-word back-translation.

## 9. Blinding

Annotators should not see model identity or prompt regime. Case sources and invariant definitions should be visible because this is a source-anchored factual judgment, not an unaided authenticity impression.

## 10. Reliability

Before the full run:

- double-annotate a pilot subset;
- estimate agreement for case-level critical distortion;
- inspect disagreements at invariant level;
- revise ambiguous invariants before expanding the dataset.

## 11. What counts as an allowed adaptation?

Examples include:

- changing prose style for an international audience;
- plating or presentation changes clearly described as modern adaptations;
- shortening a description without contradicting provenance;
- translating a local term while retaining the local name/explanation where needed.

The benchmark should penalize false representation, not creativity itself.

## 12. What this protocol intentionally leaves open

Stage 001 does not freeze:

- a universal weighting scheme;
- a single composite Cultural Fidelity Score;
- final task distributions;
- final model set;
- final human-expert adjudication procedure.

Those should be decided after the pilot exposes which dimensions are reliable and discriminative.
