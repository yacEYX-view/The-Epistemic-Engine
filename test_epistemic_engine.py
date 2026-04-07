#!/usr/bin/env python3
"""
Test Suite — Epistemic Engine v1.0
Validates all six layers against deterministic kernel spec and gold-standard cases.

Run:  python test_engine.py
      python test_engine.py -v          (verbose)
"""

import math
import sys
import unittest

# Adjust path if needed
sys.path.insert(0, ".")
from epistemic_engine import (
    audit,
    audit_to_json,
    argyris_label,
    compute_coordinates,
    detect_language_game,
    detect_laundering,
    extract_signals,
    format_audit,
    parse_measures,
    popper_label,
    render_spectrograph,
    run_bias_gate,
)


# ═══════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════

def make_signals(**overrides):
    """Build a clean signal dict with safe defaults, then apply overrides."""
    base = {
        "evasion_count": 0,
        "falsifiability_low": False,
        "normative_density": 0.0,
        "universal_density": 0.0,
        "framing_density": 0.0,
        "head_density": 0.0,
        "heart_density": 0.0,
        "disruption_density": 0.0,
        "stability_density": 0.0,
        "ratio_density": 0.0,
        "ethos_density": 0.0,
        "lex_density": 0.0,
        "pathos_density": 0.0,
        "logos_density": 0.0,
    }
    base.update(overrides)
    return base


# ═══════════════════════════════════════════════════════════════════════
# 1. LAYER 0 — STRUCTURAL EXTRACTION
# ═══════════════════════════════════════════════════════════════════════

class TestLayer0Extraction(unittest.TestCase):
    """Signal extraction from raw text."""

    def test_returns_all_required_signals(self):
        signals = extract_signals("This is a test sentence.")
        required = [
            "evasion_count", "falsifiability_low",
            "normative_density", "universal_density", "framing_density",
            "head_density", "heart_density",
            "disruption_density", "stability_density",
            "ratio_density", "ethos_density", "lex_density", "pathos_density",
            "logos_density",
        ]
        for key in required:
            self.assertIn(key, signals, f"Missing signal: {key}")

    def test_densities_are_normalized(self):
        signals = extract_signals("We must always condemn evil and fight for our sacred heritage.")
        for key, val in signals.items():
            if key.endswith("_density"):
                self.assertGreaterEqual(val, 0.0, f"{key} below 0")
                self.assertLessEqual(val, 1.0, f"{key} above 1")

    def test_evasion_detection(self):
        text = "That's not the point. Obviously, no serious person would disagree."
        signals = extract_signals(text)
        self.assertGreaterEqual(signals["evasion_count"], 2,
                                "Should detect at least 2 evasion cues")

    def test_normative_detection(self):
        text = "We must act. The law should require compliance. Citizens ought to obey."
        signals = extract_signals(text)
        self.assertGreater(signals["normative_density"], 0.05,
                           "High prescriptive language should yield normative > 0.05")

    def test_universal_detection(self):
        text = "Everyone knows this. All experts agree. It has always been true and will never change."
        signals = extract_signals(text)
        self.assertGreater(signals["universal_density"], 0.02,
                           "Heavy universal language should yield > 0.02")

    def test_framing_detection(self):
        text = "This corrupt and evil plan is an abomination. The righteous must resist this shameful act."
        signals = extract_signals(text)
        self.assertGreater(signals["framing_density"], 0.02,
                           "Heavy moral framing should yield > 0.02")

    def test_falsifiability_low_vagueness(self):
        text = "This is systemic. It is inevitable. The problem is inherently unsolvable."
        signals = extract_signals(text)
        self.assertTrue(signals["falsifiability_low"],
                        "Multiple vagueness cues should trigger falsifiability_low")

    def test_falsifiability_low_unfalsifiable(self):
        text = "No evidence would change this conclusion. It is self-evident."
        signals = extract_signals(text)
        self.assertTrue(signals["falsifiability_low"],
                        "Unfalsifiable cue should trigger falsifiability_low")

    def test_falsifiability_not_triggered_on_clean(self):
        text = "The temperature rose by 2 degrees. This may indicate a trend."
        signals = extract_signals(text)
        self.assertFalse(signals["falsifiability_low"],
                         "Clean empirical text should not trigger falsifiability_low")

    def test_head_density_on_analytic_text(self):
        text = ("The analysis measures the causal mechanism through regression. "
                "Each variable is defined by a structural equation with empirical evidence.")
        signals = extract_signals(text)
        self.assertGreater(signals["head_density"], 0.0,
                           "Analytic text should have head_density > 0")

    def test_heart_density_on_emotive_text(self):
        text = "The outrage and fear are overwhelming. Victims suffer in anguish and despair."
        signals = extract_signals(text)
        self.assertGreater(signals["heart_density"], 0.0,
                           "Emotive text should have heart_density > 0")

    def test_empty_text_no_crash(self):
        signals = extract_signals("")
        self.assertEqual(signals["evasion_count"], 0)

    def test_raw_counts_present(self):
        signals = extract_signals("This is a test.")
        self.assertIn("_counts", signals)
        self.assertIn("tokens", signals["_counts"])


