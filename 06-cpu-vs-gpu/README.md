# Which Wins? No. 6: CPU vs GPU

**Which is faster, the CPU or the GPU?**

## Run it yourself

```
pip install torch   # a CUDA build, with an NVIDIA GPU
python3 cpu_vs_gpu.py
```

## Our result

Intel Core i9-14900HX laptop with an NVIDIA RTX 4070 Laptop GPU, PyTorch 2.8, median of 3 runs.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Multiply two 4096 x 4096 matrices | GPU 14 ms, CPU 162 ms: GPU 11x faster | GPU |
| 2 | 10,000 steps, each needing the step before (x = x * 0.999 + 1) | CPU 36 ms, GPU 156 ms: CPU 4x faster | CPU |

Your numbers will differ by machine. The winner of each round should not.

## The rule

Work that splits into independent pieces goes to the GPU; work that runs step by step stays on the CPU.

## In an interview

**Why do AI models run on GPUs?**
They are mostly huge matrix multiplies, where every output cell can be computed at the same time.

[Watch the reel](https://www.instagram.com/reel/DfhTzWFFL2x/)
