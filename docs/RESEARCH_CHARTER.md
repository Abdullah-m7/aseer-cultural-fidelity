# Research Charter — Aseer Cultural Fidelity

## 1. Core problem

Generative AI can be factually fluent while changing the cultural object it is supposed to represent. A tourism description may relocate provenance. A luxury-menu rewrite may replace a defining ingredient without disclosing the change. A translation may flatten a place-specific practice into a generic “Middle Eastern” custom. A concierge answer may add a stereotype that was absent from the source.

Conventional factuality metrics only partially capture this failure because some outputs remain plausible and useful. The scientific target here is **cultural transformation fidelity**: whether a model preserves source-grounded identity constraints while performing a requested transformation.

## 2. Initial testbed

Aseer, Saudi Arabia is used as the first testbed for three reasons:

1. it has a well-documented and place-specific culinary heritage;
2. it is actively positioned for sustainable tourism and hospitality development;
3. the region's international gastronomy recognition explicitly links innovation with protection of local food and cultural uniqueness.

The project begins with culinary heritage and hospitality, then may expand to architecture, crafts, etiquette, oral heritage, destination narratives, and institutional tourism communication.

## 3. Working gap hypothesis

The current literature contains strong work on:

- cultural values and model alignment;
- cultural knowledge benchmarks;
- MENA and Saudi cultural competence;
- language-conditioned cultural behavior.

The working gap is narrower:

> **Do models preserve source-grounded cultural invariants when asked to transform culture for an applied downstream task?**

This differs from asking whether a model can answer a cultural question correctly. The benchmark makes the transformation itself the experimental intervention.

This is a hypothesis about the literature, not yet a final novelty claim.

## 4. Unit of analysis

The fundamental unit is a **source-anchored transformation case** containing:

- an authoritative or institutionally credible source;
- a paraphrased source anchor;
- hard invariants grounded in that source;
- optional soft features that add richness but are not required;
- an applied transformation request;
- an explicit definition of what would constitute critical distortion.

## 5. Primary endpoint

### Critical Cultural Distortion Rate (CCDR)

For a set of outputs:

`CCDR = outputs_with_>=1_critical_distortion / all_annotated_outputs`

A critical distortion is triggered by at least one of:

- contradiction of a hard invariant;
- replacement of a hard invariant with an incompatible cultural claim;
- provenance reassignment or fabricated origin;
- invented cultural authority or tradition;
- omission of an invariant that the case marks as `must_surface`.

CCDR is intentionally interpretable and case-level. It avoids pretending that cultural fidelity can be reduced to a universal aesthetic score.

## 6. Secondary endpoints

- invariant preservation/violation profile;
- required-invariant omission rate;
- unsupported cultural claim rate;
- stereotype intrusion count/rate;
- adaptation disclosure rate when material reinterpretation occurs;
- task-conditioned and language-conditioned distortion distributions;
- inter-annotator agreement for critical-distortion decisions.

## 7. First experimental contrast

For each case, compare at minimum:

- **Neutral transformation**: perform the requested task with no special fidelity instruction.
- **Fidelity-aware transformation**: explicitly preserve documented cultural provenance and disclose material adaptations.

The key causal contrast is whether the fidelity instruction changes CCDR, not merely whether one model “scores higher” than another.

## 8. Annotation principle

Annotators should not judge whether an output “feels authentic.” They should judge observable claims against case-specific evidence and rules.

Each hard invariant receives a status such as:

- `preserved`
- `omitted`
- `contradicted`
- `replaced`
- `not_applicable`

Case-level critical distortion follows deterministic rules from those statuses plus provenance/invention flags.

## 9. Domain-expert role

Domain experts are most valuable before large-scale model evaluation. Their role is to:

- validate which facts are genuinely identity-bearing;
- distinguish a legitimate modern adaptation from false representation;
- identify local terminology or practices that generic sources flatten;
- review cases for regional overgeneralization;
- help define cases where omission is culturally consequential.

The project should not use a domain expert merely as a ceremonial co-signature.

## 10. Claims we will not make yet

Until the pilot and literature review mature, the project will not claim:

- a universal measure of cultural authenticity;
- that one source exhaustively defines Aseer culture;
- that all change is cultural harm;
- that preservation requires freezing living culture;
- that the benchmark is representative of all Aseer communities;
- that the proposed measurement framework is globally novel.

## 11. Success criterion for Stage 001

Stage 001 succeeds if it produces a reproducible, auditable pilot where a third party can answer:

1. What source grounds each case?
2. What must the model not change?
3. What is it allowed to creatively adapt?
4. How is a critical distortion determined?
5. Can the pilot be mechanically validated before model runs begin?
