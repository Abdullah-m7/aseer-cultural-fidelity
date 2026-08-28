# Stage 002B Controller Manual Audit

## Decision
**PASS as a mechanistic exploratory signal; HOLD for expert-validated effect-size claims.**

The unified blinded factorial pass produced the following strict CCDR estimates for `llama3.2:latest` (10 cases per cell):

- neutral: **10/10 (1.00)**
- fidelity-aware only: **10/10 (1.00)**
- grounded-neutral: **5/10 (0.50)**
- grounded-fidelity: **2/10 (0.20)**

The planned paired contrast from fidelity-only to grounded+fidelity changed 8/10 cases from critical to clean and 0/10 in the reverse direction (exact two-sided paired p = 0.0078125). This is exploratory because Stage 002B was adaptively motivated by Stage 002A and the labels are AI-assisted.

## What the case audit supports
The grounding effect is qualitatively credible. Ungrounded generations repeatedly replaced Aseer identity with confident but incorrect priors (for example Omani Haneeth, Ethiopian Areeka, Yemeni/Moroccan Al-Radifah, and Al-Mashghoutha as a town). Supplying a short authoritative source anchor usually restored the core regional identity and defining facts.

The strongest interpretation is therefore not “a better prompt fixes culture.” It is:

> **Fidelity instructions appear useful only after the model has reliable local evidence to preserve.**

## Mechanistic decomposition

The case-level improvement is not only an omission effect. In the unified blind pass, **origin reassignment** fell from 8/10 neutral and 6/10 fidelity-only outputs to **0/10 in both grounded cells**. Cases containing an explicit hard-invariant contradiction or replacement fell from 8/10 neutral and 9/10 fidelity-only to 2/10 grounded-neutral and 1/10 grounded-fidelity.

This separation matters: short source grounding appears to suppress **identity drift** much more strongly than it suppresses **embellishment drift**. The latter remains visible in unsupported ingredients, historical language, provenance claims, and decorative cultural specifics.

## Residual grounded failures
Two grounded-fidelity outputs were classified critical:

1. `ACF-FOOD-001` (Haneeth): all hard-invariant statuses avoided a deterministic violation, but the judge flagged fabricated provenance because the output added unsupported heritage/traditional details. This case makes the exact CCDR sensitive to the operational definition of fabricated provenance.
2. `ACF-TOUR-003` (Food Gifts evaluation story): the output retained sustainability but omitted the required cultural/tourism evaluation dimension and presented innovation as the dominant criterion. This is a clearer residual transformation failure.

Grounded-neutral also exposes a rubric-sensitive case: `ACF-FOOD-005` explicitly labels its product a **vegan interpretation**, yet the judge marked the traditional composition as `replaced`. Under the current protocol, transparent adaptation should not automatically be treated as silent replacement. This item requires expert/rubric adjudication rather than post-hoc relabeling by the controller.

## Post-hoc sensitivity diagnostic
A diagnostic that ignores the separate `fabricated_provenance` boolean and asks only whether a case contains a hard-invariant violation gives:

- neutral: 10/10
- fidelity-aware: 10/10
- grounded-neutral: 5/10
- grounded-fidelity: **1/10**

This was not the preregistered primary endpoint and is reported only to show where annotation uncertainty enters the strict CCDR.

## Important negative finding
Grounding did **not** eliminate embellishment. In the grounded-fidelity cell, 8/10 outputs still contained at least one unsupported cultural claim under the exploratory judge (14 unsupported claims among 41 counted cultural claims). Several outputs added unsourced “ancient,” ingredient, spice, or generational-tradition details while preserving the core invariants.

That means a binary “critical vs clean” endpoint is insufficient by itself. The Stage 001 decision to retain unsupported cultural claims as a separate secondary measure is empirically justified.

## Blind reannotation consistency

The 20 Stage 002A outputs were independently re-annotated in the later unified 40-output blind pass. Critical/non-critical status agreed on **20/20 outputs (100%)**. Exact invariant-status labels agreed on **40/54 decisions (74.1%)**; fabricated-provenance flags agreed on **19/20 (95%)**, and origin-reassignment flags on **18/20 (90%)**.

This is a **same-judge-family repeatability check**, not independent human inter-rater reliability. It supports stability of the case-level ceiling result while also showing why invariant-level expert adjudication remains necessary.

## Scientific gate
Before publication-level claims, the next gate is domain-expert calibration of:

- which regional associations must surface for each task;
- when transparent substitution is legitimate adaptation rather than replacement;
- what degree of unsourced heritage language constitutes fabricated provenance;
- the cultural/tourism meaning of the Food Gifts criteria;
- the identity-bearing preparation details for Haneeth, Areeka, Mifa, Al-Radifah, and related cases.
