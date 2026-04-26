# Demo: The Inter-Model Divergence on Article 1

**Article:** "How Long, America?" (CounterPunch)
**Corpus:** SemEval Hyperpartisan Validation (7 articles)
**Date:** 2026-03-28

This is the single document in the SemEval corpus where the two formal LLM
implementations of the deterministic kernel disagree. The other 6 articles are
both classified as `clean` by both platforms. Article 1 is where the structure
breaks down — and that breakdown is exactly the kind of evidence the engine
was designed to surface.

---

## GPT o3 Output

```
A) AUDIT SNAPSHOT
The text plays a polemic, editorial-advocacy language game.
Bias gate classification: moral_framing (Gate 3) — heavy virtue/vice
labeling drives the argument.
The discourse sits in Q4 at approximately (+6 DISR, -7 HEART) with
intensity ≈ 5/10.
Authority-laundering flags: none detected; learning posture: open_loop_reasoning.
Testability label: immunizing_stratagem. Measures are estimated.

B) LOGIC RESULT
Logic flaws detected: moral_framing via Gate 3 — persuasive moral
language overrides testability.

C) SPECTROGRAPH
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · · ·
STAB <---- · · · · · ----> DISR
           · · ★ · ·
    Q3     · · · · ·     Q4
           |
       HEART (-)

X = +6 (disruption tilt from "Black Swan," "collapse")
Y = -7 (heart dominance from outrage vocabulary)
Intensity ≈ 5/10 (moderate commitment)
```

---

## Gemini Output

```
Section A — Five-sentence audit snapshot
The text operates as a polemic within an editorial advocacy context.
The logic classification is evasion because Gate 1 fired due to multiple
deflections and dismissals blocking contestation.
The discourse maps to Q4 with coordinates X = +5.0, Y = -4.0, and an
intensity of 4.5.
Authority laundering flags include identity_laundering, indicating a
defensive_routine learning posture.
The structure functions as an immunizing_stratagem; measures are estimated.

Section B — One-line logic result
Logic flaws detected: evasion via Gate 1 — evasion_count >= 2.

Section C — Spectrograph
        HEAD (+)
           |
    Q1     · · · · ·     Q2
           · · · · ·
STAB <---- · · + · · ----> DISR
           · · · ★ ·
    Q3     · · · · ·     Q4
           |
       HEART (-)

X = +5.0 (disruption cues reflecting narratives of collapse and catastrophe)
Y = -4.0 (heart-coded emotional register, moral threat over technical analysis)
Intensity = 4.5/10 (moderate commitment)
```

---

## What Just Happened

Both platforms agree on the **structural shape** of the text:

| Dimension              | GPT o3                  | Gemini                  |
|------------------------|-------------------------|-------------------------|
| Language game          | polemic / editorial     | polemic / editorial     |
| Quadrant               | Q4                      | Q4                      |
| Testability            | immunizing_stratagem    | immunizing_stratagem    |
| X coordinate           | +6                      | +5.0                    |
| Y coordinate           | -7                      | -4.0                    |
| Intensity              | ≈5/10                   | 4.5/10                  |

Both place the article in the same quadrant (Q4: high disruption, heart-coded
emotional register), both label it an immunizing stratagem, both estimate
similar intensity. This is the kind of agreement the deterministic kernel is
supposed to produce.

But the **gate that fires** is different:

| Layer                  | GPT o3                  | Gemini                  |
|------------------------|-------------------------|-------------------------|
| Bias gate              | **moral_framing (G3)**  | **evasion (G1)**        |
| Laundering             | none detected           | **identity_laundering** |
| Learning posture       | open_loop_reasoning     | **defensive_routine**   |

GPT routes the text through Gate 3 (framing_density > 0.02). Gemini routes it
through Gate 1 (evasion_count >= 2) and additionally fires identity_laundering
in Layer 3, which propagates to defensive_routine in Layer 4. The two
platforms are looking at the same article and producing two different
structural diagnoses from the same deterministic specification.

## Why This Matters

This is not noise. It is the central finding of the project, reproduced in a
single document.

The deterministic kernel is unambiguous: given identical signal inputs, it
always produces identical outputs. So when two LLM implementations of the
same kernel diverge, the divergence has to be upstream — at the Layer 0
signal-estimation boundary, where each platform tokenizes the text and counts
cues against the lexicons.

GPT estimates this article's framing_density above the 0.02 moral_framing
threshold. Gemini estimates its evasion cue count at >=2 (Gate 1's threshold).
Both estimates may be locally defensible, but they cannot both be right — and
neither platform's signal estimation is itself deterministic. This is exactly
the kernel violation pattern documented across three independent corpora in
the ICETM paper: the platforms compute the numbers, the platforms do not
faithfully execute the conditional logic, and the disagreement surfaces at
the gate boundary where conditional logic meets statistical estimation.

For a governance use case, the practical implication is direct: the Python
kernel must execute the conditional logic independently of the LLM. The LLM
should be restricted to upstream signal estimation, where its statistical
processing is an advantage rather than a liability.

## The Other 6 Articles

For the remaining 6 articles in the SemEval corpus, both platforms classify
the document as `clean` (no gate fires). This is the agreement baseline. See
`demo/gpt_full_corpus.md` and `demo/gemini_full_corpus.md` for the complete
outputs across all 7 articles.

---

**Source corpus:** SemEval-2023 Task 3 hyperpartisan articles (externally
annotated by the SemEval organizers, no engine involvement).
**Validation workbook:** v2.1, revalidated 2026-03-28.
**Pipeline:** v2.0.0 (89 automated test assertions, all passing).
