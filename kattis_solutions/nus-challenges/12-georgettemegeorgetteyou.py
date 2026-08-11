"""
Problem link: https://open.kattis.com/problems/georgettemegeorgetteyou
Problem source: Maximilliano Utomo Quok / NUS Competitive Programming
"""

import sys

def calculate_counts(max_n: int, M: int) -> tuple[list[int], list[int]]:
    permutation_counts = [1]*(max_n+1)
    self_inverses = [1]*(max_n+1)
    for n in range(1, max_n+1):
        permutation_counts[n] = (n*permutation_counts[n-1])%M
        if n >= 2:
            self_inverses[n] = (self_inverses[n-1]+(n-1)*self_inverses[n-2])%M
    return permutation_counts, self_inverses

def main() -> None:
    while True:
        data = sys.stdin.readline().strip()
        if not data:
            return
        T, M = map(int, data.split())
        questions = []
        for _ in range(T):
            questions.append(int(sys.stdin.readline().strip()))
        max_n = max(questions)
        permutation_counts, self_inverses = calculate_counts(max_n, M)
        for N in questions:
            print((permutation_counts[N]-self_inverses[N])%M)

if __name__ == "__main__":
    main()