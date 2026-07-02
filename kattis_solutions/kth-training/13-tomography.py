"""
Problem link: https://open.kattis.com/problems/tomography
Problem source: Ulf Lundström / KTH Training
"""

import sys

def main() -> None:
    m, n = map(int, sys.stdin.readline().split())
    row_constraints = list(map(int, sys.stdin.readline().split()))
    col_constraints = list(map(int, sys.stdin.readline().split()))
    if sum(row_constraints) != sum(col_constraints):
        print("No")
        return
    for r in sorted(row_constraints, reverse=True):
        col_constraints = sorted(col_constraints, reverse=True)
        if r > 0:
            if r > n or col_constraints[r - 1] == 0:
                print("No")
                return
            for i in range(r):
                col_constraints[i] -= 1
    print("Yes" if all(c == 0 for c in col_constraints) else "No")

if __name__ == "__main__":
    main()