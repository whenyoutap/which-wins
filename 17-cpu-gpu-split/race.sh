#!/usr/bin/env bash
# Which Wins? No. 17: an AI model twice the size of the GPU's memory. CPU alone, GPU alone, or both split?
# Sequel to No. 13. Same model, prompt and settings as its round 2.
# Needs: a llama.cpp build with GPU support (github.com/ggml-org/llama.cpp/releases; we used b12416, ubuntu-cuda-12.8-x64)
# and unsloth/Llama-3.1-8B-Instruct-GGUF  Llama-3.1-8B-Instruct-BF16.gguf  (16.1 GB, full 16-bit) from Hugging Face.
# Usage: ./race.sh path/to/llama-completion path/to/BF16.gguf [cpu_threads]
# Prints tokens per second for each lane. With no device flags, llama.cpp's --fit puts as many layers on the GPU as fit.
set -euo pipefail
BIN=$1; F16=$2; T=${3:-16}
P=$'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nExplain why the sky is blue to a 10 year old.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
run() { "$BIN" -m "$F16" -c 2048 -p "$P" -n 40 --temp 0 --seed 1 -no-cnv --simple-io --no-display-prompt "$@" 2>&1 >/dev/null | grep -E " eval time" | grep -v prompt | grep -oE "[0-9.]+ tokens per second"; }
echo "CPU only:   $(run -dev none -ngl 0 -t "$T")"
echo "GPU only:   $(run -ngl 99 --fit off)"
echo "Both split: $(run)"
