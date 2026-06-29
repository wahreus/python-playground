"""
Problem link: https://open.kattis.com/problems/color
Problem source: Johan Sannemo and Oskar Werkelin Ahlin / KTH Training
"""

import sys

def main() -> None:
    s, c, k = map(int, sys.stdin.readline().split())
    socks = sorted(list(map(int, sys.stdin.readline().split())))
    machines = 1
    curr_colour = socks.pop(0)
    socks_in_machine = 1
    for sock in socks:
        if socks_in_machine == c or sock - curr_colour > k:
            machines += 1
            curr_colour = sock
            socks_in_machine = 1
        else:
            socks_in_machine += 1
    print(machines)

if __name__ == "__main__":
    main()