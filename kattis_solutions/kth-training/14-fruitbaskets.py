"""
Problem link: https://open.kattis.com/problems/fruitbaskets
Problem source: Lukáš Poláček / KTH Training
"""

import sys
from itertools import combinations

def main() -> None:
    n = int(sys.stdin.readline().strip())
    fruit_weights = list(map(int, sys.stdin.readline().strip().split()))
    total_weight = sum(fruit_weights)*(2**(n-1))
    for r in range(1, 4):
        for basket in combinations(fruit_weights, r):
            weight = sum(basket)
            if weight < 200:
                total_weight -= weight
    print(total_weight)

if __name__ == "__main__":
    main()