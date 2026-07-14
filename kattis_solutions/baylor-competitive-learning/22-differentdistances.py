"""
Problem link: https://open.kattis.com/problems/differentdistances
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        case = sys.stdin.readline().strip()
        if case == "0":
            break
        x1, y1, x2, y2, p = map(float, case.split())
        print((abs(x1-x2)**p+abs(y1-y2)**p)**(1/p))

if __name__ == "__main__":
    main()