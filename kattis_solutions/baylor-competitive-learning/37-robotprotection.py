"""
Problem link: https://open.kattis.com/problems/robotprotection
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))

def polygon_area(hull):
    area = 0
    for current, following in zip(hull, hull[1:] + hull[:1]):
        x1, y1 = current
        x2, y2 = following
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]

def main():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
        hull = convex_hull(points)
        area = polygon_area(hull)
        print(f"{area:.1f}")

if __name__ == "__main__":
    main()