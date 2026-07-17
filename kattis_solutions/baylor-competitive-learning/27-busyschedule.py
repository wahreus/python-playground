"""
Problem link: https://open.kattis.com/problems/busyschedule
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from collections import defaultdict

def main() -> None:
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        times = defaultdict(list)
        for _ in range(n):
            time, unit = sys.stdin.readline().strip().split()
            H, M = map(int, time.split(":"))
            times[unit].append((H%12, H, M))
        for _, H, M in sorted(times["a.m."], key=lambda item:(item[0], item[2])):
            print(f"{H}:{M:02} a.m.")
        for _, H, M in sorted(times["p.m."], key=lambda item:(item[0], item[2])):
            print(f"{H}:{M:02} p.m.")

if __name__ == "__main__":
    main()