import math


def prims_algorithm(node_positions: dict[str, tuple[float, float]]) -> tuple[float, list[tuple[str, str, float]]]:
    if not node_positions:
        return 0.0, []
    nodes = list(node_positions)
    positions = [node_positions[node] for node in nodes]
    number_of_nodes = len(nodes)
    explored = [False] * number_of_nodes
    cheapest_squared_cost = [math.inf] * number_of_nodes
    cheapest_parent = [-1] * number_of_nodes
    cheapest_squared_cost[0] = 0.0
    total_weight = 0.0
    tree_edges = []
    for _ in range(number_of_nodes):
        current = -1
        current_cost = math.inf
        for node in range(number_of_nodes):
            if (not explored[node] and cheapest_squared_cost[node] < current_cost):
                current = node
                current_cost = cheapest_squared_cost[node]
        explored[current] = True
        if cheapest_parent[current] != -1:
            edge_weight = math.sqrt(current_cost)
            total_weight += edge_weight
            parent = cheapest_parent[current]
            tree_edges.append((nodes[parent], nodes[current], edge_weight))
        current_x, current_y = positions[current]
        for child in range(number_of_nodes):
            if not explored[child]:
                child_x, child_y = positions[child]
                dx = child_x - current_x
                dy = child_y - current_y
                squared_distance = (dx*dx + dy*dy)
                if squared_distance < cheapest_squared_cost[child]:
                    cheapest_squared_cost[child] = squared_distance
                    cheapest_parent[child] = current
    return total_weight, tree_edges


def main() -> None:
    node_positions = {
        "(A)": (0.0, 0.0),
        "(B)": (2.0, 1.0),
        "(C)": (4.0, 0.0),
        "(D)": (3.0, 3.0)
    }
    total_weight, tree_edges = prims_algorithm(node_positions)
    print("Minimum spanning tree:")
    for parent, child, weight in tree_edges:
        print(f"{parent} -> {child}: {weight}")
    print(f"Total weight: {total_weight}")


if __name__ == "__main__":
    main()