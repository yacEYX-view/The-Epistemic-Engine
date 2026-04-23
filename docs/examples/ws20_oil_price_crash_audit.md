# Example Audit: WSJ 2020 Oil Price Crash Below Zero

## Input Text
[Benchmark X.1 - WSJ Article on 2020 Oil Price Crash Below Zero]

## Full Audit Output

### Section A — Five-sentence audit snapshot

The discourse is a news interpretation (neutral) artifact within a financial journalism context. The bias gate classification is clean as no gate fired, given the text's focus on describing market mechanics without utilizing evasion or moralized framing. The text sits in the CLEAN quadrant with coordinates of X: 1.1 and Y: 0.8, yielding an intensity of 1.0. Authority laundering flags are none and the learning posture is open_loop_reasoning. The text exhibits a falsifiable_claim_structure. Measures are estimated.

### Section B — One-line logic result

Logic type used: clean claim structure — no bias gate fired.

### Section C — Spectrograph

            HEAD (+)
              |
    Q1    · · · · ·     Q2
          · · · · ·
STAB <--- · ·  ★ · · ----> DISR 
· · Q3    · · · · ·     Q4 
            |
            HEART (-)

X = 1.1, leaning toward disruption due to descriptions of a historic price crash and market "bedlam".
Y = 0.8, head-coded as the text relies on financial analysts and technical explanations of futures contracts.
Intensity = 1.0/10, representing a low commitment level as the reporting remains near the center of the spectrograph.

### Section D — Ask-for menu

1) Language game
2) Argument skeleton
3) Falsifiability and self-protection
4) Authority laundering excerpts
5) Learning posture
6) Deterministic readout (proof)
7) What would change the conclusion

### Follow-up Response: What would change the conclusion

To alter the current audit conclusion for this text, the following signal thresholds would need to be met:

- **Classification shift:** To move from `clean` to `evasion`, the discourse would need to include at least two explicit deflections (e.g., adding "obviously" or "this is beside the point"). To trigger an `ideological` classification, the text would need to combine low falsifiability (e.g., using "fundamentally") with an increase in `universal_density` above 0.02.
- **Authority laundering:** To trigger the `scientism` flag, the `ethos_density` would need to increase from ~0.01 to >0.02 (approximately 2–3 additional appeals to "experts" or "prestigious institutions" per 100 words), as the `ratio_density` is already well above the required threshold.
- **Coordinate shift:** To move the coordinate position from the `CLEAN` center into `Q2 (HEAD + DISRUPTION)`, the X-value must reach ≥ 3.0. This would require an increase in `disruption_density` relative to `stability_density` of 0.19 (roughly 4–5 more crisis or rupture cues).
- **Learning posture:** To transition from `open_loop_reasoning` to `defensive_routine`, any of the authority laundering flags (scientism, bureaucratic masking, or identity laundering) would need to fire, typically by increasing the density of bureaucratic lexicon (`lex_density`) or authority cues (`ethos_density`).
    HEAD (+)
       |
Q1     · · · · ·     Q2
       · · · · ·
STAB <---- · · ★ · · ----> DISR
Q3     · · · · · Q4
       |
   HEART (-)
  Sentence 1: X = 1.1, leaning toward disruption due to descriptions of a historic price crash and market "bedlam".
Sentence 2: Y = 0.8, head-coded as the text relies on financial analysts and technical explanations of futures contracts.
Sentence 3: Intensity = 1.0/10, plus commitment level low.

