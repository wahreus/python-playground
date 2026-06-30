"""
Problem link: https://open.kattis.com/problems/detaileddifferences
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        a = sys.stdin.readline().strip()
        b = sys.stdin.readline().strip()
        c = "".join("." if x == y else "*" for x, y in zip(a, b))
        print(a)
        print(b)
        print(c)

if __name__ == "__main__":
    main()