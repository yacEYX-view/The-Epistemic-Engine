# Methods — Epistemic Engine v2.0

## 1. Overview

The Epistemic Engine is a deterministic structural auditor for institutional discourse. It maps raw text (or pre-computed signal measures) into a reproducible set of outputs: a bias classification, authority-laundering flags, a learning-posture label, a testability label, and a two-axis coordinate position with intensity.

The engine does not judge truth, morality, risk, or predict behavior. It reports how a text behaves as an institutional artifact — where claims are open to refutation versus self-protecting, and whether the posture invites learning versus defensive routines.

### Philosophical commitments:

- **Kierkegaard:** truth as subjectivity — no claim to absolute truth, only structural integrity.
- **Wittgenstein:** meaning as language game — all text is treated as institutional discourse.
- **Popper:** falsifiability — claim structures are evaluated for openness to refutation.
- **Argyris:** learning theories — discourse is evaluated for defensive routines versus double-loop learning.

### Version history:

- **v1.0** (March 2026): Initial release. Validated against original five-document corpus.
- **v2.0** (March 2026): Incorporates cross-platform validation findings from GPT-4 and Gemini 3 Flash deployments. Key changes: extended evasion lexicon for political registers, stability lexicon exclusion list for procedural vocabulary, explicit gate-ordering enforcement, Layer 2/3 separation enforcement in output format, coordinate calibration guidance, scientism calibration note for genuine methodology documents.

## 2. Layered Logic Architecture

Six-layer stack. Each layer answers a specific question.

### Layer 0 — Structural Extraction

**Goal:** Convert raw text into analyzable signal densities.

**Inputs:** tokenized text. **Outputs:** 14 signal values.

#### 2.0.1 Gate inputs (Layer 2):

- `evasion_count` (int): count of explicit deflections that block contestation. Formal register cues: "not the point," "obviously," "no serious person," "that's ridiculous," "everyone knows," "clearly," "as I said," "I already explained," "let's move on," "beside the point," "irrelevant," "off topic," "that's a strawman," "you're missing the point," "nice try," "not worth responding," "the real issue," "what really matters." Colloquial/political register cues (added v2.0): "disaster" as categorical dismissal, "broken" as institutional dismissal, "failed" as motive attack, "out of excuses" as foreclosure, charged group labels used as dismissive shorthand.
- `falsifiability_low` (bool): see Section 2.1.
- `normative_density` (0–1): prescriptive language per token.
- `universal_density` (0–1): universal claims per token.
- `framing_density` (0–1): moralized virtue/vice framing per token.

#### 2.0.2 Coordinate inputs (Layer 5):

- `head_density` (0–1): analytic/technical cues per token.
- `heart_density` (0–1): affect/identity/moral-emotive cues per token. **v2.0 note:** When colloquial attack language co-occurs with high evasion_count (≥2), weight heart cues generously. Surface numeric vocabulary in the same document should not suppress heart density.
- `disruption_density` (0–1): rupture/change/crisis cues per token.
- `stability_density` (0–1): order/preservation cues per token. **v2.0 exclusion list:** Procedural-neutral terms do not count as stability cues: scheduled, routine, annual, quarterly, pursuant to, in accordance with, filing, filed, submitted, periodic, deadline, compliance (when used as procedural reporting, not advocacy for preservation).

#### 2.0.3 Laundering inputs (Layer 3):

- `ratio_density` (0–1): numeric/quantitative cues per token.
- `ethos_density` (0–1): authority cues per token.
- `lex_density` (0–1): bureaucratic/managerial lexicon per token.
- `pathos_density` (0–1): emotional loading per token.

#### 2.0.4 Reasoning input:

- `logos_density` (0–1): explicit logical connectives per token. Informational signal; not consumed by any gate or coordinate computation.

In measures mode, values are supplied directly. In raw-text mode, they are estimated by counting cue-type occurrences against total token count, and the output includes: "Measures are estimated."

### 2.1 Falsifiability Detection Heuristic

`falsifiability_low` = True when any of:

- **Vagueness:** ≥2 cues (systemic, inevitable, inherent, fundamentally, essentially, in principle, by nature, by definition).
- **Unfalsifiable framing:** ≥1 cue (self-evident, beyond question, undeniable, unquestionable, irrefutable, indisputable, "no evidence would change," "nothing can disprove," "proves itself").
- **Shifting criteria:** ≥1 cue ("if it fails that proves," "if it works that proves," "either way this shows," "heads I win tails you lose," "whatever happens," "no matter what").
- **Totalizing group attribution:** ≥2 regex-matched patterns ("the X are," "all X are," "no X is/are/can/will," "every X is/are/must/should").

### Layer 1 — Wittgenstein (Institutional Language Game)

