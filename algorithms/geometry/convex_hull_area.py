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
        return 0.0
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
    hull = lower[:-1] + upper[:-1]
    return polygon_area(hull)

def main() -> None:
    points = [
             (0, 0),
             (4, 0),
             (4, 3),
             (0, 3),
             (1, 1),
             (2, 2),
             ]
    area = convex_hull(points)
    print(f"Convex hull area: {area}")

if __name__ == "__main__":
    main()