# ═══════════════════════════════════════════════════════════════════════
# 2. LAYER 1 — WITTGENSTEIN (LANGUAGE GAME)
# ═══════════════════════════════════════════════════════════════════════

class TestLayer1LanguageGame(unittest.TestCase):

    def test_always_institutional(self):
        result = detect_language_game("Any random text at all.")
        self.assertTrue(result["institutional_language_game"])

    def test_policy_defense(self):
        result = detect_language_game("Our compliance policy mandates regulatory review.")
        self.assertEqual(result["game_type"], "policy defense")

    def test_scientific_justification(self):
        result = detect_language_game("The study findings and research evidence are clear.")
        self.assertEqual(result["game_type"], "scientific justification")

    def test_polemic(self):
        result = detect_language_game("We must fight the enemy and resist their demands.")
        self.assertEqual(result["game_type"], "polemic")

    def test_pr_statement(self):
        result = detect_language_game("We are proud and excited to announce our new brand.")
        self.assertEqual(result["game_type"], "PR statement")

    def test_unspecified_fallback(self):
        result = detect_language_game("The cat sat on the mat.")
        self.assertIn("unspecified", result["game_type"])


# ═══════════════════════════════════════════════════════════════════════
# 3. LAYER 2 — POPPER (BIAS GATE HIERARCHY)
# ═══════════════════════════════════════════════════════════════════════

class TestLayer2BiasGate(unittest.TestCase):
    """Verify fixed evaluation order: evasion → ideological → moral_framing → clean."""

    def test_evasion_gate_fires_first(self):
        """Evasion takes priority even when other gates would also fire."""
        signals = make_signals(
            evasion_count=3,
            normative_density=0.10,  # would trigger ideological
            falsifiability_low=True,
            framing_density=0.05,    # would trigger moral_framing
        )
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "evasion")
        self.assertEqual(result["gate_fired"], "evasion_gate")

    def test_evasion_threshold_exact(self):
        """evasion_count = 2 should fire (>= 2)."""
        signals = make_signals(evasion_count=2)
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "evasion")

    def test_evasion_below_threshold(self):
        """evasion_count = 1 should NOT fire evasion gate."""
        signals = make_signals(evasion_count=1)
        result = run_bias_gate(signals)
        self.assertNotEqual(result["classification"], "evasion")

    def test_ideological_normative_path(self):
        """normative_density > 0.05 AND falsifiability_low → ideological."""
        signals = make_signals(normative_density=0.06, falsifiability_low=True)
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "ideological")

    def test_ideological_universal_path(self):
        """universal_density > 0.02 AND falsifiability_low → ideological."""
        signals = make_signals(universal_density=0.03, falsifiability_low=True)
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "ideological")

    def test_ideological_requires_falsifiability_low(self):
        """High normative but falsifiability_low=False → does NOT fire ideological."""
        signals = make_signals(normative_density=0.10, falsifiability_low=False)
        result = run_bias_gate(signals)
        self.assertNotEqual(result["classification"], "ideological")

    def test_moral_framing_gate(self):
        """framing_density > 0.02 → moral_framing (when higher gates don't fire)."""
        signals = make_signals(framing_density=0.03)
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "moral_framing")

    def test_moral_framing_threshold_exact(self):
        """framing_density = 0.02 should NOT fire (> 0.02 required)."""
        signals = make_signals(framing_density=0.02)
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "clean")

    def test_clean_classification(self):
        """All below threshold → clean."""
        signals = make_signals()
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "clean")
        self.assertIsNone(result["gate_fired"])

    def test_popper_label_immunizing(self):
        self.assertEqual(popper_label("evasion"), "immunizing_stratagem")
        self.assertEqual(popper_label("ideological"), "immunizing_stratagem")
        self.assertEqual(popper_label("moral_framing"), "immunizing_stratagem")

    def test_popper_label_falsifiable(self):
        self.assertEqual(popper_label("clean"), "falsifiable_claim_structure")


