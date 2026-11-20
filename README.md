# Which Wins? Real code, raced on a real laptop. Run it yourself.

Every race from [@whenyoutap](https://www.instagram.com/whenyoutap/) on Instagram, with the exact code that produced the numbers in the reel. Two rounds each, and each side usually wins one.

| No. | Question | Round 1 winner | Round 2 winner | Kind | Code |
|---|---|---|---|---|---|
| 1 | Which sort finishes first: insertion sort or merge sort? | Insertion sort | Merge sort | counted | [01-sort](01-sort/) |
| 2 | Searching 128 items 64 times: linear scan or binary search? | Linear scan | Binary search | counted | [02-search](02-search/) |
| 3 | Escaping a maze: depth-first or breadth-first search? | DFS | BFS | counted | [03-maze](03-maze/) |
| 4 | On real city roads, which finds the shortest route with less work: Dijkstra or A*? | A* | Tie | counted | [04-route](04-route/) |
| 5 | Same 60 numbers, five algorithms: how many steps does each take? | O(1) | Nobody | counted | [05-big-o](05-big-o/) |
| 6 | Which is faster, the CPU or the GPU? | GPU | CPU | timed | [06-cpu-vs-gpu](06-cpu-vs-gpu/) |
| 7 | Top 10 out of 1,000,000 scores: sort everything or keep a heap of 10? | Heap of 10 | Heap of 10 | counted + timed | [07-top-k](07-top-k/) |
| 8 | Which is faster, Python or C? | C | Python (NumPy) | timed | [08-python-vs-c](08-python-vs-c/) |
| 9 | Which is faster, RAM or an SSD? | RAM | SSD | timed | [09-ram-vs-ssd](09-ram-vs-ssd/) |
| 10 | In Python, which is faster: threads or processes? | Processes | Threads | timed | [10-threads-vs-processes](10-threads-vs-processes/) |
| 11 | In SQL, is a table faster with an index or without? | Index | No index | timed | [11-sql-index](11-sql-index/) |
| 12 | Which is faster, an array or a linked list? | Array | Linked list | timed | [12-array-vs-linked-list](12-array-vs-linked-list/) |
| 13 | Which runs an AI model faster on a laptop, the CPU or the GPU? | GPU | CPU | timed | [13-cpu-vs-gpu-ai](13-cpu-vs-gpu-ai/) |
| 14 | LeetCode #1: check every pair, or remember what you've seen in a hash map? | Hash map | Nested loops | timed | [14-two-sum](14-two-sum/) |
| 15 | Is binary search always faster than a linear scan? | Linear | Binary | timed | [15-linear-vs-binary](15-linear-vs-binary/) |
| 16 | To get the top K of a million numbers, sort them all or keep a heap? | Heap | Sort | timed | [16-sort-vs-heap](16-sort-vs-heap/) |
| 17 | The AI model is twice the GPU's memory: CPU alone, GPU alone, or both split? | CPU | Split | timed | [17-cpu-gpu-split](17-cpu-gpu-split/) |

Each folder has the code, how to run it, our result and the one-line rule.

Two kinds of race. **Counted** races (1 to 5) count steps, so you get exactly our numbers. **Timed** races (6 to 17) measure real time on one Intel Core i9-14900HX laptop: your times will differ, the winner of each round should not. No. 7 has both: counted comparisons and timed milliseconds. If yours doesn't match, open an issue with your numbers and your machine.

**Want a race?** Open an issue or comment on any reel with "X vs Y" and Kage will race it.

Code is MIT licensed (see LICENSE).
