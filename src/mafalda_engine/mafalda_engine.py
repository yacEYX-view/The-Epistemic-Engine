"""
The Epistemic Engine - Core Implementation
A reasoning spectrograph that audits epistemic bias in institutional text
"""

import json
import os
import sys
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
import argparse
from datetime import datetime

import numpy as np
from pydantic import BaseModel, Field
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# ============================================================================
# DATA MODELS
# ============================================================================

class BiasLevel(str, Enum):
    """Epistemic bias severity levels"""
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class EpistemicDimension:
    """Represents one dimension of epistemic assessment"""
    name: str
    score: float  # 0.0 - 1.0
    description: str
    evidence: str
    recommendations: List[str]
    
    def __post_init__(self):
        """Validate score is in range"""
        if not 0.0 <= self.score <= 1.0:
            raise ValueError(f"Score must be between 0.0 and 1.0, got {self.score}")


@dataclass
class EpistemicAssessment:
    """Complete epistemic bias assessment"""
    input_text: str
    timestamp: str
    
    # Core dimensions (0.0 = none, 1.0 = maximum bias)
    abstraction_level: EpistemicDimension
    agency_attribution: EpistemicDimension
    falsifiability: EpistemicDimension
    power_orientation: EpistemicDimension
    
    # Composite scores
    overall_epistemic_bias: float
    bias_severity: BiasLevel
    
    # Research prompts
    research_prompts: List[str]
    recommendations: List[str]
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        return {
            "input_text": self.input_text,
            "timestamp": self.timestamp,
            "dimensions": {
                "abstraction_level": asdict(self.abstraction_level),
                "agency_attribution": asdict(self.agency_attribution),
                "falsifiability": asdict(self.falsifiability),
                "power_orientation": asdict(self.power_orientation),
            },
            "overall_epistemic_bias": float(self.overall_epistemic_bias),
            "bias_severity": self.bias_severity.value,
            "research_prompts": self.research_prompts,
            "recommendations": self.recommendations,
        }


# ============================================================================
# EPISTEMIC ENGINE - CORE LOGIC
# ============================================================================

