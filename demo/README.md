# Demo: SemEval Hyperpartisan Validation

This directory contains the actual outputs of the Epistemic Engine v2.0.0
running across 7 articles from the SemEval-2023 Task 3 hyperpartisan corpus,
scored independently by two LLM platforms (OpenAI GPT o3 and Google Gemini)
on 2026-03-28.

The SemEval corpus is one of two externally annotated validation sets in the
v2.1 workbook (the other is the 12-text MAFALDA sample). Reference labels
were assigned by the SemEval-2023 Task 3 organizers without engine
involvement, making this one of the few corpora in the project where the
ground truth is fully independent.

## What's here

| File                              | What it shows                                                          |
|-----------------------------------|------------------------------------------------------------------------|
| `article_01_divergent_case.md`    | The headline finding: GPT and Gemini disagree on Article 1 only        |
| `gpt_full_corpus.md`              | All 7 GPT o3 audit outputs                                             |
| `gemini_full_corpus.md`           | All 7 Gemini audit outputs                                             |

## Run the demo

From the repository root:

```bash
./demo.sh
```

This prints the headline divergent case (Article 1) inline.

## The headline finding in one sentence

Of 7 externally annotated articles, GPT and Gemini agree on 6 (all `clean`)
and disagree on 1 — Article 1 ("How Long, America?"), which GPT flags as
`moral_framing` and Gemini flags as `evasion`. Both correctly identify Q4
quadrant placement, immunizing-stratagem testability, and similar intensity,
but route the bias classification through different gates of the same
deterministic kernel. This single document is the inter-model agreement
problem the ICETM paper documents at scale across 6 sub-corpora.

## How this demo relates to the validation framework

| Sub-corpus            | n  | Role        | Purpose                                              |
|-----------------------|----|-------------|------------------------------------------------------|
| SEC Benchmark         | 20 | Baseline    | Ground-truth anchor                                  |
| BLS Validation        | 12 | Validation  | Labor-economics register                             |
| Energy / Oil Market   | 10 | Validation  | Commodity-price journalism                           |
| Synthetic Gate Tests  | 6  | Validation  | One per classification pathway                       |
| **SemEval Hyperpartisan** | **7**  | **Validation**  | **Externally annotated articles (this demo)**            |
| MAFALDA External      | 12 | Validation  | Externally annotated fallacies                       |

The SemEval set is the smallest externally annotated corpus in the framework,
which makes it ideal for a demo: complete coverage in 7 documents, with one
clean divergent case. For the full inter-model agreement story across all six
corpora and the formal kernel violation registry, see the ICETM paper.

## Reproducing this output

The audits in this directory are the actual GPT o3 and Gemini outputs from
the 2026-03-28 revalidation run. To reproduce, you would need:

1. The SemEval-2023 Task 3 hyperpartisan article texts (cited in the workbook)
2. The Epistemic Engine v2.0.0 pipeline (`epistemic_engine/mafalda_engine/`)
3. Access to GPT o3 and Gemini API endpoints
4. The system prompt from `README.md` (Section 4)

Output stability: LLM signal estimation is not temporally stable. The
SEC baseline shifted from Gemini 20/20 (2026-02-15) to Gemini 18/20
(2026-03-28). Re-running this demo on a different date may produce different
gate assignments at the boundaries. This temporal instability is itself a
finding documented in the ICETM paper.
