# Which Wins? No. 15: linear search vs binary search, timed for real. Python 3, standard library only.
#   python3 search.py
# 1,000,000 distinct numbers in random order (fixed seed).
# Round 1, one lookup in the unsorted list: linear scans it; binary search must sort it first (that's the price), then bisect.
# Round 2, 100 lookups once the list is sorted: linear scans for each one; binary search halves the list each step.
# Targets sit near the end (the worst case for a scan) and every answer is checked.
import bisect, random, time

N, K = 1_000_000, 100
rng = random.Random(15)
nums = rng.sample(range(10 * N), N)
target = nums[-1]                                   # round 1: the last element of the unsorted list
srt = sorted(nums)
targets = [srt[-1 - i * 7] for i in range(K)]       # round 2: values near the top of the sorted list


def linear(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i


def binary(a, x):
    i = bisect.bisect_left(a, x)
    return i if i < len(a) and a[i] == x else None


def best(f, passes=3):
    out = []
    for _ in range(passes):
        t = time.perf_counter(); r = f(); out.append(time.perf_counter() - t)
    return min(out), r


lin1, r = best(lambda: linear(nums, target)); assert nums[r] == target
bin1, r = best(lambda: binary(sorted(nums), target)); assert r is not None   # the sort counts: the list arrived unsorted
lin2, r = best(lambda: [linear(srt, x) for x in targets], passes=1); assert all(srt[i] == x for i, x in zip(r, targets))
bin2, r = best(lambda: [binary(srt, x) for x in targets]); assert all(srt[i] == x for i, x in zip(r, targets))
print(f"r1_linear {lin1 * 1000:.3f} ms")
print(f"r1_binary {bin1 * 1000:.3f} ms")
print(f"r2_linear {lin2 * 1000:.3f} ms")
print(f"r2_binary {bin2 * 1000:.3f} ms")
