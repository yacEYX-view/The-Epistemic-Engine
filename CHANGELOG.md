# Changelog — Epistemic Engine

## Document ID Convention

All benchmark documents follow a three-part ID scheme:

```
EE_{CORPUS}_{NN}[.5][_R{SOURCE}]
```

| Part | Meaning |
|---|---|
| `EE` | Epistemic Engine |
| `{CORPUS}` | `SEC` / `BLS` / `NRG` / `SYN` |
| `{NN}` | Benchmark number (two digits) |
| `.5` | Outside interpretation (technical filing = no suffix) |
| `_R{SOURCE}` | Reused filing — same source document as benchmark `{SOURCE}` |

**Reused filings in the SEC baseline corpus:**
- `EE_SEC_05_R04` — Kellanova/Mars family-control angle (reuses DEFM14A proxy from EE_SEC_04)
- `EE_SEC_09_R08` — Tesla compensation mechanics (reuses PRE14A from EE_SEC_08)

**Calibration seeds** (excluded from the six-corpus count): `EE_0001`, `EE_0002`

---

## v2.0 (March 2026) — Cross-Platform Validation Release

### Key Findings from v2.0 Validation

Three principal findings emerged from the cross-platform validation run that informed every system prompt change below.

**Finding 1 — Kernel violation pattern.** Both GPT o3 and Gemini correctly compute the 14 signal densities at Layer 0 but systematically fail to execute the deterministic co-occurrence logic required at Layers 2 and 3. Ten confirmed violations were documented across three independent corpora (Synthetic, SEC, MAFALDA). Example: SYN_06 yields lex_density = 0.1220 and ratio_density = 0.0488 on GPT — both above the 0.02 bureaucratic_masking threshold — yet GPT reports the flag as false. The architectural implication is that all Layer 2 and Layer 3 conditional logic must execute in the Python kernel, not through the LLM wrapper.

**Finding 2 — Register-mismatch gradient.** Cohen's κ tracks the degree to which input register matches the engine's institutional calibration domain: κ = 1.000 on synthetic institutional text, κ = 0.302 on Energy journalism, κ = 0.000 on BLS (classification dimension), κ = 0.053 on MAFALDA informal argumentation. The gradient is a property of the analytical domain, not a design flaw; it establishes that institutional structural auditing and general-purpose fallacy detection are distinct tasks.

**Finding 3 — Temporal instability of LLM signal estimation.** The SEC baseline was revalidated on 2026-03-28, six weeks after initial validation (2026-02-15). Gemini moved from 20/20 clean to 18/20 clean: Documents 3.5 and 9.5 now fire moral_framing with framing_density = 0.03 exceeding the 0.02 threshold. Any publication of κ or F1 values must specify the revalidation date; results are measurements at a point in time, not permanent system properties.

### Evidence basis

Changes informed by:
- Four-platform comparison: 2× Gemini Flash, 2× GPT-4 (all auditing the same 10 SEC benchmark pairs, Benchmarks 1–6 formally; Benchmarks 7–10 in supplementary runs). Note: the formal platform designations for the published validation are GPT o3 and Gemini; the cross-platform confirmation pass used GPT-4 and Gemini Flash variants. Exact model versions: [specify model strings here — e.g., `gemini-1.5-flash-001`, `gpt-4-turbo-2024-04-09`].
- Independent second-coder validation report (Spring 2026)
- BLS primary paired test: CES Preliminary Benchmark release (EE_BLS_01) vs. White House Press Secretary statement on the same data (EE_BLS_01.5) — referred to throughout this table as the "Leavitt statement"
- "Andrews" reference below = [specify document ID — e.g., EE_SEC_XX.5]
- "BLS document" reference below = EE_BLS_01 (BLS CES Preliminary Benchmark, September 9, 2025)

### System prompt changes

