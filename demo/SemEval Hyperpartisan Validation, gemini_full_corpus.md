# SemEval Hyperpartisan Validation — Gemini Full Corpus

**Platform:** Google Gemini
**Corpus:** 7 articles from the SemEval-2023 Task 3 hyperpartisan set
**Date:** 2026-03-28
**Engine:** v2.0.0 (Python kernel) + Gemini signal estimation
**Workbook reference:** v2.1

Of the 7 articles, Gemini classifies 6 as `clean` and 1 as `evasion`.
The single non-clean classification is Article 1, which GPT o3 classifies
as `moral_framing` instead. See `article_01_divergent_case.md` for the
side-by-side analysis.

---

## Document 1: How Long, America? (CounterPunch)

**Section A — Five-sentence audit snapshot**
The text operates as a polemic within an editorial advocacy context. The logic classification is **evasion** because Gate 1 fired due to multiple deflections and dismissals blocking contestation. The discourse maps to Q4 with coordinates X = +5.0, Y = -4.0, and an intensity of 4.5. Authority laundering flags include **identity_laundering**, indicating a defensive_routine learning posture. The structure functions as an immunizing_stratagem; measures are estimated.

**Section B — One-line logic result**
Logic flaws detected: evasion via Gate 1 — evasion_count >= 2.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · · ·
STAB <---- · · + · · ----> DISR
           · · · ★ ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +5.0, driven by a high density of disruption cues reflecting narratives of collapse and catastrophe.
Y = -4.0, indicating a heart-coded emotional register focused on moral threat and outrage over technical analysis.
Intensity = 4.5/10, demonstrating moderate commitment to this specific rhetorical posture.

---

## Document 2: NRCC's Sneak Preview of 2014 (FactCheck.org)

**Section A — Five-sentence audit snapshot**
The text operates as institutional discourse within a political fact-checking context. The logic classification is **clean** because no bias gate fired, relying on verifiable evaluations rather than moralized framing or structural evasion. The discourse maps to Q1 with coordinates X = 0.0, Y = +2.0, and an intensity of 1.4. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · ★ · ·     Q2
           · · · · ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = 0.0, representing a neutral stance on the disruption-to-stability axis that favors neither institutional preservation nor radical change.
Y = +2.0, indicating a mild head-coded register driven by analytical and evidentiary vocabulary over affect.
Intensity = 1.4/10, reflecting a low commitment to structural intensity typical of objective reporting.

---

## Document 3: Lagarde: IMF can Cooperate with Trump (Fox Business / Reuters)

**Section A — Five-sentence audit snapshot**
The text operates as a PR statement within an international institutional news context. The logic classification is **clean** because no bias gate fired, keeping prescriptive language below thresholds and avoiding systemic vagueness. The discourse maps to Q1 with coordinates X = -2.0, Y = +1.0, and an intensity of 1.6. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · ★ · · ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -2.0, driven by a stability-leaning posture emphasizing cooperation, order, and systemic preservation.
Y = +1.0, indicating a slightly head-coded register focused on procedural outcomes rather than emotive appeals.
Intensity = 1.6/10, showing low overall structural intensity.

---

## Document 4: Where is Apple's 'Next Big Thing'? (Fox Business / BGR)

**Section A — Five-sentence audit snapshot**
The text operates as corporate risk disclosure within an editorial analysis context. The logic classification is **clean** because no bias gate fired, avoiding totalizing group attributions or unfalsifiable claims. The discourse maps to Q2 with coordinates X = +1.0, Y = +1.5, and an intensity of 1.3. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · ★ ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +1.0, indicating a slight disruption-leaning posture focused on market changes and product shifts.
Y = +1.5, reflecting a head-coded register that utilizes financial, analytic, and strategic vocabulary.
Intensity = 1.3/10, representing low structural intensity typical of market commentary.

---

## Document 5: Staples says it's closing 60 stores (GlobalPost / The World from PRX)

**Section A — Five-sentence audit snapshot**
The text operates as institutional discourse within a corporate news reporting context. The logic classification is **clean** because no bias gate fired, presenting verifiable operational data without moralization. The discourse maps to Q2 with coordinates X = +3.0, Y = +2.0, and an intensity of 2.5. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · ★ ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +3.0, driven by a disruption-leaning narrative focused on closures, cuts, and structural overhauls.
Y = +2.0, indicating a head-coded register heavily reliant on quantitative and procedural measurements.
Intensity = 2.5/10, indicating a low-to-moderate commitment to this specific rhetorical frame.

---

## Document 6: How schools in Brazil are teaching kids to eat their vegetables (PRX)

**Section A — Five-sentence audit snapshot**
The text operates as institutional discourse within a policy reporting context. The logic classification is **clean** because no bias gate fired, maintaining a descriptive rather than prescriptive posture. The discourse maps to Q1 with coordinates X = -2.0, Y = +0.5, and an intensity of 1.5. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · ★ · · ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -2.0, reflecting a stability-leaning focus on building enduring programmatic traditions and institutional norms.
Y = +0.5, indicating a slightly head-coded register analyzing methodologies and educational mechanisms.
Intensity = 1.5/10, showing low intensity typical of feature reporting.

---

## Document 7: Public schools paid for private school crossing guard (Associated Press)

**Section A — Five-sentence audit snapshot**
The text operates as institutional discourse within an investigative news context. The logic classification is **clean** because no bias gate fired, as the text describes a local administrative decision without structural evasion or universal claims. The discourse maps to Q1 with coordinates X = -1.0, Y = +0.8, and an intensity of 0.9. Authority laundering flags include none, indicating an open_loop_reasoning learning posture. The structure functions as a falsifiable_claim_structure; measures are estimated.

**Section B — One-line logic result**
Logic type used: clean claim structure — no bias gate fired.

**Section C — Spectrograph**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · ★ · ·
STAB <---- · · + · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -1.0, leaning mildly toward stability by referencing administrative compliance, routine budgets, and longstanding arrangements.
Y = +0.8, reflecting a subtle head-coded register via financial and procedural terminology.
Intensity = 0.9/10, resulting in a low structural intensity mapping tightly to the center.

---

## Summary Table — Gemini

| # | Article                                            | Gate     | Quadrant | Intensity |
|---|----------------------------------------------------|----------|----------|-----------|
| 1 | How Long, America?                                 | evasion  | Q4       | 4.5       |
| 2 | NRCC's Sneak Preview of 2014                       | clean    | Q1       | 1.4       |
| 3 | Lagarde: IMF can Cooperate with Trump              | clean    | Q1       | 1.6       |
| 4 | Where is Apple's 'Next Big Thing'?                 | clean    | Q2       | 1.3       |
| 5 | Staples says it's closing 60 stores                | clean    | Q2       | 2.5       |
| 6 | How schools in Brazil teach kids to eat vegetables | clean    | Q1       | 1.5       |
| 7 | Public schools paid for private school guard       | clean    | Q1       | 0.9       |
