#!/usr/bin/env python3
"""Validate the Stage 001 JSONL pilot without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CASE_ID = re.compile(r"^ACF-[A-Z]+-[0-9]{3}$")
TASKS = {
    "translation_explanation",
    "global_marketing",
    "luxury_hospitality_adaptation",
    "concierge_synthesis",
    "product_innovation",
    "sustainability_storytelling",
}
REQUIRED = {
    "case_id",
    "domain",
    "task_family",
    "source",
    "source_anchor",
    "hard_invariants",
    "soft_features",
    "prompt_ar",
    "prompt_en",
    "distortion_triggers",
}


def fail(message: str) -> None:
    raise ValueError(message)


def validate_case(case: dict, line_no: int) -> None:
    prefix = f"line {line_no}: "
    missing = REQUIRED - set(case)
    if missing:
        fail(prefix + f"missing keys: {sorted(missing)}")
    if not CASE_ID.match(case["case_id"]):
        fail(prefix + f"invalid case_id: {case['case_id']}")
    if case["task_family"] not in TASKS:
        fail(prefix + f"unknown task_family: {case['task_family']}")
    if not case["prompt_ar"].strip() or not case["prompt_en"].strip():
        fail(prefix + "Arabic and English prompts are both required")
    if len(case["source_anchor"]) > 1000:
        fail(prefix + "source_anchor is unexpectedly long; paraphrase the evidence")

    source = case["source"]
    for key in ("source_id", "title", "url", "authority"):
        if not source.get(key):
            fail(prefix + f"source.{key} is required")
    if not source["url"].startswith("https://"):
        fail(prefix + "source.url must use https")

    invariants = case["hard_invariants"]
    if not invariants:
        fail(prefix + "at least one hard invariant is required")
    invariant_ids = [item.get("invariant_id") for item in invariants]
    if len(invariant_ids) != len(set(invariant_ids)):
        fail(prefix + "hard invariant IDs must be unique inside a case")
    for item in invariants:
        if not item.get("invariant_id") or not item.get("claim"):
            fail(prefix + "each hard invariant needs invariant_id and claim")
        if not isinstance(item.get("must_surface"), bool):
            fail(prefix + "must_surface must be boolean")

    if not case["distortion_triggers"]:
        fail(prefix + "at least one distortion trigger is required")


def main() -> int:
    default_path = Path(__file__).resolve().parents[1] / "benchmark" / "pilot" / "aseer_pilot_v0.1.jsonl"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path
    seen = set()
    count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            case = json.loads(raw)
            validate_case(case, line_no)
            if case["case_id"] in seen:
                fail(f"line {line_no}: duplicate case_id {case['case_id']}")
            seen.add(case["case_id"])
            count += 1
    if count == 0:
        fail("pilot contains no cases")
    print(f"PASS: validated {count} source-anchored pilot cases from {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