| Change | Rationale | Evidence |
|---|---|---|
| **Layer 2/3 separation enforcement** | Both GPT and Gemini reported laundering flags (Layer 3) in Section B, which should only contain bias gate classifications (Layer 2). Added explicit instruction: "Do NOT report laundering flags in Section B." | Gemini Machine A: 5/6 docs reported "scientism, bureaucratic_masking" in logic result. GPT "The": 3/6 docs same error. |
| **Gate ordering enforcement** | Platforms sometimes fire moral_framing when evasion should be primary (gate 1 has priority over gate 3). Added: "Evaluate gates in strict numbered sequence. The FIRST gate that fires determines classification." | Leavitt statement: evasion_count=4 but both GPT-4 and Gemini reported moral_framing. Gate hierarchy not preserved. |
| **Extended evasion lexicon** | Original lexicon covered formal/academic evasion cues but missed colloquial political attack language. Added: "disaster" (categorical dismissal), "broken" (institutional dismissal), "failed" (motive attack), "run out of excuses" (foreclosure). | Leavitt statement: Python kernel expected evasion_count=4; neither platform detected sufficient evasion cues. |
| **Stability exclusion list** | Procedural-neutral terms common to regulatory writing (filed, annual, quarterly, compliance, deadline) were inflating stability_density. Added exclusion list. | BLS document (EE_BLS_01): Gemini produced X=−8.2 (severe stability inflation) on a methodologically neutral document. |
| **Scientism calibration note** | Genuine statistical methodology documents (BLS releases) were triggering scientism because ratio_density and ethos_density exceeded thresholds — but the numbers represent real methodology, not borrowed quantitative form. Added language-game context check. | GPT-4: fired scientism + bureaucratic_masking on BLS control document (EE_BLS_01), inverting the engine's purpose. |
| **Heart/pathos amplification guidance** | When colloquial attack language co-occurs with high evasion_count, surface numeric vocabulary in the same document should not suppress heart density. | Leavitt statement: GPT-4 produced Y=+0.50 (HEAD) on a document with "disaster," "broken," "failed" — the BLS numbers inflated HEAD and suppressed HEART. |
| **Coordinate calibration guidance** | GPT-4 wrappers produced coordinates near zero for all documents (max intensity 2.41). Added reference density ranges by document type. | GPT "The": intensities 0.04–2.41. GPT "An": intensities 0.30–1.12. Both platforms cluster all documents in CLEAN zone. |
| **Spectrograph axis enforcement** | Star placed in HEAD region for documents with negative Y value (HEART). Added explicit: "Star row = 2 − dy. Positive Y = HEAD = upper rows." | Andrews (Gemini): Y=−6.0 HEART but star rendered in upper half of grid. |
| **"Audit the discourse content" instruction** | Gemini Machine B audited the packaging metadata (APA citations, corpus labels) instead of the captured text. Added explicit instruction to focus on discourse content. | Gemini Machine B: All 6 docs described as "archival artifact" with "structural provenance" — reading wrapper, not discourse. |
| **"No conversational filler" instruction** | Gemini Machine B appended "Would you like me to provide…" after audit output. | Gemini Machine B, Doc 1.5: unsolicited menu prompt after Section D. |

### METHODS.md changes

- Added Section 2.1 (Falsifiability Detection Heuristic) — carried from v1.0
- Added Section 8 (Known Cross-Platform Failure Patterns) — new; documents the kernel violation pattern as Finding 1
- Updated signal count from 13 to 14 (logos_density, carried from v1.0). Full signal list organized by functional group:
  - Gate inputs (5): evasion_count, falsifiability_low, normative_density, universal_density, framing_density
  - Coordinate inputs (4): head_density, heart_density, disruption_density, stability_density
  - Laundering inputs (4): ratio_density, ethos_density, lex_density, pathos_density
  - Reasoning input (1): logos_density
- Added stability exclusion list to Layer 0 description
- Added extended evasion cues to Layer 0 description
- Added scientism calibration note to Layer 3 description
- Added coordinate calibration guidance to Layer 5 description
- Added v2.0 gate ordering enforcement note to Layer 2 description

### Gold Standard Template changes — v2.0

Template version: v2.0. The v2.1 revalidation pass (2026-03-28) is tracked separately below.

**Texts sheet — rows added:**

