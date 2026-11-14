# Which Wins? No. 3: DFS vs BFS

**Escaping a maze: depth-first or breadth-first search?**

## Run it yourself

```
python3 race.py
```

Python 3, standard library only.

## Our result

Counted steps, not timed: you should get exactly these numbers on any machine. One step is one cell taken off the stack or queue. 13 x 13 maze with a few loops, a typical one of 3,000, seed 25.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Reach the exit | DFS after 75 cells checked, BFS after 136 | DFS |
| 2 | Find the shortest route | BFS's route is 35 cells (the shortest); DFS's is 57 | BFS |

## The rule

Any way out: DFS. The shortest way: BFS. Over 3,000 mazes, DFS got out first in 94% and took the longer route in 94%.

## In an interview

**Why does BFS always find the shortest path in an unweighted grid?**
It checks every cell 1 step away, then 2, then 3, so the first time it reaches the exit is by the fewest steps.

[Watch the reel](https://www.instagram.com/reel/DfZTrwMErfj/)