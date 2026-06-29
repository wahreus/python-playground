"""
Problem link: https://open.kattis.com/problems/teacherevaluation
Problem source: Johan Sannemo / KTH Training
"""

import sys

def main() -> None:
    n, p = map(int, sys.stdin.readline().split())
    if p == 100:
        print("impossible")
        return
    scores = list(map(int, sys.stdin.readline().split()))
    scores_sum = sum(scores)
    additional_score = 0
    while scores_sum / (n + additional_score) < p:
        scores_sum += 100
        additional_score += 1
    print(additional_score)

if __name__ == "__main__":
    main()