class EpistemicEngine:
    """
    Main engine for detecting and analyzing epistemic bias in text.
    
    Measures:
    - Abstraction: Psychological distance and construal level
    - Agency: Attribution patterns and responsibility assignment
    - Falsifiability: Testability and empirical grounding of claims
    - Power Orientation: Rhetorical authority and expertise assertion
    """
    
    def __init__(self, use_llm: bool = False, api_key: Optional[str] = None):
        """
        Initialize the Epistemic Engine
        
        Args:
            use_llm: If True, use OpenAI API for enhanced analysis
            api_key: OpenAI API key (uses environment variable if not provided)
        """
        self.use_llm = use_llm and OPENAI_AVAILABLE
        self.client = None
        self.console = Console()
        
        if self.use_llm:
            try:
                api_key = api_key or os.getenv("OPENAI_API_KEY")
                if not api_key:
                    self.console.print(
                        "[yellow]⚠️  OpenAI API key not found. Using local analysis only.[/yellow]"
                    )
                    self.use_llm = False
                else:
                    self.client = OpenAI(api_key=api_key)
                    self.console.print("[green]✓ OpenAI API connected[/green]")
            except Exception as e:
                self.console.print(f"[yellow]⚠️  Could not initialize OpenAI: {e}[/yellow]")
                self.use_llm = False
    
    def analyze(self, text: str, verbose: bool = True) -> EpistemicAssessment:
        """
        Perform complete epistemic bias analysis on input text
        
        Args:
            text: Input text to analyze
            verbose: Whether to print progress and results
            
        Returns:
            EpistemicAssessment object with full analysis
        """
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")
        
        if verbose:
            self.console.print("\n[bold cyan]🔍 EPISTEMIC ENGINE - TEXT ANALYSIS[/bold cyan]")
            self.console.print(f"[dim]Analyzing {len(text.split())} words...[/dim]\n")
        
        # Analyze each dimension
        with Progress() as progress:
            task = progress.add_task("[cyan]Analyzing dimensions...", total=4)
            
            abstraction = self._analyze_abstraction(text)
            progress.update(task, advance=1)
            
            agency = self._analyze_agency(text)
            progress.update(task, advance=1)
            
            falsifiability = self._analyze_falsifiability(text)
            progress.update(task, advance=1)
            
            power_orientation = self._analyze_power_orientation(text)
            progress.update(task, advance=1)
        
        # Compute composite scores
        dimension_scores = [
            abstraction.score,
            agency.score,
            falsifiability.score,
            power_orientation.score
        ]
        overall_bias = float(np.mean(dimension_scores))
        severity = self._classify_severity(overall_bias)
        
        # Generate research prompts
        prompts = self._generate_research_prompts(text, dimension_scores)
        recommendations = self._generate_recommendations(dimension_scores)
        
        # Create assessment object
        assessment = EpistemicAssessment(
            input_text=text,
            timestamp=datetime.now().isoformat(),
            abstraction_level=abstraction,
            agency_attribution=agency,
            falsifiability=falsifiability,
            power_orientation=power_orientation,
            overall_epistemic_bias=overall_bias,
            bias_severity=severity,
            research_prompts=prompts,
            recommendations=recommendations,
        )
        
        if verbose:
            self._display_assessment(assessment)
        
        return assessment
    
    def _analyze_abstraction(self, text: str) -> EpistemicDimension:
        """Analyze psychological distance and construal level"""
        abstract_markers = [
            "will", "could", "may", "possible", "potentially", "generally",
            "typically", "often", "tendency", "pattern", "concept", "framework"
        ]
        concrete_markers = [
            "is", "was", "been", "specific", "observed", "measured", "data",
            "evidence", "showed", "demonstrated", "found", "resulted"
        ]
        
        text_lower = text.lower()
        abstract_count = sum(text_lower.count(marker) for marker in abstract_markers)
        concrete_count = sum(text_lower.count(marker) for marker in concrete_markers)
        
        total = abstract_count + concrete_count
        score = abstract_count / total if total > 0 else 0.5
        
        evidence = f"Abstract language markers: {abstract_count}, Concrete markers: {concrete_count}"
        
        return EpistemicDimension(
            name="Abstraction Level",
            score=min(1.0, score),
            description="Psychological distance from concrete experience (0=concrete, 1=highly abstract)",
            evidence=evidence,
            recommendations=[
                "Ground abstract concepts with specific examples",
                "Include concrete data and measurements",
                "Define abstract terms operationally"
            ]
        )
    
    def _analyze_agency(self, text: str) -> EpistemicDimension:
        """Analyze agency attribution and responsibility patterns"""
        passive_markers = ["was", "were", "been", "is", "are", "be"]
        active_markers = ["has", "have", "did", "does", "conducted", "performed"]
        
        text_lower = text.lower()
        passive_count = sum(text_lower.count(marker) for marker in passive_markers)
        active_count = sum(text_lower.count(marker) for marker in active_markers)
        
        total = passive_count + active_count
        score = passive_count / total if total > 0 else 0.5
        
        evidence = f"Passive constructions: {passive_count}, Active constructions: {active_count}"
        
        return EpistemicDimension(
            name="Agency Attribution",
            score=min(1.0, score),
            description="Tendency to obscure agency (0=clear agency, 1=agency obscured/passive)",
            evidence=evidence,
            recommendations=[
                "Use active voice to clarify who performs actions",
                "Identify agents and recipients explicitly",
                "Avoid nominalizations that hide agency"
            ]
        )
    
    def _analyze_falsifiability(self, text: str) -> EpistemicDimension:
        """Analyze empirical grounding and testability"""
        unfalsifiable_markers = [
            "always", "never", "everything", "nothing", "obvious", "clear",
            "undeniable", "inevitable", "certainly", "without question"
        ]
        falsifiable_markers = [
            "if", "then", "test", "hypothesis", "measure", "observe",
            "predict", "verify", "compare", "evidence", "data", "found"
        ]
        
        text_lower = text.lower()
        unfalsifiable_count = sum(text_lower.count(marker) for marker in unfalsifiable_markers)
        falsifiable_count = sum(text_lower.count(marker) for marker in falsifiable_markers)
        
        total = unfalsifiable_count + falsifiable_count
        score = unfalsifiable_count / total if total > 0 else 0.5
        
        evidence = f"Unfalsifiable markers: {unfalsifiable_count}, Falsifiable markers: {falsifiable_count}"
        
        return EpistemicDimension(
            name="Falsifiability",
            score=min(1.0, score),
            description="Extent to which claims are testable (0=highly testable, 1=unfalsifiable)",
            evidence=evidence,
            recommendations=[
                "State claims in falsifiable terms",
                "Specify conditions under which claims could be disproven",
                "Provide empirical benchmarks or metrics"
            ]
        )
    
    def _analyze_power_orientation(self, text: str) -> EpistemicDimension:
        """Analyze rhetorical authority and expertise assertion"""
        authority_markers = [
            "expert", "authority", "proven", "established", "consensus",
            "universally", "scientifically", "empirically", "research shows",
            "studies demonstrate", "evidence proves"
        ]
        tentative_markers = [
            "suggests", "may", "could", "might", "appears", "seems",
            "possibly", "arguably", "arguably", "tentatively", "preliminary"
        ]
        
        text_lower = text.lower()
        authority_count = sum(text_lower.count(marker) for marker in authority_markers)
        tentative_count = sum(text_lower.count(marker) for marker in tentative_markers)
        
        total = authority_count + tentative_count
        score = authority_count / total if total > 0 else 0.5
        
        evidence = f"Authority markers: {authority_count}, Tentative markers: {tentative_count}"
        
        return EpistemicDimension(
            name="Power Orientation",
            score=min(1.0, score),
            description="Assertion of rhetorical authority (0=humble/tentative, 1=high authority)",
            evidence=evidence,
            recommendations=[
                "Qualify claims with appropriate certainty levels",
                "Acknowledge limitations and alternative interpretations",
                "Distinguish between evidence strength levels"
            ]
        )
    
    def _classify_severity(self, overall_bias: float) -> BiasLevel:
        """Classify bias severity based on overall score"""
        if overall_bias < 0.25:
            return BiasLevel.LOW
        elif overall_bias < 0.50:
            return BiasLevel.MODERATE
        elif overall_bias < 0.75:
            return BiasLevel.HIGH
        else:
            return BiasLevel.CRITICAL
    
    def _generate_research_prompts(self, text: str, scores: List[float]) -> List[str]:
        """Generate targeted research questions based on bias patterns"""
        prompts = []
        
        if scores[0] > 0.6:  # High abstraction
            prompts.append(
                "🔬 How might this analysis change with concrete, real-world examples? "
                "What specific cases or data points could ground these abstract concepts?"
            )
        
        if scores[1] > 0.6:  # High agency obscuring
            prompts.append(
                "👥 Who bears responsibility for the outcomes described? "
                "What active agents or stakeholders are implicit or invisible?"
            )
        
        if scores[2] > 0.6:  # Low falsifiability
            prompts.append(
                "✅ How could this claim be tested or disproven? "
                "What evidence would count against this interpretation?"
            )
        
        if scores[3] > 0.6:  # High power orientation
            prompts.append(
                "⚖️ What counterarguments or alternative perspectives exist? "
                "How certain is this claim relative to the evidence presented?"
            )
        
        if not prompts:
            prompts.append(
                "📚 What additional perspectives or evidence would strengthen this analysis?"
            )
        
        return prompts
    
    def _generate_recommendations(self, scores: List[float]) -> List[str]:
        """Generate actionable recommendations for improvement"""
        recommendations = []
        
        if scores[0] > 0.5:
            recommendations.append("Add concrete examples and case studies")
        if scores[1] > 0.5:
            recommendations.append("Use active voice to clarify responsibility")
        if scores[2] > 0.5:
            recommendations.append("Include testable hypotheses and metrics")
        if scores[3] > 0.5:
            recommendations.append("Acknowledge limitations and uncertainties")
        
        return recommendations if recommendations else ["Text shows good epistemic grounding"]
    
    def _display_assessment(self, assessment: EpistemicAssessment):
        """Display assessment results in rich terminal format"""
        console = self.console
        
        # Title
        console.print("\n" + "="*80)
        console.print("[bold cyan]📊 EPISTEMIC ASSESSMENT RESULTS[/bold cyan]")
        console.print("="*80 + "\n")
        
        # Overall score
        severity_color = {
            BiasLevel.LOW: "green",
            BiasLevel.MODERATE: "yellow",
            BiasLevel.HIGH: "orange1",
            BiasLevel.CRITICAL: "red"
        }
        
        color = severity_color.get(assessment.bias_severity, "white")
        overall_text = f"[bold {color}]{assessment.overall_epistemic_bias:.1%}[/bold {color}]"
        
        console.print(f"\n[bold]Overall Epistemic Bias Score:[/bold] {overall_text}")
        console.print(f"[bold]Severity Level:[/bold] [{color}]{assessment.bias_severity.value.upper()}[/{color}]\n")
        
        # Dimension scores table
        table = Table(title="[bold]Epistemic Dimensions[/bold]", show_header=True, header_style="bold cyan")
        table.add_column("Dimension", style="cyan")
        table.add_column("Score", justify="center")
        table.add_column("Level", justify="center")
        table.add_column("Description", justify="left")
        
        for dim in [
            assessment.abstraction_level,
            assessment.agency_attribution,
            assessment.falsifiability,
            assessment.power_orientation,
        ]:
            score_pct = f"{dim.score:.0%}"
            
            # Color code score
            if dim.score < 0.33:
                score_color = "green"
            elif dim.score < 0.66:
                score_color = "yellow"
            else:
                score_color = "red"
            
            table.add_row(
                dim.name,
                f"[{score_color}]{score_pct}[/{score_color}]",
                "[dim]" + dim.description[:40] + "...[/dim]" if len(dim.description) > 40 else "[dim]" + dim.description + "[/dim]",
                "[dim]" + dim.evidence[:50] + "...[/dim]" if len(dim.evidence) > 50 else "[dim]" + dim.evidence + "[/dim]"
            )
        
        console.print(table)
        
        # Research prompts
        console.print("\n[bold cyan]🔬 RESEARCH PROMPTS[/bold cyan]")
        for i, prompt in enumerate(assessment.research_prompts, 1):
            console.print(f"  {i}. {prompt}\n")
        
        # Recommendations
        console.print("[bold cyan]💡 RECOMMENDATIONS[/bold cyan]")
        for i, rec in enumerate(assessment.recommendations, 1):
            console.print(f"  {i}. {rec}\n")
        
        console.print("="*80 + "\n")


