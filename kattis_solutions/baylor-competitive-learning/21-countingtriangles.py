"""
Problem link: https://open.kattis.com/problems/countingtriangles
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from itertools import combinations

def intersects(l1, l2):
    (x1, y1), (x2, y2) = l1
    (x3, y3), (x4, y4) = l2
    dx1, dy1 = x2-x1, y2-y1
    dx2, dy2 = x4-x3, y4-y3
    denominator = dx1*dy2 - dy1*dx2
    if dx1*dy2 - dy1*dx2 == 0:
        return False
    px = ((x3-x1)*dy2 - (y3-y1)*dx2)/denominator
    py = ((x3-x1)*dy1 - (y3-y1)*dx1)/denominator
    return 0 <= px <= 1 and 0 <= py <= 1

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            break
        lines = []
        for _ in range(n):
            x1, y1, x2, y2 = map(float, sys.stdin.readline().split())
            lines.append(((x1, y1), (x2, y2)))
        triangles = 0
        for a, b, c in combinations(lines, 3):
            if intersects(a, b) and intersects(a, c) and intersects(b, c):
                triangles += 1
        print(triangles)

if __name__ == "__main__":
    main()