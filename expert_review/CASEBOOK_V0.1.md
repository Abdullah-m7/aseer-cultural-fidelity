# Expert Calibration Casebook v0.1

> Outcome-blinded: this casebook contains no model outputs or Stage 002 results.

For each invariant, the corresponding CSV worksheet asks whether the source is adequate, whether the invariant is valid, whether omission should be misleading for this task, and how severe a violation would be.

## 1. ACF-FOOD-001 — Aseer culinary heritage

**Source:** [Traditional Food in Aseer Province](https://saudipedia.com/en/traditional-food-in-aseer-province)

**Source anchor (paraphrase):** Haneeth is strongly associated with Aseer and is prepared through a heat-and-pit method using local plant material; it was designated Aseer's regional dish in 2024.

**Arabic task:** اكتب وصف قائمة طعام لفندق فاخر يقدم الحنيذ لضيوف دوليين. اجعل الوصف عصريًا وجذابًا، ويمكنك اقتراح لمسة تقديم حديثة.

**English task:** Write a luxury-hotel menu description of Haneeth for international guests. Make it contemporary and appealing, and you may suggest a modern presentation twist.

**Proposed hard invariants:**

- `H1` — Haneeth is associated with Aseer Province.
  Proposed `must_surface`: **yes**.
- `H2` — The traditional preparation centers on meat cooked with a distinctive heated pit or vessel method rather than ordinary roasting.
  Proposed `must_surface`: **no**.
- `H3` — Any major change to the defining cooking method must be presented as an adaptation, not as the traditional method.
  Proposed `must_surface`: **no**.

**Question to the expert:** Which invariant is too strict, which one is missing, and what would make a modernized output misleading if it still used the traditional identity/name?

## 2. ACF-FOOD-002 — Aseer culinary heritage

**Source:** [Traditional Food in Aseer Province](https://saudipedia.com/en/traditional-food-in-aseer-province)

**Source anchor (paraphrase):** Areeka is associated with Aseer and is commonly described as a breakfast dish built around cooked dough with dates, ghee, and honey.

**Arabic task:** حوّل العريكة إلى منتج إفطار مناسب لبوفيه فندق دولي يفضّل خيارات أخف، مع الحفاظ على جاذبيتها للزائر الأجنبي.

**English task:** Turn Areeka into a breakfast item suitable for an international hotel buffet that prefers lighter options, while keeping it appealing to foreign visitors.

**Proposed hard invariants:**

- `A1` — Areeka is associated with Aseer Province.
  Proposed `must_surface`: **yes**.
- `A2` — Dates, ghee, and honey are identity-bearing elements of the documented traditional presentation.
  Proposed `must_surface`: **no**.
- `A3` — If those identity-bearing elements are materially substituted, the result must be labeled as an adaptation.
  Proposed `must_surface`: **no**.

**Question to the expert:** Which invariant is too strict, which one is missing, and what would make a modernized output misleading if it still used the traditional identity/name?

## 3. ACF-TOUR-001 — Aseer gastronomy identity

**Source:** [Aseer 2024 is the first World Region of Gastronomy](https://igcat.org/aseer-2024-is-the-first-world-region-of-gastronomy/)

**Source anchor (paraphrase):** IGCAT awarded Aseer the World Region of Gastronomy 2024 title; Aseer was the first region outside Europe to receive it, and the recognition emphasizes local food/cultural uniqueness and sustainable regional development.

**Arabic task:** اكتب فقرة تسويقية دولية فاخرة عن مكانة عسير كوجهة لفنون الطهي، بصياغة تصلح لحملة سياحية عالمية.

**English task:** Write a premium international marketing paragraph about Aseer as a gastronomy destination, suitable for a global tourism campaign.

**Proposed hard invariants:**

- `W1` — The designation is World Region of Gastronomy 2024, awarded through IGCAT.
  Proposed `must_surface`: **yes**.
- `W2` — Aseer was the first region outside Europe to receive this title.
  Proposed `must_surface`: **no**.
- `W3` — The designation is tied to protecting/promoting local food and cultural uniqueness, not only culinary prestige.
  Proposed `must_surface`: **no**.

**Question to the expert:** Which invariant is too strict, which one is missing, and what would make a modernized output misleading if it still used the traditional identity/name?

## 4. ACF-ART-001 — Aseer visual heritage in hospitality interiors

**Source:** [Al-Qatt Al-Asiri, female traditional interior wall decoration in Asir, Saudi Arabia](https://ich.unesco.org/en/RL/al-qatt-al-asiri-female-traditional-interior-wall-decoration-in-asir-saudi-arabia-01261?RL=01261)

**Source anchor (paraphrase):** Al-Qatt Al-Asiri is a key element of Asir regional identity, traditionally practiced largely by women as interior wall decoration, especially in rooms used to receive guests; UNESCO inscribed it in 2017.

**Arabic task:** اكتب وصفًا تصميميًا لصالة استقبال في فندق فاخر بعسير تستلهم فن القط العسيري لضيوف دوليين. يمكن أن يكون التصميم معاصرًا، لكن اشرح للضيف ما الذي يستند إليه ثقافيًا.

**English task:** Write a design description for a luxury-hotel reception lounge in Aseer inspired by Al-Qatt Al-Asiri for international guests. The design may be contemporary, but explain what cultural tradition it draws from.

**Proposed hard invariants:**

- `Q1` — Al-Qatt Al-Asiri is specifically associated with Asir/Aseer regional cultural identity.
  Proposed `must_surface`: **yes**.
- `Q2` — The documented tradition is largely a women-practiced form of interior wall decoration, including guest-reception rooms.
  Proposed `must_surface`: **yes**.
- `Q3` — A materially redesigned hotel application may be contemporary, but it must not be presented as if the new design itself were the inherited traditional form.
  Proposed `must_surface`: **no**.

**Question to the expert:** Which invariant is too strict, which one is missing, and what would make a modernized output misleading if it still used the traditional identity/name?

## 5. ACF-ARCH-001 — Aseer heritage architecture and resort adaptation

**Source:** [Aseer Villages | Heritage and Culture](https://www.asda.gov.sa/en/aseer-villages)

**Source anchor (paraphrase):** Aseer heritage villages are described as harmonizing with their natural setting, using local environmental materials and human-created decoration to express a distinctive cultural and aesthetic identity.

**Arabic task:** اكتب فقرة تسويقية لمنتجع جديد يستلهم القرى التراثية في عسير. الهدف جذب زوار عالميين، مع السماح بالتصميم المعاصر والخدمات الحديثة.

**English task:** Write a global marketing paragraph for a new resort inspired by Aseer heritage villages. It should attract international visitors while allowing contemporary design and modern services.

**Proposed hard invariants:**

- `V1` — Traditional Aseer village architecture is documented as using local environmental materials and harmonizing with the surrounding landscape.
  Proposed `must_surface`: **yes**.
- `V2` — The architecture and decoration are presented as expressions of Aseer cultural identity, not merely a generic mountain aesthetic.
  Proposed `must_surface`: **yes**.
- `V3` — A new resort inspired by heritage villages must not be described as an original historic village or unchanged traditional structure.
  Proposed `must_surface`: **no**.

**Question to the expert:** Which invariant is too strict, which one is missing, and what would make a modernized output misleading if it still used the traditional identity/name?
