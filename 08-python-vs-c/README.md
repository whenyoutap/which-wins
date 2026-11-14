# Which Wins? No. 8: Python vs C

**Which is faster, Python or C?**

## Run it yourself

```
gcc -O2 -o sum sum.c && ./sum
pip install numpy
python3 sum.py
```

## Our result

Intel Core i9-14900HX laptop, Python 3.10, NumPy 1.26, gcc 13.3 with -O2, median of 7 runs.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Add up the squares of 100,000,000 numbers in a plain loop | C 63 ms, Python 3,882 ms: C 62x faster | C |
| 2 | Same job, Python makes one NumPy call: np.dot(a, a) | Python 34 ms, C's loop 63 ms | Python (NumPy) |

Your numbers will differ by machine. The winner of each round should not.

## The rule

A plain Python loop is slow; one library call that runs the loop in compiled code is fast.

## In an interview

**Why is Python slow, and why is it still used for AI?**
The interpreter runs a loop one step at a time; the heavy loops in AI run in compiled code underneath (NumPy, PyTorch).

[Watch the reel](https://www.instagram.com/reel/Dfmc0c7jqz2/)
