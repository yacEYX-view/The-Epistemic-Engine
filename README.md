<<<<<<< HEAD
# The Epistemic Engine

Detects epistemic bias in institutional text through abstraction, agency, and power analysis.

## Status: GREEN - On schedule (Feb 2026)

## Quick Start
```bash

=======
# The-Epistemic-Engine

The Epistemic Engine is an epistemic bias auditor that acts as a reasoning spectrograph for text. It takes user‑provided text and produces a multidimensional assessment of abstraction, agency, falsifiability, and power orientation, along with targeted research prompts and a visual plot‑point representation of epistemic bias.

## Table of Contents

- [Project Overview](#project-overview)
- [Current Status](#current-status)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Usage](#usage)
- [Key Accomplishments](#key-accomplishments)
- [Current Focus](#current-focus)
- [Upcoming Milestones](#upcoming-milestones)
- [Repository Structure](#repository-structure)
- [Key Concepts](#key-concepts)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

**The Epistemic Engine**: A Single LLM-as-a-Judge analytic framework that detects epistemic bias in institutional text by measuring psychological distance, rhetorical authority, and linguistic construal.

## Current Status

![Status](https://img.shields.io/badge/status-on--schedule-brightgreen) **On Schedule** — February 2026

✨ **Status**: GREEN - No major issues, on schedule

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yacEYX-view/The-Epistemic-Engine.git
   cd The-Epistemic-Engine
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the core engine**
   ```bash
   python src/mafalda_engine/mafalda_engine.py --input "Your text here"
   ```

4. **Explore the documentation**
   - 📋 [Project Charter](docs/project-charter.md)
   - 📊 [Communication Plan](docs/communication-plan.md)
   - 📚 [Philosophical Framework](docs/framework.md)

## Installation

### Requirements
- Python 3.9+
- Dependencies listed in `requirements.txt`

### Steps

```bash
# Clone the repository
git clone https://github.com/yacEYX-view/The-Epistemic-Engine.git
cd The-Epistemic-Engine

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python src/mafalda_engine/mafalda_engine.py --input "Your institutional text here"
```

### Output

The engine produces:
- **Multidimensional Assessment**: Scores for abstraction, agency, falsifiability, and power orientation
- **Targeted Research Prompts**: Suggestions for deeper analysis
- **Visual Representation**: Plot-point visualization of epistemic bias

### Example

```bash
python src/mafalda_engine/mafalda_engine.py --input "The policy was implemented to optimize operational efficiency." --output results.json
```

## Key Accomplishments

- ✅ **Core Theoretical Framework Complete**
- ✅ **Functional Python Prototype** (`mafalda_engine.py`)
- ✅ **Project Charter Approved** (Jan 30, 2026)
- ✅ **Communication Plan Established** (Feb 16, 2026)

## Current Focus

**Objective 3: Model Validation** — Construction of Gold Standard corpus and annotation study design

## Upcoming Milestones

- 📅 **Week 6 (Feb 27)**: Philosophical Framework Documentation submission
- 📅 **Week 10 (Mar 15)**: Prototype Demonstration to Sponsor

## Repository Structure

```
The-Epistemic-Engine/
├── src/
│   ├── mafalda_engine/          # Core engine modules
│   └── validation/              # Validation datasets and protocols
├── docs/                         # Comprehensive documentation
├── data/
│   └── benchmarks/              # SBC-100 and other datasets
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Key Concepts

- **Epistemic Bias**: Systematic distortions in how knowledge is represented or reasoned about in text
- **Psychological Distance**: How "far" or "near" a concept feels cognitively; influences abstraction level
- **Construal Level**: The abstractness/concreteness of how we think about or represent information
- **Rhetorical Authority**: The degree to which text asserts authority or expertise without evidence
- **Falsifiability**: The extent to which claims in text can be tested or disproven

## Contributing

We welcome contributions! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**For questions or issues**, please open a GitHub Issue or contact the maintainers.
>>>>>>> f94c7881457e1e8f1cdc9c8544368528a208ce7d
