"""
Problem link: https://open.kattis.com/problems/metaprogramming
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def main() -> None:
    definitions = {}
    for line in sys.stdin.readlines():
        command = line.strip().split()
        command_type = command.pop(0)
        if command_type == "eval":
            x, y = command[0], command[2]
            if x not in definitions or y not in definitions:
                print("undefined")
                continue
            operator = command[1]
            if operator == "<":
                if definitions[x] < definitions[y]:
                    print("true")
                else:
                    print("false")
            elif operator == ">":
                if definitions[x] > definitions[y]:
                    print("true")
                else:
                    print("false")
            else:
                if definitions[x] == definitions[y]:
                    print("true")
                else:
                    print("false")
        else:
            definitions[command[1]] = int(command[0])

if __name__ == "__main__":
    main()