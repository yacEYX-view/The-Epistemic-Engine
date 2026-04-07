# Epistemic Engine v2.0

A deterministic structural auditor for institutional discourse.

## What It Does

The Epistemic Engine reports how a text behaves as an institutional artifact: the argument's structure, where claims are open to refutation versus self-protecting, whether the posture invites learning versus defensive routines, and where the tone sits on two axes (HEAD/HEART and DISRUPTION/STABILITY).

**Not included:** fact-checking, moral judgment, risk scoring, or behavior prediction.

## Philosophical Commitments

- **Kierkegaard:** truth as subjectivity — no claim to absolute truth, only structural integrity.
- **Wittgenstein:** meaning as language game — all text is treated as institutional discourse.
- **Popper:** falsifiability — claim structures are evaluated for openness to refutation.
- **Argyris:** learning theories — discourse is evaluated for defensive routines versus double-loop learning.

## Repository Structure

```
epistemic-engine/
├── README.md                            ← This file
├── METHODS.md                           ← Authoritative methods specification (v2.0)
├── SYSTEM_PROMPT.md                     ← Deployment-ready system prompt for LLM wrappers
├── SEC_BENCHMARK_GUIDE.md               ← SEC benchmark corpus documentation
├── epistemic_engine.py                  ← Python kernel (deterministic reference implementation)
├── test_epistemic_engine.py             ← Test suite
├── __init__.py                          ← Package init
├── requirements.txt                     ← Dependencies
├── Epistemic_Engine_Gold_Standard_Template_v2.0.xlsx
│                                        ← Workbook with seed cases + SEC benchmark data
├── benchmark_docs/                      ← SEC benchmark corpus (6 PDFs, 3 paired sets)
│   ├── benchmark_1_coinbase_form_8k.pdf
│   ├── benchmark_1_5_coinbase_reuters_interpretation.pdf
│   ├── benchmark_2_supermicro_8k_compliance.pdf
│   ├── benchmark_2_5_supermicro_reuters_deadline.pdf
│   ├── benchmark_3_tupperware_nt10k.pdf
│   └── benchmark_3_5_tupperware_reuters_going_concern.pdf
└── reference/                           ← Non-modified reference documents
    ├── Specs_E_E_03_04_26.pdf
    ├── MAFALDA_Logic_Coded.pdf
    └── 1Fallacy_Classification_Gold_Standard_Spec_v1_0.docx
```

## Quick Start

### Python kernel (deterministic reference)

```bash
# Raw-text mode
python epistemic_engine.py --text "We must act now. The crisis is inevitable."

# Measures mode
python epistemic_engine.py --measures "evasion_count: 3
falsifiability_low: true
normative_density: 0.08"

# File mode
python epistemic_engine.py --file benchmark_docs/benchmark_1_coinbase_form_8k.pdf

# Drill-down
python epistemic_engine.py --text "..." --drilldown 2,6

# JSON output
python epistemic_engine.py --text "..." --format json
```

### LLM wrapper deployment (Gemini / GPT)

1. Copy the contents of `SYSTEM_PROMPT.md` into the system instruction field.
2. Set runtime: Temperature 0.0, Top-p 1.0, Tools off.
3. Supply text via user prompt: "Audit this text. Text: [PASTE]"
4. For measures mode: "Audit these measures. Measures: [LIST]"

## SEC Benchmark Corpus

Six documents organized as three paired sets, each pairing a technical SEC filing with its Reuters outside interpretation:

| Pair | Technical (SEC filing) | Interpretation (Reuters) |
|------|----------------------|------------------------|
| **1** | Coinbase Form 8-K: material cybersecurity incident | Reuters: Coinbase cyberattack, $180–$400M hit |
| **2** | Super Micro Form 8-K: reporting compliance update | Reuters: delayed annual report, share-price reaction |
| **3** | Tupperware Form 12b-25: late 10-K notice | Reuters: going-concern doubts, inadequate liquidity |

**Design rationale:** The pairing structure tests whether the engine differentiates between a regulatory filing's technical register and a news organization's interpretive framing of the same underlying event. Technical filings should produce higher head_density, higher lex_density, and stronger stability leanings. Interpretations should show more disruption orientation and lower signal density overall.

See `SEC_BENCHMARK_GUIDE.md` for detailed expected outputs.

## Running Tests

```bash
python -m pytest test_epistemic_engine.py -v
```

## Version History

- **v1.0** (March 2026): Initial release. Five-document proof-of-concept corpus.
- **v2.0** (March 2026): Cross-platform validation release. Adds SEC benchmark corpus, extended evasion lexicon, stability exclusion list, Layer 2/3 separation enforcement, coordinate calibration guidance, scientism calibration for genuine methodology documents. Informed by four-engine comparison (2× GPT-4, 2× Gemini 3 Flash).

## Runtime Settings (for reproducibility)

- Temperature: 0.0 (or lowest available)
- Top-p: 1.0
- Tools: off (unless required by deployment)
- All classification logic is deterministic — threshold-based with no stochastic components.

## Author

Andres Fortino, Ph.D., New York University, School of Professional Studies

## License

Proprietary. See accompanying license documentation.
