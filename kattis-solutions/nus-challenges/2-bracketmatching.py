"""
Problem link: https://open.kattis.com/problems/bracketmatching
Problem source: Zhang Guangxuan / NUS Competitive Programming
"""

import sys

def main() -> None:
    _, sequence = sys.stdin.read().splitlines()
    open_bracket = "([{"
    expected_close = {"(":")", "[":"]", "{":"}"}
    stack = []
    for bracket in sequence:
        if bracket in open_bracket:
            stack.append(bracket)
        elif not stack or expected_close[stack[-1]] != bracket:
            print("Invalid")
            return
        else:
            stack.pop()
    print("Valid" if not stack else "Invalid")

main()