"""
Problem link: https://open.kattis.com/problems/busnumbers
Problem source: Lukáš Poláček / KTH Training
"""

import sys

def append_expr(output: list[str], curr_expr: list[int]) -> None:
    if len(curr_expr) > 2:
        output.append(str(curr_expr[0]) + "-" + str(curr_expr[-1]))
    else:
        for number in curr_expr:
            output.append(str(number))

def main() -> None:
    n = int(sys.stdin.readline().strip())
    bus_numbers = list(map(int, sys.stdin.readline().split()))
    bus_numbers.sort()
    output = []
    curr_expr = [bus_numbers.pop(0)]
    for number in bus_numbers:
        if number == curr_expr[-1] + 1:
            curr_expr.append(number)
        else:
            append_expr(output, curr_expr)
            curr_expr = [number]
    append_expr(output, curr_expr)
    print(*output)

if __name__ == "__main__":
    main()