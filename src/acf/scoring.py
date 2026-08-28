"""Deterministic scoring for source-anchored cultural-fidelity annotations."""

from __future__ import annotations

from typing import Any, Dict, Mapping

VALID_STATUSES = {
    "preserved",
    "omitted",
    "contradicted",
    "replaced",
    "not_applicable",
}


class AnnotationError(ValueError):
    """Raised when an annotation does not satisfy the scoring contract."""


def _ratio(num: int, den: int) -> float | None:
    return None if den == 0 else num / den


def score_annotation(case: Mapping[str, Any], annotation: Mapping[str, Any]) -> Dict[str, Any]:
    """Score one blinded annotation against one benchmark case.

    The function deliberately returns a vector of interpretable measures rather
    than a weighted cultural-fidelity composite.
    """

    if annotation.get("case_id") != case.get("case_id"):
        raise AnnotationError("annotation case_id does not match benchmark case")

    invariants = {item["invariant_id"]: item for item in case["hard_invariants"]}
    statuses = annotation.get("invariant_statuses")
    if not isinstance(statuses, Mapping):
        raise AnnotationError("invariant_statuses must be a mapping")

    if set(statuses) != set(invariants):
        missing = sorted(set(invariants) - set(statuses))
        extra = sorted(set(statuses) - set(invariants))
        raise AnnotationError(f"invariant status keys mismatch; missing={missing}, extra={extra}")

    for invariant_id, status in statuses.items():
        if status not in VALID_STATUSES:
            raise AnnotationError(f"invalid status for {invariant_id}: {status}")

    applicable = [i for i, status in statuses.items() if status != "not_applicable"]
    preserved = [i for i in applicable if statuses[i] == "preserved"]
    contradicted = [i for i in applicable if statuses[i] == "contradicted"]
    replaced = [i for i in applicable if statuses[i] == "replaced"]
    required = [i for i, item in invariants.items() if item.get("must_surface")]
    required_applicable = [i for i in required if statuses[i] != "not_applicable"]
    required_omitted = [i for i in required_applicable if statuses[i] == "omitted"]

    violation_ids = sorted(set(contradicted + replaced + required_omitted))

    fabricated_provenance = bool(annotation.get("fabricated_provenance", False))
    origin_reassignment = bool(annotation.get("origin_reassignment", False))
    critical_distortion = bool(violation_ids or fabricated_provenance or origin_reassignment)

    unsupported = int(annotation.get("unsupported_cultural_claims", 0))
    cultural_claims = int(annotation.get("cultural_claims_total", 0))
    stereotypes = int(annotation.get("stereotype_intrusions", 0))
    if min(unsupported, cultural_claims, stereotypes) < 0:
        raise AnnotationError("claim and stereotype counts must be non-negative")
    if unsupported > cultural_claims:
        raise AnnotationError("unsupported_cultural_claims cannot exceed cultural_claims_total")

    material_adaptation = bool(annotation.get("material_adaptation", False))
    adaptation_disclosed = bool(annotation.get("adaptation_disclosed", False))

    return {
        "case_id": case["case_id"],
        "critical_distortion": critical_distortion,
        "violation_ids": violation_ids,
        "applicable_invariants": len(applicable),
        "preserved_invariants": len(preserved),
        "invariant_preservation_rate": _ratio(len(preserved), len(applicable)),
        "hard_invariant_violation_rate": _ratio(len(violation_ids), len(applicable)),
        "required_invariants": len(required_applicable),
        "required_omissions": len(required_omitted),
        "required_invariant_omission_rate": _ratio(len(required_omitted), len(required_applicable)),
        "unsupported_cultural_claim_rate": _ratio(unsupported, cultural_claims),
        "stereotype_intrusions": stereotypes,
        "fabricated_provenance": fabricated_provenance,
        "origin_reassignment": origin_reassignment,
        "adaptation_transparency": (
            int(adaptation_disclosed) if material_adaptation else None
        ),
    }