# ============================================================================
# VISUALIZATION
# ============================================================================

class VisualizationEngine:
    """Creates visual representations of epistemic assessments"""    
    @staticmethod
    def create_radar_chart(assessment: EpistemicAssessment, output_file: Optional[str] = None) -> go.Figure:
        """Create interactive radar chart of epistemic dimensions"""
        dimensions = [
            assessment.abstraction_level.name,
            assessment.agency_attribution.name,
            assessment.falsifiability.name,
            assessment.power_orientation.name,
        ]
        
        scores = [
            assessment.abstraction_level.score,
            assessment.agency_attribution.score,
            assessment.falsifiability.score,
            assessment.power_orientation.score,
        ]
        
        fig = go.Figure(data=go.Scatterpolar(
            r=scores,
            theta=dimensions,
            fill='toself',
            name='Epistemic Bias Dimensions',
            marker=dict(color='rgba(65, 105, 225, 0.8)'),
            line=dict(color='rgba(25, 55, 195, 1)', width=2),
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1],
                    tickfont=dict(size=10),
                ),
                bgcolor='rgba(240, 240, 240, 0.5)',
            ),
            title=f"<b>Epistemic Bias Spectrograph</b><br><sub>Overall Bias: {assessment.overall_epistemic_bias:.1%} ({assessment.bias_severity.value.upper()})</sub>",
            font=dict(size=12),
            hovermode='closest',
            height=600,
            showlegend=True,
        )
        
        if output_file:
            fig.write_html(output_file)
        
        return fig
    
    @staticmethod
    def create_bar_chart(assessment: EpistemicAssessment, output_file: Optional[str] = None) -> go.Figure:
        """Create bar chart comparing dimensions"""
        dimensions = [
            assessment.abstraction_level.name,
            assessment.agency_attribution.name,
            assessment.falsifiability.name,
            assessment.power_orientation.name,
        ]
        
        scores = [
            assessment.abstraction_level.score,
            assessment.agency_attribution.score,
            assessment.falsifiability.score,
            assessment.power_orientation.score,
        ]
        
        colors = ['red' if s > 0.6 else 'orange' if s > 0.3 else 'green' for s in scores]
        
        fig = go.Figure(data=[
            go.Bar(
                x=dimensions,
                y=scores,
                marker=dict(color=colors),
                text=[f"{s:.0%}" for s in scores],
                textposition='outside',
                hovertemplate='<b>%{x}</b><br>Score: %{y:.1%}<extra></extra>',
            )
        ])
        
        fig.update_layout(
            title="<b>Epistemic Bias by Dimension</b>",
            yaxis_title="Bias Score",
            yaxis=dict(range=[0, 1]),
            height=500,
            showlegend=False,
            template='plotly_white',
        )
        
        if output_file:
            fig.write_html(output_file)
        
        return fig


