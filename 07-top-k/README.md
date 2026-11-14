# Which Wins? No. 7: Sort All vs Heap of 10

**Top 10 out of 1,000,000 scores: sort everything or keep a heap of 10?**

## Run it yourself

```
python3 race.py
```

Python 3, standard library only.

## Our result

The comparison counts are counted, not timed, and match on any machine (seed 34). The milliseconds are from one Intel Core i9-14900HX laptop, Python 3.10, median of 3, and will differ on yours.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Comparisons | Heap 1,000,419, sort 18,605,151: same top 10 | Heap of 10 |
| 2 | Time in Python | Heap 21 ms, sort 151 ms (one laptop; times vary) | Heap of 10 |

## The rule

For the top K of anything, keep a heap of size K: one comparison per item for most items. In Python: heapq.nlargest(10, scores).

## In an interview

**Find the K largest numbers in a huge list.**
Keep a min-heap of K; replace its smallest whenever a bigger number arrives. O(n log K) instead of O(n log n) for a full sort.

[Watch the reel](https://www.instagram.com/reel/Dfj5Mv4gdnR/)