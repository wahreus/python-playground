"""
Problem link: https://open.kattis.com/problems/knightjump
Problem source: Sidhant Bansal / NUS Competitive Programming
"""

import sys
from collections import deque

def valid_moves(current_position, directions, board_size, occupied_cells) -> list[tuple[int, int]]:
    row, col = current_position
    moves = []
    for dy, dx in directions:
        new_row = row + dy
        new_col = col + dx
        if 0 <= new_row < board_size and 0 <= new_col < board_size:
            new_position = (new_row, new_col)
            if new_position not in occupied_cells:
                moves.append(new_position)
    return moves

def BFS(start_position, board_size, occupied_cells) -> int:
    target = (0, 0)
    if start_position == target:
        return 0
    queue = deque([(start_position, 0)])
    visited = {start_position}
    directions = [(2, 1), (2, -1),
                  (1, 2), (1, -2),
                  (-2, 1), (-2, -1),
                  (-1, 2), (-1, -2)
                  ]
    while queue:
        position, steps = queue.popleft()
        for next_position in valid_moves(position, directions, board_size, occupied_cells):
            if next_position in visited:
                continue
            if next_position == target:
                return steps + 1
            visited.add(next_position)
            queue.append((next_position, steps + 1))
    return -1

def main() -> None:
    board_size = int(sys.stdin.readline().strip())
    occupied_cells: set[tuple[int, int]] = set()
    knight_position = None
    for i in range(board_size):
        row = sys.stdin.readline().strip()
        for j, cell in enumerate(row):
            if cell == "#":
                occupied_cells.add((i, j))
            elif cell == "K":
                knight_position = (i, j)
                if knight_position == (0,0):
                    print(0)
                    return
    print(BFS(knight_position, board_size, occupied_cells))
    return

if __name__ == "__main__":
    main()