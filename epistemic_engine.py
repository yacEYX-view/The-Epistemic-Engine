#!/usr/bin/env python3
"""
The Epistemic Engine v2.0.0 — Deterministic Structural Auditor for Institutional Discourse

Implements the full layered logic architecture:
  Layer 0: Structural Extraction (14 signal densities)
  Layer 1: Wittgenstein (Institutional Language Game)
  Layer 2: Popper (Bias Gate Hierarchy & Immunizing Stratagems)
  Layer 3: Authority Laundering (Scientism, Bureaucratic Masking, Identity Laundering)
  Layer 4: Argyris (Learning Logic: Defensive Routines vs Open-Loop)
  Layer 5: Coordinate (HEAD/HEART, DISRUPTION/STABILITY, Amplitude)
  Layer 6: Philosophical Meta-Layer

Spec reference: METHODS.md, Specs_E_E_03_04_26.pdf
"""

import argparse
import json
import math
import re
import sys
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════
# LAYER 0 — STRUCTURAL EXTRACTION: LEXICONS & DENSITY COMPUTATION
# ═══════════════════════════════════════════════════════════════════════

# --- Gate-input lexicons ---

NORMATIVE_CUES = {
    "should", "must", "ought", "need to", "have to", "require", "requires",
    "required", "shall", "obliged", "obligated", "mandate", "mandated",
    "condemn", "condemns", "demand", "demands", "imperative", "duty",
    "compel", "compelled", "forbid", "forbidden", "prohibit", "prohibited",
}

UNIVERSAL_CUES = {
    "always", "never", "all", "none", "every", "everyone", "no one",
    "nobody", "everything", "nothing", "everywhere", "nowhere",
    "entirely", "absolutely", "without exception", "invariably",
    "the x are",  # placeholder pattern handled separately
}
# Blanket patterns: "the [group] are", "all [group]"
UNIVERSAL_PATTERNS = [
    r"\b(the\s+\w+\s+are)\b",
    r"\b(all\s+\w+\s+are)\b",
    r"\b(no\s+\w+\s+(is|are|can|will|would))\b",
    r"\b(every\s+\w+\s+(is|are|must|should))\b",
]

FRAMING_CUES = {
    "evil", "corrupt", "righteous", "immoral", "shameful", "virtuous",
    "heroic", "villainous", "moral", "sinful", "sacred", "profane",
    "disgraceful", "noble", "wicked", "reprehensible", "unconscionable",
    "progress", "regress", "reaction", "reactionary", "enlightened",
    "backward", "abomination", "crusade", "salvation",
}

EVASION_CUES = [
    "not the point", "obviously", "no serious person", "that's ridiculous",
    "everyone knows", "clearly", "as i said", "i already explained",
    "let's move on", "beside the point", "irrelevant", "off topic",
    "that's a strawman", "you're missing the point", "nice try",
    "not worth responding", "the real issue", "what really matters",
    # v2.0 — colloquial/political register extensions
    "is broken", "is a disaster", "was a disaster", "has failed",
    "run out of excuses", "out of excuses", "enough is enough",
    "wake up", "open your eyes", "get real",
]

# --- Coordinate-input lexicons ---

HEAD_CUES = {
    "definition", "definitions", "mechanism", "mechanisms", "causal",
    "causality", "cause", "effect", "correlation", "measurement",
    "measure", "measured", "analysis", "analytical", "hypothesis",
    "variable", "variables", "coefficient", "regression", "model",
    "formula", "equation", "theorem", "proof", "derive", "derived",
    "calculation", "computed", "algorithm", "systematic", "methodology",
    "empirical", "observation", "experiment", "experimental", "evidence",
    "quantitative", "parameter", "parameters", "factor", "factors",
    "function", "structure", "structural", "logic", "logical",
    "framework", "criterion", "criteria", "taxonomy", "classify",
    "classification", "diagnose", "diagnosis", "inference",
}

HEART_CUES = {
    "outrage", "outraged", "contempt", "fear", "afraid", "terrified",
    "terror", "horrified", "horrifying", "disgust", "disgusting",
    "dignity", "indignity", "insult", "insulting", "shame", "shamed",
    "humiliation", "humiliated", "anger", "angry", "furious", "rage",
    "suffering", "pain", "anguish", "despair", "hopeless", "betrayal",
    "betrayed", "injustice", "oppression", "oppressed", "victim",
    "victimized", "solidarity", "compassion", "empathy", "grief",
    "mourning", "trauma", "traumatic", "devastating", "heartbreaking",
    "us", "them", "our people", "those people", "we must stand",
    "fight for", "enemy", "enemies", "ally", "allies", "patriot",
}

