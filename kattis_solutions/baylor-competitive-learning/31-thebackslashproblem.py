"""
Problem link: https://open.kattis.com/problems/thebackslashproblem
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    lines = sys.stdin.readlines()
    special_characters = {"!", '"', "#", "$", "%", "&", "'", "(", ")", "*","[", "\\", "]"}
    while lines:
        level = int(lines.pop(0).strip())
        line = lines.pop(0).strip()
        to_print = ""
        for char in line:
            if char in special_characters:
                to_print += "\\"*(2**level - 1) + char
            else:
                to_print += char
        print(to_print)

if __name__ == "__main__":
    main()