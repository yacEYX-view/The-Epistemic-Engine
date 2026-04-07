# The Epistemic Engine

**A deterministic structural auditor for institutional discourse.**

The Epistemic Engine evaluates *how* institutional text makes its claims, not *what* it claims. It is not a fact-checker. It is a six-layer pipeline that classifies the structural epistemic properties of institutional text — whether claims are open to refutation or self-protecting, whether authority is deployed to foreclose contestation, and where the rhetorical posture sits on two axes (analytic-to-emotive and change-to-preservation) — and produces reproducible, interrogable outputs.

Developed at **NYU School of Professional Studies** under the sponsorship of **Dr. Andres Fortino** through The Digital Forge.

---

## Table of Contents

- [Status](#status)
- [What It Does](#what-it-does)
- [Architecture](#architecture)
- [Validation Framework (v2.1)](#validation-framework-v21)
- [Principal Findings](#principal-findings)
- [Quick Start](#quick-start)
- [Repository Structure](#repository-structure)
- [Philosophical Grounding](#philosophical-grounding)
- [Publications](#publications)
- [Limitations](#limitations)
- [License](#license)

---

## Status

**Current release:** Validation Workbook v2.1 (revalidated 2026-03-28)
**Pipeline version:** v2.0.0 (89 automated test assertions, all passing)
**Manuscript:** *The Epistemic Engine: A Deterministic Structural Auditor for Institutional Discourse* — finalized for ICETM submission (Concepcion & Fortino, 2026).

The proof of concept is complete. Three independent corpora plus two externally annotated benchmarks have been processed, and 10 kernel violations have been documented in a public registry. Active work is on independent blind annotation, ESG/political corpus expansion, and v2.1 lexicon refinements.

---

## What It Does

Given an institutional text, the engine produces:

1. **Bias gate classification** — `clean`, `evasion`, `ideological`, or `moral_framing`
2. **Authority laundering flags** — `scientism`, `bureaucratic_masking`, `identity_laundering` (independent, multiple allowed)
3. **Learning posture** — `open_loop_reasoning` or `defensive_routine`
4. **Testability label** — `falsifiable_claim_structure` or `immunizing_stratagem`
5. **Rhetorical coordinate** — `(X, Y)` on HEAD/HEART × DISRUPTION/STABILITY axes, with intensity and quadrant
6. **ASCII spectrograph** — visual plot of where the text sits in coordinate space

All classification logic is deterministic and threshold-based. Given identical signal inputs, the kernel always produces identical outputs.

---

## Architecture

The engine is a six-layer pipeline. Layers 1–5 are fully deterministic; Layer 0 depends on how the host platform tokenizes and counts cues.

| Layer | Name | Question Answered | Output |
|---|---|---|---|
| 0 | Structural Extraction | What signals does this text emit? | 14 signal densities; falsifiability flag |
| 1 | Wittgenstein | What institutional language game is being played? | Game type (policy defense, PR statement, scientific justification, polemic, corporate risk disclosure, editorial advocacy, legislative persuasion) |
| 2 | Popper Bias Gate | Are claims open to refutation or self-protecting? | Classification + Popper marker |
| 3 | Authority Laundering | Is authority being laundered through form or identity? | Three independent flags |
| 4 | Argyris | Does the discourse invite learning or protect assumptions? | Learning posture |
| 5 | Coordinate Spectrograph | Where does this discourse sit in affect-cognition × change-stability space? | (X, Y), intensity, quadrant, ASCII plot |

**Lexicon scale:** 1,091 terms across 11 categories (expanded from 424 in v1.0) using a function-first, domain-agnostic methodology. Every term is traceable in `Lexicon_Registry`, with cross-lexicon overlaps documented in `Lexicon_Overlaps`.

---

## Validation Framework (v2.1)

The validation workbook consolidates **69 texts** comprising 67 documents across six sub-corpora and 2 calibration seeds, scored by two formal LLM platforms (OpenAI GPT o3, Google Gemini) plus informal cross-checking on Anthropic Claude.

| Corpus | Role | n | Function |
|---|---|---|---|
| SEC Benchmark | Baseline | 20 | Ground-truth anchor; 10 technical filings paired with 10 Reuters editorial interpretations across 6 corporate events (Coinbase, Super Micro, Tupperware, Kellanova–Mars, Tesla, Microsoft) |
| BLS Validation | Validation | 12 | Labor-economics register generalization; 6 BLS releases paired with 6 outside interpretations |
| Energy / Oil Market | Validation | 10 | Commodity-price journalism; 5 WSJ/FT primary articles paired with 5 wire reconstructions |
| Synthetic Gate Tests | Validation | 6 | One document per classification pathway (SYN_01–SYN_06) |
| SemEval Hyperpartisan | Validation | 7 | Externally annotated articles (independent ground truth) |
| MAFALDA External | Validation | 12 | Blind-scored fallacy corpus (independent ground truth) |
| Calibration Seeds | Calibration | 2 | Anchor cases (excluded from the six-corpus count) |

**Workbook structure (10 sheets):** `Texts`, `Annotations`, `Taxonomy`, `Philosophical_Signals`, `Validation_Lists`, `Inter_Model_Agreement`, `Lexicon_Registry`, `Lexicon_Overlaps`, `Domain_Generalization`, `Energy_Benchmark`.

**Cohen's κ across corpora (Classification dimension):**

| Corpus | n | κ | Strength | Key finding |
|---|---|---|---|---|
| Synthetic | 6 | 1.000 | Perfect | Gate 6/6 both models |
| SEC Baseline | 20 | 0.375 | Fair | Post-revalidation Gemini 18/20 clean |
| SemEval | 7 | 0.462 | Moderate | Article 1 gate divergence only |
| Energy | 10 | 0.302 | Fair | Scientism pattern confirmed |
| BLS | 12 | 0.000 | None | GPT all-clean majority bias |
| MAFALDA | 12 | 0.053 | Slight | Register mismatch |

The κ gradient *itself* is informative: it tracks the degree to which the input register matches the engine's institutional calibration domain.

---

## Principal Findings

### 1. The Kernel Violation Pattern

Both LLM platforms correctly compute Layer 0 signal densities but **fail to execute the deterministic conditional logic** at Layers 2 and 3. Ten violations are documented in a public registry:

- **Layer 3 violations** (laundering co-occurrence conditions met but flag not fired) appear on **both** platforms across **three** independent corpora.
- **Layer 2 violations** (gate classification departing from signal data) appear on GPT and only on editorial-register text.
- **SYN_05 (Gemini)** is the most diagnostic single case: two independent co-occurrence conditions are met simultaneously and neither flag fires (KV-03, KV-10).

**Implication for governance:** A deterministic specification does not guarantee deterministic execution when upstream signal estimation is delegated to a probabilistic model. The Python kernel must execute the conditional logic independently.

### 2. The Register-Mismatch Gradient

On synthetic institutional text, both platforms achieve **6/6 gate classification**. On the externally annotated MAFALDA informal-argumentation corpus, the engine produces **κ = 0.053 (Gemini)** and **κ = 0.000 (GPT)**. This is not a failure mode — it is empirical evidence that institutional structural constructs (evasion, authority laundering, defensive routines) do not map onto general-purpose argumentation fallacies. They operate through different lexical mechanisms in different communicative contexts.

The strongest single MAFALDA result is **MAF_02** (a textbook appeal to false authority): Gemini correctly detects scientism in Layer 3, exactly as the architecture predicts for Ethos fallacies.

### 3. The JRC Scale Contrast

The European Commission's Joint Research Centre annotation campaigns required **over seventy scholars** annotating **2,500 documents** across nine languages with months of calibration and persistent expert disagreement. The deterministic kernel produces reproducible output on 69 documents with **zero inter-annotator variability** and **zero marginal cost per document** — at the price of domain specificity and fully documented failure modes.

---

## Quick Start

### Requirements

- Python 3.9+
- Dependencies in `requirements.txt`

### Installation

```bash
git clone https://github.com/yacEYX-view/The-Epistemic-Engine.git
cd The-Epistemic-Engine

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Run on text

```bash
python src/mafalda_engine/mafalda_engine.py --input "Your institutional text here"
```

### Run the demo

```bash
./demo.sh
```

### Run the test suite

```bash
pytest test_epistemic_engine.py
```

All 89 assertions should pass on v2.0.0.

---

## Repository Structure

```
The-Epistemic-Engine/
├── src/
│   └── mafalda_engine/          # Core six-layer pipeline
├── epistemic_engine/
│   └── mafalda_engine/          # Pipeline modules
├── data/
│   └── benchmarks/
│       └── sbc-100/             # Benchmark datasets
├── demo.sh                       # Interactive demonstration
├── requirements.txt
├── Quick Setup Command
└── README.md
```

---

## Philosophical Grounding

The engine's analytical categories are operationalizations of three philosophical traditions, plus a fourth that operates at the meta-design level.

- **Wittgenstein (Layer 1).** All institutional text is treated as a rule-governed language game. The same word performs different functions in different games — `compliance` performs bureaucratic register in an SEC filing and authority invocation in an editorial.
- **Popper (Layer 2).** The falsifiability criterion is the core evaluative standard. Claims structured to be immune from evidence (immunizing stratagems) are epistemically inferior to claims that expose themselves to refutation.
- **Argyris (Layer 3).** The distinction between discourse enabling genuine inquiry (open-loop reasoning, compatible with double-loop learning) and discourse encoding defensive routines that protect existing assumptions from revision.
- **Kierkegaard (meta-design).** Foundational humility. The engine reports continuous coordinates rather than binary verdicts, preserves inter-model disagreement as informational data, and refuses to collapse interpretive uncertainty into false precision.

---

## Publications

- Concepcion, Y., & Fortino, A. (2026). *The Epistemic Engine: A Deterministic Structural Auditor for Institutional Discourse.* Submitted, ICETM 2026.
- Concepcion, Y. (2026). *Epistemic Engine BLS Validation Corpus: Empirical Scoring Report with Conceptual Integration.* New York University, School of Professional Studies.
- Concepcion, Y. (2026). *Epistemic Engine Validation Workbook v2.1.* New York University, School of Professional Studies.

---

## Limitations

- **Lexicon-based signal estimation** has limits; near-threshold cases in speculative financial writing and mixed-register policy documents represent the boundary of reliable classification.
- **Corpus class balance.** The evasion and ideological gates remain empirically thin outside synthetic texts, with one confirmed ideological case (BLS_B06E), one evasion case (SemEval Article 1), and zero confirmed on MAFALDA.
- **Circularity risk.** Reference classifications were partially adjudicated against engine outputs; an independent human-annotated reference standard scored blind is the priority near-term task.
- **English-only.** All tested documents are U.S. institutional English. Cross-linguistic validity is untested.
- **Temporal stability.** LLM signal estimation drifts across time. Any reported κ or F1 should specify the revalidation date.

---

## License

MIT License. See `LICENSE` for details.

---

**Project lead:** Yenesey Concepcion (yac2027@nyu.edu)
**Sponsor:** Dr. Andres Fortino (agf249@nyu.edu) — NYU School of Professional Studies, The Digital Forge

For questions or issues, please open a GitHub Issue.
