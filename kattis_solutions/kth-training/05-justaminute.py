"""
Problem link: https://open.kattis.com/problems/justaminute
Problem source: Johan Sannemo and Oskar Werkelin Ahlin / KTH Training
"""

import sys

def main() -> None:
    n = int(sys.stdin.readline().strip())
    tot_waited = 0
    tot_displayed = 0
    for _ in range(n):
        displayed, waited =  map(int, sys.stdin.readline().split())
        tot_displayed += displayed * 60
        tot_waited += waited
    avg = tot_waited/tot_displayed
    if avg > 1:
        print(avg)
    else:
        print("measurement error")

if __name__ == "__main__":
    main()