| ID | Benchmark | Document | Type |
|---|---|---|---|
| EE_SEC_01 | SEC Benchmark 1 | Coinbase Form 8-K (May 15, 2025) | Technical filing |
| EE_SEC_01.5 | SEC Benchmark 1 | Reuters: Coinbase warns of up to $400M hit | Outside interpretation |
| EE_SEC_02 | SEC Benchmark 2 | Super Micro Form 8-K (Feb 26, 2025) | Technical filing |
| EE_SEC_02.5 | SEC Benchmark 2 | Reuters: Super Micro to file delayed annual report | Outside interpretation |
| EE_SEC_03 | SEC Benchmark 3 | Tupperware Form 12b-25 (Mar 29, 2024) | Technical filing |
| EE_SEC_03.5 | SEC Benchmark 3 | Reuters: Iconic Tupperware flags doubts | Outside interpretation |
| EE_SEC_04 | SEC Benchmark 4 | Kellanova DEFM14A Merger Proxy (Sep 26, 2024) | Technical filing |
| EE_SEC_04.5 | SEC Benchmark 4 | Reuters: Mars to buy Pringles maker Kellanova | Outside interpretation |
| EE_SEC_05_R04 | SEC Benchmark 5 | Kellanova DEFM14A (reuse of EE_SEC_04) | Technical filing (reused) |
| EE_SEC_05.5 | SEC Benchmark 5 | Reuters: Mars' biggest deal clinched by secretive family | Outside interpretation |
| EE_SEC_06 | SEC Benchmark 6 | Super Micro Form 8-K re: Nasdaq Extension (Dec 6, 2024) | Technical filing |
| EE_SEC_06.5 | SEC Benchmark 6 | Reuters: Super Micro gets extension to file delayed report | Outside interpretation |
| EE_SEC_07 | SEC Benchmark 7 | Super Micro Form 10-K for FY ended June 30, 2024 | Technical filing |
| EE_SEC_07.5 | SEC Benchmark 7 | Reuters: Super Micro names BDO as auditor | Outside interpretation |
| EE_SEC_08 | SEC Benchmark 8 | Tesla PRE14A Preliminary Proxy (Sep 5, 2025) | Technical filing |
| EE_SEC_08.5 | SEC Benchmark 8 | Reuters: Tesla to award Musk an unparalleled $1 trillion | Outside interpretation |
| EE_SEC_09_R08 | SEC Benchmark 9 | Tesla PRE14A (reuse of EE_SEC_08) | Technical filing (reused) |
| EE_SEC_09.5 | SEC Benchmark 9 | Reuters: Inside Tesla's $1 trillion pay proposal | Outside interpretation |
| EE_SEC_10 | SEC Benchmark 10 | Microsoft Form 10-K for FY ended June 30, 2025 | Technical filing |
| EE_SEC_10.5 | SEC Benchmark 10 | Reuters Legal: SEC's new cybersecurity disclosure rules | Outside interpretation |

**Engine_Signals sheet:** 20 corresponding rows added (EE_SEC_01 through EE_SEC_10.5) with expected signal values per the SEC Benchmark Guide.

**Validation_Lists sheet — source corpus options added:**
- `SEC_benchmark` (baseline corpus, 20 documents)
- `BLS_validation` (validation corpus, 12 documents — see v2.1 below)
- `Energy_benchmark` (validation corpus, 10 documents — see v2.1 below)

### New files

- `SEC_BENCHMARK_GUIDE.md` — expected outputs for all 20 SEC documents with diagnostic deltas
- `USER_PROMPTS.md` — prompt templates for Gemini deployment
- `CHANGELOG.md` — this file

---

## v2.1 (March 28, 2026) — Revalidation Pass

This pass was not in the original project plan. It was added after Phase 6 validation runs raised two questions: whether Gemini's κ = 1.000 on the BLS corpus reflected genuine fidelity or a circularity artifact, and whether LLM signal estimation was temporally stable. The revalidation answered both.

### Corpus changes

- SEC baseline revalidated; 2 Gemini outputs shifted (see SEC Baseline Temporal Shift below)
- BLS corpus reduced from 22 to 12 documents for class-distribution balance
- MAFALDA External sub-corpus added (12 documents, externally annotated by Helwe et al. 2024)
- SemEval Hyperpartisan sub-corpus added (7 documents, annotated by SemEval-2023 Task 3 organizers)
- Calibration seeds (EE_0001, EE_0002) formally distinguished from validation units in workbook

