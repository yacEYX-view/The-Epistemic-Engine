# The Epistemic Engine

**A Deterministic Structural Auditor for Institutional Discourse**

Yenesey Concepcion | Dr. Andres Fortino  
New York University, School of Professional Studies  
Spring 2026

## Overview

The Epistemic Engine is a deterministic, philosophy-grounded auditing system that classifies the structural epistemic properties of institutional text. It evaluates *how* institutional text makes its claims—whether claims are open to refutation or self-protecting, whether authority is deployed to foreclose contestation, and where the rhetorical posture sits on two axes (analytic-to-emotive and change-to-preservation).

The system implements a six-layer architecture:

| Layer | Name | Question Answered |
|-------|------|-------------------|
| 0 | Structural Extraction | What signals does this text emit? (14 signal densities) |
| 1 | Wittgenstein | What institutional language game is being played? |
| 2 | Popper Bias Gate | Are claims open to refutation or self-protecting? |
| 3 | Authority Laundering | Is authority being laundered through form or identity? |
| 4 | Argyris Learning Posture | Does the discourse invite learning or protect assumptions? |
| 5 | Coordinate Spectrograph | Where does it sit in affect-cognition and change-stability space? |

## Repository Contents

```
The-Epistemic-Engine/
├── README.md
├── data/
│   ├── Texts.csv                    # 69 corpus documents across 6 sub-corpora
│   ├── Annotations.csv              # 53 MAFALDA-aligned annotation records
│   ├── Taxonomy.csv                 # 8 fallacy subtypes with philosophical mappings
│   ├── Philosophical_Signals.csv    # 14-dimension signal density records (all texts)
│   ├── Validation_Lists.csv         # Controlled vocabulary for categorical fields
│   ├── Inter_Model_Agreement.csv    # Cohen's κ and F1 across merged dimensions
│   ├── Lexicon_Registry.csv         # Complete lexicon term inventory (1,091 terms)
│   ├── Lexicon_Overlaps.csv         # Cross-lexicon overlap documentation
│   ├── Domain_Generalization.csv    # Cross-domain signal pattern analysis
│   └── Energy_Benchmark.csv         # Energy/Oil Market corpus signal profiles
├── docs/
│   ├── Concepcion_Epistemic_Engine_Applied_Project_Final.pdf
│   └── ICETM_215.pdf
└── Epistemic_Engine_Workbook.xlsx   # Complete validation workbook (v2.1)
```

## Validation Corpus Structure (69 Documents)

| Sub-Corpus | Role | n | Description |
|------------|------|---|-------------|
| SEC Benchmark | BASELINE | 20 | 10 technical filings + 10 Reuters editorial interpretations |
| BLS Validation | VALIDATION | 12 | 6 BLS technical releases + 6 outside interpretations |
| Energy/Oil Market | VALIDATION | 10 | 5 WSJ/FT primary articles + 5 wire reconstructions |
| Synthetic Gate Tests | VALIDATION | 6 | One document per classification pathway |
| SemEval Hyperpartisan | VALIDATION | 7 | Externally annotated articles (independent ground truth) |
| MAFALDA External | VALIDATION | 12 | Blind-scored fallacy corpus (independent ground truth) |
| Calibration Seeds | CALIBRATION | 2 | Original synthetic anchor cases |

## Key Findings

1. **Kernel Violation Pattern**: Both LLM platforms correctly compute signal densities but fail to execute deterministic co-occurrence logic for authority laundering detection (10 confirmed violations across 3 corpora).

2. **Register-Mismatch Gradient**: Cohen's κ ranges from 1.000 on synthetic institutional text to 0.053 on MAFALDA informal argumentation, confirming that institutional structural auditing and general fallacy detection are distinct analytical tasks.

3. **Baseline Temporal Shift**: Gemini classification shifted from 20/20 to 18/20 on SEC revalidation over six weeks, establishing that LLM signal estimation requires periodic recalibration.

## Data Format

All CSV files use UTF-8 encoding with standard comma delimiters. The first row of each file contains column headers. Signal densities are recorded as decimal values normalized per 100 tokens. Coordinate values range from -10 to +10. The complete field definitions are documented in the Validation_Lists.csv file.

## Citation

```
Concepcion, Y., & Fortino, A. (2026). The Epistemic Engine: A Deterministic 
Structural Auditor for Institutional Discourse. In Proceedings of the 2nd 
International Conference on Engineering, Technology & Management (ICETM 2026). IEEE.
```

## License

This project was developed as an Applied Project for the Master of Science in Management and Systems program at NYU School of Professional Studies under the guidance of Dr. Andres Fortino.
