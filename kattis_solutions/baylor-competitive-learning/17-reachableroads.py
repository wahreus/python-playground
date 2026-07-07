"""
Problem link: https://open.kattis.com/problems/reachableroads
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import sys

def dfs(graph: dict[str, list[str]], start: str, seen: set[str]) -> None:
    seen.add(start)
    for child in graph[start]:
        if child not in seen:
            dfs(graph, child, seen)

def main() -> None:
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        m = int(sys.stdin.readline().strip())
        r = int(sys.stdin.readline().strip())
        graph = {str(i): [] for i in range(m)}
        for _ in range(r):
            a, b = sys.stdin.readline().strip().split()
            graph[a].append(b)
            graph[b].append(a)
        seen = set()
        road_networks = 0
        for endpoint in graph:
            if endpoint not in seen:
                road_networks += 1
                dfs(graph, endpoint, seen)
        print(road_networks - 1)

if __name__ == "__main__":
    main()