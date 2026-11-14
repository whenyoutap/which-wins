"""CPU vs GPU, two rounds, timed on one laptop (from @whenyoutap's "Which wins? #6").

Round 1, work that splits: multiply two 4096 x 4096 matrices (about 137 billion multiply-adds).
  Every output cell is independent, so the GPU's thousands of cores all work at once.
Round 2, work that doesn't split: 10,000 steps where each step needs the one before (x = x * 0.999 + 1).
  Only one thing can happen at a time, and the GPU pays a launch cost on every step, so the CPU wins.

Needs: python3 with torch (CUDA build) and a CUDA GPU. Run: python3 cpu_vs_gpu.py
"""
import json, time, torch

def best(fn, reps):
    out = []
    for _ in range(reps):
        t = time.perf_counter(); fn(); out.append(time.perf_counter() - t)
    return min(out)

def round1(dev, n=4096):
    a = torch.rand(n, n, device=dev); b = torch.rand(n, n, device=dev)
    def go():
        c = a @ b
        if dev == "cuda": torch.cuda.synchronize()
        return c
    go()                                   # warm up (loads kernels, allocates)
    return best(go, 5)

def round2(dev, steps=10_000):
    x0 = torch.ones(1, device=dev)
    def go():
        x = x0.clone()
        for _ in range(steps): x = x * 0.999 + 1
        if dev == "cuda": torch.cuda.synchronize()
        return x
    go()
    return best(go, 3)

if __name__ == "__main__":
    torch.set_num_threads(torch.get_num_threads())
    r = {"cpu_threads": torch.get_num_threads(), "gpu": torch.cuda.get_device_name(0), "torch": torch.__version__}
    r["r1_cpu"], r["r1_gpu"] = round1("cpu"), round1("cuda")
    r["r2_cpu"], r["r2_gpu"] = round2("cpu"), round2("cuda")
    r["r1_flops"] = 2 * 4096 ** 3
    print(json.dumps(r, indent=1))
    print(f"Round 1 (4096x4096 matmul): CPU {r['r1_cpu']:.3f} s, GPU {r['r1_gpu']:.4f} s -> GPU {r['r1_cpu'] / r['r1_gpu']:.0f}x faster")
    print(f"Round 2 (10,000 dependent steps): CPU {r['r2_cpu']:.3f} s, GPU {r['r2_gpu']:.3f} s -> CPU {r['r2_gpu'] / r['r2_cpu']:.1f}x faster")
