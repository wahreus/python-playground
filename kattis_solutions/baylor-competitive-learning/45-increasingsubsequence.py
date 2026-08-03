"""
Problem link: https://open.kattis.com/problems/increasingsubsequence
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        line = sys.stdin.readline().strip()
        if line == "0":
            return
        sequence = list(map(int, line.split()))
        sequence_len = sequence.pop(0)
        candidates = []
        for i in range(sequence_len):
            candidate = [sequence[i]]
            for j in range(i):
                if sequence[j] < sequence[i]:
                    new_candidate = candidates[j] + [sequence[i]]
                    if (len(new_candidate) > len(candidate) or (len(new_candidate) == len(candidate) and new_candidate < candidate)):
                        candidate = new_candidate
            candidates.append(candidate)
        top_candidate = min(candidates, key=lambda candidate: (-len(candidate), candidate))
        print(len(top_candidate), *top_candidate)

if __name__ == "__main__":
    main()