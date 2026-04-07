# Changelog — Epistemic Engine

## v2.0 (March 2026) — Cross-Platform Validation Release

### Evidence basis
Changes informed by:
- Four-engine comparison: 2× Gemini 3 Flash, 2× GPT-4 (all auditing the same 6 SEC benchmark documents)
- Independent second-coder validation report (Spring 2026)
- BLS delta analysis (control–variable pair, September 2025 corpus)

### System prompt changes

| Change | Rationale | Evidence |
|---|---|---|
| **Layer 2/3 separation enforcement** | Both GPT and Gemini engines reported laundering flags (Layer 3) in Section B, which should only contain bias gate classifications (Layer 2). Added explicit instruction: "Do NOT report laundering flags in Section B." | Gemini Machine A: 5/6 docs reported "scientism, bureaucratic_masking" in logic result. GPT "The": 3/6 docs same error. |
| **Gate ordering enforcement** | Platforms sometimes fire moral_framing when evasion should be primary (gate 1 has priority over gate 3). Added: "Evaluate gates in strict numbered sequence. The FIRST gate that fires determines classification." | Leavitt statement: evasion_count=4 but both GPT-4 and Gemini reported moral_framing. Gate hierarchy not preserved. |
| **Extended evasion lexicon** | Original lexicon covered formal/academic evasion cues but missed colloquial political attack language. Added: "disaster" (categorical dismissal), "broken" (institutional dismissal), "failed" (motive attack), "run out of excuses" (foreclosure). | Leavitt statement: Python kernel expected evasion_count=4; neither platform detected sufficient evasion cues. |
| **Stability exclusion list** | Procedural-neutral terms common to regulatory writing (filed, annual, quarterly, compliance, deadline) were inflating stability_density. Added exclusion list. | BLS document: Gemini produced X=-8.2 (severe stability inflation) on a methodologically neutral document. |
| **Scientism calibration note** | Genuine statistical methodology documents (BLS releases) were triggering scientism because ratio_density and ethos_density exceeded thresholds — but the numbers represent real methodology, not borrowed quantitative form. Added language-game context check. | GPT-4: fired scientism + bureaucratic_masking on BLS control document, inverting the engine's purpose. |
| **Heart/pathos amplification guidance** | When colloquial attack language co-occurs with high evasion_count, surface numeric vocabulary in the same document should not suppress heart density. | Leavitt statement: GPT-4 produced Y=+0.50 (HEAD) on a document with "disaster," "broken," "failed" — the BLS numbers inflated HEAD and suppressed HEART. |
| **Coordinate calibration guidance** | GPT-4 wrappers produced coordinates near zero for all documents (max intensity 2.41). Added reference density ranges by document type. | GPT "The": intensities 0.04–2.41. GPT "An": intensities 0.30–1.12. Both platforms cluster all documents in CLEAN zone. |
| **Spectrograph axis enforcement** | Star placed in HEAD region for documents with negative Y value (HEART). Added explicit: "Star row = 2 − dy. Positive Y = HEAD = upper rows." | Andrews (Gemini): Y=-6.0 HEART but star rendered in upper half of grid. |
| **"Audit the discourse content" instruction** | Gemini Machine B audited the packaging metadata (APA citations, corpus labels) instead of the captured text. Added explicit instruction to focus on discourse content. | Gemini Machine B: All 6 docs described as "archival artifact" with "structural provenance" — reading wrapper, not discourse. |
| **"No conversational filler" instruction** | Gemini Machine B appended "Would you like me to provide…" after audit output. | Gemini Machine B, Doc 1.5: unsolicited menu prompt after Section D. |

### METHODS.md changes

- Added Section 2.1 (Falsifiability Detection Heuristic) — carried from v1.0
- Added Section 8 (Known Cross-Platform Failure Patterns) — new
- Updated signal count from 13 to 14 (logos_density, carried from v1.0)
- Added stability exclusion list to Layer 0 description
- Added extended evasion cues to Layer 0 description
- Added scientism calibration note to Layer 3 description
- Added coordinate calibration guidance to Layer 5 description
- Added v2.0 gate ordering enforcement note to Layer 2 description

### Gold Standard Template changes

- Added 6 SEC benchmark rows to Texts sheet (EE_SEC_01 through EE_SEC_03R)
- Added 6 corresponding rows to Engine_Signals sheet with expected signal values
- Added SEC_benchmark to Validation_Lists source corpus options
- Template version: v2.0

### New files

- `SEC_BENCHMARK_GUIDE.md` — expected outputs for all 6 SEC documents with diagnostic deltas
- `USER_PROMPTS.md` — prompt templates for Gemini deployment
- `CHANGELOG.md` — this file

## v1.0 (March 2026) — Initial Release

- Core Python kernel with all 6 layers
- Test suite (unittest)
- METHODS.md specification
- Gold Standard Template v1.1 with seed cases (EE_0001, EE_0002)
- README.md
- requirements.txt
