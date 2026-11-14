# Which Wins? No. 10: Threads vs Processes

**In Python, which is faster: threads or processes?**

## Run it yourself

```
python3 race.py
```

## Our result

Intel Core i9-14900HX laptop (20 cores), Python 3.10 on Linux, standard build with the GIL, median of 5 runs.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | 8 jobs of pure maths, all started at once | 8 processes 132 ms, 8 threads 702 ms: processes 5.3x faster | Processes |
| 2 | 1,000 tiny jobs, a new worker started for each | Threads 65 ms, processes 1,124 ms: threads 17x faster | Threads |

Your numbers will differ by machine. The winner of each round should not.

## The rule

Heavy calculation goes to processes; many small or waiting jobs go to threads.

## In an interview

**What is the GIL?**
In standard Python only one thread runs Python code at a time. Threads still help while waiting on files or the network, and they are cheap to start.

[Watch the reel](https://www.instagram.com/reel/Dfrl1w8jN62/)
