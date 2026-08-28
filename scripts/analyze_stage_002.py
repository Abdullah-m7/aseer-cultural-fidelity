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
    annotations = {x["response_id"]: x for x in load_jsonl(result_dir / "annotations_ai_assisted.jsonl")}
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
    (result_dir / "scored_outputs.jsonl").write_text(
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
    paired = {}
    for model in sorted({x["model"] for x in scored}):
        pairs = [v for k, v in by_pair.items() if k[0] == model and {"neutral", "fidelity-aware"} <= set(v)]
        neutral_only = sum(p["neutral"]["critical_distortion"] and not p["fidelity-aware"]["critical_distortion"] for p in pairs)
        fidelity_only = sum(p["fidelity-aware"]["critical_distortion"] and not p["neutral"]["critical_distortion"] for p in pairs)
        both = sum(p["neutral"]["critical_distortion"] and p["fidelity-aware"]["critical_distortion"] for p in pairs)
        neither = len(pairs) - neutral_only - fidelity_only - both
        n_ccdr = sum(p["neutral"]["critical_distortion"] for p in pairs) / len(pairs)
        f_ccdr = sum(p["fidelity-aware"]["critical_distortion"] for p in pairs) / len(pairs)
        paired[model] = {
            "pairs": len(pairs),
            "neutral_critical_to_fidelity_clean": neutral_only,
            "neutral_clean_to_fidelity_critical": fidelity_only,
            "both_critical": both,
            "neither_critical": neither,
            "ccdr_difference_fidelity_minus_neutral": f_ccdr - n_ccdr,
            "exact_mcnemar_two_sided_p": exact_mcnemar(neutral_only, fidelity_only),
        }

    summary = {
        "analysis_status": "exploratory_ai_assisted_not_expert_validated",
        "generations": len(generations),
        "annotations": len(annotations),
        "aggregate": aggregate,
        "paired": paired,
    }
    (result_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")

    lines = [
        "# Stage 002A Results — Exploratory AI-Assisted Pilot",
        "",
        "> **Evidence status:** exploratory only. Annotations are blinded and source-grounded but AI-assisted; no domain expert has validated these labels yet.",
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
    lines += ["", "## Paired transition analysis", ""]
    for model, item in paired.items():
        lines += [
            f"### {model}",
            f"- Neutral critical → fidelity-aware clean: **{item['neutral_critical_to_fidelity_clean']}**",
            f"- Neutral clean → fidelity-aware critical: **{item['neutral_clean_to_fidelity_critical']}**",
            f"- Both critical: **{item['both_critical']}**",
            f"- Neither critical: **{item['neither_critical']}**",
            f"- CCDR difference (fidelity − neutral): **{item['ccdr_difference_fidelity_minus_neutral']:+.3f}**",
            f"- Exact paired p-value: **{item['exact_mcnemar_two_sided_p']}**",
            "",
        ]
    lines += [
        "## Interpretation boundary",
        "",
        "This stage tests whether the instrument and intervention produce a plausible signal. It is not a paper-level effectiveness estimate. The next scientific gate is manual case inspection followed by domain-expert validation of the invariants and disputed labels.",
        "",
    ]
    (ROOT / "docs/STAGE_002_RESULTS.md").write_text("\n".join(lines))
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
