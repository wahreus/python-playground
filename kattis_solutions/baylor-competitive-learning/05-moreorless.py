"""
Problem link: https://open.kattis.com/problems/moreorless
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    lines = sys.stdin.readlines()
    for line in lines:
        a, b = map(int, line.strip().split())
        if a > b:
            print("More")
        elif b > a:
            print("Less")
        else:
            return

if __name__ == "__main__":
    main()