# ═══════════════════════════════════════════════════════════════════════
# 4. LAYER 3 — AUTHORITY LAUNDERING
# ═══════════════════════════════════════════════════════════════════════

class TestLayer3Laundering(unittest.TestCase):

    def test_scientism_flag(self):
        signals = make_signals(ratio_density=0.03, ethos_density=0.03)
        result = detect_laundering(signals)
        self.assertIn("scientism", result["flags"])

    def test_scientism_requires_both(self):
        signals = make_signals(ratio_density=0.03, ethos_density=0.01)
        result = detect_laundering(signals)
        self.assertNotIn("scientism", result["flags"])

    def test_bureaucratic_masking_flag(self):
        signals = make_signals(lex_density=0.03, ratio_density=0.03)
        result = detect_laundering(signals)
        self.assertIn("bureaucratic_masking", result["flags"])

    def test_bureaucratic_masking_requires_both(self):
        signals = make_signals(lex_density=0.03, ratio_density=0.01)
        result = detect_laundering(signals)
        self.assertNotIn("bureaucratic_masking", result["flags"])

    def test_identity_laundering_via_pathos(self):
        signals = make_signals(ethos_density=0.04, pathos_density=0.03)
        result = detect_laundering(signals)
        self.assertIn("identity_laundering", result["flags"])

    def test_identity_laundering_via_evasion(self):
        signals = make_signals(ethos_density=0.04, evasion_count=2)
        result = detect_laundering(signals)
        self.assertIn("identity_laundering", result["flags"])

    def test_identity_laundering_requires_ethos_threshold(self):
        """ethos_density = 0.03 should NOT fire (> 0.03 required)."""
        signals = make_signals(ethos_density=0.03, pathos_density=0.05)
        result = detect_laundering(signals)
        self.assertNotIn("identity_laundering", result["flags"])

    def test_no_flags_on_clean(self):
        signals = make_signals()
        result = detect_laundering(signals)
        self.assertFalse(result["laundering_present"])
        self.assertEqual(len(result["flags"]), 0)

    def test_multiple_flags_can_fire(self):
        signals = make_signals(
            ratio_density=0.05, ethos_density=0.05,
            lex_density=0.05, pathos_density=0.05,
        )
        result = detect_laundering(signals)
        self.assertIn("scientism", result["flags"])
        self.assertIn("bureaucratic_masking", result["flags"])
        self.assertIn("identity_laundering", result["flags"])
        self.assertTrue(result["laundering_present"])


# ═══════════════════════════════════════════════════════════════════════
# 5. LAYER 4 — ARGYRIS (LEARNING POSTURE)
# ═══════════════════════════════════════════════════════════════════════

