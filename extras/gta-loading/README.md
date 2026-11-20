# GTA Online's 6-minute loading screen, rebuilt small

In February 2021 a player, t0st, profiled why GTA Online took about 6 minutes to load on his PC
([his write-up](https://nee.lv/2021/02/28/How-I-cut-GTA-Online-loading-times-by-70/)). A ~10 MB JSON shop catalogue of ~63,000 items was read so that:

1. for every item, the parser (`sscanf`) scanned to the end of the same text again, and
2. every new item was compared with every item before it, about 2 billion checks.

Fixing both took his load from about 6 min to 1 min 50 s.

`load.c` is **our rebuild of that pattern, not Rockstar's code** (not affiliated with Rockstar Games). It generates its own catalogue and
loads it two ways: the old approach (sscanf per item + a linear duplicate check) and a fix (read straight through + a hash set). Both must
return identical items, or it exits with an error.

## Run it

```
gcc -O2 load.c -o load
./load 1000      # small shop: both feel instant
./load 63000     # ~9.6 MB, the size in t0st's write-up
./load 63000 split   # also times "only the reading fixed"
```

## Our result

Intel Core i9-14900HX, gcc 13 -O2, median of 5 runs (21 Nov 2026).

| Items | Old approach | Fix | |
|---|---|---|---|
| 1,000 (0.15 MB) | 1.46 ms | 0.031 ms | both instant |
| 63,000 (9.57 MB) | 7.56 s | 0.0027 s | 2,853× slower |

With only the reading fixed, 63,000 items still take 3.56 s: each of the two bugs costs about half on our machine.

## The rule

A duplicate check that compares each new item with every earlier one does n(n-1)/2 comparisons: 1,984,468,500 for 63,000 items.
That loop is O(n²). It is invisible at 1,000 items and a loading screen at 63,000.
