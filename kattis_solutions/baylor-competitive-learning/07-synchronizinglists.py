"""
Problem link: https://open.kattis.com/problems/synchronizinglists
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        first_list = []
        second_list = []
        for _ in range(n):
            first_list.append(int(sys.stdin.readline()))
        for _ in range(n):
            second_list.append(int(sys.stdin.readline()))
        first_sorted = sorted(first_list)
        second_sorted = sorted(second_list)
        rank = {value: i for i, value in enumerate(first_sorted)}
        for value in first_list:
            print(second_sorted[rank[value]])
        print()

if __name__ == "__main__":
    main()