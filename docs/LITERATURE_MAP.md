# Literature Map — Stage 001

This is a **targeted map**, not yet a systematic review. Its purpose is to prevent reinvention and to sharpen the project's empirical gap.

## A. Cultural values and alignment

### Tao et al. — Cultural bias and cultural alignment of large language models
PNAS Nexus (2024). DOI: 10.1093/pnasnexus/pgae346

Uses nationally representative value surveys to audit cultural bias and tests cultural prompting as an alignment intervention. Important precedent for disaggregated cultural evaluation, but the target is value alignment rather than source-preserving transformation of a cultural artifact or practice.

### AlKhamissi et al. — Investigating Cultural Alignment of Large Language Models
ACL 2024. DOI: 10.18653/v1/2024.acl-long.671

Shows that language and pretraining mix affect cultural alignment when models simulate survey respondents. Relevant to our bilingual experimental conditions.

### Masoud et al. — Cultural Alignment in Large Language Models
COLING 2025.

Introduces a Cultural Alignment Test based on Hofstede dimensions. Relevant as another example of operationalizing culture through latent value dimensions.

### MENAValues — I Am Aligned, But With Whom?
Preprint (2025).

Evaluates MENA values across languages and perspective framings and reports cross-lingual shifts. Relevant because our protocol treats language as a possible intervention rather than a neutral wrapper.

## B. Cultural knowledge benchmarks

### CDEval
C3NLP 2024.

Evaluates cultural dimensions across domains. It establishes that cultural competence needs dedicated evaluation beyond general alignment.

### CulturalBench
ACL 2025.

Human-written and human-verified cultural knowledge questions spanning many global regions. Particularly important because it demonstrates the need for human/domain validation of culturally specific items.

### FrameNet-Cultures
Findings of ACL 2026.

Moves beyond closed-form questionnaires toward cross-cultural frame semantics. This reduces confidence in any claim that “non-survey cultural evaluation” is itself novel; our gap must therefore be defined more specifically around source-anchored transformation drift.

## C. Saudi-specific benchmarks

### SaudiCulture
Ayash et al. (2025).

Evaluates Saudi cultural competence across geographic regions and cultural domains including food, clothing, celebrations, and crafts. This is the nearest obvious benchmark-level neighbor. Its presence means this project should **not** pitch itself as the first Saudi regional culture benchmark.

### Saudi-Alignment Benchmark
ArabicNLP 2025.

Contains 874 manually curated questions covering Saudi cultural/ethical norms and domain knowledge. It further establishes that static Saudi knowledge and norm alignment are already active research areas.

## D. Why the working gap still appears plausible

The nearest prior work largely asks variants of:

- Does the model know the right cultural fact?
- Do its values align with a population or region?
- Does language change its cultural response?
- Can it choose or generate the culturally appropriate answer?

Our intended intervention is different:

1. provide a source-grounded cultural object or fact set;
2. require an applied transformation such as translation, luxury adaptation, destination marketing, or concierge synthesis;
3. define hard invariants and allowed adaptation space **before** generation;
4. measure whether the transformation itself induces contradiction, replacement, false provenance, unsupported additions, or non-transparent reinterpretation.

The distinction is between **knowledge competence** and **transformation integrity**.

## E. Aseer / gastronomy context

### IGCAT — Aseer 2024 is the first World Region of Gastronomy
IGCAT documents Aseer as the first region outside Europe to receive the World Region of Gastronomy title and explicitly links the recognition to protecting local food and cultural uniqueness, sustainability, heritage, and innovation.

Source: https://igcat.org/aseer-2024-is-the-first-world-region-of-gastronomy/

### Saudipedia — Traditional Food in Aseer Province
Provides a source-grounded overview of Aseer dishes, ingredients, preparation practices, and the regional designation of Haneeth.

Source: https://saudipedia.com/en/traditional-food-in-aseer-province

### Visit Saudi — Popular Cuisine in Abha
Official tourism-facing material that describes Aseer/Abha dishes for visitors. It is useful for comparing heritage description with tourism communication.

