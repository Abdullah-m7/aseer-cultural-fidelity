#!/usr/bin/env python3
"""Integrity gate for the Stage 003 pre-expert / pre-generation freeze."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HELDOUT = ROOT / "benchmark/heldout/aseer_heldout_v0.1.jsonl"
WORKSHEET = ROOT / "expert_review/calibration_worksheet_v0.1.csv"
MANIFEST = ROOT / "expert_review/FREEZE_MANIFEST_V0.1.json"
SOURCE_REGISTRY = ROOT / "references/sources.yaml"
EXPECTED_HELDOUT = 6
EXPECTED_REVIEW_CASES = {
    "ACF-FOOD-001",
    "ACF-FOOD-002",
    "ACF-TOUR-001",
    "ACF-ART-001",
    "ACF-ARCH-001",
}
RESPONSE_COLUMNS = {
    "source_adequacy",
    "invariant_verdict",
    "must_surface_verdict",
    "severity_if_violated",
    "missing_nuance_or_note",
}
ALLOWED_BASES = {"source_fact", "source_interpretation", "adaptation_boundary"}
EXPECTED_BASE_MAIN_SHA = "6149ca6e25f633a2ae415c31ca72abc4a6e1a430"


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    pilot = load_jsonl(ROOT / "benchmark/pilot/aseer_pilot_v0.1.jsonl")
    heldout = load_jsonl(HELDOUT)
    if len(heldout) != EXPECTED_HELDOUT:
        fail(f"expected {EXPECTED_HELDOUT} held-out cases; got {len(heldout)}")

    pilot_ids = {row["case_id"] for row in pilot}
    heldout_ids = [row["case_id"] for row in heldout]
    if len(set(heldout_ids)) != EXPECTED_HELDOUT:
        fail("held-out case IDs are not unique")
    if pilot_ids & set(heldout_ids):
        fail(f"pilot/held-out case-ID overlap: {sorted(pilot_ids & set(heldout_ids))}")

    source_ids = set(re.findall(r"^\s+- id:\s*([^\s]+)\s*$", SOURCE_REGISTRY.read_text(), re.MULTILINE))
    missing_sources = sorted({row["source"]["source_id"] for row in heldout} - source_ids)
    if missing_sources:
        fail(f"held-out source IDs absent from source registry: {missing_sources}")

    for row in heldout:
        if len(row["hard_invariants"]) < 2:
            fail(f"{row['case_id']} has fewer than two hard invariants")
        if not any(item["must_surface"] for item in row["hard_invariants"]):
            fail(f"{row['case_id']} has no task-specific must-surface invariant")
        if "model" in row or "response" in row or "annotation" in row:
            fail(f"{row['case_id']} contains post-generation fields")

    with WORKSHEET.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        fail("expert worksheet is empty")
    if set(rows[0]) < RESPONSE_COLUMNS:
        fail("expert worksheet is missing response columns")
    if {row["case_id"] for row in rows} != EXPECTED_REVIEW_CASES:
        fail("expert worksheet case set differs from the frozen five-case subset")
    if len(rows) != 15:
        fail(f"expected 15 invariant rows in expert worksheet; got {len(rows)}")
    if "proposed_basis" not in rows[0]:
        fail("expert worksheet is missing proposed_basis")
    for row in rows:
        if row["proposed_basis"] not in ALLOWED_BASES:
            fail(f"invalid proposed_basis for {row['case_id']}:{row['invariant_id']}: {row['proposed_basis']}")
        if any(row[col].strip() for col in RESPONSE_COLUMNS):
            fail("v0.1 expert worksheet already contains reviewer responses")

    result_dir = ROOT / "results/stage_003"
    if result_dir.exists() and any(result_dir.rglob("*")):
        fail("Stage 003 result artifacts exist before expert calibration freeze")

    manifest = json.loads(MANIFEST.read_text())
    if manifest.get("freeze_status") != "pre-expert_pre-generation":
        fail("freeze manifest has unexpected status")
    if manifest.get("base_main_sha") != EXPECTED_BASE_MAIN_SHA:
        fail(f"freeze manifest base_main_sha mismatch: {manifest.get('base_main_sha')}")
    if manifest.get("heldout_generation_count") != 0 or manifest.get("expert_response_count") != 0:
        fail("freeze manifest must record zero held-out generations and zero expert responses")
    for relpath, expected_hash in manifest.get("files", {}).items():
        path = ROOT / relpath
        if not path.exists():
            fail(f"manifest file missing: {relpath}")
        actual = digest(path)
        if actual != expected_hash:
            fail(f"freeze hash mismatch for {relpath}: expected {expected_hash}, got {actual}")

    print("PASS: Stage 003 pre-expert integrity gate")
    print(f"  heldout_cases={len(heldout)} unique_and_disjoint_from_stage001_pilot")
    print(f"  expert_subset_cases={len(EXPECTED_REVIEW_CASES)} invariant_rows={len(rows)}")
    basis_counts = {basis: sum(row["proposed_basis"] == basis for row in rows) for basis in sorted(ALLOWED_BASES)}
    print("  reviewer_response_cells=blank")
    print(f"  invariant_basis_counts={basis_counts}")
    print("  heldout_generation_artifacts=none")
    print(f"  freeze_manifest_files={len(manifest['files'])} hashes_match")
    print(f"  freeze_base_main_sha={manifest['base_main_sha']}")


if __name__ == "__main__":
    main()