### Gold Standard Template changes — v2.1

**Texts sheet — rows added:**

*BLS Validation Corpus (12 documents, 6 pairs):*

| ID | BLS Benchmark | Document | Type |
|---|---|---|---|
| EE_BLS_01 | BLS Benchmark 1 | BLS: 2025 Preliminary Benchmark Revision Announcement (Sep 8, 2025) | Technical release |
| EE_BLS_01.5 | BLS Benchmark 1 | American Action Forum: The 2025 Preliminary Benchmark Revisions (Ashton, Sep 4, 2025) | Outside interpretation |
| EE_BLS_02 | BLS Benchmark 2 | BLS: CES Preliminary Benchmark (National) — March 2025 (Sep 9, 2025) | Technical release |
| EE_BLS_02.5 | BLS Benchmark 2 | Econbrowser: Implications of the Preliminary Benchmark Revision (Chinn, Sep 9, 2025) | Outside interpretation |
| EE_BLS_03_R02 | BLS Benchmark 3 | BLS: CES Preliminary Benchmark (reuse of EE_BLS_02) | Technical release (reused) |
| EE_BLS_03.5 | BLS Benchmark 3 | PIIE: BLS investigation — Challenges? Yes. Rigged data? No. (Wilcox, Oct 23, 2025) | Outside interpretation |
| EE_BLS_04_R01 | BLS Benchmark 4 | BLS: 2025 Preliminary Benchmark Revision Announcement (reuse of EE_BLS_01) | Technical release (reused) |
| EE_BLS_04.5 | BLS Benchmark 4 | MacroMostly: Recap — CES Preliminary Benchmark Estimate, March 2025 (Berger, Sep 9, 2025) | Outside interpretation |
| EE_BLS_05 | BLS Benchmark 5 | BLS: CES Preliminary Benchmark Summary (Sep 9, 2025) | Technical release |
| EE_BLS_05.5 | BLS Benchmark 5 | Reuters: US payrolls benchmark revision estimate suggests labor market weaker (Mutikani, Sep 9, 2025) | Outside interpretation |
| EE_BLS_06 | BLS Benchmark 6 | BLS: CES National Benchmark Article (Feb 11, 2026) | Technical release |
| EE_BLS_06.5 | BLS Benchmark 6 | Reuters: US employment growth through March revised down by 862,000 jobs (Feb 11, 2026) | Outside interpretation |

*Energy/Oil Market Validation Corpus (10 documents, 5 pairs):*

| ID | Energy Benchmark | Document | Type |
|---|---|---|---|
| EE_NRG_X1 | Energy Benchmark X.1 | WSJ: 2020 Oil Price Crash Below Zero (Apr 21, 2020) | Primary article |
| EE_NRG_X1.5 | Energy Benchmark X.1 | Wire reconstruction: CNN Business, Bloomberg, EIA, Fortune coverage | Outside reconstruction |
| EE_NRG_X2 | Energy Benchmark X.2 | WSJ: 2023 Saudi Unilateral Production Cut | Primary article |
| EE_NRG_X2.5 | Energy Benchmark X.2 | Wire reconstruction: NPR, CNN Business, Al Jazeera, PBS coverage | Outside reconstruction |
| EE_NRG_X3 | Energy Benchmark X.3 | FT: 2018 Brent Crude Rally to $80 | Primary article |
| EE_NRG_X3.5 | Energy Benchmark X.3 | Synthesized from EIA, Wikipedia oil price history, CRS, contemporaneous reporting | Outside reconstruction |
| EE_NRG_X4 | Energy Benchmark X.4 | FT: 2020 Negative US Oil Prices — What It Means for the Industry | Primary article |
| EE_NRG_X4.5 | Energy Benchmark X.4 | Wire reconstruction: Bloomberg, CNBC, Fortune, PMC academic paper coverage | Outside reconstruction |
| EE_NRG_X5 | Energy Benchmark X.5 | FT: 2023 Surprise OPEC+ Production Cuts | Primary article |
| EE_NRG_X5.5 | Energy Benchmark X.5 | Wire reconstruction: NPR, AP, CNN Business coverage | Outside reconstruction |

