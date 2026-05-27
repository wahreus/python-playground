import heapq


def dijkstra(graph: dict[str, list[tuple[str, int]]], start: str) -> dict[str, int]:
    distances = {start: 0}
    queue = [(0, start)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue
        for child, weight in graph[current_node]:
            if weight < 0:
                raise ValueError("Dijkstra's algorithm does not support negative weights.")
            new_distance = current_distance + weight
            if child not in distances or new_distance < distances[child]:
                distances[child] = new_distance
                heapq.heappush(queue, (new_distance, child))
    return distances


def main() -> None:
    graph = {
            "(A)": [("(B)", 4), ("(C)", 2)],
            "(B)": [("(C)", 5), ("(D)", 10)],
            "(C)": [("(E)", 3)],
            "(D)": [],
            "(E)": [("(D)", 4)],
            }
    start = "(A)"

    distances = dijkstra(graph, start)
    print(f"Shortest distances from {start}:")
    for node in graph:
        if node in distances:
            print(f"- {node}: {distances[node]}")
        else:
            print(f"- {node}: unreachable")


if __name__ == "__main__":
    main()