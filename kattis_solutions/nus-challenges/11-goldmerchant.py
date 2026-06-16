"""
Problem link: https://open.kattis.com/problems/goldmerchant
Problem source: Tan Yi Kai / NUS Competitive Programming
"""

from collections import defaultdict
import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a

def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    weights = list(map(int, sys.stdin.readline().split()))
    buyer_values = list(map(int, sys.stdin.readline().split()))
    uf = UnionFind(n)
    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())
        uf.union(i - 1, j - 1)
    swap_groups = defaultdict(list)
    for i in range(n):
        swap_groups[uf.find(i)].append(i)
    total = 0
    for swap_group in swap_groups.values():
        swap_group_weights = sorted(weights[i] for i in swap_group)
        swap_group_values = sorted(buyer_values[i] for i in swap_group)
        total += sum(w * v for w, v in zip(swap_group_weights, swap_group_values))
    print(total)

if __name__ == "__main__":
    main()