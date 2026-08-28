# Stage 003A Report — Expert Calibration / Held-Out Freeze

## Controller decision

**PRE-EXPERT FREEZE: PASS**
**EXPERT CALIBRATION: PENDING**
**HELD-OUT GENERATION: BLOCKED BY DESIGN**

Stage 002 established an exploratory grounding signal, but the current bottleneck is construct validity rather than model throughput. Stage 003A therefore freezes the next measurement decisions before any new model output is observed.

## Frozen artifacts

- `benchmark/heldout/aseer_heldout_v0.1.jsonl` — 6 new source-anchored cases.
- `expert_review/calibration_worksheet_v0.1.csv` — 15 invariant judgments across 5 cases.
- `expert_review/CASEBOOK_V0.1.md` — human-readable review packet.
- `expert_review/BLINDED_CALIBRATION_BRIEF.md` — outcome-blinded instructions.
- `expert_review/FREEZE_MANIFEST_V0.1.json` — SHA-256 freeze manifest.

## Held-out domain expansion

The six cases move beyond the Stage 001 gastronomy-heavy pilot into:

1. Al-Qatt Al-Asiri in a hotel interior;
2. Aseeri honey as a modern hospitality gift;
3. heritage-village architecture adapted into a new resort;
4. concierge explanation of Al-Quriyyah village;
5. official Aseer destination strategy;
6. tangible + intangible heritage in tourism storytelling.

This expansion is deliberate: the research construct should survive outside food before it is presented as a general cultural-transformation benchmark.

## Expert subset

The first expert packet intentionally stays small and includes:

- Haneeth;
- Areeka;
- World Region of Gastronomy positioning;
- Al-Qatt Al-Asiri in hospitality interiors;
- heritage-village-inspired resort adaptation.

The expert sees source anchors, tasks, and proposed invariants, but **no model outputs and no Stage 002 outcome table**. This reduces outcome anchoring during construct calibration.

## Source audit

The new cases use UNESCO, Saudipedia, and Aseer Development Authority sources. The source anchors were cross-checked before freeze for:

- regional provenance;
- the documented role of women and guest-room context in Al-Qatt;
- honey as inherited craft linked to Aseer ecology;
- local-material architecture and landscape relationship;
- Al-Quriyyah-specific `Al-Masareeb` and stone/clay houses;
- official strategy language connecting authentic culture, diverse nature, competitive advantage, and community participation;
- official framing of tangible and intangible Aseer heritage.

Institutional source adequacy is still a **reviewable construct decision**, not treated as cultural ground truth by fiat.

## Anti-leakage controls

At freeze time:

- held-out cases: **6**;
- held-out model generations: **0**;
- expert response cells filled: **0**;
- Stage 001/held-out case-ID overlap: **0**;
- frozen expert subset: **5 cases / 15 invariants**;
- freeze-manifest files: **7**, all SHA-256 verified.

The `v0.1` expert worksheet must never be overwritten with feedback. External input will be copied into a new version and every benchmark change will be logged before any Stage 003B generation.

## Quality gates

- held-out structural validator: PASS, 6/6;
- Stage 003 integrity gate: PASS;
- Stage 001 pilot validator: PASS, 10/10;
- Stage 002 factorial integrity gate: PASS;
- unit tests: PASS;
- `git diff --check`: PASS.

## Next scientific gate

Obtain one domain-expert calibration pass on the five-case packet. Then:

1. classify each external change as source / invariant / `must_surface` / severity / prompt / missing-trigger change;
2. create `v0.2` rather than editing `v0.1`;
3. freeze the post-expert instrument and replication design;
4. only then run Stage 003B on the six held-out cases.

The goal of the first external contact is therefore not “join the project.” It is a bounded scientific question: **where is our boundary between legitimate tourism adaptation and cultural misrepresentation wrong?**
