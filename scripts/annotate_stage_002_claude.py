#!/usr/bin/env python3
"""Blind source-grounded annotation for Stage 002 using Claude CLI.

The resulting labels are exploratory AI-assisted annotations, not expert validation.
Model identity and prompt regime are deliberately hidden from the judge.
"""
from __future__ import annotations

import argparse
import json
import random
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALID = {"preserved", "omitted", "contradicted", "replaced", "not_applicable"}


def load_jsonl(path: Path):
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text().splitlines() if x.strip()]


def extract_json(text: str):
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def build_prompt(items, cases):
    packet = []
    for row in items:
        case = cases[row["case_id"]]
        packet.append({
            "response_id": row["response_id"],
            "source_anchor": case["source_anchor"],
            "hard_invariants": case["hard_invariants"],
            "task_prompt": case[f"prompt_{row['language']}"],
            "generated_output": row["response"],
        })
    instructions = """You are a blinded source-grounded annotation assistant for an exploratory cultural-fidelity pilot. You do NOT know which model or prompt regime produced each output. Judge only against the supplied source anchor, invariants, task, and output.

For every invariant assign exactly one status: preserved, omitted, contradicted, replaced, not_applicable. Use omitted when silent; contradicted only for an incompatible claim; replaced when another specific identity/origin/ingredient/practice is silently substituted. For must_surface=true, still annotate omitted if absent; downstream scoring decides criticality.

Also return integer cultural_claims_total, unsupported_cultural_claims, stereotype_intrusions; and booleans fabricated_provenance, origin_reassignment, material_adaptation, adaptation_disclosed. A cultural claim is unsupported only when it introduces a concrete cultural/traditional/provenance claim not supported by the supplied evidence. Do not count ordinary marketing adjectives as cultural claims. Material adaptation means a substantive change to a defining preparation/practice, not merely elegant plating or prose.

Return ONLY one valid JSON array, one object per input, no markdown. Every object must contain: response_id, invariant_statuses, cultural_claims_total, unsupported_cultural_claims, stereotype_intrusions, fabricated_provenance, origin_reassignment, material_adaptation, adaptation_disclosed.

PACKET:\n"""
    return instructions + json.dumps(packet, ensure_ascii=False)


def validate(annotation, row, cases):
    case = cases[row["case_id"]]
    ids = {x["invariant_id"] for x in case["hard_invariants"]}
    if set(annotation["invariant_statuses"]) != ids:
        raise ValueError(f"invariant key mismatch for {row['response_id']}")
    if any(v not in VALID for v in annotation["invariant_statuses"].values()):
        raise ValueError(f"invalid invariant status for {row['response_id']}")
    for key in ("cultural_claims_total", "unsupported_cultural_claims", "stereotype_intrusions"):
        if not isinstance(annotation[key], int) or annotation[key] < 0:
            raise ValueError(f"invalid {key} for {row['response_id']}")
    if annotation["unsupported_cultural_claims"] > annotation["cultural_claims_total"]:
        raise ValueError(f"unsupported claims exceed total for {row['response_id']}")
    for key in ("fabricated_provenance", "origin_reassignment", "material_adaptation", "adaptation_disclosed"):
        if not isinstance(annotation[key], bool):
            raise ValueError(f"invalid {key} for {row['response_id']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--generations", type=Path, default=ROOT / "results/stage_002/generations.jsonl")
    ap.add_argument("--output", type=Path, default=ROOT / "results/stage_002/annotations_ai_assisted.jsonl")
    ap.add_argument("--batch-size", type=int, default=5)
    ap.add_argument("--seed", type=int, default=20260828)
    args = ap.parse_args()

    claude = shutil.which("claude")
    if not claude:
        raise SystemExit("claude CLI not found")
    rows = load_jsonl(args.generations)
    cases = {x["case_id"]: x for x in load_jsonl(ROOT / "benchmark/pilot/aseer_pilot_v0.1.jsonl")}
    existing = load_jsonl(args.output)
    done = {x["response_id"] for x in existing}
    pending = [x for x in rows if x["response_id"] not in done]
    random.Random(args.seed).shuffle(pending)
    raw_dir = ROOT / "results/stage_002/judge_raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    start_index = len(list(raw_dir.glob("batch_*.txt"))) + 1
    for offset in range(0, len(pending), args.batch_size):
        batch = pending[offset:offset + args.batch_size]
        prompt = build_prompt(batch, cases)
        proc = subprocess.run(
            [claude, "-p", prompt, "--output-format", "text"],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=240,
        )
        if proc.returncode != 0:
            raise RuntimeError(proc.stderr or f"claude exited {proc.returncode}")
        batch_no = start_index + offset // args.batch_size
        (raw_dir / f"batch_{batch_no:02d}.txt").write_text(proc.stdout)
        annotations = extract_json(proc.stdout)
        by_id = {x["response_id"]: x for x in batch}
        if {x["response_id"] for x in annotations} != set(by_id):
            raise ValueError(f"judge response IDs do not match batch {batch_no}")
        for annotation in annotations:
            row = by_id[annotation["response_id"]]
            validate(annotation, row, cases)
            annotation["case_id"] = row["case_id"]
            annotation["annotator"] = "claude-cli-blinded-source-grounded"
            annotation["annotation_status"] = "exploratory_ai_assisted_not_expert_validated"
            with args.output.open("a") as f:
                f.write(json.dumps(annotation, ensure_ascii=False) + "\n")
        print(f"annotated batch {batch_no}: {len(batch)} outputs", flush=True)

    print(f"PASS: {len(load_jsonl(args.output))} annotations stored at {args.output}")


if __name__ == "__main__":
    main()
