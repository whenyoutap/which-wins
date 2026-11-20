# Which Wins? No. 17: CPU vs GPU vs both

**The AI model is 16.1 GB. The laptop's GPU has 8 GB. Which answers fastest: the CPU alone, the GPU alone, or both split?**

A sequel to [No. 13](../13-cpu-vs-gpu-ai/).

## Run it yourself

1. Get llama.cpp with GPU support from [its releases](https://github.com/ggml-org/llama.cpp/releases) (we used b12416).
2. Download `Llama-3.1-8B-Instruct-BF16.gguf` (16.1 GB) from unsloth/Llama-3.1-8B-Instruct-GGUF on Hugging Face.
3. Run:

```
./race.sh path/to/llama-completion Llama-3.1-8B-Instruct-BF16.gguf 16
```

The last number is the CPU thread count. Try a few and keep the fastest.

The three commands, if you'd rather type them (bash):

```
P=$'<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\nExplain why the sky is blue to a 10 year old.<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n'
M=Llama-3.1-8B-Instruct-BF16.gguf

# CPU only
llama-completion -m $M -c 2048 -p "$P" -n 40 --temp 0 --seed 1 -no-cnv -dev none -ngl 0 -t 16
# GPU only
llama-completion -m $M -c 2048 -p "$P" -n 40 --temp 0 --seed 1 -no-cnv -ngl 99 --fit off
# Both, split (llama.cpp fits as many layers on the GPU as it can)
llama-completion -m $M -c 2048 -p "$P" -n 40 --temp 0 --seed 1 -no-cnv
```

## Our result

Intel Core i9-14900HX, NVIDIA RTX 4070 Laptop GPU (8 GB), llama.cpp b12416, greedy decoding, 2,048-token context,
40 tokens, median of 5 runs on an idle machine (20 Nov 2026).

| Round | Lanes | Result | Winner |
|---|---|---|---|
| 1 | CPU vs GPU | CPU 4.79 tokens/s, GPU 0.85 | CPU, 5.7× |
| 2 | CPU vs both, split | Split 6.22 tokens/s, CPU 4.79 | Split, 1.3× |

In the split run llama.cpp put 12 of the model's 33 layers on the GPU and ran the other 21 on the CPU.

On Windows the GPU driver lets a model bigger than the GPU's memory spill into system RAM, so the GPU-only lane runs slowly
instead of failing. On Linux without that fallback it stops with "out of memory".

## The rule

Put on the GPU what fits. Let the CPU run the rest.

## In an interview

**How do you run a model that is bigger than your GPU's memory?**
Offload part of it: keep as many layers as fit in GPU memory and run the rest on the CPU from system RAM. Each token still
reads every weight, so the layers on the faster memory make the whole pass faster.
