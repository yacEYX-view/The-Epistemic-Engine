#!/bin/bash
echo "=========================================="
echo "EPISTEMIC ENGINE DEMO"
echo "=========================================="
echo ""
echo "Analyzing sample institutional text..."
echo ""

python3 -m epistemic_engine.mafalda_engine.mafalda_engine --input "$(cat data/benchmarks/sbc-100/sample_01.txt)"

echo ""
echo "Demo complete!"
