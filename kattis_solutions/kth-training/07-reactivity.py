"""
Problem link: https://open.kattis.com/problems/reactivity
Problem source: Johan Sannemo and Oskar Werkelin Ahlin / KTH Training
"""

import sys
from collections import deque


def kahns_algorithm(graph: dict[str, list[str]]) -> list[str] | None:
    indegrees = _get_indegrees(graph)
    queue = deque()
    for node in graph:
        if indegrees[node] == 0:
            queue.append(node)
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for child in graph[current]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)
    if len(order) != len(graph):
        return None
    return order


def _get_indegrees(graph: dict[str, list[str]]) -> dict[str, int]:
    indegrees = {}
    for node in graph:
        indegrees[node] = 0
    for node in graph:
        for child in graph[node]:
            indegrees[child] += 1
    return indegrees


def main() -> None:
    n, k = map(int, sys.stdin.readline().split())
    experiments = {i: [] for i in range(n)}
    edges = set()
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        experiments[a].append(b)
        edges.add((a, b))
    order = kahns_algorithm(experiments)
    if order is None:
        print("back to the lab")
        return
    for i in range(len(order) - 1):
        if (order[i], order[i + 1]) not in edges:
            print("back to the lab")
            return
    print(*order)

if __name__ == "__main__":
    main()