#!/usr/bin/env bash
# Which Wins? No. 13: CPU vs GPU running the same AI model (Meta Llama 3.1 8B Instruct) with llama.cpp.
# Needs: a llama.cpp build with GPU support (github.com/ggml-org/llama.cpp/releases; we used b12416, ubuntu-cuda-12.8-x64)
# and two model files from Hugging Face:
#   round 1: bartowski/Meta-Llama-3.1-8B-Instruct-GGUF  Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf  (4.9 GB, 4-bit)
#   round 2: unsloth/Llama-3.1-8B-Instruct-GGUF        Llama-3.1-8B-Instruct-BF16.gguf         (16.1 GB, full 16-bit)
# Usage: ./race.sh path/to/llama-completion path/to/Q4.gguf path/to/BF16.gguf [cpu_threads]
# Prints tokens per second for each lane. If your GPU has more memory than the model, round 2 goes the other way: that's the point.
set -euo pipefail
BIN=$1; Q4=$2; F16=$3; T=${4:-12}
P=$'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nExplain why the sky is blue to a 10 year old.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
run() { "$BIN" -c 2048 -p "$P" --temp 0 --seed 1 -no-cnv --simple-io --no-display-prompt "$@" 2>&1 >/dev/null | grep -E " eval time" | grep -v prompt | grep -oE "[0-9.]+ tokens per second"; }
echo "round 1, GPU: $(run -m "$Q4" -n 120 -ngl 99)"
echo "round 1, CPU: $(run -m "$Q4" -n 120 -dev none -ngl 0 -t "$T")"
echo "round 2, GPU: $(run -m "$F16" -n 40 -ngl 99 --fit off)"
echo "round 2, CPU: $(run -m "$F16" -n 40 -dev none -ngl 0 -t "$T")"
