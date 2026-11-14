"""Dijkstra vs A* on real roads, as raced in @whenyoutap's "Which wins? #4".

Both searches are the same function. The only change is the priority:
  Dijkstra: distance so far
  A*:       distance so far + straight-line distance to the goal
Both return the shortest route. A* checks far fewer junctions, because the straight-line
guess (never longer than the real road distance) points it toward the goal.

Roads: OpenStreetMap, (c) OpenStreetMap contributors, ODbL. Get the same area with:
  curl https://overpass-api.de/api/interpreter --data-urlencode \
    'data=[out:json];way["highway"~"^(motorway|trunk|primary|secondary|tertiary|unclassified|residential|motorway_link|trunk_link|primary_link|secondary_link|tertiary_link|living_street)$"](12.950,77.588,13.002,77.660);(._;>;);out body;' -o osm.json
Then: python3 route_race.py osm.json
"""
import heapq, json, math, sys

def meters(a, b):
    """Straight-line (great-circle) distance in metres between two (lat, lon) points."""
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371000 * math.asin(math.sqrt(h))

def load_graph(path):
    """Junctions and the roads between them. Shape points along a road are folded into its polyline."""
    els = json.load(open(path))["elements"]
    pos = {e["id"]: (e["lat"], e["lon"]) for e in els if e["type"] == "node"}
    ways = [e["nodes"] for e in els if e["type"] == "way"]
    uses = {}
    for w in ways:
        for i, n in enumerate(w): uses[n] = uses.get(n, 0) + (1 if 0 < i < len(w) - 1 else 2)
    G, poly = {}, {}
    for w in ways:
        a, pts, length = w[0], [pos[w[0]]], 0.0
        for p, n in zip(w, w[1:]):
            pts.append(pos[n]); length += meters(pos[p], pos[n])
            if uses[n] != 2 or n == w[-1]:                     # a junction or the end of the road
                if a != n and (length < G.get(a, {}).get(n, math.inf)):
                    G.setdefault(a, {})[n] = length; G.setdefault(n, {})[a] = length; poly[(a, n)] = pts
                a, pts, length = n, [pos[n]], 0.0
    return G, {n: pos[n] for n in G}, poly

def nearest(pos, lat, lon):
    return min(pos, key=lambda n: meters(pos[n], (lat, lon)))

def search(G, pos, start, goal, astar):
    """Returns (junctions in the order they were checked, parent links, route length in metres)."""
    h = (lambda n: meters(pos[n], pos[goal])) if astar else (lambda n: 0.0)
    dist, par, done, order = {start: 0.0}, {start: None}, set(), []
    todo = [(h(start), start)]
    while todo:
        _, n = heapq.heappop(todo)
        if n in done: continue
        done.add(n); order.append(n)
        if n == goal: break
        for m, w in G[n].items():
            d = dist[n] + w
            if d < dist.get(m, math.inf):
                dist[m], par[m] = d, n
                heapq.heappush(todo, (d + h(m), m))   # the one line that differs: + h(m)
    return order, par, dist[goal]

if __name__ == "__main__":
    G, pos, _ = load_graph(sys.argv[1] if len(sys.argv) > 1 else "osm.json")
    S, X = nearest(pos, 12.97560, 77.60670), nearest(pos, 12.97840, 77.63860)   # MG Road metro -> Indiranagar metro
    for name, a in (("Dijkstra", False), ("A*", True)):
        order, _, d = search(G, pos, S, X, a)
        print(f"{name:8s} checked {len(order):5d} junctions, route {d / 1000:.2f} km")
