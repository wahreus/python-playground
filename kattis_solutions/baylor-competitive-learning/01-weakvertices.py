"""
Problem link: https://open.kattis.com/problems/weakvertices
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == -1:
            break
        mtrx = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
        weak_vertices = []
        for i in range(n):
            weak_vertex = True
            for j in range(n):
                for k in range(n):
                    if mtrx[i][j] == 1 and mtrx[i][k] == 1 and mtrx[j][k] == 1:
                        weak_vertex = False
            if weak_vertex:
                weak_vertices.append(i)
        print(*weak_vertices)

if __name__ == "__main__":
    main()