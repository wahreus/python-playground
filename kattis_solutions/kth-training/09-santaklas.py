"""
Problem link: https://open.kattis.com/problems/santaklas
Problem source: Oskar Werkelin Ahlin / KTH Training
"""

import sys
import math

def main() -> None:
    h, v = map(int, sys.stdin.readline().strip().split())
    if v <= 180:
        print("safe")
        return
    else:
        print(math.floor(h/math.sin(math.radians(v - 180))))

if __name__ == "__main__":
    main()