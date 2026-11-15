# Which Wins? No. 13: CPU vs GPU running AI

**Which runs an AI model faster on a laptop, the CPU or the GPU?**

## Run it yourself

1. Get llama.cpp with GPU support from [its releases](https://github.com/ggml-org/llama.cpp/releases) (we used b12416).
2. Download the two model files from Hugging Face:
   - Round 1: `Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf` (4.9 GB) from bartowski/Meta-Llama-3.1-8B-Instruct-GGUF
   - Round 2: `Llama-3.1-8B-Instruct-BF16.gguf` (16.1 GB) from unsloth/Llama-3.1-8B-Instruct-GGUF
3. Run:

```
./race.sh path/to/llama-completion Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf Llama-3.1-8B-Instruct-BF16.gguf 16
```

The last number is the CPU thread count. Try a few and keep the fastest.

## Our result

Intel Core i9-14900HX, NVIDIA RTX 4070 Laptop GPU (8 GB), llama.cpp b12416, greedy decoding, 2,048-token context, median of 5 runs (15 Nov 2026).

| Round | Model | Result | Winner |
|---|---|---|---|
| 1 | Llama 3.1 8B, 4-bit, 4.9 GB | GPU 50.3 tokens/s, CPU 13.7 | GPU, 3.7× |
| 2 | Llama 3.1 8B, 16-bit, 16.1 GB | CPU 5.0 tokens/s, GPU 0.86 | CPU, 5.8× |

Split across both (llama.cpp picks the layers): 6.2 tokens/s in round 2, the fastest.

On Windows the GPU driver lets a model bigger than the GPU's memory spill into system RAM, so round 2 runs slowly instead of failing. On Linux without that fallback, round 2 on the GPU stops with "out of memory". If your GPU has more than 16 GB, round 2 goes to the GPU.

## The rule

A GPU is fastest while the whole model fits in its own memory. Past that, every word waits on data crossing from system RAM.

## In an interview

**Why does LLM inference speed depend so much on memory?**
Each new token reads every weight of the model once, so speed is limited by how fast memory delivers the weights, not by arithmetic.

The reel is coming soon on [@whenyoutap](https://www.instagram.com/whenyoutap/).
