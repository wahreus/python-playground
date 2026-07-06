"""
Problem link: https://open.kattis.com/problems/halfacookie
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
import math

def main() -> None:
    for line in sys.stdin:
        r, x, y = map(float, line.strip().split())
        d = math.sqrt(x**2+y**2)
        if d > r:
            print("miss")
            continue
        area2 = r*r*math.acos(d/r)-d*math.sqrt(r*r-d*d)
        area1 = math.pi*r*r - area2
        print(area1, area2)

if __name__ == "__main__":
    main()