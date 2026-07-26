"""
Problem link: https://open.kattis.com/problems/parsinghex
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import re
import sys

HEX_PATTERN = re.compile(r"0[xX][0-9a-fA-F]+")

def main():
    for line in sys.stdin:
        for match in HEX_PATTERN.finditer(line):
            hexadecimal = match.group()
            print(hexadecimal, int(hexadecimal, 16))

if __name__ == "__main__":
    main()