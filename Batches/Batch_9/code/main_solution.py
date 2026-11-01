#!/usr/bin/env python3
"""Karatsuba integer multiplication for learning/benchmarking only.
NOT constant-time; do not use with secret cryptographic operands.
"""
def schoolbook(x: int, y: int) -> int:
    if x < 0 or y < 0:
        raise ValueError("Only non-negative integers are supported")
    # Digit-by-digit decimal schoolbook method.
    a = [int(c) for c in str(x)][::-1]
    b = [int(c) for c in str(y)][::-1]
    out = [0] * (len(a) + len(b) + 1)
    for i, da in enumerate(a):
        carry = 0
        for j, db in enumerate(b):
            v = out[i + j] + da * db + carry
            out[i + j] = v % 10
            carry = v // 10
        k = i + len(b)
        while carry:
            v = out[k] + carry
            out[k] = v % 10
            carry = v // 10
            k += 1
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return int("".join(map(str, out[::-1])))

def karatsuba(x: int, y: int, threshold_digits: int = 16) -> int:
    if x < 0 or y < 0:
        raise ValueError("Only non-negative integers are supported")
    if x == 0 or y == 0:
        return 0
    n = max(len(str(x)), len(str(y)))
    if n <= threshold_digits:
        return schoolbook(x, y)
    m = n // 2
    base = 10 ** m
    a, b = divmod(x, base)
    c, d = divmod(y, base)
    z2 = karatsuba(a, c, threshold_digits)
    z0 = karatsuba(b, d, threshold_digits)
    zsum = karatsuba(a + b, c + d, threshold_digits)
    z1 = zsum - z2 - z0
    return z2 * (base * base) + z1 * base + z0

if __name__ == "__main__":
    import random, sys
    tests = [(5678, 1234), (0, 999), (999999, 999999), (10**100-1, 10**100-1)]
    rng = random.Random(2026)
    for _ in range(2000):
        digits = rng.randint(1, 200)
        x = rng.randrange(10**(digits-1), 10**digits) if digits > 1 else rng.randrange(10)
        y = rng.randrange(10**(digits-1), 10**digits) if digits > 1 else rng.randrange(10)
        tests.append((x, y))
    for x, y in tests:
        assert karatsuba(x, y) == x * y
        assert schoolbook(x, y) == x * y
    print(f"PASS: {len(tests)} correctness cases")
    x, y = 5678, 1234
    print(f"{x} x {y} = {karatsuba(x, y)}")
