"""
Problem link: https://open.kattis.com/problems/cursethedarkness
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys

def distance(book_x, book_y, candle_x, candle_y):
    return (abs(book_x-candle_x)**2 + (abs(book_y-candle_y)**2))**0.5

def main() -> None:
    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        book_x, book_y = map(float, sys.stdin.readline().strip().split())
        n =  int(sys.stdin.readline().strip())
        found = False
        for _ in range(n):
            candle_x, candle_y = map(float, sys.stdin.readline().strip().split())
            if not found:
                if distance(book_x, book_y, candle_x, candle_y) <= 8:
                    print("light a candle")
                    found = True
        if not found:
            print("curse the darkness")

if __name__ == "__main__":
    main()