"""
Problem link: https://open.kattis.com/problems/bitbybit
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def main() -> None:
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        output = ["?"] * 32
        for _ in range(n):
            instruction = sys.stdin.readline().split()
            instruction_type = instruction[0]
            i = int(instruction[1])
            if instruction_type == "SET":
                output[i] = "1"
            elif instruction_type == "CLEAR":
                output[i] = "0"
            else:
                j = int(instruction[2])
                if instruction_type == "AND":
                    if output[i] == "0" or output[j] == "0":
                        output[i] = "0"
                    elif output[i] == "1" and output[j] == "1":
                        output[i] = "1"
                    else:
                        output[i] = "?"
                elif instruction_type == "OR":
                    if output[i] == "1" or output[j] == "1":
                        output[i] = "1"
                    elif output[i] == "0" and output[j] == "0":
                        output[i] = "0"
                    else:
                        output[i] = "?"
        print(*reversed(output), sep="")

if __name__ == "__main__":
    main()