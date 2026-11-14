"""Big-O race from @whenyoutap's "Which wins? #5": five jobs on the same 60 numbers, every step counted.

  O(1)       read a[42]                         1 step
  O(log n)   binary search a sorted copy        about log2(60) = 6 comparisons
  O(n)       find the largest number            60 steps
  O(n^2)     check every pair for the closest   60*59/2 = 1,770 pair checks
  O(2^n)     try every subset for a target sum  2^60 subsets

Run: python3 bigo_race.py
The O(2^n) lane is run for real on small lists (n up to 22) to show it is exactly 2^n; 2^60 would take
about 36 years even at a billion subsets a second.
"""
import random

def make_list(n, seed=7):
    r = random.Random(seed)
    return r.sample(range(1, 1000), n)

def lanes(a):
    n = len(a); s = sorted(a)
    # O(1): one read.
    one = 1
    # O(log n): binary search for the value at index 42 of the sorted list, counting comparisons.
    target, lo, hi, logn = s[42], 0, n - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2; logn += 1
        if s[mid] == target: break
        if s[mid] < target: lo = mid + 1
        else: hi = mid - 1
    # O(n): largest number, one look at each.
    lin, best = 0, a[0]
    for x in a:
        lin += 1
        if x > best: best = x
    # O(n^2): closest pair, every pair once.
    quad, gap = 0, float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            quad += 1; gap = min(gap, abs(a[i] - a[j]))
    return {"one": dict(steps=one), "log": dict(steps=logn), "lin": dict(steps=lin), "quad": dict(steps=quad), "exp": dict(steps=None)}

def subset_steps(a, target=-1):
    """Try every subset (target -1 is never reached, so it tries all of them). Returns subsets tried."""
    n, tried = len(a), 0
    for mask in range(1 << n):
        tried += 1
        if sum(a[i] for i in range(n) if mask >> i & 1) == target: break
    return tried

if __name__ == "__main__":
    a = make_list(60); L = lanes(a)
    for k in ("one", "log", "lin", "quad"): print(f"{k:5s} {L[k]['steps']:>6} steps")
    for n in (10, 16, 20): print(f"subsets of {n} numbers: {subset_steps(make_list(n)):,} tried (2^{n} = {2 ** n:,})")
    print(f"subsets of 60 numbers: 2^60 = {2 ** 60:,}, about {2 ** 60 / 1e9 / 31557600:.1f} years at a billion a second")