DISRUPTION_CUES = {
    "collapse", "overthrow", "break", "broken", "catastrophe",
    "catastrophic", "crisis", "radical", "revolution", "revolutionary",
    "transformation", "transform", "disrupt", "disruption", "disruptive",
    "unprecedented", "emergency", "urgent", "urgently", "overhaul",
    "abolish", "abolition", "destroy", "destruction", "upend",
    "shatter", "tear down", "rebuild", "reimagine", "rethink",
    "rupture", "seismic", "paradigm shift", "existential threat",
    "turning point", "tipping point", "point of no return",
}

STABILITY_CUES = {
    "tradition", "traditional", "restore", "restored", "maintain",
    "maintained", "continuity", "safeguard", "safeguards", "preserve",
    "preservation", "conserve", "conservation", "protect", "protection",
    "stability", "stable", "steady", "order", "orderly", "heritage",
    "legacy", "enduring", "time-tested", "proven", "established",
    "institution", "institutional", "foundation", "foundational",
    "precedent", "norm", "norms", "standard", "standards", "custom",
    "customs", "reliability", "reliable", "consistent", "consistency",
    "anchor", "anchored", "bedrock", "cornerstone",
}

# v2.0 — Procedural-neutral terms that should NOT count as stability cues.
# These are common in regulatory writing and do not indicate stability advocacy.
STABILITY_EXCLUSIONS = {
    "scheduled", "routine", "annual", "quarterly", "pursuant",
    "filed", "filing", "filings", "submitted", "periodic",
    "deadline", "deadlines", "compliance", "compliant",
    "in accordance with", "pursuant to",
}

# --- Laundering-input lexicons ---

RATIO_CUES = {
    "percent", "percentage", "%", "rate", "rates", "ratio", "chart",
    "charts", "graph", "graphs", "figure", "figures", "table", "tables",
    "data", "dataset", "statistic", "statistics", "statistical",
    "projection", "projections", "forecast", "trend", "trends",
    "metric", "metrics", "index", "score", "baseline", "benchmark",
    "quartile", "decile", "percentile", "median", "mean", "average",
    "standard deviation", "variance", "the data show", "the numbers",
    "studies show", "research shows", "according to data",
}

ETHOS_CUES = {
    "expert", "experts", "authority", "authorities", "institution",
    "institutions", "credential", "credentials", "certified",
    "accredited", "peer-reviewed", "peer reviewed", "published",
    "renowned", "prestigious", "leading", "world-class", "eminent",
    "distinguished", "professor", "dr.", "ph.d", "scientist",
    "scientists", "researcher", "researchers", "scholar", "scholars",
    "science says", "experts agree", "the science is clear",
    "the committee", "the board", "the agency", "the commission",
    "according to experts", "studies confirm", "harvard", "mit",
    "stanford", "oxford", "cambridge",
}

LEX_CUES = {
    "framework", "frameworks", "stakeholder", "stakeholders",
    "compliance", "implementation", "governance", "mandate",
    "protocol", "protocols", "deliverable", "deliverables",
    "operationalize", "operationalized", "leverage", "leveraging",
    "synergy", "synergies", "best practice", "best practices",
    "ecosystem", "holistic", "paradigm", "methodology", "metrics",
    "scalable", "sustainable", "accountability", "alignment",
    "capacity building", "optimization", "strategic", "initiative",
    "initiatives", "outcome", "outcomes", "impact", "roadmap",
    "actionable", "robust", "streamline", "streamlined",
}

PATHOS_CUES = {
    "alarm", "alarming", "alarmed", "disgust", "disgusting",
    "disgusted", "ridicule", "ridiculous", "absurd", "laughable",
    "triumph", "triumphant", "glorious", "glory", "shocking",
    "shocked", "horrific", "horrifying", "terrifying", "chilling",
    "heartwarming", "inspiring", "moved", "touching", "moving",
    "devastating", "jubilant", "elated",
    "outrageous", "unbelievable", "incredible", "astounding",
    "appalling", "monstrous", "hideous", "revolting",
}

# --- Reasoning-input lexicons ---

LOGOS_CUES = {
    "therefore", "because", "hence", "thus", "consequently",
    "implies", "imply", "follows", "it follows", "given that",
    "for this reason", "as a result", "accordingly", "so that",
    "in order to", "if then", "assuming", "suppose", "granted",
    "since", "whereas", "insofar as", "provided that",
    "on the grounds that", "due to", "owing to",
}

# --- Falsifiability cue detection ---

VAGUENESS_CUES = {
    "systemic", "inevitable", "inherent", "inherently", "fundamentally",
    "essentially", "in principle", "by nature", "by definition",
}

