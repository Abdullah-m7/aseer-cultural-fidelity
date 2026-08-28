#!/usr/bin/env python3
"""Analyze the paired Stage 002 exploratory pilot."""
from __future__ import annotations

import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from acf.scoring import score_annotation  # noqa: E402


def load_jsonl(path: Path):
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def wilson(k: int, n: int, z: float = 1.959963984540054):
    if n == 0:
        return [None, None]
    p = k / n
    den = 1 + z * z / n
    center = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return [max(0.0, center - half), min(1.0, center + half)]


def exact_mcnemar(b: int, c: int):
    n = b + c
    if n == 0:
        return None
    m = min(b, c)
    tail = sum(math.comb(n, i) for i in range(m + 1)) / (2 ** n)
    return min(1.0, 2 * tail)


def mean_or_none(values):
    values = [v for v in values if v is not None]
    return statistics.mean(values) if values else None


def main():
    result_dir = ROOT / "results/stage_002"
    generations = load_jsonl(result_dir / "generations.jsonl")
    annotations = {x["response_id"]: x for x in load_jsonl(result_dir / "annotations_factorial_blinded.jsonl")}
    cases = {x["case_id"]: x for x in load_jsonl(ROOT / "benchmark/pilot/aseer_pilot_v0.1.jsonl")}
    if len(annotations) != len(generations):
        raise SystemExit(f"annotation/generation mismatch: {len(annotations)} vs {len(generations)}")

    scored = []
    for generation in generations:
        ann = annotations[generation["response_id"]]
        score = score_annotation(cases[generation["case_id"]], ann)
        scored.append({
            **{k: generation[k] for k in ("response_id", "case_id", "model", "model_digest", "regime", "language", "repeat")},
            **score,
        })
    (result_dir / "scored_outputs_factorial.jsonl").write_text(
        "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in scored)
    )

    groups = defaultdict(list)
    for row in scored:
        groups[(row["model"], row["regime"])].append(row)
    aggregate = {}
    for (model, regime), rows in sorted(groups.items()):
        critical = sum(bool(x["critical_distortion"]) for x in rows)
        aggregate[f"{model}|{regime}"] = {
            "n": len(rows),
            "critical": critical,
            "ccdr": critical / len(rows),
            "ccdr_wilson_95": wilson(critical, len(rows)),
            "mean_invariant_preservation_rate": mean_or_none([x["invariant_preservation_rate"] for x in rows]),
            "mean_required_invariant_omission_rate": mean_or_none([x["required_invariant_omission_rate"] for x in rows]),
            "mean_unsupported_cultural_claim_rate": mean_or_none([x["unsupported_cultural_claim_rate"] for x in rows]),
        }

    by_pair = defaultdict(dict)
    for row in scored:
        key = (row["model"], row["language"], row["repeat"], row["case_id"])
        by_pair[key][row["regime"]] = row

    planned_contrasts = {
        "instruction_without_grounding": ("neutral", "fidelity-aware"),
        "grounding_without_instruction": ("neutral", "grounded-neutral"),
        "grounding_with_instruction": ("fidelity-aware", "grounded-fidelity"),
        "instruction_with_grounding": ("grounded-neutral", "grounded-fidelity"),
    }
    contrasts = {}
    for model in sorted({x["model"] for x in scored}):
        model_results = {}
        for name, (a_regime, b_regime) in planned_contrasts.items():
            pairs = [
                v for k, v in by_pair.items()
                if k[0] == model and {a_regime, b_regime} <= set(v)
            ]
            if not pairs:
                continue
            a_to_clean = sum(p[a_regime]["critical_distortion"] and not p[b_regime]["critical_distortion"] for p in pairs)
            a_clean_to_b = sum(p[b_regime]["critical_distortion"] and not p[a_regime]["critical_distortion"] for p in pairs)
            both = sum(p[a_regime]["critical_distortion"] and p[b_regime]["critical_distortion"] for p in pairs)
            neither = len(pairs) - a_to_clean - a_clean_to_b - both
            a_ccdr = sum(p[a_regime]["critical_distortion"] for p in pairs) / len(pairs)
            b_ccdr = sum(p[b_regime]["critical_distortion"] for p in pairs) / len(pairs)
            model_results[name] = {
                "from_regime": a_regime,
                "to_regime": b_regime,
                "pairs": len(pairs),
                "from_critical_to_clean": a_to_clean,
                "from_clean_to_critical": a_clean_to_b,
                "both_critical": both,
                "neither_critical": neither,
                "ccdr_difference_to_minus_from": b_ccdr - a_ccdr,
                "exact_mcnemar_two_sided_p": exact_mcnemar(a_to_clean, a_clean_to_b),
            }
        contrasts[model] = model_results

    summary = {
        "analysis_status": "exploratory_ai_assisted_not_expert_validated",
        "generations": len(generations),
        "annotations": len(annotations),
        "aggregate": aggregate,
        "planned_contrasts": contrasts,
    }
    (result_dir / "summary_factorial.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")

    lines = [
        "# Stage 002 Results — Exploratory 2×2 Pilot",
        "",
        "> **Evidence status:** exploratory only. Annotations are blinded and source-grounded but AI-assisted; no domain expert has validated these labels yet. Stage 002B was adaptively specified after Stage 002A.",
        "",
        f"Total generated outputs: **{len(generations)}**.",
        "",
        "## Aggregate CCDR",
        "",
        "| Model | Regime | Critical / n | CCDR |",
        "|---|---|---:|---:|",
    ]
    for key, item in aggregate.items():
        model, regime = key.split("|", 1)
        lines.append(f"| {model} | {regime} | {item['critical']} / {item['n']} | {item['ccdr']:.3f} |")
    lines += ["", "## Planned paired contrasts", ""]
    for model, model_contrasts in contrasts.items():
        lines.append(f"### {model}")
        for name, item in model_contrasts.items():
            lines += [
                f"**{name}** — `{item['from_regime']}` → `{item['to_regime']}`",
                f"- Critical → clean: **{item['from_critical_to_clean']}**; clean → critical: **{item['from_clean_to_critical']}**",
                f"- Both critical: **{item['both_critical']}**; neither critical: **{item['neither_critical']}**",
                f"- CCDR difference (to − from): **{item['ccdr_difference_to_minus_from']:+.3f}**",
                f"- Exact paired p-value: **{item['exact_mcnemar_two_sided_p']}**",
                "",
            ]
    lines += [
        "## Interpretation boundary",
        "",
        "Stage 002A tested instruction-only prompting and produced a ceiling failure. Stage 002B is an adaptive mechanistic follow-up testing source grounding. These data are hypothesis-generating; any apparent grounding effect must be replicated on held-out cases and expert-validated annotations.",
        "",
        "See `docs/STAGE_002A_MANUAL_AUDIT.md` for the controller's post-Stage-002A case inspection.",
        "",
    ]
    (ROOT / "docs/STAGE_002_FACTORIAL_RESULTS.md").write_text("\n".join(lines))
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
