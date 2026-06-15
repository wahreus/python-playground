"""
Problem link: https://open.kattis.com/problems/brillianceofwings
Problem source: Maximilliano Utomo Quok / NUS Competitive Programming
"""

import sys

def main() -> None:
    n = int(sys.stdin.readline().strip())
    current_tree = set()
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        edge = (u, v) if u < v else (v, u)
        current_tree.add(edge)
    target_tree = set()
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        edge = (u, v) if u < v else (v, u)
        target_tree.add(edge)
    print(len(current_tree - target_tree))
    return

if __name__ == "__main__":
    main()