UNFALSIFIABLE_CUES = {
    "no evidence would change", "nothing can disprove", "proves itself",
    "self-evident", "beyond question", "undeniable", "unquestionable",
    "irrefutable", "indisputable",
}

SHIFTING_CRITERIA_CUES = {
    "if it fails that proves", "if it works that proves",
    "either way this shows", "heads i win tails you lose",
    "whatever happens", "no matter what",
}


def _tokenize(text: str) -> list[str]:
    """Simple whitespace + punctuation-aware tokenizer."""
    return re.findall(r"\b[\w'%.-]+\b", text.lower())


def _count_cues(text: str, tokens: list[str], cue_set: set) -> int:
    """Count occurrences of cue words/phrases in text."""
    text_lower = text.lower()
    count = 0
    # Multi-word phrases first
    multi_word = [c for c in cue_set if " " in c]
    for phrase in multi_word:
        count += text_lower.count(phrase)
    # Single-word cues
    single_word = {c for c in cue_set if " " not in c}
    for token in tokens:
        if token in single_word:
            count += 1
    return count


def _count_patterns(text: str, patterns: list[str]) -> int:
    """Count regex pattern matches."""
    text_lower = text.lower()
    count = 0
    for pat in patterns:
        count += len(re.findall(pat, text_lower))
    return count


def _count_evasions(text: str) -> int:
    """Count evasion moves (phrase-level matching)."""
    text_lower = text.lower()
    count = 0
    for phrase in EVASION_CUES:
        count += text_lower.count(phrase)
    return count


def _detect_falsifiability_low(text: str) -> bool:
    """Detect if core claims are structurally hard to test."""
    text_lower = text.lower()
    vague = sum(1 for c in VAGUENESS_CUES if c in text_lower)
    unfals = sum(1 for c in UNFALSIFIABLE_CUES if c in text_lower)
    shifting = sum(1 for c in SHIFTING_CRITERIA_CUES if c in text_lower)
    # Also check for totalizing group attributions via universal patterns
    totalizing = _count_patterns(text, UNIVERSAL_PATTERNS)
    return (vague >= 2) or (unfals >= 1) or (shifting >= 1) or (totalizing >= 2)


def extract_signals(text: str) -> dict:
    """
    Layer 0: Structural Extraction.
    Extract all signal densities and counts from raw text.
    """
    tokens = _tokenize(text)
    n = max(len(tokens), 1)

    evasion_count = _count_evasions(text)
    falsifiability_low = _detect_falsifiability_low(text)

    normative_raw = _count_cues(text, tokens, NORMATIVE_CUES)
    universal_raw = (_count_cues(text, tokens, UNIVERSAL_CUES)
                     + _count_patterns(text, UNIVERSAL_PATTERNS))
    framing_raw = _count_cues(text, tokens, FRAMING_CUES)

    head_raw = _count_cues(text, tokens, HEAD_CUES)
    heart_raw = _count_cues(text, tokens, HEART_CUES)
    disruption_raw = _count_cues(text, tokens, DISRUPTION_CUES)
    stability_raw = _count_cues(text, tokens, STABILITY_CUES)
    # v2.0 — subtract procedural-neutral false positives
    stability_excl = _count_cues(text, tokens, STABILITY_EXCLUSIONS)
    stability_raw = max(0, stability_raw - stability_excl)

    ratio_raw = _count_cues(text, tokens, RATIO_CUES)
    ethos_raw = _count_cues(text, tokens, ETHOS_CUES)
    lex_raw = _count_cues(text, tokens, LEX_CUES)
    pathos_raw = _count_cues(text, tokens, PATHOS_CUES)
    logos_raw = _count_cues(text, tokens, LOGOS_CUES)

    return {
        "evasion_count": evasion_count,
        "falsifiability_low": falsifiability_low,
        "normative_density": round(normative_raw / n, 4),
        "universal_density": round(universal_raw / n, 4),
        "framing_density": round(framing_raw / n, 4),
        "head_density": round(head_raw / n, 4),
        "heart_density": round(heart_raw / n, 4),
        "disruption_density": round(disruption_raw / n, 4),
        "stability_density": round(stability_raw / n, 4),
        "ratio_density": round(ratio_raw / n, 4),
        "ethos_density": round(ethos_raw / n, 4),
        "lex_density": round(lex_raw / n, 4),
        "pathos_density": round(pathos_raw / n, 4),
        "logos_density": round(logos_raw / n, 4),
        # Raw counts for drill-down
        "_counts": {
            "tokens": n,
            "evasion": evasion_count,
            "normative": normative_raw,
            "universal": universal_raw,
            "framing": framing_raw,
            "head": head_raw,
            "heart": heart_raw,
            "disruption": disruption_raw,
            "stability": stability_raw,
            "ratio": ratio_raw,
            "ethos": ethos_raw,
            "lex": lex_raw,
            "pathos": pathos_raw,
            "logos": logos_raw,
        },
    }


