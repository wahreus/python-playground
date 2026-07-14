"""
Problem link: https://open.kattis.com/problems/functionalfun
Problem x: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def is_injective(mappings: dict[str, str]) -> bool:
    mapped_values = list(mappings.values())
    return len(mapped_values) == len(set(mapped_values))

def is_surjective(codomain: list[str], mappings: dict[str, str]) -> bool:
    return set(codomain).issubset(set(mappings.values()))

def main() -> None:
    while True:
        domain = sys.stdin.readline()
        if not domain:
            break
        domain = domain.strip().split()[1:]
        codomain = sys.stdin.readline().strip().split()[1:]
        n = int(sys.stdin.readline().strip())
        mappings = {}
        is_function = True
        for _ in range(n):
            x, _, y_of_x = sys.stdin.readline().strip().split()
            if x in mappings and mappings[x] != y_of_x:
                is_function = False
            else:
                mappings[x] = y_of_x
        if not is_function:
            print("not a function")
            continue
        injective = is_injective(mappings)
        surjective = is_surjective(codomain, mappings)
        if injective and surjective:
            print("bijective")
        elif injective:
            print("injective")
        elif surjective:
            print("surjective")
        else:
            print("neither injective nor surjective")

if __name__ == "__main__":
    main()