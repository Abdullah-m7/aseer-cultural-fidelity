#!/usr/bin/env python3
"""Score one annotation JSON against its case in the pilot JSONL."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from acf.scoring import score_annotation  # noqa: E402


def load_cases(path: Path) -> dict[str, dict]:
    cases = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            case = json.loads(raw)
            cases[case["case_id"]] = case
    return cases


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 scripts/score_annotation.py <annotation.json>", file=sys.stderr)
        return 2
    annotation = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    cases = load_cases(ROOT / "benchmark" / "pilot" / "aseer_pilot_v0.1.jsonl")
    case_id = annotation.get("case_id")
    if case_id not in cases:
        raise KeyError(f"case_id not found in pilot: {case_id}")
    print(json.dumps(score_annotation(cases[case_id], annotation), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
