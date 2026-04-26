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
