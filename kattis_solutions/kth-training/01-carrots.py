"""
Problem link: https://open.kattis.com/problems/carrots
Problem source: Johan Sannemo and Oskar Werkelin Ahlin / KTH Training
"""

import sys

def main() -> None:
    _, p = map(int, sys.stdin.readline().strip().split())
    print(p)

if __name__ == "__main__":
    main()