# Which Wins? No. 11: a SQL table with an index vs without, in SQLite. Run: python3 race.py DIR
import os, sqlite3, sys, time
D = sys.argv[1] if len(sys.argv) > 1 else "."; N, M = 5_000_000, 1_000_000
def fresh(name, index):
    p = os.path.join(D, name); [os.remove(p + s) for s in ("", "-journal") if os.path.exists(p + s)]
    db = sqlite3.connect(p); db.execute("create table users(id integer primary key, email text, age int)")
    if index: db.execute("create index by_email on users(email)")
    return db
rows = lambda a, b: ((f"user{i}@mail.com", i % 90) for i in range(a, b))
for name, index in (("plain.db", False), ("indexed.db", True)):
    db = fresh(name, index)
    t = time.perf_counter(); db.executemany("insert into users(email, age) values(?, ?)", rows(0, N)); db.commit(); load = time.perf_counter() - t
    plan = db.execute("explain query plan select id from users where email = ?", ("x",)).fetchall()[0][-1]
    best = 1e9
    for _ in range(5):   # Round 1: find one user by email (the last one inserted)
        t = time.perf_counter(); r = db.execute("select id from users where email = ?", (f"user{N - 1}@mail.com",)).fetchall(); best = min(best, time.perf_counter() - t)
    assert r == [(N,)]
    t = time.perf_counter(); db.executemany("insert into users(email, age) values(?, ?)", rows(N, N + M)); db.commit(); add = time.perf_counter() - t   # Round 2: add 1,000,000 more users
    size = os.path.getsize(os.path.join(D, name)); db.close(); os.remove(os.path.join(D, name))
    print(f"{name} index={index} load_5M_s={load:.2f} find_ms={best * 1e3:.4f} add_1M_s={add:.3f} size_MB={size / 1e6:.0f} plan={plan}")
print("sqlite", sqlite3.sqlite_version)
