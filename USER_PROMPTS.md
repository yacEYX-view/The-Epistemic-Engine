# Epistemic Engine — User Prompt Templates

## Standard Audit (Raw Text)

```
Audit this text.

Text:
[PASTE TEXT HERE]
```

## Standard Audit (Measures)

```
Audit these measures.

Measures:
- evasion_count: <int>
- falsifiability_low: <true/false>
- normative_density: <0-1>
- universal_density: <0-1>
- framing_density: <0-1>
- head_density: <0-1>
- heart_density: <0-1>
- disruption_density: <0-1>
- stability_density: <0-1>
- ratio_density: <0-1>
- ethos_density: <0-1>
- lex_density: <0-1>
- pathos_density: <0-1>
- logos_density: <0-1>
```

## Drill-Down Request

After receiving an initial audit, request specific menu items:

```
Show me items 2, 4, and 6.
```

Or:

```
Give me the argument skeleton and the deterministic readout.
```

## Batch Audit (Multiple Documents)

```
Audit each of the following documents separately. Produce a complete A/B/C/D output for each.

Document 1:
[PASTE TEXT]

Document 2:
[PASTE TEXT]

Document 3:
[PASTE TEXT]
```

## SEC Benchmark Validation Run

Use this prompt to validate the engine against the benchmark corpus:

```
Audit the following SEC benchmark document. This is a corpus-ready packaging document. Audit the captured text / content note section — not the packaging metadata (source labels, URLs, APA citations, benchmark instructions). Report how the underlying discourse behaves as an institutional artifact.

[PASTE OR ATTACH BENCHMARK PDF]
```
