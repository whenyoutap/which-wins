# Which Wins? No. 2: Linear Scan vs Binary Search

**Searching 128 items 64 times: linear scan or binary search?**

## Run it yourself

```
python3 race.py   # about 20 seconds
```

Python 3, standard library only.

## Our result

Counted steps, not timed: you should get exactly these numbers on any machine. One step is one comparison or one array write. A typical draw of list and targets (closest to the average of 3,000), seed 20.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | The first 1,629 steps | Binary search spends them sorting and finds nothing; the scan is already finding items | Linear scan |
| 2 | Find all 64 | Binary 2,343 steps (sort included); scan 4,116. When binary finished, scan had found 34 | Binary search |

## The rule

Search once: just scan. Search a lot: sort first, then binary search. That is why databases keep sorted indexes.

## In an interview

**When is binary search not worth it?**
When you search only once or twice: sorting costs more than the scans you save. It pays off over many searches.

[Watch the reel](https://www.instagram.com/reel/DfMxc2GFm7D/)