# ═══════════════════════════════════════════════════════════════════════
# LAYER 1 — WITTGENSTEIN: INSTITUTIONAL LANGUAGE GAME
# ═══════════════════════════════════════════════════════════════════════

GAME_TYPE_KEYWORDS = {
    "policy defense": ["policy", "compliance", "regulation", "regulatory", "mandate"],
    "PR statement": ["proud", "committed", "excited", "pleased", "announce", "brand"],
    "scientific justification": ["study", "studies", "findings", "research", "evidence", "data"],
    "polemic": ["fight", "enemy", "battle", "resist", "demand", "oppose"],
    "corporate risk disclosure": ["risk", "material", "disclosure", "filing", "sec", "audit"],
    "editorial advocacy": ["opinion", "believe", "argue", "column", "editorial"],
    "legislative persuasion": ["bill", "legislation", "vote", "congress", "law", "statute"],
}


def detect_language_game(text: str) -> dict:
    """Layer 1: Classify the institutional language game."""
    text_lower = text.lower()
    scores = {}
    for game, keywords in GAME_TYPE_KEYWORDS.items():
        scores[game] = sum(1 for kw in keywords if kw in text_lower)
    best = max(scores, key=scores.get) if max(scores.values()) > 0 else "institutional discourse (unspecified)"
    return {
        "institutional_language_game": True,
        "game_type": best,
        "game_scores": {k: v for k, v in scores.items() if v > 0},
    }


# ═══════════════════════════════════════════════════════════════════════
# LAYER 2 — POPPER: BIAS GATE HIERARCHY
# ═══════════════════════════════════════════════════════════════════════

def run_bias_gate(signals: dict) -> dict:
    """
    Deterministic bias gate — fixed evaluation order.
    Returns classification and the gate that fired (if any).
    """
    ec = signals["evasion_count"]
    nd = signals["normative_density"]
    ud = signals["universal_density"]
    fl = signals["falsifiability_low"]
    fd = signals["framing_density"]

    if ec >= 2:
        return {
            "classification": "evasion",
            "gate_fired": "evasion_gate",
            "reason": f"evasion_count = {ec} (>= 2)",
        }
    elif (nd > 0.05 or ud > 0.02) and fl:
        parts = []
        if nd > 0.05:
            parts.append(f"normative_density = {nd:.4f} (> 0.05)")
        if ud > 0.02:
            parts.append(f"universal_density = {ud:.4f} (> 0.02)")
        parts.append("falsifiability_low = True")
        return {
            "classification": "ideological",
            "gate_fired": "ideological_gate",
            "reason": " AND ".join(parts),
        }
    elif fd > 0.02:
        return {
            "classification": "moral_framing",
            "gate_fired": "moral_framing_gate",
            "reason": f"framing_density = {fd:.4f} (> 0.02)",
        }
    else:
        return {
            "classification": "clean",
            "gate_fired": None,
            "reason": "No gate fired",
        }


def popper_label(classification: str) -> str:
    """Testability label (Popper)."""
    if classification != "clean":
        return "immunizing_stratagem"
    return "falsifiable_claim_structure"


# ═══════════════════════════════════════════════════════════════════════
# LAYER 3 — AUTHORITY LAUNDERING FLAGS
# ═══════════════════════════════════════════════════════════════════════

def detect_laundering(signals: dict) -> dict:
    """Detect authority laundering flags. Multiple can fire."""
    rd = signals["ratio_density"]
    ed = signals["ethos_density"]
    ld = signals["lex_density"]
    pd = signals["pathos_density"]
    ec = signals["evasion_count"]

    flags = {}

    if rd > 0.02 and ed > 0.02:
        flags["scientism"] = (
            f"ratio_density = {rd:.4f} (> 0.02) AND ethos_density = {ed:.4f} (> 0.02)"
        )

    if ld > 0.02 and rd > 0.02:
        flags["bureaucratic_masking"] = (
            f"lex_density = {ld:.4f} (> 0.02) AND ratio_density = {rd:.4f} (> 0.02)"
        )

    if ed > 0.03 and (pd > 0.02 or ec >= 2):
        parts = [f"ethos_density = {ed:.4f} (> 0.03)"]
        if pd > 0.02:
            parts.append(f"pathos_density = {pd:.4f} (> 0.02)")
        if ec >= 2:
            parts.append(f"evasion_count = {ec} (>= 2)")
        flags["identity_laundering"] = " AND ".join(parts)

    return {
        "laundering_present": len(flags) > 0,
        "flags": flags,
    }


