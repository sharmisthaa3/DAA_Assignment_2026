# Build and run

Requirements: Python 3.10 or newer. Plot generation requires matplotlib. Run these commands from `Batches/Batch_9` (or from the repository root using the paths shown below).

```bash
python --version
python code/main_solution.py
python code/rejected_alternative.py 5678 1234
python -m pip install matplotlib
python code/benchmark.py
```

The correctness script checks the worked example and 2,000 deterministic random cases against Python's exact integer result. The benchmark creates six input sizes and writes `results/timing.csv` and `results/timing_plot.png`. Timing values depend on the computer and runtime; rerun before submission and describe the actual environment.

**Security limitation:** these Python implementations are educational references, not constant-time cryptographic code. Python big-integer operations and control flow must not be used with secret RSA operands. The separate analysis sheet discusses a C implementation, but that C source file was not included in the supplied archive; do not claim this Python benchmark reproduces the C experiment or measures an HSM.
