# Which Wins? No. 12: Array vs Linked List

**Which is faster, an array or a linked list?**

## Run it yourself

```
gcc -O2 -o race race.c && ./race
```

## Our result

Intel Core i9-14900HX laptop, gcc -O2, median of 5 runs (14 Nov 2026). The reel is coming next.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Add up 10,000,000 values | Array 5.3 ms, shuffled linked list 1,060 ms | Array |
| 2 | Insert 2,000 values at the front of 200,000 | Linked list 0.002 ms, array 42 ms | Linked list |

Your numbers will differ by machine. The winner of each round should not.

## The rule

Arrays win at reading in order (the CPU fetches neighbours together); linked lists win at inserting at the front.

## In an interview

**Why is a linked list slow to walk even though each step is O(1)?**
Its nodes are scattered in memory, so almost every step is a cache miss; an array's values sit next to each other.

The reel is coming soon on [@whenyoutap](https://www.instagram.com/whenyoutap/).
