"""
Problem link: https://open.kattis.com/problems/enlarginghashtables
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        if number % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        min_prime = 2 * n + 1
        while not is_prime(min_prime):
            min_prime += 2
        if is_prime(n):
            print(min_prime)
        else:
            print(f"{min_prime} ({n} is not prime)")

if __name__ == "__main__":
    main()