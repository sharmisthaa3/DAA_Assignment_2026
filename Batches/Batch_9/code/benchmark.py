#!/usr/bin/env python3
"""Benchmark schoolbook vs Karatsuba and create CSV/plot.
Run from repository root: python code/benchmark.py
Timings are from the machine on which this script is run.
"""
import csv, statistics, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from main_solution import schoolbook, karatsuba
from generate_inputs import make_pair

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)
SIZES = [8, 16, 32, 64, 128, 256]  # decimal digits; at least five sizes
REPEATS = 3

def time_call(fn, x, y, repeats=REPEATS):
    samples = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        ans = fn(x, y)
        samples.append((time.perf_counter_ns() - t0) / 1e6)
    return statistics.median(samples), ans

rows = []
for digits in SIZES:
    x, y = make_pair(digits)
    t_school, a = time_call(schoolbook, x, y)
    t_kara, b = time_call(karatsuba, x, y)
    assert a == b == x * y
    rows.append((digits, f"{t_kara:.6f}", f"{t_school:.6f}"))
    print(f"{digits} digits: Karatsuba={t_kara:.6f} ms, schoolbook={t_school:.6f} ms")

with (RESULTS / "timing.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["input_size_digits", "time_chosen_ms", "time_rejected_ms"])
    w.writerows(rows)

try:
    import matplotlib.pyplot as plt
except ImportError:
    print("CSV created. To create the plot, install matplotlib: python -m pip install matplotlib")
    raise SystemExit(0)

sizes = [int(r[0]) for r in rows]
chosen = [float(r[1]) for r in rows]
rejected = [float(r[2]) for r in rows]
plt.figure()
plt.plot(sizes, chosen, marker="o", label="Karatsuba (chosen)")
plt.plot(sizes, rejected, marker="o", label="Schoolbook (rejected)")
plt.xlabel("Input size (decimal digits)")
plt.ylabel("Median running time (ms)")
plt.title("Karatsuba vs schoolbook multiplication")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(RESULTS / "timing_plot.png", dpi=160)
print("Wrote results/timing.csv and results/timing_plot.png")
