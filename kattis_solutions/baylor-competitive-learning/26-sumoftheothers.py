"""
Problem link: https://open.kattis.com/problems/sumoftheothers
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    for line in sys.stdin:
        numbers = list(map(int, line.split()))
        number_sum = sum(numbers)
        for number in numbers:
            if number_sum == 2 * number:
                print(number)
                break

if __name__ == "__main__":
    main()