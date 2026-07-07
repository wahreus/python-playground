"""
Problem link: https://open.kattis.com/problems/baconeggsandspam
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from collections import defaultdict

def main() -> None:
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            return
        breakfast_items = defaultdict(list)
        for _ in range(n):
            order = sys.stdin.readline().strip().split()
            name = order.pop(0)
            for item in order:
                breakfast_items[item].append(name)
        for item, names in sorted(breakfast_items.items()):
            print(item, *sorted(names))
        print()

if __name__ == "__main__":
    main()