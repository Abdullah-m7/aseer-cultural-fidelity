# Stage 002 preflight note

The first 20-output generation run used a 220-token ceiling. Before annotation, termination metadata showed 17/20 outputs ended because of the length ceiling. This creates an unacceptable omission confound for CCDR.

No semantic annotations or aggregate cultural-fidelity outcomes had been produced when this was detected. The raw preflight is retained as `preflight/generations_220_truncated.jsonl`; it is excluded from Stage 002A analysis. The analysis run uses a 512-token ceiling.
