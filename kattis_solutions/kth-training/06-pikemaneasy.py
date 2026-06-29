"""
Problem link: https://open.kattis.com/problems/pikemaneasy
Problem source: Oskar Werkelin Ahlin and Johan Sannemo / KTH Training
"""

import sys

def main() -> None:
    n, t = map(int, sys.stdin.readline().split())
    a, b, c, t0 = map(int, sys.stdin.readline().split())
    times = [t0]
    for _ in range(1, n):
        times.append((a * times[-1] + b) % c + 1)
    times.sort()
    elapsed, solved, penalty = 0, 0, 0
    for time in times:
        if elapsed + time > t:
            break
        elapsed += time
        solved += 1
        penalty = (penalty + elapsed) % 1000000007
    print(solved, penalty)

if __name__ == "__main__":
    main()