# Which Wins? No. 16: sort everything vs a heap, to get the top K of 1,000,000 numbers. Python 3, standard library only.
#   python3 topk.py
# Round 1: the top 10. Round 2: the top half (500,000). Same random numbers (fixed seed); both answers are checked against each other.
import heapq, random, time

N = 1_000_000
nums = random.Random(16).sample(range(10 * N), N)   # distinct numbers, random order


def by_sort(a, k):
    return sorted(a, reverse=True)[:k]


def by_heap(a, k):
    return heapq.nlargest(k, a)


def best(f, k, passes=3):
    out = []
    for _ in range(passes):
        t = time.perf_counter(); r = f(nums, k); out.append(time.perf_counter() - t)
    return min(out), r


for name, k in (("r1", 10), ("r2", N // 2)):
    s, a = best(by_sort, k); h, b = best(by_heap, k)
    assert a == b
    print(f"{name}_sort {s * 1000:.3f} ms")
    print(f"{name}_heap {h * 1000:.3f} ms")
