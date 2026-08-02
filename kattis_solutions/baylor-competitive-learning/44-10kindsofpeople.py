"""
Problem link: https://open.kattis.com/problems/10kindsofpeople
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, first: int, second: int) -> None:
        root_first = self.find(first)
        root_second = self.find(second)
        if root_first != root_second:
            self.parent[root_second] = root_first

    def connected(self, first: int, second: int) -> bool:
        return self.find(first) == self.find(second)

def main() -> None:
    r, c = map(int, sys.stdin.readline().strip().split())
    grid = []
    for _ in range(r):
        grid.append(sys.stdin.readline().strip())
    union_find = UnionFind(r*c)
    for i in range(r):
        for j in range(c):
            current = i * c + j
            if j > 0 and grid[i][j] == grid[i][j - 1]:
                left = current - 1
                union_find.union(current, left)
            if i > 0 and grid[i][j] == grid[i - 1][j]:
                above = current - c
                union_find.union(current, above)
    queries = int(sys.stdin.readline().strip())
    for _ in range(queries):
        r1, c1, r2, c2 = map(int, [int(i)-1 for i in sys.stdin.readline().strip().split()])
        start = r1*c + c1
        target = r2*c + c2
        if not union_find.connected(start, target):
            print("neither")
        elif grid[r1][c1] == "0":
            print("binary")
        else:
            print("decimal")

if __name__ == "__main__":
    main()