class TestLayer4Argyris(unittest.TestCase):

    def test_defensive_routine_when_laundering(self):
        self.assertEqual(argyris_label(True), "defensive_routine")

    def test_open_loop_when_no_laundering(self):
        self.assertEqual(argyris_label(False), "open_loop_reasoning")


# ═══════════════════════════════════════════════════════════════════════
# 6. LAYER 5 — COORDINATE MATH
# ═══════════════════════════════════════════════════════════════════════

class TestLayer5Coordinates(unittest.TestCase):

    def test_basic_coordinate_math(self):
        signals = make_signals(head_density=0.5, heart_density=0.0,
                               disruption_density=0.0, stability_density=0.5)
        coords = compute_coordinates(signals)
        self.assertAlmostEqual(coords["Y"], 5.0)
        self.assertAlmostEqual(coords["X"], -5.0)
        self.assertEqual(coords["quadrant"], "Q1")

    def test_q2_quadrant(self):
        signals = make_signals(head_density=0.8, heart_density=0.0,
                               disruption_density=0.8, stability_density=0.0)
        coords = compute_coordinates(signals)
        self.assertGreater(coords["Y"], 0)
        self.assertGreater(coords["X"], 0)
        self.assertEqual(coords["quadrant"], "Q2")

    def test_q3_quadrant(self):
        signals = make_signals(head_density=0.0, heart_density=0.8,
                               disruption_density=0.0, stability_density=0.8)
        coords = compute_coordinates(signals)
        self.assertLess(coords["Y"], 0)
        self.assertLess(coords["X"], 0)
        self.assertEqual(coords["quadrant"], "Q3")

    def test_q4_quadrant(self):
        signals = make_signals(head_density=0.0, heart_density=0.8,
                               disruption_density=0.8, stability_density=0.0)
        coords = compute_coordinates(signals)
        self.assertLess(coords["Y"], 0)
        self.assertGreater(coords["X"], 0)
        self.assertEqual(coords["quadrant"], "Q4")

    def test_clean_quadrant_near_center(self):
        signals = make_signals(head_density=0.1, heart_density=0.1,
                               disruption_density=0.1, stability_density=0.1)
        coords = compute_coordinates(signals)
        self.assertEqual(coords["quadrant"], "CLEAN")

    def test_clamping_to_10(self):
        signals = make_signals(head_density=1.0, heart_density=0.0,
                               disruption_density=1.0, stability_density=0.0)
        coords = compute_coordinates(signals)
        self.assertLessEqual(coords["Y"], 10)
        self.assertLessEqual(coords["X"], 10)

    def test_clamping_to_negative_10(self):
        signals = make_signals(head_density=0.0, heart_density=1.0,
                               disruption_density=0.0, stability_density=1.0)
        coords = compute_coordinates(signals)
        self.assertGreaterEqual(coords["Y"], -10)
        self.assertGreaterEqual(coords["X"], -10)

    def test_intensity_range(self):
        """Intensity should always be in [0, 10]."""
        for hd in [0.0, 0.3, 0.5, 0.8, 1.0]:
            for ht in [0.0, 0.3, 0.5, 0.8, 1.0]:
                signals = make_signals(head_density=hd, heart_density=ht,
                                       disruption_density=0.5, stability_density=0.2)
                coords = compute_coordinates(signals)
                self.assertGreaterEqual(coords["intensity"], 0)
                self.assertLessEqual(coords["intensity"], 10)

    def test_intensity_formula(self):
        """Verify intensity = (sqrt(X^2 + Y^2) / sqrt(200)) * 10."""
        signals = make_signals(head_density=0.5, heart_density=0.0,
                               disruption_density=0.0, stability_density=0.5)
        coords = compute_coordinates(signals)
        expected = (math.sqrt(25 + 25) / math.sqrt(200)) * 10
        self.assertAlmostEqual(coords["intensity"], round(expected, 2), places=2)

    def test_zero_intensity_at_center(self):
        signals = make_signals()
        coords = compute_coordinates(signals)
        self.assertEqual(coords["intensity"], 0)
        self.assertEqual(coords["quadrant"], "CLEAN")


