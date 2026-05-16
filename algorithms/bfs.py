from collections import deque


def bfs(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return _bfs(graph, start, target, seen=set())


def _bfs(
        graph: dict[str, list[str]],
        node: str,
        target: str,
        seen: set[str],
        ) -> bool:
        
    queue = deque([node])
    seen.add(node)
    while queue:
        current = queue.popleft()
        if current == target:
            return True
        for child in graph[current]:
            if child not in seen:
                seen.add(child)
                queue.append(child)
    return False


def main() -> None:
    graph = {
            "(A)": ["(B)", "(C)"],
            "(B)": ["(D)", "(E)"],
            "(C)": ["(F)"],
            "(D)": [],
            "(E)": [],
            "(F)": [],
            }
    start = "(A)"
    target = "(F)"

    found = bfs(graph, start, target)
    if found:
        print(f"Target {target} was found!")
    else:
        print(f"Target {target} was not found.")


if __name__ == "__main__":
    main()