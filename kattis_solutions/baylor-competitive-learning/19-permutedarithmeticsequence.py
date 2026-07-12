"""
Problem link: https://open.kattis.com/problems/permutedarithmeticsequence
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def is_arithmetic(numbers: list[int]) -> bool:
    difference = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers[i - 1] != difference:
            return False
    return True

def main() -> None:
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        numbers = list(map(int, sys.stdin.readline().split()))[1:]
        if is_arithmetic(numbers):
            print("arithmetic")
        elif is_arithmetic(sorted(numbers)):
            print("permuted arithmetic")
        else:
            print("non-arithmetic")

if __name__ == "__main__":
    main()