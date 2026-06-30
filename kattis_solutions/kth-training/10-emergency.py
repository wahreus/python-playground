"""
Problem link: https://open.kattis.com/problems/emergency
Problem source: Oskar Werkelin Ahlin / KTH Training
"""

import sys

def main() -> None:
    n, k = map(int, sys.stdin.readline().strip().split())
    print(min(n-1, k + 1 + (n-1) % k))
    
if __name__ == "__main__":
    main()