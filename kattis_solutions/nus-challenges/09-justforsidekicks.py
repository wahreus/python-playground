"""
Problem link: https://open.kattis.com/problems/justforsidekicks
Problem source: Robin Christopher Yu / NUS Competitive Programming
"""

import sys

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
    def add(self, index, value):
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index
    def prefix_sum(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total
    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

def main() -> None:
    n, q = map(int, sys.stdin.readline().split())
    gem_value = list(map(int, sys.stdin.readline().split()))
    gems = [int(i) for i in sys.stdin.readline().strip()]
    trees = [FenwickTree(n) for _ in range(6)]
    for index, gem_type in enumerate(gems, start=1):
        trees[gem_type - 1].add(index, 1)
    for _ in range(q):
        query = list(map(int, sys.stdin.readline().split()))
        query_type = query[0]
        if query_type == 1:
            k, p = query[1], query[2]
            old_type = gems[k - 1]
            trees[old_type - 1].add(k, -1)
            trees[p - 1].add(k, 1)
            gems[k - 1] = p
        elif query_type == 2:
            p, v = query[1], query[2]
            gem_value[p - 1] = v
        else:
            l, r = query[1], query[2]
            total = 0
            for gem_type in range(6):
                count = trees[gem_type].range_sum(l, r)
                total += count * gem_value[gem_type]
            print(total)

if __name__ == "__main__":
    main()