**Engine_Signals sheet:** 22 corresponding rows added (EE_BLS_01 through EE_BLS_06.5, EE_NRG_X1 through EE_NRG_X5.5) with expected signal values.

### SEC Baseline Temporal Shift

Two Gemini outputs on the SEC baseline shifted between initial validation (2026-02-15) and revalidation (2026-03-28):

| Document | ID | Shift | Classification |
|---|---|---|---|
| Tupperware / Reuters editorial | EE_SEC_03.5 | Gemini: clean → moral_framing (framing_density 0.03 > 0.02 threshold) | Genuine Layer 2 firing |
| Tesla pay plan / Reuters editorial | EE_SEC_09.5 | Gemini: clean → moral_framing (framing_density 0.03 > 0.02 threshold) | Genuine Layer 2 firing |
| Tesla / Reuters editorial | EE_SEC_08.5 | GPT reports ideological; normative_density 0.0149 < 0.05; universal_density 0.0025 < 0.02 | Kernel Violation KV-07 |
| Tupperware and Kellanova editorials | EE_SEC_03.5, EE_SEC_04.5 | GPT reports identity_laundering; ethos_density 0.0188 and 0.0176 < 0.03 threshold | Kernel Violations KV-05, KV-06 |

SEC baseline status post-revalidation: GPT 20/20 clean (gate), Gemini 18/20 clean (gate).

### Kernel Violation Registry (v2.1)

10 confirmed violations documented across three corpora. Full registry in `KERNEL_VIOLATION_REGISTRY.md` (Appendix D of project paper).

| Violation ID | Corpus | Document | Layer | Description |
|---|---|---|---|---|
| KV-01 | Synthetic | SYN_01 | 3 | GPT under-fires bureaucratic_masking despite lex_density and ratio_density both > 0.02 |
| KV-02 | Synthetic | SYN_02 | 3 | GPT under-fires bureaucratic_masking despite lex_density and ratio_density both > 0.02 |
| KV-03 | Synthetic | SYN_06 | 3 | GPT under-fires bureaucratic_masking despite lex_density = 0.1220 and ratio_density = 0.0488, both > 0.02 |
| KV-04 | Synthetic | SYN_05 | 3 | Gemini under-fires scientism and bureaucratic_masking despite ratio, ethos, and lex densities all exceeding threshold |
| KV-05 | SEC | EE_SEC_03.5 | 2 | GPT over-fires identity_laundering; ethos_density 0.0188 does not exceed 0.03 threshold |
| KV-06 | SEC | EE_SEC_04.5 | 2 | GPT over-fires identity_laundering; ethos_density 0.0176 does not exceed 0.03 threshold |
| KV-07 | SEC | EE_SEC_08.5 | 2 | GPT over-fires ideological; normative_density 0.0149 < 0.05 and universal_density 0.0025 < 0.02 |
| KV-08 | MAFALDA | MAF_03 | 2 | GPT under-fires moral_framing gate despite framing_density > 0.02 |
| KV-09 | MAFALDA | MAF_11 | 2 | GPT under-fires moral_framing gate despite framing_density > 0.02 |
| KV-10 | Synthetic | SYN_01 | 2 | [See full registry for details] |

**Layer 2 violations** appear only on GPT and only on editorial-register text. **Layer 3 violations** appear on both platforms across three independent corpora. The Layer 3 pattern is the more consequential finding: both platforms compute signal densities correctly and then do not evaluate the conditional logic. The violation is structured, not random.

### New files (v2.1)

- `KERNEL_VIOLATION_REGISTRY.md` — full registry of 10 confirmed violations with signal values, expected outputs, and platform outputs
- `ENERGY_BENCHMARK_COMPRESSION_ANALYSIS.md` — compression analysis for the Energy/Oil Market corpus (Appendix E of project paper)

---

## v1.0 (March 2026) — Initial Release

- Core Python kernel with all 6 layers (`epistemic_engine.py v1.0.0`)
- Test suite (unittest, initial assertions)
- `METHODS.md` specification
- Gold Standard Template v1.1 with 2 calibration seeds (EE_0001, EE_0002) and 5 initial test documents
- `README.md`
- `requirements.txt`
