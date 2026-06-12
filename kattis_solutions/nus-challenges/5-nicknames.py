"""
Problem link: https://open.kattis.com/problems/nicknames
Problem source: Shantanu Modak / NUS Competitive Programming
"""

import sys

def main() -> None:
    noNames = int(sys.stdin.readline().strip())
    names = []
    for _ in range(noNames):
        names.append(sys.stdin.readline().strip())
    noNicknames = int(sys.stdin.readline().strip())
    nicknames = []
    for _ in range(noNicknames):
        nicknames.append(sys.stdin.readline().strip())
    prefix_count = {}
    for name in names:
        prefix = ""
        for char in name:
            prefix += char
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1
    for nickname in nicknames:
        print(prefix_count.get(nickname, 0))

if __name__ == "__main__":
    main()