#!/bin/bash
# ============================================================================
# EPISTEMIC ENGINE DEMO
# ----------------------------------------------------------------------------
# Shows the headline finding from the SemEval Hyperpartisan validation corpus:
# the same deterministic specification produces structurally divergent
# classifications when delegated to two different LLM platforms.
#
# Article 1 ("How Long, America?", CounterPunch) is the single document in
# the 7-article corpus where GPT and Gemini disagree. This is the entire
# inter-model agreement story in one example.
#
# Full corpus outputs for all 7 articles are in demo/.
# ============================================================================

cat demo/article_01_divergent_case.md

echo ""
echo "============================================================================"
echo "  See demo/gpt_full_corpus.md and demo/gemini_full_corpus.md"
echo "  for all 7 SemEval articles."
echo "============================================================================"
