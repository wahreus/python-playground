"""
Problem link: https://open.kattis.com/problems/fastestavailableroute
Problem source: Dan Alden Baterisna / NUS Competitive Programming
"""

import sys

def main() -> None:
    h, w, s = map(int, sys.stdin.readline().split())
    path_cells = 0
    for _ in range(h):
        row = sys.stdin.readline().strip()
        for symbol in row:
            if symbol in "@$.":
                path_cells += 1
    distance = (path_cells - 1) * s
    print(f"Your destination will arrive in {distance} meters")

if __name__ == "__main__":
    main()