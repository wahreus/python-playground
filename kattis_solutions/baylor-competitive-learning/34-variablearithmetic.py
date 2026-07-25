"""
Problem link: https://open.kattis.com/problems/variablearithmetic
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    known_variables = {}
    while True:
        items = sys.stdin.readline().strip().split()
        if items == ["0"]:
            return
        if len(items) == 3 and items[1] == "=":
            known_variables[items[0]] = int(items[2])
            continue
        unknown_variables = []
        numeric_sum = 0
        for item in items:
            if item == "+":
                continue
            if item.isnumeric():
                numeric_sum += int(item)
            elif item in known_variables:
                numeric_sum += known_variables[item]
            else:
                unknown_variables.append(item)
        output = []
        if numeric_sum != 0:
            output.append(str(numeric_sum))
        output.extend(unknown_variables)
        if not output:
            output.append("0")
        print(" + ".join(output))

if __name__ == "__main__":
    main()