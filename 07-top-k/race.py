# Which Wins? No. 7 (@whenyoutap): top 10 out of 1,000,000 random scores. Lane A sorts everything and takes the last 10; lane B keeps a min-heap of 10
# (compare each new score with the heap's smallest; push/pop only when it is bigger). Comparisons are counted with a wrapper whose __lt__ counts
# (sorted() and heapq only use <). Plain timings use ints, median of 3. Both must give the same top 10. Run: python3 race.py
import heapq, json, random, statistics, sys, time
N, K, SEED = 1_000_000, 10, 34
rng = random.Random(SEED); scores = [rng.randrange(10_000_000) for _ in range(N)]
class C:
    n = 0
    __slots__ = ("v",)
    def __init__(self, v): self.v = v
    def __lt__(self, o): C.n += 1; return self.v < o.v
W = [C(v) for v in scores]
C.n = 0; topA = [c.v for c in sorted(W)[-K:]][::-1]; compA = C.n
C.n = 0; h = W[:K]; heapq.heapify(h); events = []
for i in range(K, N):
    c = W[i]
    if h[0] < c:
        out = heapq.heapreplace(h, c); events.append([i, c.v, out.v])
compB = C.n; topB = sorted((c.v for c in h), reverse=True)
assert topA == topB, (topA, topB)
def tA(): return sorted(scores)[-K:]
def tB():
    hh = scores[:K]; heapq.heapify(hh)
    for x in scores[K:]:
        if x > hh[0]: heapq.heapreplace(hh, x)
    return hh
def timeit(f):
    ts = []
    for _ in range(3): t = time.perf_counter(); f(); ts.append(time.perf_counter() - t)
    return statistics.median(ts), ts
ta, tas = timeit(tA); tb, tbs = timeit(tB); tn, tns = timeit(lambda: heapq.nlargest(K, scores))
assert sorted(tB(), reverse=True) == topA == heapq.nlargest(K, scores)
print(f"top 10: {topA}")
print(f"sort: {compA:,} comparisons, {ta*1000:.0f} ms  ({[round(x*1000) for x in tas]})")
print(f"heap: {compB:,} comparisons, {tb*1000:.0f} ms  ({[round(x*1000) for x in tbs]}), {len(events)} knock-outs")
print(f"heapq.nlargest: {tn*1000:.0f} ms; ratio comparisons {compA/compB:.1f}x, time {ta/tb:.1f}x")
