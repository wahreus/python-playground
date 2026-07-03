"""
Problem link: https://open.kattis.com/problems/hidingplaces
Problem source: David Sturgill / Baylor Competitive Learning
"""

import sys
from collections import deque

def bfs(graph: dict[str, list[str]], start: str) -> dict[str, int]:
    return _bfs(graph, start, seen=set())

def _bfs(
        graph: dict[str, list[str]],
        node: str,
        seen: set[str],
        ) -> dict[str, int]:
    queue = deque([node])
    seen.add(node)
    distances = {node: 0}
    while queue:
        current = queue.popleft()
        for child in graph[current]:
            if child not in seen:
                seen.add(child)
                distances[child] = distances[current] + 1
                queue.append(child)
    return distances

def build_graph() -> dict[str, list[str]]:
    files = "abcdefgh"
    ranks = "12345678"
    moves = [
            (2, 1), (2, -1),
            (-2, 1), (-2, -1),
            (1, 2), (1, -2),
            (-1, 2), (-1, -2),
            ]
    graph = {}
    for col in range(8):
        for row in range(8):
            square = files[col] + ranks[row]
            graph[square] = []
            for dc, dr in moves:
                new_col = col + dc
                new_row = row + dr
                if 0 <= new_col < 8 and 0 <= new_row < 8:
                    graph[square].append(files[new_col] + ranks[new_row])
    return graph


def main() -> None:
    graph = build_graph()
    n = int(sys.stdin.readline())
    for _ in range(n):
        start = sys.stdin.readline().strip()
        distances = bfs(graph, start)
        max_distance = max(distances.values())
        hiding_places = [
                        square for square, distance in distances.items()
                        if distance == max_distance
                        ]
        hiding_places.sort(key=lambda square: (-int(square[1]), square[0]))
        print(max_distance, *hiding_places)

if __name__ == "__main__":
    main()