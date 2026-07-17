"""
Problem link: https://open.kattis.com/problems/iboard
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    for line in sys.stdin.readlines():
        binary = ''.join(f"{ord(char):07b}" for char in line.strip())
        if binary.count("1")%2==1 or binary.count("0")%2==1:
            print("trapped")
        else:
            print("free")

if __name__ == "__main__":
    main()