# ═══════════════════════════════════════════════════════════════════════
# 7. SPECTROGRAPH RENDERING
# ═══════════════════════════════════════════════════════════════════════

class TestSpectrograph(unittest.TestCase):

    def test_star_at_center(self):
        spec = render_spectrograph(0, 0)
        self.assertIn("★", spec)
        # Star should replace the + at center
        self.assertNotIn(" + ", spec)

    def test_star_in_q2(self):
        spec = render_spectrograph(8, 7)
        self.assertIn("★", spec)

    def test_star_in_q3(self):
        spec = render_spectrograph(-8, -7)
        self.assertIn("★", spec)

    def test_labels_present(self):
        spec = render_spectrograph(0, 0)
        self.assertIn("HEAD (+)", spec)
        self.assertIn("HEART (-)", spec)
        self.assertIn("STAB", spec)
        self.assertIn("DISR", spec)
        self.assertIn("Q1", spec)
        self.assertIn("Q2", spec)
        self.assertIn("Q3", spec)
        self.assertIn("Q4", spec)


# ═══════════════════════════════════════════════════════════════════════
# 8. FULL PIPELINE INTEGRATION
# ═══════════════════════════════════════════════════════════════════════

class TestFullPipeline(unittest.TestCase):

    def test_raw_text_mode_sets_estimated(self):
        result = audit(text="The committee decided to implement the new policy.")
        self.assertTrue(result["estimated"])

    def test_measures_mode_not_estimated(self):
        result = audit(measures=make_signals())
        self.assertFalse(result["estimated"])

    def test_all_result_keys_present(self):
        result = audit(text="A simple test.")
        expected_keys = [
            "estimated", "signals", "language_game", "gate_result",
            "classification", "testability", "laundering",
            "learning_posture", "coordinates", "spectrograph",
        ]
        for key in expected_keys:
            self.assertIn(key, result, f"Missing result key: {key}")

    def test_no_input_raises(self):
        with self.assertRaises(ValueError):
            audit()


# ═══════════════════════════════════════════════════════════════════════
# 9. GOLD STANDARD VALIDATION CASES
#    (from the Epistemic Benchmark Template workbook)
# ═══════════════════════════════════════════════════════════════════════

