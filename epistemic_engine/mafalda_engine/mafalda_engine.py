#!/usr/bin/env python3
"""
The Epistemic Engine - Epistemic Bias Auditor
Analyzes institutional text for abstraction, agency, falsifiability, and power orientation.
"""

import argparse
import json
import sys


def analyze_text(text: str) -> dict:
    """
    Analyze text for epistemic bias indicators.
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary containing analysis results
    """
    words = text.split()
    word_count = len(words)
    
    # Abstraction analysis (simple word length heuristic for demo)
    avg_word_length = sum(len(word) for word in words) / max(word_count, 1)
    abstraction_score = min(avg_word_length / 10, 1.0)
    
    # Agency detection (passive voice indicators for demo)
    passive_indicators = ['was', 'were', 'been', 'being', 'is', 'are', 'by']
    passive_count = sum(1 for word in text.lower().split() if word in passive_indicators)
    agency_obscured = passive_count > word_count * 0.15
    
    # Falsifiability check (tentative language vs. absolute claims)
    hedge_words = ['may', 'might', 'could', 'possibly', 'perhaps', 'sometimes']
    absolute_words = ['always', 'never', 'must', 'all', 'none', 'every']
    
    hedge_count = sum(1 for word in text.lower().split() if word in hedge_words)
    absolute_count = sum(1 for word in text.lower().split() if word in absolute_words)
    
    falsifiability = "low" if absolute_count > hedge_count else "moderate" if hedge_count > 0 else "unknown"
    
    # Power orientation (institutional language markers)
    institutional_markers = ['policy', 'decision', 'implementation', 'framework', 
                            'structure', 'governance', 'mandate', 'compliance']
    power_count = sum(1 for word in text.lower().split() if word in institutional_markers)
    power_orientation = "high" if power_count > 0 else "neutral"
    
    return {
        "word_count": word_count,
        "abstraction_score": round(abstraction_score, 3),
        "agency_obscured": agency_obscured,
        "passive_indicator_count": passive_count,
        "falsifiability": falsifiability,
        "power_orientation": power_orientation,
        "institutional_marker_count": power_count
    }


def format_output(result: dict, output_format: str = "text") -> str:
    """Format analysis results for display."""
    if output_format == "json":
        return json.dumps(result, indent=2)
    
    # Text format
    output = []
    output.append("=" * 50)
    output.append("EPISTEMIC ENGINE ANALYSIS")
    output.append("=" * 50)
    output.append("")
    output.append(f"Word Count: {result['word_count']}")
    output.append(f"Abstraction Score: {result['abstraction_score']:.3f}")
    output.append(f"Agency Obscured: {'YES' if result['agency_obscured'] else 'NO'}")
    output.append(f"  └─ Passive Indicators: {result['passive_indicator_count']}")
    output.append(f"Falsifiability: {result['falsifiability'].upper()}")
    output.append(f"Power Orientation: {result['power_orientation'].upper()}")
    output.append(f"  └─ Institutional Markers: {result['institutional_marker_count']}")
    output.append("=" * 50)
    
    return "\n".join(output)


def main():
    parser = argparse.ArgumentParser(
        description="The Epistemic Engine - Analyze text for epistemic bias",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mafalda_engine.py --input "The decision was made by the board."
  python mafalda_engine.py --input "$(cat sample.txt)" --format json
        """
    )
    
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Text to analyze (use quotes for strings, or $(cat file.txt) for files)"
    )
    
    parser.add_argument(
        "--format",
        type=str,
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    
    args = parser.parse_args()
    
    if not args.input.strip():
        print("Error: Input text cannot be empty", file=sys.stderr)
        sys.exit(1)
    
    try:
        result = analyze_text(args.input)
        output = format_output(result, args.format)
        print(output)
    except Exception as e:
        print(f"Error during analysis: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
