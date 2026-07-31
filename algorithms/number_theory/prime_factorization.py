import math

def prime_factorization(number: int) -> dict[int, int]:
    primes = _generate_primes(math.isqrt(number))
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

def _generate_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for number in range(2, math.isqrt(limit) + 1):
        if is_prime[number]:
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
    return [number for number in range(2, limit + 1) if is_prime[number]]

def main() -> None:
    number = 360
    factors = prime_factorization(number)
    factorization = " * ".join(f"{prime}^{exponent}"for prime, exponent in factors.items())
    print(f"Prime factorization of {number}:\n{factorization}")


if __name__ == "__main__":
    main()