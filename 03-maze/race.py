"""Which Wins? No. 3: DFS vs BFS escaping a maze, from @whenyoutap.

Same 13 x 13 maze (a few loops), start top left, exit bottom right. One step is one cell taken off the
stack (DFS) or the queue (BFS): counted steps, not timed. The only difference in the code is pop() vs popleft().
We use a typical maze: of the first 300, the one closest to the average over 3,000 random mazes.
Run: python3 race.py   (a few seconds)
"""
import collections, random
W = H = 13; S, X = (0, 0), (W - 1, H - 1)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def maze(rnd, braid=.12):
    open_ = set(); seen = {S}; st = [S]
    while st:
        x, y = st[-1]; nb = [(x + dx, y + dy) for dx, dy in DIRS if 0 <= x + dx < W and 0 <= y + dy < H and (x + dx, y + dy) not in seen]
        if not nb: st.pop(); continue
        n = rnd.choice(nb); open_.add(frozenset(((x, y), n))); seen.add(n); st.append(n)
    walls = [frozenset(((x, y), (x + dx, y + dy))) for x in range(W) for y in range(H) for dx, dy in ((1, 0), (0, 1)) if x + dx < W and y + dy < H]
    walls = [w for w in walls if w not in open_]; rnd.shuffle(walls)
    for w in walls[:int(len(walls) * braid)]: open_.add(w)
    return open_

def nbrs(o, c): x, y = c; return [(x + dx, y + dy) for dx, dy in DIRS if frozenset((c, (x + dx, y + dy))) in o]

def search(o, bfs):
    todo, seen, par, order = collections.deque([S]), set(), {S: None}, []
    while todo:
        c = todo.popleft() if bfs else todo.pop()      # the only difference
        if c in seen: continue
        seen.add(c); order.append(c)
        if c == X: break
        for n in nbrs(o, c):
            if n not in seen:
                if bfs: par.setdefault(n, c)
                else: par[n] = c
                todo.append(n)
    return order, par

def path_len(par):
    n, c = 0, X
    while c is not None: n += 1; c = par[c]
    return n

def run(o):
    bo, bp = search(o, True); do, dp = search(o, False)
    return len(bo), path_len(bp), len(do), path_len(dp)

rnd = random.Random(25); mazes = [maze(rnd) for _ in range(3000)]; R = [run(o) for o in mazes]
mean = [sum(r[i] for r in R) / len(R) for i in range(4)]
k = min(range(300), key=lambda i: sum(abs(R[i][j] - mean[j]) / mean[j] for j in range(4)))
b, bl, d, dl = R[k]
print(f"This maze: DFS got out after checking {d} cells (route {dl} cells); BFS after {b} cells (route {bl} cells, the shortest)")
print(f"Over 3,000 mazes: DFS got out first in {100 * sum(r[2] < r[0] for r in R) / len(R):.0f}%, and its route was longer in {100 * sum(r[3] > r[1] for r in R) / len(R):.0f}%")
