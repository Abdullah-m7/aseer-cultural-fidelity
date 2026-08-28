"""Utilities for the Stage 002 generation experiment."""
from __future__ import annotations

import hashlib
import json
import urllib.request
from typing import Any, Mapping

FIDELITY_INSTRUCTION = (
    "Preserve documented cultural provenance and identity-bearing details. "
    "Do not invent traditions, origins, ingredients, or practices. "
    "If you materially modernize or substitute something, label it clearly as an adaptation."
)


def response_id(case_id: str, model: str, regime: str, language: str, repeat: int) -> str:
    raw = f"{case_id}|{model}|{regime}|{language}|{repeat}".encode()
    return "R-" + hashlib.sha256(raw).hexdigest()[:12]


def ollama_generate(model: str, prompt: str, regime: str, *, temperature: float, seed: int, num_predict: int = 512) -> Mapping[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"temperature": temperature, "seed": seed, "num_predict": num_predict},
    }
    if regime == "fidelity-aware":
        payload["system"] = FIDELITY_INSTRUCTION
    request = urllib.request.Request(
        "http://127.0.0.1:11434/api/generate",
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.load(response)
