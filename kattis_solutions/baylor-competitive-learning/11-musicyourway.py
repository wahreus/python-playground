"""
Problem link: https://open.kattis.com/problems/musicyourway
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    attributes = sys.stdin.readline().strip().split()
    n = int(sys.stdin.readline().strip())
    data_entries = []
    for _ in range(n):
        temp = {}
        data_entry = sys.stdin.readline().strip().split()
        for i, data in enumerate(data_entry):
            temp[attributes[i]] = data
        data_entries.append(temp)
    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        sorting_attribute = sys.stdin.readline().strip()
        data_entries.sort(key=lambda item: item[sorting_attribute])
        print(*attributes)
        for item in data_entries:
            print(*(item[attr] for attr in attributes))
        print()

if __name__ == "__main__":
    main()