Source: https://www.visitsaudi.com/en/aseer/stories/traditional-dishes-and-flavors-of-abha

### King Khalid University — Food Gifts 2026
The College of Tourism and Hospitality describes innovation in tourism food gifts while preserving Aseer heritage and cultural identity. The closing report states that evaluation included cultural/tourism value and sustainability.

Sources:
- https://www.kku.edu.sa/en/news/106642
- https://www.kku.edu.sa/en/news/106651

### Southern Saudi culinary heritage review
“Culinary heritage and innovation in Southern Saudi Arabia: Linking tradition, smart agriculture, and sustainable gastronomy within the Vision 2030 framework.” International Journal of Gastronomy and Food Science, 2026, 44, 101519. DOI: 10.1016/j.ijgfs.2026.101519

This is highly relevant background because it explicitly links heritage preservation and culinary innovation across southern Saudi Arabia.

## F. Immediate review tasks before a paper-level novelty claim

1. Search tourism and hospitality journals for generative-AI authenticity/fidelity evaluations.
2. Search cultural-heritage NLP and digital-humanities venues for transformation-preservation metrics.
3. Search food/gastronomy AI literature for recipe modernization and provenance preservation.
4. Search translation literature for culture-specific semantic preservation metrics.
5. Citation-chase SaudiCulture, Saudi-Alignment, CulturalBench, and FrameNet-Cultures.

## Provisional conclusion

There is enough adjacent work that a broad “cultural fidelity benchmark” claim would be weak. The more defensible contribution is a **source-anchored, task-induced cultural transformation benchmark** with predeclared invariants and case-level distortion rules, demonstrated in a high-value Aseer tourism/hospitality testbed.

## G. Critical tourism/hospitality adjacency identified after the first scan

The project must also distinguish itself from a fast-growing 2025–2026 tourism literature where **authenticity is already an explicit construct**.

### Shen, Chen & Xiong — Responsible generative AI in tourism
Journal of Hospitality and Tourism Management (2026). DOI: 10.1016/j.jhtm.2026.101441

Develops and validates a responsible-GenAI-in-tourism construct with authenticity among its five dimensions. This means the paper cannot claim that tourism research has ignored authenticity in GenAI. Our distinction is measurement level: source-grounded output transformations versus users' or stakeholders' perception of responsible/authentic AI.

### Yang, Leung & Xiong — Authenticity in the Age of Generative AI
Journal of Travel Research (2026). DOI: 10.1177/00472875261420609

Conceptualizes travel planning with GenAI as a co-performance of authenticity through digital host–guest relations. This is theoretically important for framing authenticity as dynamic rather than frozen.

### AI-Driven Cultural Storytelling and Tourists' Behavioral Intentions
Heritage (2026). DOI: 10.3390/heritage9020078

Studies perceived authenticity and destination image as mediators between AI-enabled cultural storytelling and tourist behavioral intentions. Again, the target is downstream human perception rather than whether the generated story preserved a declared set of source facts/invariants.

### Artificial Intelligence in Gastronomic Heritage Preservation
Heritage (2026).

Examines governance and community acceptance of AI for documenting and promoting gastronomic heritage, emphasizing authenticity, community participation, cultural identity, and risks of simplification/commodification. This is highly adjacent conceptually and strengthens the need for domain-expert validation in our design.

### Wang, Ruan & Li — AI heritage tourism interpretations and cultural memory
Journal of Hospitality and Tourism Management (2025). DOI: 10.1016/j.jhtm.2025.03.011

Tests human-versus-AI heritage interpretation effects on tourists' cultural memory. Relevant deployment context, but not a source-level integrity audit of the generated interpretation.

### Revised gap after tourism scan

The defensible gap is therefore **not** “GenAI authenticity in tourism.” That field already exists.

The sharper contribution is:

> a source-anchored audit of *what the generated cultural representation changes during an applied transformation*, using predeclared invariants, explicit allowed adaptation space, and deterministic critical-distortion rules.

This produces an output-integrity measure that can later be connected to tourism constructs such as perceived authenticity, trust, cultural memory, or behavioral intention, rather than competing with them.
