# Which Wins? No. 14: Two Sum, nested loops vs hash map

**LeetCode #1: is it better to check every pair, or to remember what you've seen in a hash map?**

## Run it yourself

```
python3 twosum.py
```

## Our result

Intel Core i9-14900HX laptop, Python 3.10, 15,000 numbers with the answer pair at the very end, median of 7 runs (16 Nov 2026).

| Round | Measure | Result | Winner |
|---|---|---|---|
| 1 | Time to find the pair | Hash map 0.93 ms, nested loops 3,591 ms | Hash map, 3,844× |
| 2 | Extra memory while it runs | Nested loops 284 bytes, hash map 1.18 MB | Nested loops, 4,167× |

Your times will differ by machine; the winner of each round should not.

## The rule

A hash map trades memory for time: it stores every number it sees so each lookup is one step. Nested loops store nothing and pay with every pair.

## In an interview

**What's the time and space complexity of each Two Sum solution?**
Nested loops: O(n²) time, O(1) extra space. Hash map: O(n) time, O(n) extra space.

The reel is coming soon on [@whenyoutap](https://www.instagram.com/whenyoutap/).
