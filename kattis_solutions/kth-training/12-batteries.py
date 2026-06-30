"""
Problem link: https://open.kattis.com/problems/batteries
Problem source: Gunnar Kreitz / KTH Training
"""

import sys

def main() -> None:
    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        max_current = n - 1
        no_tests, covered = 0, 0
        while covered < max_current:
            no_tests += 1
            covered += no_tests
        print(no_tests)

if __name__ == "__main__":
    main()