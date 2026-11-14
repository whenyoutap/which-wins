# Which Wins? No. 4: Dijkstra vs A*

**On real city roads, which finds the shortest route with less work: Dijkstra or A*?**

## Run it yourself

```
python3 route_race.py osm.json
```

Python 3, standard library only.

## Our result

Counted steps, not timed: you should get exactly these numbers on any machine. One step is one junction taken off the queue. Roads: OpenStreetMap data read on 6 Nov 2026, included as osm.json (© OpenStreetMap contributors, ODbL). Fresh downloads can differ slightly.

| Round | Job | Result | Winner |
|---|---|---|---|
| 1 | Junctions checked, MG Road metro to Indiranagar metro (Bengaluru) | A* 746, Dijkstra 13,406 | A* |
| 2 | Route found | Both: the same 3.74 km route | Tie |

## The rule

A* adds one guess, the straight-line distance to the goal. It still finds the shortest route, with far less searching.

## In an interview

**Why is A* still guaranteed the shortest route?**
Its guess, the straight-line distance, is never longer than the real road distance, so it never skips a shorter path.

[Watch the reel](https://www.instagram.com/reel/DfcO3d2lGuW/)

Road data © OpenStreetMap contributors, available under the Open Database License (ODbL).
