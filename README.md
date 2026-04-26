# The Epistemic Engine

A deterministic structural auditor for institutional discourse.

## Overview

The Epistemic Engine is a Python tool that analyzes the structural properties of institutional texts - focusing on *how* texts make their claims rather than *what* they claim. It identifies patterns like bias, authority laundering, and rhetorical positioning without relying on AI-based classification.

## Quick Start

```bash
git clone https://github.com/yacEYX-view/The-Epistemic-Engine.git
cd The-Epistemic-Engine
python epistemic_engine.py --text "Your institutional text here"
python epistemic_engine.py --file path/to/document.txt
```

Requirements: Python 3.8+ (no external dependencies)

## What's Included

- **epistemic_engine.py**: Main analysis engine
- **METHODS.md**: Complete technical specification 
- **CHANGELOG.md**: Version history and development notes
- **data/**: Validation datasets and benchmark results
- **docs/**: Thesis and additional documentation
- **demo/**: Example analyses and outputs

## How It Works

The engine processes texts through 6 analytical layers:

1. **Structural Extraction** - Counts 14 types of linguistic signals
2. **Language Game Classification** - Identifies institutional context
3. **Bias Detection** - Flags evasion, ideological, or moral framing patterns
4. **Authority Laundering** - Detects scientism, bureaucratic masking, identity laundering
5. **Learning Posture** - Determines if discourse is open or defensive
6. **Coordinate Placement** - Maps text position on HEAD/HEART and DISRUPTION/STABILITY axes

Results are deterministic and reproducible across platforms and time.

## Sample Output

```
A) AUDIT SNAPSHOT
Language game: corporate_risk_disclosure
Bias gate: clean
Laundering: bureaucratic_masking
Learning posture: defensive_routine
Testability: immunizing_stratagem

B) LOGIC RESULT
Logic type used: clean claim structure — no bias gate fired.

C) SPECTROGRAPH
        HEAD (+)
           |
    Q1     ★     Q2
           |
STAB <---- + ----> DISR
           |
    Q3           Q4
           |
       HEART (-)

X = -1.2, Y = -0.8, Intensity = 3.4/10

D) ASK-FOR MENU
1) Language game
2) Argument skeleton  
3) Falsifiability and self-protection
4) Authority laundering excerpts
5) Learning posture
6) Deterministic readout (proof)
7) What would change the conclusion
```

## Repository Structure

```
The-Epistemic-Engine/
├── epistemic_engine.py        # Core engine
├── METHODS.md                 # Technical specification
├── CHANGELOG.md               # Development history
├── README.md                  # This file
├── requirements.txt           # No dependencies
├── LICENSE                    # MIT License
├── data/                      # Validation datasets
│   ├── Texts.csv
│   ├── Annotations.csv
│   └── ...                   
├── docs/                      # Documentation
│   ├── Concepcion_Epistemic_Engine_2026.pdf
│   └── ...
└── demo/                      # Examples
    ├── _article1_divergence.md
    └── ...
```

## Validation

The engine was validated against 69 texts including SEC filings, BLS reports, and news articles. Key findings:
- **Kernel Violation Pattern**: LLMs compute signals correctly but fail deterministic logic execution
- **Register-Mismatch Gradient**: Performance drops from institutional (κ=1.000) to informal text (κ=0.053)
- **Temporal Stability**: Signal estimation varies over time (documented shifts in revalidation)

For complete validation results, see `data/` directory and `docs/Concepcion_Epistemic_Engine_2026.pdf`.

## License

MIT License - see LICENSE file
```
