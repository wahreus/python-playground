"""
Problem link: https://open.kattis.com/problems/universityzoning
Problem source: Matthew Ng Zhen Rui / NUS Competitive Programming
"""

import sys

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main() -> None:
    _, _, F, S, G = map(int, sys.stdin.readline().split())
    faculty_zones = {}
    for zone_id in range(1, F+1):
        zone_info = list(map(int, sys.stdin.readline().split()))
        cells = []
        for i in range(zone_info.pop(0)):
            cells.append((zone_info[2*i], zone_info[2*i+1]))
        faculty_zones[zone_id] = {"cells": sorted(cells), "students": [], "target": None}
    for _ in range(S):
        r, c, student_id, zone_id = map(int, sys.stdin.readline().split())
        faculty_zones[zone_id]["students"].append((student_id, (r, c)))
    for zone_id, target in enumerate(map(int, sys.stdin.readline().split()), start=1):
        faculty_zones[zone_id]["target"] = target
    steps_per_zone = []
    for zone_id in range(1, F+1):
        distances = []
        cells = faculty_zones[zone_id]["cells"]
        for i, (_, position) in enumerate(sorted(faculty_zones[zone_id]["students"])):
            faculty_cell = cells[i]
            distances.append(manhattan_distance(position, faculty_cell))
        distances.sort()
        steps_per_zone.append(sum(distances[:faculty_zones[zone_id]["target"]]))
    steps_per_zone.sort()
    print(sum(steps_per_zone[:G]))

if __name__ == "__main__":
    main()