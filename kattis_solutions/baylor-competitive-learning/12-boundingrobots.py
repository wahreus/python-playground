"""
Problem link: https://open.kattis.com/problems/boundingrobots
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def make_move(robot_position, actual_position, move, distance, w, l):
    directions = {
                 "u": (0, 1),
                 "d": (0, -1),
                 "l": (-1, 0),
                 "r": (1, 0)
                 }
    dx, dy = directions[move]
    dx *= distance
    dy *= distance
    robot_position[0] += dx
    robot_position[1] += dy
    actual_position[0] = max(0, min(actual_position[0] + dx, w))
    actual_position[1] = max(0, min(actual_position[1] + dy, l))
    return robot_position, actual_position

def main() -> None:
    while True:
        w, l = map(int, sys.stdin.readline().strip().split())
        if w == 0 and l == 0:
            return
        robot_position, actual_position = [0, 0], [0, 0]
        for _ in range(int(sys.stdin.readline().strip())):
            move, distance = sys.stdin.readline().strip().split()
            robot_position, actual_position = make_move(robot_position,
                                                        actual_position,
                                                        move,
                                                        int(distance),
                                                        w-1,
                                                        l-1)
        print(f"Robot thinks {robot_position[0]} {robot_position[1]}")
        print(f"Actually at {actual_position[0]} {actual_position[1]}\n")

if __name__ == "__main__":
    main()