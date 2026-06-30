"""
Problem link: https://open.kattis.com/problems/paintbuckets
Problem source: Johan Sannemo / KTH Training
"""

import sys
from bisect import bisect_left, bisect_right

def main() -> None:
    n, q = map(int, sys.stdin.readline().split())
    inventory = {}
    for _ in range(n):
        hue, volume = map(int, sys.stdin.readline().split())
        inventory[hue] = inventory.get(hue, 0) + volume
    hues = sorted(inventory)
    prefix = [0]
    for hue in hues:
        prefix.append(prefix[-1] + inventory[hue])
    for _ in range(q):
        hue, volume = map(int, sys.stdin.readline().split())
        left = bisect_left(hues, hue - 1000)
        right = bisect_right(hues, hue + 1000)
        available = prefix[right] - prefix[left]
        if available >= volume:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()