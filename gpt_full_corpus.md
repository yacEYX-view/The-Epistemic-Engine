# SemEval Hyperpartisan Validation — GPT o3 Full Corpus

**Platform:** OpenAI GPT o3
**Corpus:** 7 articles from the SemEval-2023 Task 3 hyperpartisan set
**Date:** 2026-03-28
**Engine:** v2.0.0 (Python kernel) + GPT o3 signal estimation
**Workbook reference:** v2.1

Of the 7 articles, GPT classifies 6 as `clean` and 1 as `moral_framing`.
The single non-clean classification is Article 1, which Gemini classifies
as `evasion` instead. See `article_01_divergent_case.md` for the side-by-side.

---

## Audit 1 — "How Long, America?"

**A) AUDIT SNAPSHOT**
The text plays a polemic, editorial-advocacy language game.
Bias gate classification: **moral_framing** (Gate 3) — heavy virtue/vice labeling drives the argument.
The discourse sits in Q4 at approximately (+6 DISR, -7 HEART) with intensity ≈ 5/10.
Authority-laundering flags: none detected; learning posture: open_loop_reasoning.
Testability label: immunizing_stratagem. Measures are estimated.

**B) LOGIC RESULT**
Logic flaws detected: moral_framing via Gate 3 — persuasive moral language overrides testability.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · · ·
STAB <---- · · · · · ----> DISR
           · · ★ · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +6 (disruption tilt from "Black Swan," "collapse"), Y = -7 (heart dominance from outrage vocabulary), Intensity ≈ 5/10 (moderate commitment).

---

## Audit 2 — "NRCC's Sneak Preview of 2014"

**A) AUDIT SNAPSHOT**
The article functions as fact-checking editorial advocacy within an institutional language game.
Bias gate classification: **clean** (no gate fired).
Position Q1 (-1 STAB, +2 HEAD), intensity ≈ 1.5/10.
Authority-laundering flags: none; learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · ★ · · ·     Q2
           · · · · ·
STAB <---- · · · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -1 (slight stability from procedural vote lists), Y = +2 (head emphasis through analytic correction), Intensity ≈ 1.5/10 (low).

---

## Audit 3 — "Lagarde: IMF can Cooperate with Trump..."

**A) AUDIT SNAPSHOT**
This is a diplomatic press-conference statement (PR / policy-defense blend).
Bias gate classification: **clean**.
Near-centre CLEAN zone (+0 DISR, +1 HEAD), intensity ≈ 0.7/10.
Authority-laundering flags: none; learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · · ★ · ·     Q2
           · · · · ·
STAB <---- · · · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X ≈ 0, Y ≈ +1, Intensity ≈ 0.7/10 (low).

---

## Audit 4 — "Where is Apple's 'Next Big Thing'?"

**A) AUDIT SNAPSHOT**
Market-analysis commentary framed as investor guidance (institutional discourse).
Bias gate classification: **clean**.
Quadrant Q2 (+2 DISR, +1 HEAD), intensity ≈ 1/10.
Authority-laundering flags: scientism not triggered (numeric content is contextual); learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · ★ · ·
STAB <---- · · · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +2 (disruption cues around "revive," "launch"), Y = +1 (head tilt from analyst reasoning), Intensity ≈ 1/10.

---

## Audit 5 — "Staples says it's closing 60 stores..."

**A) AUDIT SNAPSHOT**
Straight business news (institutional discourse, corporate restructuring report).
Bias gate classification: **clean**.
Quadrant Q2 (+1 DISR, +1 HEAD), intensity ≈ 0.9/10.
Authority-laundering flags: none; learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · ★ · ·
STAB <---- · · · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = +1, Y = +1, Intensity ≈ 0.9/10.

---

## Audit 6 — "How schools in Brazil are teaching kids to eat their vegetables"

**A) AUDIT SNAPSHOT**
Human-interest feature with public-health framing (institutional discourse).
Bias gate classification: **clean**.
Quadrant Q3 (-1 STAB, -2 HEART), intensity ≈ 1.2/10.
Authority-laundering flags: none; learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · · ·
STAB <---- · ★ · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -1 (slight stability via tradition-school context), Y = -2 (heart emphasis on children's health), Intensity ≈ 1.2/10.

---

## Audit 7 — "Public schools paid for private school crossing guard"

**A) AUDIT SNAPSHOT**
Brief local-accountability report (institutional discourse).
Bias gate classification: **clean**.
Near-centre CLEAN zone (-1 STAB, 0 HEAD), intensity ≈ 0.5/10.
Authority-laundering flags: none; learning posture: open_loop_reasoning.
Testability label: falsifiable_claim_structure. Measures are estimated.

**B) LOGIC RESULT**
Logic type used: clean claim structure — no bias gate fired.

**C) SPECTROGRAPH**
```
        HEAD (+)
           |
    Q1     · ★ · · ·     Q2
           · · · · ·
STAB <---- · · · · · ----> DISR
           · · · · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)
```
X = -1, Y ≈ 0, Intensity ≈ 0.5/10 (very low).

---

## Summary Table — GPT o3

| # | Article                                            | Gate          | Quadrant | Intensity |
|---|----------------------------------------------------|---------------|----------|-----------|
| 1 | How Long, America?                                 | moral_framing | Q4       | 5.0       |
| 2 | NRCC's Sneak Preview of 2014                       | clean         | Q1       | 1.5       |
| 3 | Lagarde: IMF can Cooperate with Trump              | clean         | CLEAN    | 0.7       |
| 4 | Where is Apple's 'Next Big Thing'?                 | clean         | Q2       | 1.0       |
| 5 | Staples says it's closing 60 stores                | clean         | Q2       | 0.9       |
| 6 | How schools in Brazil teach kids to eat vegetables | clean         | Q3       | 1.2       |
| 7 | Public schools paid for private school guard       | clean         | CLEAN    | 0.5       |
