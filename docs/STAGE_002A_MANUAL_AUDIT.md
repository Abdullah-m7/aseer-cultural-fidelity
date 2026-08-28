# Stage 002A Controller Manual Audit

## Purpose
This audit was performed after the blinded AI-assisted annotations and aggregate Stage 002A analysis. It does not overwrite the blinded labels. Its role is to decide whether the 100% CCDR result is obviously a judge artifact and to identify disputed items for later expert adjudication.

## Decision
**HOLD for expert-validity claims; PASS as an exploratory failure signal.**

The all-critical result is not explained by a single annotation quirk. Many outputs contain severe, directly inspectable transformations of identity or meaning:

- Haneeth was reassigned to Oman in both conditions; the traditional preparation was replaced with casserole/braising narratives.
- Areeka was reassigned to Ethiopia and reconstructed around teff/lentils rather than the documented Aseer breakfast composition.
- Aseeda was described as a desert feast in one output and a cold yogurt-rice dessert in another.
- Al-Radifah was treated as Moroccan architecture in one condition and a Yemeni meat-and-rice dish in the other.
- Al-Mashghoutha was converted from a winter dish into a Saudi town/destination in both conditions.
- Food Gifts / its evaluation criteria were replaced by invented generic or international competition narratives in multiple outputs.
- Haneeth concierge responses replaced the documented Aseer pit/plant-material preparation with generic stew/clay-pot explanations; one also relocated its origin to Hejaz.

## Disputed / expert-sensitive item
`ACF-FOOD-004` (Mifa) is the clearest sensitivity check. The neutral output was critical primarily because the case currently marks the Aseer association (`M1`) as `must_surface=true`. Whether every gluten-free adaptation must explicitly surface the regional association is a domain/task-design judgment that should be reviewed by an Aseer food/tourism expert before the benchmark is frozen.

This dispute does not remove the broader Stage 002A signal because numerous other cases contain explicit contradiction, replacement, fabricated provenance, or origin reassignment.

## What Stage 002A actually establishes
It does **not** establish that fidelity instructions never work. It establishes a narrower failure mode worth testing:

> A generic instruction to preserve cultural provenance can fail when the generator does not possess correct local knowledge; it may confidently preserve its own incorrect prior instead.

This motivates an adaptive Stage 002B factorial follow-up separating **instruction** from **source grounding**.

## Evidence boundary
- Blinded labels remain AI-assisted, not expert ground truth.
- Manual inspection was performed after condition identities were available and is therefore diagnostic, not a replacement blinded annotation.
- No Stage 002A outputs or labels are changed in response to this audit.
