"""
Problem link: https://open.kattis.com/problems/vacuumba
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
import math

def make_move(degree, distance, position):
    radians = math.radians(degree+90)
    position[0] += math.cos(radians)*distance
    position[1] += math.sin(radians)*distance
    return position

def main() -> None:
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        position = [0, 0]
        degree = 0
        for _ in range(int(sys.stdin.readline().strip())):
            degree_delta, distance = map(float, sys.stdin.readline().strip().split())
            degree += degree_delta
            position = make_move(degree, distance, position)
        print('{0:.6g}'.format(position[0]), '{0:.6g}'.format(position[1]))

if __name__ == "__main__":
    main()