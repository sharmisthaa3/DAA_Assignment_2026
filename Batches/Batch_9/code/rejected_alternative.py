#!/usr/bin/env python3
"""Rejected alternative: decimal-digit schoolbook multiplication."""
from main_solution import schoolbook
if __name__ == "__main__":
    import sys
    x = int(sys.argv[1]) if len(sys.argv) > 1 else 5678
    y = int(sys.argv[2]) if len(sys.argv) > 2 else 1234
    print(schoolbook(x, y))
