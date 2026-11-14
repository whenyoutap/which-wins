# Which Wins? No. 1: Insertion Sort vs Merge Sort

**Which sort finishes first: insertion sort or merge sort?**

## Run it yourself

```
python3 race.py   # about a minute
```

Python 3, standard library only.

## Our result

Counted steps, not timed: you should get exactly these numbers on any machine. One step is one comparison or one array write. For each size, a typical shuffle (closest to the average of 2,000), seed 19.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Small lists (6 to 10 items) | 6 items: insertion 23 steps, merge 26. Insertion leads until the 10-item list | Insertion sort |
| 2 | All nine lists, up to 256 items | Merge 6,685 steps in total, insertion 44,591 | Merge sort |

## The rule

Insertion sort (O(n²)) wins on tiny lists; merge sort (O(n log n)) wins as lists grow. Python's own sort uses both.

## In an interview

**Why would a real sort use insertion sort at all?**
On a handful of items it does less work than merge sort, so libraries sort short runs with it and merge the runs (CPython's list sort does this).

[Watch the reel](https://www.instagram.com/reel/DfJpLa0DRX3/)