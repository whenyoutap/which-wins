"""Which Wins? No. 1: insertion sort vs merge sort, from @whenyoutap.

Each lane sorts a shuffled list; finish it and a bigger one opens: 6, 8, 10, 12, 16, 32, 64, 128, then 256 items.
One step is one comparison or one array write (counted steps, not timed).
For each size we use a typical list: of 300 shuffles, the one closest to the average steps of both sorts.
Run: python3 race.py   (about a minute)
"""
import random

def insertion(a):
    a = a[:]; steps = 0
    for i in range(1, len(a)):
        v = a[i]; j = i - 1
        while j >= 0:
            steps += 1                      # compare
            if a[j] <= v: break
            a[j + 1] = a[j]; steps += 1; j -= 1   # write
        a[j + 1] = v; steps += 1            # write
    return steps

def merge(a):
    a = a[:]; steps = 0
    def go(lo, hi):
        nonlocal steps
        if hi - lo < 2: return
        m = (lo + hi) // 2; go(lo, m); go(m, hi)
        aux = []; i, j = lo, m
        while i < m and j < hi:
            steps += 1                      # compare
            if a[i] <= a[j]: aux.append(a[i]); i += 1
            else: aux.append(a[j]); j += 1
        aux += a[i:m] + a[j:hi]
        for k, v in enumerate(aux): a[lo + k] = v; steps += 1   # write
    go(0, len(a))
    return steps

SIZES = [6, 8, 10, 12, 16, 32, 64, 128, 256]
rnd = random.Random(19); ins_tot = mer_tot = 0
print(f"{'size':>5} {'insertion':>10} {'merge':>7}   running totals")
for n in SIZES:
    ss = [rnd.sample(range(1, n + 1), n) for _ in range(2000 if n < 64 else 200)]
    mi = sum(insertion(x) for x in ss) / len(ss); mm = sum(merge(x) for x in ss) / len(ss)
    pick = min(ss[:300], key=lambda x: abs(insertion(x) - mi) / mi + abs(merge(x) - mm) / mm)
    a, b = insertion(pick), merge(pick); ins_tot += a; mer_tot += b
    print(f"{n:>5} {a:>10,} {b:>7,}   insertion {ins_tot:,}, merge {mer_tot:,}")
print(f"Total steps: insertion sort {ins_tot:,}, merge sort {mer_tot:,}")