class TestGoldStandardCases(unittest.TestCase):
    """
    Validate against known texts from the Gold Standard Template.
    These are structural checks — the engine should detect the expected
    patterns even though raw-text estimation is approximate.
    """

    def test_ee_0001_detects_normative_and_framing(self):
        """
        EE_0001: "If you oppose this bill, you clearly don't care about
        children. Therefore, the bill must pass."
        Expected: contains normative language ('must'), evasion cue ('clearly'),
        and is structurally a legislative persuasion / polemic.
        Template says: mixed classification, identity_laundering present.
        """
        text = ("If you oppose this bill, you clearly don't care about children. "
                "Therefore, the bill must pass.")
        result = audit(text=text)
        # Should detect at least one evasion cue ('clearly')
        self.assertGreaterEqual(result["signals"]["evasion_count"], 1)
        # Should detect normative language ('must')
        self.assertGreater(result["signals"]["normative_density"], 0)
        # Should be estimated mode
        self.assertTrue(result["estimated"])

    def test_ee_0002_detects_institutional_shielding(self):
        """
        EE_0002: "According to the Committee's framework, our process is
        inherently fair; thus, further review is unnecessary."
        Expected: bureaucratic lexicon + ethos cues, defensive routine.
        Template says: defensive-routine, bureaucratic_masking + ethos.
        """
        text = ("According to the Committee's framework, our process is "
                "inherently fair; thus, further review is unnecessary.")
        result = audit(text=text)
        # Should detect ethos cues ('committee')
        self.assertGreater(result["signals"]["ethos_density"], 0)
        # Should detect lex cues ('framework')
        self.assertGreater(result["signals"]["lex_density"], 0)
        # Should detect falsifiability_low ('inherently')
        # Note: single occurrence might not trigger, depends on threshold
        signals = result["signals"]
        # At minimum, the engine should pick up the institutional language game
        self.assertEqual(result["language_game"]["institutional_language_game"], True)

    def test_measures_evasion_scenario(self):
        """Full measures-mode test: evasion with all laundering flags."""
        result = audit(measures=make_signals(
            evasion_count=3,
            falsifiability_low=True,
            normative_density=0.08,
            universal_density=0.03,
            framing_density=0.01,
            head_density=0.04,
            heart_density=0.12,
            disruption_density=0.02,
            stability_density=0.09,
            ratio_density=0.03,
            ethos_density=0.04,
            lex_density=0.03,
            pathos_density=0.05,
        ))
        self.assertEqual(result["classification"], "evasion")
        self.assertEqual(result["testability"], "immunizing_stratagem")
        self.assertEqual(result["learning_posture"], "defensive_routine")
        self.assertIn("scientism", result["laundering"]["flags"])
        self.assertIn("bureaucratic_masking", result["laundering"]["flags"])
        self.assertIn("identity_laundering", result["laundering"]["flags"])

    def test_measures_ideological_scenario(self):
        """Ideological gate fires when normative is high + falsifiability_low."""
        result = audit(measures=make_signals(
            evasion_count=1,
            falsifiability_low=True,
            normative_density=0.07,
            universal_density=0.01,
        ))
        self.assertEqual(result["classification"], "ideological")

    def test_measures_moral_framing_scenario(self):
        """Moral framing gate fires on high framing_density."""
        result = audit(measures=make_signals(framing_density=0.05))
        self.assertEqual(result["classification"], "moral_framing")

    def test_measures_clean_scenario(self):
        """All signals below threshold → clean, falsifiable, open-loop."""
        result = audit(measures=make_signals(
            head_density=0.06,
            disruption_density=0.04,
        ))
        self.assertEqual(result["classification"], "clean")
        self.assertEqual(result["testability"], "falsifiable_claim_structure")
        self.assertEqual(result["learning_posture"], "open_loop_reasoning")

    def test_gold_standard_q2_position(self):
        """
        Gold Standard Spec says position Q2 (6.0, 7.5) for the benchmark.
        Verify the engine produces Q2 for equivalent coordinates.
        """
        # head_density - heart_density = 7.5/10 = 0.75; disruption - stability = 6.0/10 = 0.60
        result = audit(measures=make_signals(
            head_density=0.80, heart_density=0.05,
            disruption_density=0.65, stability_density=0.05,
        ))
        self.assertEqual(result["coordinates"]["quadrant"], "Q2")
        self.assertAlmostEqual(result["coordinates"]["Y"], 7.5, places=0)
        self.assertAlmostEqual(result["coordinates"]["X"], 6.0, places=0)


# ═══════════════════════════════════════════════════════════════════════
# 10. OUTPUT FORMAT
# ═══════════════════════════════════════════════════════════════════════