# ═══════════════════════════════════════════════════════════════════════
# LAYER 4 — ARGYRIS: LEARNING LOGIC
# ═══════════════════════════════════════════════════════════════════════

def argyris_label(laundering_present: bool) -> str:
    """Learning posture (Argyris)."""
    if laundering_present:
        return "defensive_routine"
    return "open_loop_reasoning"


# ═══════════════════════════════════════════════════════════════════════
# LAYER 5 — COORDINATE LAYER
# ═══════════════════════════════════════════════════════════════════════

def compute_coordinates(signals: dict) -> dict:
    """
    Compute HEAD/HEART (Y), DISRUPTION/STABILITY (X), Intensity, Quadrant.
    """
    hd = signals["head_density"]
    ht = signals["heart_density"]
    dd = signals["disruption_density"]
    sd = signals["stability_density"]

    Y_raw = (hd - ht) * 10
    X_raw = (dd - sd) * 10

    Y = max(-10, min(10, Y_raw))
    X = max(-10, min(10, X_raw))

    intensity = (math.sqrt(X ** 2 + Y ** 2) / math.sqrt(200)) * 10
    intensity = round(max(0, min(10, intensity)), 2)

    # Quadrant
    if abs(X) < 3 and abs(Y) < 3:
        quadrant = "CLEAN"
    elif X <= 0 and Y >= 0:
        quadrant = "Q1"  # HEAD + STABILITY
    elif X > 0 and Y >= 0:
        quadrant = "Q2"  # HEAD + DISRUPTION
    elif X <= 0 and Y < 0:
        quadrant = "Q3"  # HEART + STABILITY
    else:
        quadrant = "Q4"  # HEART + DISRUPTION

    return {
        "X": round(X, 2),
        "Y": round(Y, 2),
        "intensity": intensity,
        "quadrant": quadrant,
    }


# ═══════════════════════════════════════════════════════════════════════
# SPECTROGRAPH RENDERER
# ═══════════════════════════════════════════════════════════════════════

def render_spectrograph(X: float, Y: float) -> str:
    """
    Deterministic 5x5 ASCII spectrograph.
    dx = clamp(round(X/5), -2, 2)
    dy = clamp(round(Y/5), -2, 2)
    """
    dx = max(-2, min(2, round(X / 5)))
    dy = max(-2, min(2, round(Y / 5)))

    # Grid: row 0 = top (HEAD+), row 4 = bottom (HEART-)
    # Col 0 = left (STAB-), col 4 = right (DISR+)
    # Center is (2, 2), star goes to (2 + dx, 2 - dy)
    star_col = 2 + dx
    star_row = 2 - dy

    lines = []
    lines.append("        HEAD (+)")
    lines.append("           |")

    labels_left = ["    Q1", "      ", "STAB <", "      ", "    Q3"]
    labels_right = ["Q2", "  ", "> DISR", "  ", "Q4"]
    mid_markers = [" ", " ", "-", " ", " "]

    for r in range(5):
        row_chars = []
        for c in range(5):
            if r == star_row and c == star_col:
                row_chars.append("★")
            elif r == 2 and c == 2:
                row_chars.append("+")
            elif r == 2:
                row_chars.append("-")
            elif c == 2:
                row_chars.append("|")
            else:
                row_chars.append(" ")
        grid_str = " ".join(row_chars)

        if r == 0:
            lines.append(f"    Q1     {grid_str}     Q2")
        elif r == 1:
            lines.append(f"           {grid_str}")
        elif r == 2:
            lines.append(f"STAB <---- {grid_str} ----> DISR")
        elif r == 3:
            lines.append(f"           {grid_str}")
        elif r == 4:
            lines.append(f"    Q3     {grid_str}     Q4")

    lines.append("           |")
    lines.append("       HEART (-)")

    return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════
# FULL AUDIT PIPELINE
# ═══════════════════════════════════════════════════════════════════════

