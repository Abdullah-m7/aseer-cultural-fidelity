#!/usr/bin/env python3
"""Run the Stage 002 neutral-vs-fidelity-aware local-model pilot."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from acf.experiment import build_generation_prompt, ollama_generate, response_id  # noqa: E402


def load_cases(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def model_digest(model: str) -> str | None:
    proc = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
    for line in proc.stdout.splitlines()[1:]:
        parts = line.split()
        if parts and parts[0] == model and len(parts) > 1:
            return parts[1]
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=["qwen3:4b", "llama3.2:latest"])
    ap.add_argument("--language", choices=["en", "ar"], default="en")
    ap.add_argument("--regimes", nargs="+", default=["neutral", "fidelity-aware"])
    ap.add_argument("--repeats", type=int, default=1)
    ap.add_argument("--temperature", type=float, default=0.2)
    ap.add_argument("--seed", type=int, default=20260828)
    ap.add_argument("--output", type=Path, default=ROOT / "results/stage_002/generations.jsonl")
    args = ap.parse_args()

    cases = load_cases(ROOT / "benchmark/pilot/aseer_pilot_v0.1.jsonl")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    completed = {}
    if args.output.exists():
        for line in args.output.read_text().splitlines():
            if line.strip():
                row = json.loads(line)
                completed[row["response_id"]] = row

    for model in args.models:
        digest = model_digest(model)
        for case in cases:
            for regime in args.regimes:
                for repeat in range(1, args.repeats + 1):
                    rid = response_id(case["case_id"], model, regime, args.language, repeat)
                    if rid in completed:
                        continue
                    result = ollama_generate(
                        model,
                        build_generation_prompt(case, args.language, regime),
                        regime,
                        temperature=args.temperature,
                        seed=args.seed + repeat - 1,
                    )
                    row = {
                        "response_id": rid,
                        "case_id": case["case_id"],
                        "model": model,
                        "model_digest": digest,
                        "regime": regime,
                        "language": args.language,
                        "repeat": repeat,
                        "temperature": args.temperature,
                        "seed": args.seed + repeat - 1,
                        "generated_at": datetime.now(timezone.utc).isoformat(),
                        "response": result.get("response", "").strip(),
                        "done_reason": result.get("done_reason"),
                        "eval_count": result.get("eval_count"),
                    }
                    with args.output.open("a") as f:
                        f.write(json.dumps(row, ensure_ascii=False) + "\n")
                    print(f"generated {rid} {model} {regime} {case['case_id']}", flush=True)

    total = sum(1 for line in args.output.read_text().splitlines() if line.strip())
    print(f"PASS: {total} generations stored at {args.output}")


if __name__ == "__main__":
    main()
