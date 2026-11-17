# Which Wins? No. 15: Linear search vs binary search

**Is binary search always faster than a linear scan?**

## Run it yourself

```
python3 search.py
```

## Our result

Intel Core i9-14900HX laptop, Python 3.10.20, 1,000,000 distinct numbers in random order, median of 7 runs (17 Nov 2026).

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | One search in the unsorted list | Linear 17.6 ms, binary (sort first, then search) 142.1 ms | Linear, 8× |
| 2 | 100 searches once the list is sorted | Binary 0.023 ms, linear 2,650 ms | Binary, 115,200× |

Your times will differ by machine; the winner of each round should not.

## The rule

Binary search needs a sorted list. For one search in unsorted data, a scan is cheaper than sorting; once sorted, every search takes about 20 steps.

## In an interview

**When would you NOT use binary search?**
When the data isn't sorted and you only search it once or twice: sorting costs O(n log n), more than an O(n) scan.

This race reworks No. 2 (linear vs binary, counted steps): [02-search](../02-search/).
