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
    graph = {
            "(A)": ["(B)", "(C)"],
            "(B)": ["(D)", "(E)"],
            "(C)": ["(F)"],
            "(D)": [],
            "(E)": [],
            "(F)": [],
            }

    order = kahns_algorithm(graph)

    if order is None:
        print("The graph has a cycle.")
    else:
        print("Topological order:")
        print(*order)


if __name__ == "__main__":
    main()