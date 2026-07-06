"""
Problem link: https://open.kattis.com/problems/compoundwords
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from itertools import permutations

def main() -> None:
    words = []
    for line in sys.stdin:
        words.extend(line.strip().split())
    compoundwords = set()
    for a, b in permutations(words, 2):
        compoundwords.add(a + b)
    for word in sorted(compoundwords):
        print(word)

if __name__ == "__main__":
    main()