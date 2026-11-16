# Which Wins? No. 14: Two Sum (LeetCode #1), nested loops vs a hash map. Python 3, standard library only.
#   python3 twosum.py
# Same list for both rounds: 15,000 numbers, and the answer pair is the last two, so neither method gets lucky and stops early.
# Round 1, time: how long each takes to find the pair (best of 3).
# Round 2, space: how much extra memory each needs while it runs (Python's tracemalloc, peak).
import time, tracemalloc

N = 15_000


def nested(nums, target):            # check every pair: about n*n/2 checks, no extra memory
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j


def hashmap(nums, target):           # one pass, remembering every number seen: about n checks, a dict of up to n entries
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return seen[target - x], i
        seen[x] = i


nums = list(range(1, 2 * N, 2))[:N - 2] + [10 ** 7, 10 ** 7 + 1]   # odd numbers, then the pair at the very end
target = 2 * 10 ** 7 + 1

for f in (nested, hashmap):
    times = []
    for _ in range(3):
        t = time.perf_counter(); r = f(nums, target); times.append(time.perf_counter() - t)
    assert r == (N - 2, N - 1), r
    tracemalloc.start(); f(nums, target); _, peak = tracemalloc.get_traced_memory(); tracemalloc.stop()
    print(f"{f.__name__} time {min(times) * 1000:.3f} ms  extra memory {peak} bytes")
