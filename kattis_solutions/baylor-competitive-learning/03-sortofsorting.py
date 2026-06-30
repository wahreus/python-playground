"""
Problem link: https://open.kattis.com/problems/sortofsorting
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            return
        output = []
        for _ in range(n):
            output.append(sys.stdin.readline().strip())
        output.sort(key=lambda name: name[:2])
        for item in output:
            print(item)
        print("")
       

if __name__ == "__main__":
    main()