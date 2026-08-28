# Stage 002 Results — Exploratory 2×2 Pilot

> **Evidence status:** exploratory only. Annotations are blinded and source-grounded but AI-assisted; no domain expert has validated these labels yet. Stage 002B was adaptively specified after Stage 002A.

Total generated outputs: **40**.

## Aggregate CCDR

| Model | Regime | Critical / n | CCDR |
|---|---|---:|---:|
| llama3.2:latest | fidelity-aware | 10 / 10 | 1.000 |
| llama3.2:latest | grounded-fidelity | 2 / 10 | 0.200 |
| llama3.2:latest | grounded-neutral | 5 / 10 | 0.500 |
| llama3.2:latest | neutral | 10 / 10 | 1.000 |

## Planned paired contrasts

### llama3.2:latest
**instruction_without_grounding** — `neutral` → `fidelity-aware`
- Critical → clean: **0**; clean → critical: **0**
- Both critical: **10**; neither critical: **0**
- CCDR difference (to − from): **+0.000**
- Exact paired p-value: **None**

**grounding_without_instruction** — `neutral` → `grounded-neutral`
- Critical → clean: **5**; clean → critical: **0**
- Both critical: **5**; neither critical: **0**
- CCDR difference (to − from): **-0.500**
- Exact paired p-value: **0.0625**

**grounding_with_instruction** — `fidelity-aware` → `grounded-fidelity`
- Critical → clean: **8**; clean → critical: **0**
- Both critical: **2**; neither critical: **0**
- CCDR difference (to − from): **-0.800**
- Exact paired p-value: **0.0078125**

**instruction_with_grounding** — `grounded-neutral` → `grounded-fidelity`
- Critical → clean: **3**; clean → critical: **0**
- Both critical: **2**; neither critical: **5**
- CCDR difference (to − from): **-0.300**
- Exact paired p-value: **0.25**

## Interpretation boundary

Stage 002A tested instruction-only prompting and produced a ceiling failure. Stage 002B is an adaptive mechanistic follow-up testing source grounding. These data are hypothesis-generating; any apparent grounding effect must be replicated on held-out cases and expert-validated annotations.

See `docs/STAGE_002A_MANUAL_AUDIT.md` for the controller's post-Stage-002A case inspection.
