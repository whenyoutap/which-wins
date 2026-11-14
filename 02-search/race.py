"""Which Wins? No. 2: linear scan vs binary search, from @whenyoutap.

Both lanes search the same 128 items for the same 64 targets. Binary search needs a sorted list,
so it pays for one merge sort first. One step is one comparison or one array write (counted steps, not timed).
We use a typical draw: of 300, the one closest to the average steps of both lanes over 3,000.
Run: python3 race.py   (about 20 seconds)
"""
import random
N, Q = 128, 64

def merge_sort_steps(a):
    a = a[:]; steps = 0
    def go(lo, hi):
        nonlocal steps
        if hi - lo < 2: return
        m = (lo + hi) // 2; go(lo, m); go(m, hi); aux = []; i, j = lo, m
        while i < m and j < hi:
            steps += 1
            if a[i] <= a[j]: aux.append(a[i]); i += 1
            else: aux.append(a[j]); j += 1
        aux += a[i:m] + a[j:hi]
        for k, v in enumerate(aux): a[lo + k] = v; steps += 1
    go(0, N); return steps, a

def linear_steps(a, ts): return sum(a.index(x) + 1 for x in ts)

def binary_steps(s, x):
    """Comparisons to find x in sorted s: an equality check, then a less-than check, per probe."""
    lo, hi, steps = 0, N - 1, 0
    while lo <= hi:
        m = (lo + hi) // 2
        if s[m] == x: return steps + 1
        steps += 2
        if s[m] < x: lo = m + 1
        else: hi = m - 1
    return steps

def cost(d):
    a, ts = d
    return linear_steps(a, ts), merge_sort_steps(a)[0] + sum(binary_steps(list(range(1, N + 1)), x) for x in ts)

rnd = random.Random(20)
draws = [(rnd.sample(range(1, N + 1), N), rnd.sample(range(1, N + 1), Q)) for _ in range(3000)]
cs = [cost(d) for d in draws]; ml = sum(c[0] for c in cs) / len(cs); mb = sum(c[1] for c in cs) / len(cs)
A, TS = min(draws[:300], key=lambda d: abs(cost(d)[0] - ml) / ml + abs(cost(d)[1] - mb) / mb)
sort_steps, S = merge_sort_steps(A)
lin = [A.index(x) + 1 for x in TS]                 # steps each linear search took
binary_total = sort_steps + sum(binary_steps(S, x) for x in TS)
linear_total = sum(lin)
found_by_scan, done = 0, 0
for s in lin:
    if done + s > binary_total: break
    done += s; found_by_scan += 1
print(f"Binary search: {sort_steps:,} steps sorting first (finds nothing), {binary_total:,} steps to find all {Q}")
print(f"Linear scan: {linear_total:,} steps to find all {Q}; after {binary_total:,} steps it had found {found_by_scan}")