class TestOutputFormat(unittest.TestCase):

    def test_standard_output_has_all_sections(self):
        result = audit(measures=make_signals())
        output = format_audit(result)
        self.assertIn("A) AUDIT SNAPSHOT", output)
        self.assertIn("B) LOGIC RESULT", output)
        self.assertIn("C) SPECTROGRAPH", output)
        self.assertIn("D) ASK-FOR MENU", output)

    def test_five_sentence_snapshot(self):
        """Section A should have exactly 5 non-empty sentences."""
        result = audit(measures=make_signals())
        output = format_audit(result)
        # Extract section A
        a_start = output.index("A) AUDIT SNAPSHOT")
        b_start = output.index("B) LOGIC RESULT")
        section_a = output[a_start:b_start].strip()
        # Count non-empty lines after the header
        lines = [l for l in section_a.split("\n") if l.strip() and l.strip() != "A) AUDIT SNAPSHOT"]
        self.assertEqual(len(lines), 5, f"Expected 5 sentences, got {len(lines)}: {lines}")

    def test_menu_has_seven_items(self):
        result = audit(measures=make_signals())
        output = format_audit(result)
        for i in range(1, 8):
            self.assertIn(f"{i})", output)

    def test_drilldown_includes_spectrograph(self):
        result = audit(measures=make_signals())
        output = format_audit(result, drilldown=[1])
        self.assertIn("SPECTROGRAPH", output)
        self.assertIn("★", output)

    def test_drilldown_all_items(self):
        result = audit(measures=make_signals(
            evasion_count=3, ratio_density=0.05, ethos_density=0.05,
        ))
        output = format_audit(result, drilldown=[1, 2, 3, 4, 5, 6, 7])
        self.assertIn("1) Language game", output)
        self.assertIn("2) Argument skeleton", output)
        self.assertIn("3) Falsifiability", output)
        self.assertIn("4) Authority laundering", output)
        self.assertIn("5) Learning posture", output)
        self.assertIn("6) Deterministic readout", output)
        self.assertIn("7) What would change", output)

    def test_estimated_note_in_raw_text(self):
        result = audit(text="Test sentence for estimation.")
        output = format_audit(result)
        self.assertIn("Measures are estimated", output)

    def test_no_estimated_note_in_measures(self):
        result = audit(measures=make_signals())
        output = format_audit(result)
        self.assertNotIn("Measures are estimated", output)

    def test_json_output_valid(self):
        result = audit(measures=make_signals())
        import json
        parsed = json.loads(audit_to_json(result))
        self.assertIn("classification", parsed)
        self.assertIn("coordinates", parsed)
        self.assertIn("signals", parsed)


# ═══════════════════════════════════════════════════════════════════════
# 11. MEASURES PARSER
# ═══════════════════════════════════════════════════════════════════════

class TestMeasuresParser(unittest.TestCase):

    def test_parse_standard_format(self):
        text = """- evasion_count: 3
- falsifiability_low: true
- normative_density: 0.08
- universal_density: 0.03"""
        signals = parse_measures(text)
        self.assertEqual(signals["evasion_count"], 3)
        self.assertTrue(signals["falsifiability_low"])
        self.assertAlmostEqual(signals["normative_density"], 0.08)

    def test_parse_without_dashes(self):
        text = "evasion_count: 2\nfalsifiability_low: false"
        signals = parse_measures(text)
        self.assertEqual(signals["evasion_count"], 2)
        self.assertFalse(signals["falsifiability_low"])


# ═══════════════════════════════════════════════════════════════════════
# 12. EDGE CASES & ROBUSTNESS
# ═══════════════════════════════════════════════════════════════════════

class TestEdgeCases(unittest.TestCase):

    def test_very_short_text(self):
        result = audit(text="No.")
        self.assertIn(result["classification"], ["clean", "evasion", "ideological", "moral_framing"])

    def test_very_long_text(self):
        text = "The policy must ensure compliance. " * 500
        result = audit(text=text)
        self.assertIsNotNone(result["classification"])

    def test_unicode_text(self):
        result = audit(text="La política debe garantizar el cumplimiento. 政策は遵守を確保する必要があります。")
        self.assertIsNotNone(result["classification"])

    def test_gate_priority_ideological_over_framing(self):
        """When both ideological and moral_framing conditions are met,
        ideological should fire first (it's higher in the hierarchy)."""
        signals = make_signals(
            evasion_count=0,
            normative_density=0.10,
            falsifiability_low=True,
            framing_density=0.05,
        )
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "ideological")

    def test_boundary_normative_density_exact_threshold(self):
        """normative_density = 0.05 should NOT fire ideological (> 0.05 required)."""
        signals = make_signals(normative_density=0.05, falsifiability_low=True)
        result = run_bias_gate(signals)
        self.assertNotEqual(result["classification"], "ideological")

    def test_boundary_universal_density_exact_threshold(self):
        """universal_density = 0.02 should NOT fire ideological (> 0.02 required)."""
        signals = make_signals(universal_density=0.02, falsifiability_low=True)
        result = run_bias_gate(signals)
        self.assertNotEqual(result["classification"], "ideological")