def audit(text: Optional[str] = None, measures: Optional[dict] = None) -> dict:
    """
    Run the full audit pipeline.
    Mode 1 (measures): supply a measures dict with all signals.
    Mode 2 (raw-text): supply text, signals are estimated.
    """
    estimated = False

    if measures is not None:
        signals = measures
    elif text is not None:
        signals = extract_signals(text)
        estimated = True
    else:
        raise ValueError("Provide either text or measures.")

    # Layer 1: Language game
    if text:
        lang_game = detect_language_game(text)
    else:
        lang_game = {"institutional_language_game": True, "game_type": "unknown (measures mode)"}

    # Layer 2: Bias gate
    gate_result = run_bias_gate(signals)
    classification = gate_result["classification"]
    testability = popper_label(classification)

    # Layer 3: Laundering
    laundering = detect_laundering(signals)

    # Layer 4: Argyris
    learning = argyris_label(laundering["laundering_present"])

    # Layer 5: Coordinates
    coords = compute_coordinates(signals)

    # Spectrograph
    spectrograph = render_spectrograph(coords["X"], coords["Y"])

    return {
        "estimated": estimated,
        "signals": signals,
        "language_game": lang_game,
        "gate_result": gate_result,
        "classification": classification,
        "testability": testability,
        "laundering": laundering,
        "learning_posture": learning,
        "coordinates": coords,
        "spectrograph": spectrograph,
    }


# ═══════════════════════════════════════════════════════════════════════
# OUTPUT FORMATTER — Spec-compliant sections A–D + drill-downs
# ═══════════════════════════════════════════════════════════════════════

QUAD_LABELS = {
    "Q1": "HEAD-coded + STABILITY-coded",
    "Q2": "HEAD-coded + DISRUPTION-coded",
    "Q3": "HEART-coded + STABILITY-coded",
    "Q4": "HEART-coded + DISRUPTION-coded",
    "CLEAN": "near-center (low rhetorical commitment)",
}


