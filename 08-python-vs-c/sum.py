# Which Wins? No. 8: the Python side. Add up the squares of 100,000,000 numbers, two ways.
# Run: python3 sum.py
import time, numpy as np
N = 100_000_000
a = np.arange(N, dtype=np.float64) % 1000
lst = a.tolist()

for run in range(2):                      # Round 1: a plain Python loop
    t0 = time.perf_counter(); total = 0.0
    for x in lst:
        total += x * x
    print(f"py_loop {(time.perf_counter() - t0) * 1e3:.1f} ms total {total:.0f}")

for run in range(5):                      # Round 2: one NumPy call
    t0 = time.perf_counter(); total = float(np.dot(a, a))
    print(f"py_numpy {(time.perf_counter() - t0) * 1e3:.1f} ms total {total:.0f}")

for run in range(3):                      # For the caption: the other obvious NumPy line makes a 100,000,000-number temporary first
    t0 = time.perf_counter(); total = float((a * a).sum())
    print(f"py_numpy_temp {(time.perf_counter() - t0) * 1e3:.1f} ms total {total:.0f}")