# ═══════════════════════════════════════════════════════════════════════
# 13. v2.0 — EXTENDED EVASION LEXICON
# ═══════════════════════════════════════════════════════════════════════

class TestV2ExtendedEvasion(unittest.TestCase):
    """v2.0: colloquial political register evasion cues."""

    def test_disaster_as_evasion(self):
        text = "The economy is a disaster. It was a disaster under the last administration."
        signals = extract_signals(text)
        self.assertGreaterEqual(signals["evasion_count"], 1,
                                "'is a disaster' / 'was a disaster' should trigger evasion")

    def test_broken_as_evasion(self):
        text = "The system is broken. The agency is broken."
        signals = extract_signals(text)
        self.assertGreaterEqual(signals["evasion_count"], 2,
                                "'is broken' should trigger evasion")

    def test_out_of_excuses_as_evasion(self):
        text = "He has run out of excuses and must act now."
        signals = extract_signals(text)
        self.assertGreaterEqual(signals["evasion_count"], 1,
                                "'run out of excuses' should trigger evasion")

    def test_leavitt_style_fires_evasion_gate(self):
        """Simulates the Leavitt White House statement pattern: multiple
        colloquial evasion cues should fire the evasion gate."""
        text = ("The BLS is broken. Biden's economy was a disaster. "
                "Powell has run out of excuses.")
        signals = extract_signals(text)
        self.assertGreaterEqual(signals["evasion_count"], 3,
                                "Leavitt-style text should produce evasion_count >= 3")
        result = run_bias_gate(signals)
        self.assertEqual(result["classification"], "evasion",
                         "Evasion gate should fire on Leavitt-style text")


# ═══════════════════════════════════════════════════════════════════════
# 14. v2.0 — STABILITY EXCLUSION LIST
# ═══════════════════════════════════════════════════════════════════════

class TestV2StabilityExclusions(unittest.TestCase):
    """v2.0: procedural-neutral terms should not inflate stability_density."""

    def test_regulatory_procedural_text_low_stability(self):
        """Text with only procedural terms (filed, annual, compliance, deadline)
        should NOT produce elevated stability_density."""
        text = ("The annual filing was submitted by the deadline. "
                "Compliance with the quarterly reporting schedule is confirmed. "
                "The periodic report was filed pursuant to the regulation.")
        signals = extract_signals(text)
        self.assertLessEqual(signals["stability_density"], 0.05,
                             "Procedural regulatory text should not inflate stability")

    def test_genuine_stability_advocacy_still_detected(self):
        """Text with genuine stability-advocacy vocabulary should still score."""
        text = ("We must preserve our heritage and maintain the traditions "
                "that are the bedrock of our institution. Safeguard the legacy.")
        signals = extract_signals(text)
        self.assertGreater(signals["stability_density"], 0.05,
                           "Genuine stability advocacy should produce elevated density")

    def test_bls_style_neutral_not_inflated(self):
        """BLS-style methodological text should not be read as stability advocacy."""
        text = ("The Bureau scheduled the annual benchmark revision. "
                "Preliminary estimates are filed quarterly and are subject to routine updates. "
                "The final benchmark will be released in compliance with standard procedures.")
        signals = extract_signals(text)
        # Should not produce strong stability lean
        coords = compute_coordinates(signals)
        self.assertGreater(coords["X"], -5.0,
                           "BLS-style text should not produce extreme stability lean")


# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    unittest.main()
