import math

def prime_factorization(number: int, primes: list[int]) -> dict[int, int]:
    factors: dict[int, int] = {}
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

def generate_primes(limit: int) -> list[int]:
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for multiple in range(i * i, limit + 1, i):
                is_prime[multiple] = False
    return [num for num in range(2, limit + 1) if is_prime[num]]

def main() -> None:
    example = 120
    primes = generate_primes(math.isqrt(example))
    factors = prime_factorization(example, primes)
    factorization = " * ".join(f"{prime}^{exponent}"for prime, exponent in factors.items())
    print(f"Prime factorization of {example}:\n{factorization}")

if __name__ == "__main__":
    main()