**Question:** "What game is this text playing?"

Classifies contextual role: policy defense, PR statement, scientific justification, polemic, corporate risk disclosure, editorial advocacy, legislative persuasion, or institutional discourse (unspecified).

In measures mode: defaults to "unknown (measures mode)."

### Layer 2 — Popper (Bias Gate Hierarchy)

**Question:** "Is this claim structurally falsifiable, or is it protected from being wrong?"

**Gate evaluation is strictly sequential. The first gate that fires determines classification. Gates are never reordered.**

1. **Evasion gate:** `evasion_count >= 2` → classification = `evasion`
2. **Ideological gate:** (`normative_density > 0.05` OR `universal_density > 0.02`) AND `falsifiability_low = True` → classification = `ideological`
3. **Moral framing gate:** `framing_density > 0.02` → classification = `moral_framing`
4. **Default:** → classification = `clean`

Derived labels:
- Any gate fires → `popper_marker = "immunizing_stratagem"`
- No gate fires → `popper_marker = "falsifiable_claim_structure"`

**v2.0 enforcement note:** Cross-platform testing revealed that both GPT-4 and Gemini wrappers sometimes fire moral_framing on documents where evasion should be primary (e.g., Leavitt White House statement: evasion_count = 4, but platforms reported moral_framing). The gate hierarchy is not advisory — it is the engine's deterministic contract. Any implementation that reorders gates is producing incorrect output.

### Layer 3 — Authority Laundering

**Question:** "Is authority being laundered through form, jargon, or identity?"

Three flags, independently evaluated:

- **Scientism:** `ratio_density > 0.02` AND `ethos_density > 0.02`
- **Bureaucratic masking:** `lex_density > 0.02` AND `ratio_density > 0.02`
- **Identity laundering:** `ethos_density > 0.03` AND (`pathos_density > 0.02` OR `evasion_count >= 2`)

Aggregate: `laundering_present = (scientism OR bureaucratic_masking OR identity_laundering)`

**v2.0 scientism calibration:** If Layer 1 classifies the document as "scientific justification" and the quantitative vocabulary represents genuine methodology (numbers as method, not numbers as shield), apply higher scrutiny before firing scientism. The BLS Preliminary Benchmark Revision is the calibration case: it is a genuine statistical methodology document where ratio vocabulary does epistemic work. GPT-4 falsely fired scientism on this control document, inverting the engine's purpose.

**CRITICAL — Layer 3 is separate from Layer 2.** Laundering flags must never appear in the Section B logic result line. Section B reports the bias gate classification only (evasion, ideological, moral_framing, or clean). Laundering flags appear in Section A sentence 4 and drill-down item 4.

### Layer 4 — Argyris (Learning Logic)

- If `laundering_present = True` → `defensive_routine`
- Else → `open_loop_reasoning`

**Design note:** This layer currently derives entirely from Layer 3. Future revisions may incorporate bias classification and evasion count as additional inputs.

### Layer 5 — Coordinate Layer

**Formulas:**
```
Y = (head_density − heart_density) × 10, clamped [-10, +10]
X = (disruption_density − stability_density) × 10, clamped [-10, +10]
Intensity = (√(X² + Y²) / √200) × 10, normalized 0–10
```

**Quadrant:**
```
|X| < 3 AND |Y| < 3  → CLEAN
X ≤ 0 AND Y ≥ 0      → Q1 (HEAD + STABILITY)
X > 0  AND Y ≥ 0      → Q2 (HEAD + DISRUPTION)
X ≤ 0 AND Y < 0       → Q3 (HEART + STABILITY)
X > 0  AND Y < 0       → Q4 (HEART + DISRUPTION)
```

**Spectrograph:**
```
dx = clamp(round(X / 5), -2, 2)
dy = clamp(round(Y / 5), -2, 2)
Star at grid position: row = 2 − dy, col = 2 + dx
```

**Axis convention:** Positive Y = HEAD = upper rows. Negative Y = HEART = lower rows. Positive X = DISRUPTION = right columns. Negative X = STABILITY = left columns.

**v2.0 calibration guidance:** Cross-platform testing revealed systematic coordinate compression. GPT-4 wrappers produced intensity values of 0.04–2.41 on texts described as "dense with institutional and technical terminology." Gemini wrappers produced values of 3.8–7.5 on the same texts. The Python kernel is the ground truth. Density estimates in raw-text mode should produce coordinates that use the full spectrograph range when appropriate. Reference ranges:

| Document type | Typical head | Typical heart | Typical Y |
|---|---|---|---|
| SEC filing / regulatory | 0.15–0.40 | 0.00–0.03 | +1.5 to +4.0 |
| Political press (heated) | 0.02–0.10 | 0.10–0.30 | -2.0 to -8.0 |
| News interpretation | 0.05–0.15 | 0.02–0.05 | +0.3 to +1.3 |

