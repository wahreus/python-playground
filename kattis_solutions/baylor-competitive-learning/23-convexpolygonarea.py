"""
Problem link: https://open.kattis.com/problems/weakvertices
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def polygon_area(points):
    area = 0
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2

def main() -> None:
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        points = []
        polygon = list(map(int, sys.stdin.readline().strip().split()))
        m = polygon.pop(0)
        for _ in range(m):
            x = polygon.pop(0)
            y = polygon.pop(0)
            points.append((x, y))
        print(polygon_area(points))

if __name__ == "__main__":
    main()