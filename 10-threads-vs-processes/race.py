# Which Wins? No. 10: threads vs processes in Python. Run: python3 race.py
import sys, time, threading, multiprocessing as mp

def heavy(n=3_000_000):          # one job of pure maths
    s = 0
    for i in range(n):
        s += i * i
    return s

def tiny():                       # one small job
    return 1

def timed(make, jobs):
    t = time.perf_counter(); ws = [make() for _ in range(jobs)]
    for w in ws: w.start()
    for w in ws: w.join()
    return (time.perf_counter() - t) * 1e3

def one_by_one(make, jobs):
    t = time.perf_counter()
    for _ in range(jobs):
        w = make(); w.start(); w.join()
    return (time.perf_counter() - t) * 1e3

if __name__ == "__main__":
    t = time.perf_counter(); heavy(); print(f"one_job {(time.perf_counter() - t) * 1e3:.1f} ms")
    for _ in range(3):   # Round 1: the same 8 heavy jobs, all at once
        print(f"r1_threads {timed(lambda: threading.Thread(target=heavy), 8):.1f} ms")
        print(f"r1_processes {timed(lambda: mp.Process(target=heavy), 8):.1f} ms")
    for _ in range(3):   # Round 2: 1,000 small jobs, a new worker for each, one after another
        print(f"r2_threads {one_by_one(lambda: threading.Thread(target=tiny), 1000):.1f} ms")
        print(f"r2_processes {one_by_one(lambda: mp.Process(target=tiny), 1000):.1f} ms")
    print("python", sys.version.split()[0], "start method", mp.get_start_method(), "switch interval", sys.getswitchinterval())