def format_audit(result: dict, drilldown: Optional[list[int]] = None) -> str:
    """
    Format the audit output per spec.
    If drilldown is None: output sections A–D.
    If drilldown is a list of ints (1–7): output only those sections + spectrograph.
    """
    out = []

    cls = result["classification"]
    coords = result["coordinates"]
    laundering = result["laundering"]
    learning = result["learning_posture"]
    testability = result["testability"]
    lang_game = result["language_game"]
    gate = result["gate_result"]
    signals = result["signals"]

    estimated_note = " Measures are estimated." if result["estimated"] else ""

    # ── DRILL-DOWN MODE ──
    if drilldown:
        for item in drilldown:
            if item == 1:
                out.append("── 1) Language game ──")
                out.append(f"Institutional language game: {lang_game['game_type']}.")
                if "game_scores" in lang_game:
                    for g, s in lang_game["game_scores"].items():
                        out.append(f"  {g}: {s} cue(s)")
                out.append(f"All text is treated as institutional discourse (Wittgenstein).")
                out.append("")

            elif item == 2:
                out.append("── 2) Argument skeleton ──")
                out.append(f"Classification: {cls}")
                out.append(f"Gate fired: {gate['gate_fired'] or 'none'}")
                out.append(f"Reason: {gate['reason']}")
                out.append(f"Testability: {testability.replace('_', ' ')}")
                out.append(f"Learning posture: {learning.replace('_', ' ')}")
                out.append("")

            elif item == 3:
                out.append("── 3) Falsifiability and self-protection ──")
                out.append(f"Popper marker: {testability.replace('_', ' ')}")
                out.append(f"Falsifiability_low: {signals.get('falsifiability_low', 'N/A')}")
                out.append(f"Evasion count: {signals.get('evasion_count', 0)}")
                if cls == "clean":
                    out.append("The claim structure is open to empirical or logical refutation.")
                else:
                    out.append(f"The text deploys an immunizing stratagem via the {gate['gate_fired'] or 'bias gate'}.")
                out.append("")

            elif item == 4:
                out.append("── 4) Authority laundering excerpts ──")
                if laundering["flags"]:
                    for flag, reason in laundering["flags"].items():
                        out.append(f"  [{flag}] {reason}")
                else:
                    out.append("  No authority laundering flags triggered.")
                out.append("")

            elif item == 5:
                out.append("── 5) Learning posture ──")
                out.append(f"Argyris marker: {learning.replace('_', ' ')}")
                if learning == "defensive_routine":
                    out.append("The text structurally protects current assumptions from revision (single-loop).")
                    out.append("Laundering flags present → defensive routine classification.")
                else:
                    out.append("The text is structurally compatible with questioning governing assumptions (double-loop).")
                    out.append("No laundering flags → open-loop reasoning classification.")
                out.append("")

            elif item == 6:
                out.append("── 6) Deterministic readout (proof) ──")
                out.append(f"  evasion_count       = {signals.get('evasion_count', 'N/A')}")
                out.append(f"  falsifiability_low  = {signals.get('falsifiability_low', 'N/A')}")
                out.append(f"  normative_density   = {signals.get('normative_density', 'N/A')}")
                out.append(f"  universal_density   = {signals.get('universal_density', 'N/A')}")
                out.append(f"  framing_density     = {signals.get('framing_density', 'N/A')}")
                out.append(f"  head_density        = {signals.get('head_density', 'N/A')}")
                out.append(f"  heart_density       = {signals.get('heart_density', 'N/A')}")
                out.append(f"  disruption_density  = {signals.get('disruption_density', 'N/A')}")
                out.append(f"  stability_density   = {signals.get('stability_density', 'N/A')}")
                out.append(f"  ratio_density       = {signals.get('ratio_density', 'N/A')}")
                out.append(f"  ethos_density       = {signals.get('ethos_density', 'N/A')}")
                out.append(f"  lex_density         = {signals.get('lex_density', 'N/A')}")
                out.append(f"  pathos_density      = {signals.get('pathos_density', 'N/A')}")
                out.append(f"  logos_density       = {signals.get('logos_density', 'N/A')}")
                out.append(f"  ---")
                out.append(f"  Gate: {gate['gate_fired'] or 'none'} → classification = {cls}")
                out.append(f"  Y = ({signals.get('head_density','?')} - {signals.get('heart_density','?')}) × 10 = {coords['Y']}")
                out.append(f"  X = ({signals.get('disruption_density','?')} - {signals.get('stability_density','?')}) × 10 = {coords['X']}")
                out.append(f"  Intensity = {coords['intensity']}")
                out.append(f"  Quadrant = {coords['quadrant']}")
                flags_str = ", ".join(laundering["flags"].keys()) if laundering["flags"] else "none"
                out.append(f"  Laundering flags: {flags_str}")
                out.append(f"  Argyris: {learning.replace('_', ' ')}")
                out.append(f"  Popper: {testability.replace('_', ' ')}")
                if result["estimated"]:
                    out.append(f"  Measures are estimated.")
                out.append("")

            elif item == 7:
                out.append("── 7) What would change the conclusion ──")
                if cls == "evasion":
                    out.append("Reduce evasion_count below 2 (remove deflections like 'not the point,' 'obviously').")
                elif cls == "ideological":
                    out.append("Either lower normative_density below 0.05 AND universal_density below 0.02,")
                    out.append("or make core claims explicitly falsifiable (falsifiability_low → False).")
                elif cls == "moral_framing":
                    out.append("Reduce framing_density below 0.02 (replace virtue/vice labels with testable descriptions).")
                else:
                    out.append("Currently clean. Classification would change if:")
                    out.append("  - evasion_count reaches 2+, or")
                    out.append("  - normative/universal density rises with low falsifiability, or")
                    out.append("  - framing_density exceeds 0.02.")
                if laundering["flags"]:
                    out.append("To clear laundering flags:")
                    if "scientism" in laundering["flags"]:
                        out.append("  - Scientism: lower ratio_density or ethos_density below 0.02.")
                    if "bureaucratic_masking" in laundering["flags"]:
                        out.append("  - Bureaucratic masking: lower lex_density or ratio_density below 0.02.")
                    if "identity_laundering" in laundering["flags"]:
                        out.append("  - Identity laundering: lower ethos_density below 0.03, or lower pathos + evasion.")
                out.append("")

        # Always append spectrograph after drill-down
        out.append("── SPECTROGRAPH ──")
        out.append(result["spectrograph"])
        out.append(f"X = {coords['X']}, Y = {coords['Y']}, Intensity = {coords['intensity']}")
        return "\n".join(out)

    # ── STANDARD OUTPUT (A–D) ──

    # A) Five-sentence audit snapshot
    out.append("A) AUDIT SNAPSHOT")
    out.append("")

    quad_label = QUAD_LABELS.get(coords["quadrant"], coords["quadrant"])
    flags_list = list(laundering["flags"].keys())
    flags_str = ", ".join(flags_list) if flags_list else "none"

    s1 = f"The text operates as {lang_game['game_type']} within an institutional language game."
    s2 = f"Bias gate classification: {cls} ({gate['reason']})."
    s3 = f"The discourse sits in {coords['quadrant']} ({quad_label}) at intensity {coords['intensity']}/10."
    s4 = f"Authority laundering flags: {flags_str}; learning posture: {learning.replace('_', ' ')}."
    s5 = f"Testability label: {testability.replace('_', ' ')}.{estimated_note}"

    out.append(s1)
    out.append(s2)
    out.append(s3)
    out.append(s4)
    out.append(s5)
    out.append("")

    # B) One-line logic result
    out.append("B) LOGIC RESULT")
    out.append("")
    if cls != "clean":
        out.append(f"Logic flaws detected: {cls} via {gate['gate_fired']} — {gate['reason']}.")
    else:
        out.append(f"Logic type used: clean claim structure — no bias gate fired.")
    out.append("")

    # C) Spectrograph + three sentences
    out.append("C) SPECTROGRAPH")
    out.append("")
    out.append(result["spectrograph"])
    out.append("")
    out.append(f"X = {coords['X']} (DISRUPTION − STABILITY scaled ×10): {'disruption-leaning' if coords['X'] > 0 else 'stability-leaning' if coords['X'] < 0 else 'balanced'}.")
    out.append(f"Y = {coords['Y']} (HEAD − HEART scaled ×10): {'head-coded (analytic)' if coords['Y'] > 0 else 'heart-coded (emotive)' if coords['Y'] < 0 else 'balanced'}.")
    out.append(f"Intensity = {coords['intensity']}/10: {'high rhetorical commitment' if coords['intensity'] > 6 else 'moderate commitment' if coords['intensity'] > 3 else 'low commitment'}.")
    out.append("")

    # D) Ask-for menu
    out.append("D) ASK-FOR MENU")
    out.append("")
    out.append("1) Language game")
    out.append("2) Argument skeleton")
    out.append("3) Falsifiability and self-protection")
    out.append("4) Authority laundering excerpts")
    out.append("5) Learning posture")
    out.append("6) Deterministic readout (proof)")
    out.append("7) What would change the conclusion")

    return "\n".join(out)


