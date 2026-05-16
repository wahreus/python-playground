def dfs(graph: dict[str, list[str]], start: str, target: str) -> bool:
    return _dfs(graph, start, target, seen=set())


def _dfs(
        graph: dict[str, list[str]],
        node: str,
        target: str,
        seen: set[str]
        ) -> bool:

    if node == target:
        return True
    seen.add(node)
    for child in graph[node]:
        if child not in seen:
            if _dfs(graph, child, target, seen):
                return True
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

    found = dfs(graph, start, target)
    if found:
        print(f"Target {target} was found!")
    else:
        print(f"Target {target} was not found.")


if __name__ == "__main__":
    main()