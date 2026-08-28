# Expert Validation Protocol v0.1

## Purpose

Domain experts should validate the benchmark **before** their judgments are used to compare models. The goal is not to ask whether an item feels authentic in the abstract; it is to test whether the benchmark has encoded the right source-grounded constraints and the right boundary between preservation and legitimate adaptation.

## What the expert sees

For each case:

1. source title and link;
2. short paraphrased source anchor;
3. proposed hard invariants;
4. which invariants are marked `must_surface`;
5. proposed transformation prompt;
6. listed distortion triggers.

No model output is needed for the first validation pass.

## Five judgments per case

### 1. Source adequacy

Is the source credible and sufficiently specific for the claim being encoded?

- `adequate`
- `needs_supplement`
- `unsuitable`

### 2. Invariant validity

For each hard invariant:

- `valid_as_written`
- `too_strict`
- `too_broad`
- `incorrect`
- `needs_local_nuance`

### 3. Must-surface decision

Would omission of this invariant make the requested output culturally misleading, or merely less informative?

This is important because the benchmark should not convert every omission into a serious error.

### 4. Adaptation boundary

Can the requested modernization/localization be legitimately performed while still using the traditional name? If yes, what disclosure is needed? If no, what label should a transformed version use?

### 5. Missing distortion mode

What locally obvious mistake could a fluent outsider/model make that the current triggers fail to capture?

## Expert-facing workload

The first review should use only 5–10 cases and target roughly 20–30 minutes. The purpose is to expose bad assumptions early, not to impose a large annotation burden.

## How feedback changes the benchmark

Every expert-driven change should be logged as one of:

- source correction;
- invariant correction;
- `must_surface` change;
- prompt correction;
- new distortion trigger;
- case deletion because the construct is ambiguous.

The repository should preserve the pre- and post-review versions so expert input is auditable.

## Research-ethics boundary

Informal methodological consultation and research data collection are not automatically the same activity. If expert judgments, identities, quotes, or identifiable responses will be analyzed and reported as study data, the project should obtain the appropriate ethics/IRB determination for the researchers' institutional context before data collection. Until then, expert outreach should be framed as design consultation and should avoid collecting unnecessary personal data.

## Ideal first expert question

Instead of asking “What do you think of the project?”, ask:

> We defined these three details as identity-bearing for this transformation. Which one is too strict, which one is missing, and what change would make a modernized version misleading if it were still presented as traditional?

That produces actionable scientific feedback and makes the expert's contribution substantive.
