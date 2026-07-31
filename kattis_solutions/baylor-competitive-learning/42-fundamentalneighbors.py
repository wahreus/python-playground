"""
Problem link: https://open.kattis.com/problems/fundamentalneighbours
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import math
import sys

def generate_primes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for number in range(2, math.isqrt(limit) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
    return [number for number in range(2, limit + 1) if is_prime[number]]

def prime_factorization(number: int, primes: list[int]) -> dict[int, int]:
    factors = {}
    for prime in primes:
        if prime * prime > number:
            break
        exponent = 0
        while number % prime == 0:
            number //= prime
            exponent += 1
        if exponent > 0:
            factors[prime] = exponent
    if number > 1:
        factors[number] = 1
    return factors

def fundamental_neighbour(number: int, primes: list[int]) -> int:
    factors = prime_factorization(number, primes)
    neighbour = 1
    for prime, exponent in factors.items():
        neighbour *= exponent ** prime
    return neighbour

def main() -> None:
    numbers = list(map(int, sys.stdin.read().split()))
    if not numbers:
        return
    prime_limit = math.isqrt(max(numbers))
    primes = generate_primes(prime_limit)
    for number in numbers:
        neighbour = fundamental_neighbour(number, primes)
        print(number, neighbour)

if __name__ == "__main__":
    main()