# ============================================================================
# COMMAND LINE INTERFACE
# ============================================================================

def main():
    """Command-line interface for the Epistemic Engine"""
    parser = argparse.ArgumentParser(
        description="The Epistemic Engine - Reasoning Spectrograph for Text",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mafalda_engine.py --input "Your text here"
  python mafalda_engine.py --file input.txt --output results.json
  python mafalda_engine.py --input "Text" --viz radar --output-viz spectrograph.html
        """
    )
    
    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input", type=str, help="Input text for analysis")
    input_group.add_argument("--file", type=str, help="Path to input text file")
    
    # Output options
    parser.add_argument("--output", type=str, help="Save results as JSON")
    parser.add_argument("--viz", choices=["radar", "bar", "both"], default="radar",
                        help="Visualization type (default: radar)")
    parser.add_argument("--output-viz", type=str, help="Save visualization as HTML")
    parser.add_argument("--quiet", action="store_true", help="Suppress console output")
    
    # API options
    parser.add_argument("--use-llm", action="store_true", help="Use OpenAI API for enhanced analysis")
    parser.add_argument("--api-key", type=str, help="OpenAI API key")
    
    args = parser.parse_args()
    
    # Load input text
    if args.input:
        text = args.input
    else:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}")
            sys.exit(1)
    
    # Initialize engine
    engine = EpistemicEngine(use_llm=args.use_llm, api_key=args.api_key)
    
    # Run analysis
    assessment = engine.analyze(text, verbose=not args.quiet)
    
    # Save JSON output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(assessment.to_dict(), f, indent=2)
        if not args.quiet:
            engine.console.print(f"[green]✓[/green] Results saved to {args.output}")
    
    # Generate visualizations
    viz_engine = VisualizationEngine()
    
    if args.output_viz:
        if args.viz in ["radar", "both"]:
            radar_file = args.output_viz.replace(".html", "_radar.html") if args.viz == "both" else args.output_viz
            viz_engine.create_radar_chart(assessment, radar_file)
            if not args.quiet:
                engine.console.print(f"[green]✓[/green] Radar chart saved to {radar_file}")
        
        if args.viz in ["bar", "both"]:
            bar_file = args.output_viz.replace(".html", "_bar.html") if args.viz == "both" else args.output_viz
            viz_engine.create_bar_chart(assessment, bar_file)
            if not args.quiet:
                engine.console.print(f"[green]✓[/green] Bar chart saved to {bar_file}")


if __name__ == "__main__":
    main()