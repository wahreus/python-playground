"""
Problem link: https://open.kattis.com/problems/estimatingtheareaofacircle
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys
import math

def main() -> None:
    for line in sys.stdin:
        r, m, c = map(float, line.split())
        if r == 0:
            break
        area = math.pi*r*r
        estimate = 4*r*r*c/m
        print(area, estimate)

if __name__ == "__main__":
    main()