### Layer 6 — Philosophical Meta-Layer

Implicit. Defines what the engine claims and refuses to claim.

## 3. Output Format

Four sections, exact sequence:

- **A)** Five-sentence audit snapshot: (1) language game, (2) bias classification + gate, (3) quadrant + coordinates + intensity, (4) laundering flags + learning posture, (5) testability label + estimation note.
- **B)** One-line logic result. Valid values for classification: evasion, ideological, moral_framing, clean. No other terms.
- **C)** Spectrograph grid + exactly three sentences (X, Y, intensity with numeric values).
- **D)** Seven-item ask-for menu.

Drill-down items:

1. Language game
2. Argument skeleton
3. Falsifiability and self-protection
4. Authority laundering excerpts
5. Learning posture
6. Deterministic readout (proof)
7. What would change the conclusion

## 4. Input Modes

- **Raw-text mode:** supply text, signals estimated via lexicon-based density computation.
- **Measures mode:** supply pre-computed signal values, kernel computes deterministically.
- **File mode:** supply a path to a text file (treated as raw-text mode).

## 5. Runtime Settings

- Temperature: 0.0 (or lowest available)
- Top-p: 1.0
- Tools: off (unless required by deployment)
- All classification logic is deterministic.

## 6. Signal Reference Table

| Signal | Type | Range | Layer | Description |
|--------|------|-------|-------|-------------|
| evasion_count | int | 0+ | L2 | Deflections blocking contestation |
| falsifiability_low | bool | T/F | L2 | Core claims hard to test |
| normative_density | float | 0–1 | L2 | Prescriptive language per token |
| universal_density | float | 0–1 | L2 | Universal claims per token |
| framing_density | float | 0–1 | L2 | Virtue/vice framing per token |
| head_density | float | 0–1 | L5 | Analytic/technical cues per token |
| heart_density | float | 0–1 | L5 | Affect/identity/emotive cues per token |
| disruption_density | float | 0–1 | L5 | Change/crisis cues per token |
| stability_density | float | 0–1 | L5 | Order/preservation cues per token |
| ratio_density | float | 0–1 | L3 | Quantitative cues per token |
| ethos_density | float | 0–1 | L3 | Authority cues per token |
| lex_density | float | 0–1 | L3 | Bureaucratic lexicon per token |
| pathos_density | float | 0–1 | L3 | Emotional loading per token |
| logos_density | float | 0–1 | Info | Logical connectives per token |

## 7. Classification Vocabulary

| Layer | Field | Valid Values |
|-------|-------|--------------|
| L2 Bias Gate | classification | clean, evasion, ideological, moral_framing |
| L2 Popper | testability | falsifiable_claim_structure, immunizing_stratagem |
| L3 Laundering | flags | scientism, bureaucratic_masking, identity_laundering |
| L4 Argyris | learning_posture | open_loop_reasoning, defensive_routine |
| L5 Coordinates | quadrant | CLEAN, Q1, Q2, Q3, Q4 |

## 8. Known Cross-Platform Failure Patterns (v2.0)

The following systematic failures were documented during Spring 2026 cross-platform validation. These patterns inform the v2.0 prompt and lexicon changes.

| Failure | Platforms affected | Root cause | v2.0 fix |
|---|---|---|---|
| Layer 2/3 conflation | GPT-4, Gemini (Machine A) | Section B reports laundering flags instead of bias gate | Explicit separation enforcement in prompt |
| Evasion gate never fires | GPT-4, Gemini (both) | Colloquial political language not in evasion lexicon | Extended evasion cues |
| Scientism false positive on genuine methodology | GPT-4 | No language-game context check | Scientism calibration note |
| Stability over-inflation on regulatory docs | Gemini | Procedural vocabulary counted as stability advocacy | Stability exclusion list |
| Coordinate compression | GPT-4 (severe), Gemini (moderate) | Conservative density estimation | Calibration guidance table |
| Spectrograph Y-axis inversion | Gemini | Star placed in HEAD region for negative-Y documents | Axis convention enforcement |
| Uniform readings across different documents | Gemini (Machine B) | Auditing metadata wrapper instead of discourse | "Audit the discourse content" instruction |

## 9. Reference Documents

- `Specs_E_E_03_04_26.pdf` — Visual spec reference
- `Epistemic_Engine_Gold_Standard_Template_v2.0.xlsx` — Workbook template with SEC benchmark data
- `MAFALDA_Logic_Coded.pdf` — Fallacy taxonomy reference
- `SYSTEM_PROMPT.md` — Deployment-ready system prompt
