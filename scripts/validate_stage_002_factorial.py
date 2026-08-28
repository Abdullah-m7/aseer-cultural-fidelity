#!/usr/bin/env python3
"""Integrity gate for the frozen Stage 002 2x2 factorial artifacts."""
from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from acf.scoring import score_annotation  # noqa: E402

REGIMES = ("neutral", "fidelity-aware", "grounded-neutral", "grounded-fidelity")
EXPECTED_SHA256 = {
    "generations.jsonl": "3e26445b1a958a498b0c611a3f8ac3e554a517a71a296cc74e2b36ccf1aa47ae",
    "annotations_factorial_blinded.jsonl": "803f545fb8a05a4173fd41b3b7a2eb4687d88a7de08305d748bb51670d9dd71d",
    "summary_factorial.json": "1d871e7318f30a94cab8507af4317f15c73226dd7b776b136fcb48d25342b7aa",
}
FORBIDDEN_ANNOTATION_METADATA = {"model", "model_digest", "regime", "language", "temperature", "seed"}


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    result_dir = ROOT / "results/stage_002"
    generations = load_jsonl(result_dir / "generations.jsonl")
    annotations = load_jsonl(result_dir / "annotations_factorial_blinded.jsonl")
    stage_a = load_jsonl(result_dir / "annotations_ai_assisted.jsonl")
    cases = {row["case_id"]: row for row in load_jsonl(ROOT / "benchmark/pilot/aseer_pilot_v0.1.jsonl")}

    if len(generations) != 40 or len(annotations) != 40:
        fail(f"expected 40 generations and 40 factorial annotations; got {len(generations)} and {len(annotations)}")
    generation_ids = [row["response_id"] for row in generations]
    annotation_ids = [row["response_id"] for row in annotations]
    if len(set(generation_ids)) != 40 or len(set(annotation_ids)) != 40:
        fail("response IDs must be unique")
    if set(generation_ids) != set(annotation_ids):
        fail("generation and annotation response-ID sets differ")

    counts = Counter(row["regime"] for row in generations)
    expected = Counter({regime: 10 for regime in REGIMES})
    if counts != expected:
        fail(f"factorial cell counts differ from 10 each: {dict(counts)}")
    if any(row.get("done_reason") != "stop" for row in generations):
        fail("at least one generation did not terminate with done_reason=stop")
    if {row.get("language") for row in generations} != {"en"}:
        fail("Stage 002 frozen set must be English-only")
    if len({(row.get("model"), row.get("model_digest")) for row in generations}) != 1:
        fail("Stage 002 frozen set must use one generator build")

    by_generation = {row["response_id"]: row for row in generations}
    for annotation in annotations:
        generation = by_generation[annotation["response_id"]]
        case = cases[generation["case_id"]]
        if annotation.get("case_id") != generation["case_id"]:
            fail(f"case mismatch for {annotation['response_id']}")
        score_annotation(case, annotation)

    if len(stage_a) != 20 or len({row["response_id"] for row in stage_a}) != 20:
        fail("historical Stage 002A annotation artifact must remain frozen at 20 unique rows")
    if not {row["response_id"] for row in stage_a} <= set(generation_ids):
        fail("historical Stage 002A IDs are not a subset of the factorial generation set")
    historical_regimes = {by_generation[row["response_id"]]["regime"] for row in stage_a}
    if historical_regimes != {"neutral", "fidelity-aware"}:
        fail(f"historical Stage 002A artifact contains unexpected regimes: {historical_regimes}")

    if any(FORBIDDEN_ANNOTATION_METADATA & set(row) for row in annotations):
        fail("factorial annotation rows contain generator/condition metadata")

    for filename, expected_hash in EXPECTED_SHA256.items():
        digest = hashlib.sha256((result_dir / filename).read_bytes()).hexdigest()
        if digest != expected_hash:
            fail(f"SHA-256 mismatch for {filename}: {digest}")

    raw_factorial = sorted((result_dir / "judge_raw_factorial").glob("batch_*.txt"))
    if len(raw_factorial) != 4:
        fail(f"expected four unified blind-pass raw batches; got {len(raw_factorial)}")
    raw_text = "\n".join(path.read_text() for path in raw_factorial)
    for leaked in ("llama3.2:latest", "grounded-neutral", "grounded-fidelity", "fidelity-aware"):
        if leaked in raw_text:
            fail(f"condition/model string leaked into stored blind judge output: {leaked}")

    print("PASS: Stage 002 factorial integrity gate")
    print(f"  generations={len(generations)} annotations={len(annotations)}")
    print(f"  cells={dict(counts)}")
    print(f"  historical_stage002a_annotations={len(stage_a)} raw_factorial_batches={len(raw_factorial)}")


if __name__ == "__main__":
    main()
