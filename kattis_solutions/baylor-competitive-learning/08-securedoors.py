"""
Problem link: https://open.kattis.com/problems/securedoors
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    n = int(sys.stdin.readline().strip())
    building = []
    log = []
    for _ in range(n):
        action, name = sys.stdin.readline().strip().split()
        if name not in building and action == "exit":
            log.append(f"{name} exited (ANOMALY)")
        elif name in building and action == "exit":
            log.append(f"{name} exited")
            building.remove(name)
        elif name in building and action == "entry":
            log.append(f"{name} entered (ANOMALY)")
        else:
            log.append(f"{name} entered")
            building.append(name)
    print("\n".join(log))

if __name__ == "__main__":
    main()