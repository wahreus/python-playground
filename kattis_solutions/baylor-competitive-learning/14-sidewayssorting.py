"""
Problem link: https://open.kattis.com/problems/sidewayssorting
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        r, c = map(int, sys.stdin.readline().strip().split())
        if r == 0 and c == 0:
            return
        blocks = ["" for i in range(c)]
        for _ in range(r):
            block = sys.stdin.readline().strip()
            for i, item in enumerate(block):
                blocks[i] += item
        blocks.sort(key=lambda item: item.lower())
        output = []
        for i in range(r):
            temp = ""
            for j in range(c):
                temp += blocks[j][i]
            output.append(temp)
        output[-1] += "\n"
        for line in output:
            print(line)

if __name__ == "__main__":
    main()