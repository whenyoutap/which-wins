# Which Wins? No. 11: Index vs No Index

**In SQL, is a table faster with an index or without?**

## Run it yourself

```
python3 race.py .     # creates and deletes two test databases in the given folder (about 600 MB at peak)
```

## Our result

Intel Core i9-14900HX laptop, SQLite 3.52 from Python, median of 3 runs, lookup is the best of 5.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Find one user by email among 5,000,000 | With index 0.0031 ms, without 121 ms: about 39,000x faster | Index |
| 2 | Add 1,000,000 new users | Without index 507 ms, with index 920 ms: 1.8x faster; the index also doubled the file (191 MB to 381 MB) | No index |

Your numbers will differ by machine. The winner of each round should not.

## The rule

Lots of reads: add the index. Lots of writes: keep indexes few.

## In an interview

**Why not index every column?**
Each index makes every insert and update slower and takes disk space.

The reel is coming soon on [@whenyoutap](https://www.instagram.com/whenyoutap/).
