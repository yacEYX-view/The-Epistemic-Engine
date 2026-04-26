# The Epistemic Engine

**A Deterministic Structural Auditor for Institutional Discourse**

Yenesey Athena Concepcion  
NYU NetID: yac2027  
Applied Technical Project  
NYU School of Professional Studies | Spring 2026  

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

The Epistemic Engine is a deterministic, philosophy-grounded auditing system that classifies the structural epistemic properties of institutional text. It evaluates *how* text makes its claims — whether claims are open to refutation or self-protecting, whether authority is deployed to foreclose contestation, and where the rhetorical posture sits on two axes (analytic-to-emotive and change-to-preservation).

This is not fact-checking. The engine addresses structural opacity: how a document behaves as an epistemic artifact, not what it claims. As demonstrated in the project (Section 13.2), when comparing the September 9, 2025 BLS Preliminary Benchmark Revision with the White House statement on the same data, the BLS release classifies as `clean` with `open_loop_reasoning` posture, while the White House statement classifies as `evasion`, `Q4 quadrant`, intensity near `6.2`, with `defensive_routine` posture and `identity_laundering` flag — the engine quantifies that structural difference.

The system implements a six-layer architecture:

| Layer | Name | Question Answered |
|-------|------|-------------------|
| 0 | Structural Extraction | What signals does this text emit? (14 densities) |
| 1 | Wittgenstein | What institutional language game is being played? |
| 2 | Popper Bias Gate | Are claims open to refutation or self-protecting? |
| 3 | Authority Laundering | Is authority laundered through form or identity? |
| 4 | Argyris Learning Posture | Does discourse invite learning or protect assumptions? |
| 5 | Coordinate Spectrograph | Where does it sit in affect–cognition and change–stability space? |

## Installation

```bash
git clone https://github.com/yacEYX-view/The-Epistemic-Engine.git
cd The-Epistemic-Engine

Python 3.8+ required. No external dependencies — the engine uses only the standard library.

Usage
python epistemic_engine.py --text "Your institutional text here"
python epistemic_engine.py --file path/to/document.txt

The engine runs in under two seconds on a standard laptop. API keys are only needed if you are
using an LLM platform as the interface wrapper (GPT o3 or Gemini). The Python kernel itself runs
locally and independently of any AI provider.

Sample Output

A) AUDIT SNAPSHOT

Language game:    corporate_risk_disclosure
Bias gate:        clean
Laundering:       bureaucratic_masking
Learning posture: defensive_routine
Testability:      immunizing_stratagem

B) LOGIC RESULT

Logic type used: clean claim structure — no bias gate fired.
Layer 3 (Laundering):  bureaucratic_masking FIRED
  lex_density (0.038) > 0.02 AND ratio_density (0.041) > 0.02

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

To audit the audit, request:
  "Show full signal densities"
  "Show gate threshold comparisons"
  "Explain bureaucratic_masking flag"

Validation Highlights
The engine was validated against a 69-text corpus. Key findings include:

Kernel Violation Pattern: LLMs correctly compute signals but fail to execute deterministic logic (see docs/KERNEL_VIOLATION_REGISTRY.md).
Register-Mismatch Gradient: Performance (Cohen's κ) drops from 1.000 on synthetic institutional text to 0.053 on informal argumentation (MAFALDA), proving distinct analytical tasks.
Learn More
Thesis: docs/Concepcion_Epistemic_Engine_2026.pdf
Methods: METHODS.md
Examples: demo/ directory