# ═══════════════════════════════════════════════════════════════════════
# MEASURES-MODE PARSER
# ═══════════════════════════════════════════════════════════════════════

def parse_measures(measures_str: str) -> dict:
    """Parse a measures block (key: value lines) into a signal dict."""
    signals = {}
    for line in measures_str.strip().splitlines():
        line = line.strip().lstrip("- ")
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()

        if key == "evasion_count":
            signals[key] = int(val)
        elif key == "falsifiability_low":
            signals[key] = val.lower() in ("true", "yes", "1")
        else:
            try:
                signals[key] = float(val)
            except ValueError:
                pass
    return signals


# ═══════════════════════════════════════════════════════════════════════
# JSON OUTPUT
# ═══════════════════════════════════════════════════════════════════════

def audit_to_json(result: dict) -> str:
    """Serialize audit result to JSON (excluding spectrograph ASCII)."""
    export = {
        "estimated": result["estimated"],
        "classification": result["classification"],
        "testability": result["testability"],
        "learning_posture": result["learning_posture"],
        "gate_result": result["gate_result"],
        "laundering": {
            "present": result["laundering"]["laundering_present"],
            "flags": list(result["laundering"]["flags"].keys()),
        },
        "coordinates": result["coordinates"],
        "language_game": {
            "type": result["language_game"]["game_type"],
        },
        "signals": {k: v for k, v in result["signals"].items() if not k.startswith("_")},
    }
    return json.dumps(export, indent=2)


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="The Epistemic Engine v2.0.0 — Deterministic Discourse Auditor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Modes:
  Raw-text:   --text "The policy must be implemented..."
  Measures:   --measures "evasion_count: 3\\nfalsifiability_low: true\\n..."
  File:       --file input.txt

Drill-down:
  --drilldown 1,3,6   (comma-separated menu items 1-7)

Output:
  --format text|json   (default: text)

Examples:
  python epistemic_engine.py --text "We must act now. The crisis is inevitable."
  python epistemic_engine.py --file speech.txt --drilldown 2,6
  python epistemic_engine.py --measures "evasion_count: 3" --format json
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="Raw text to audit")
    group.add_argument("--file", type=str, help="Path to text file to audit")
    group.add_argument("--measures", type=str, help="Signal measures (key: value, newline-separated)")

    parser.add_argument(
        "--format", type=str, choices=["text", "json"], default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--drilldown", type=str, default=None,
        help="Comma-separated drill-down items (1-7)",
    )

    args = parser.parse_args()

    # Parse drill-down
    dd = None
    if args.drilldown:
        dd = [int(x.strip()) for x in args.drilldown.split(",") if x.strip().isdigit()]

    try:
        if args.measures:
            signals = parse_measures(args.measures)
            result = audit(measures=signals)
        else:
            if args.file:
                with open(args.file, "r", encoding="utf-8") as f:
                    text = f.read()
            else:
                text = args.text
            if not text or not text.strip():
                print("Error: Input text cannot be empty.", file=sys.stderr)
                sys.exit(1)
            result = audit(text=text)

        if args.format == "json":
            print(audit_to_json(result))
        else:
            print(format_audit(result, drilldown=dd))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
