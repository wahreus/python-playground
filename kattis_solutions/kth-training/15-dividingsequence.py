"""
Problem link: https://open.kattis.com/problems/dividingsequence
Problem source: Lukáš Poláček / KTH Training
"""

import sys

def main():
    N = int(sys.stdin.readline())
    sequence = []
    i = 1
    while i <= N:
        sequence.append(i)
        i *= 2
    print(len(sequence))
    print(*sequence)

if __name__ == "__main__":
    main()
