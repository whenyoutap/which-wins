# Which Wins? No. 16: Sort everything vs a heap

**To get the top K of a million numbers, should you sort them all or keep a heap?**

## Run it yourself

```
python3 topk.py
```

## Our result

Intel Core i9-14900HX laptop, Python 3.10.20, 1,000,000 distinct numbers in random order, median of 7 runs (17 Nov 2026).

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | The top 10 | heapq.nlargest 11.0 ms, sorted() 146 ms | Heap, 13× |
| 2 | The top half (500,000) | sorted() 150 ms, heapq.nlargest 811 ms | Sort, 5.4× |

Your times will differ by machine; the winner of each round should not.

## The rule

A heap of size K costs O(n log K): great when K is small. When K is close to n, one O(n log n) sort is simpler and faster.

## In an interview

**How do you find the top K elements of a huge list?**
Keep a min-heap of size K while scanning once: O(n log K) time, O(K) space. If K is large, sort instead.

This race reworks No. 7 (top 10 of 1,000,000): [07-top-k](../07-top-k/).
