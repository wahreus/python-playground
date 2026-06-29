"""
Problem link: https://open.kattis.com/problems/pauleigon
Problem source: Oskar Werkelin Ahlin / KTH Training
"""

import sys

def main() -> None:
    n, p, q = map(int, sys.stdin.readline().strip().split())
    turns_played = p + q
    if (turns_played//n) % 2 == 0:
        print("paul")
    else:
        print("opponent")
    
if __name__ == "__main__":
    main()