#!/usr/bin/env python3
"""Generate deterministic input sizes for the benchmark."""
import random
def make_pair(digits, seed=2026):
    rng = random.Random(seed + digits)
    lo = 10 ** (digits - 1) if digits > 1 else 0
    hi = 10 ** digits
    return rng.randrange(lo, hi), rng.randrange(lo, hi)
