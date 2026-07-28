"""
Problem link: https://open.kattis.com/problems/almostperfect
Problem source: David Sturgill / Baylor Competitive Learning
"""

import math
import sys

def main() -> None:
    for line in sys.stdin:
        p = int(line)
        proper_divisor_sum = 0
        for d in range(1, math.isqrt(p) + 1):
            if p % d == 0:
                d2 = p // d
                if d != p:
                    proper_divisor_sum += d
                if d2 != d and d2 != p:
                    proper_divisor_sum += d2
        if proper_divisor_sum == p:
            print(f"{p} perfect")
        elif abs(proper_divisor_sum - p) <= 2:
            print(f"{p} almost perfect")
        else:
            print(f"{p} not perfect")

if __name__ == "__main__":
    main()