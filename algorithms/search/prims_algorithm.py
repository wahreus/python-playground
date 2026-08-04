import math

def closest_unexplored_node(explored: list[bool],
                            cheapest_squared_cost: list[float],
                            ) -> int:
    return min((node for node, is_explored in enumerate(explored)
                if not is_explored
                ), key=lambda node: cheapest_squared_cost[node])

def squared_distance(first_position: tuple[float, float],
                     second_position: tuple[float, float],
                     ) -> float:
    dx = second_position[0] - first_position[0]
    dy = second_position[1] - first_position[1]
    return dx * dx + dy * dy

def prims_algorithm(node_positions: dict[str, tuple[float, float]]
                    ) -> tuple[float, list[tuple[str, str, float]]]:
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
        current = closest_unexplored_node(explored, cheapest_squared_cost)
        current_cost = cheapest_squared_cost[current]
        explored[current] = True
        if cheapest_parent[current] != -1:
            edge_weight = math.sqrt(current_cost)
            total_weight += edge_weight
            parent = cheapest_parent[current]
            tree_edges.append((nodes[parent], nodes[current], edge_weight))
        for child in range(number_of_nodes):
            if not explored[child]:
                distance = squared_distance(positions[current],
                                            positions[child])
                if distance < cheapest_squared_cost[child]:
                    cheapest_squared_cost[child] = distance
                    cheapest_parent[child] = current
    return total_weight, tree_edges

def main() -> None:
    node_positions = {"(A)": (0.0, 0.0),
                      "(B)": (2.0, 1.0),
                      "(C)": (4.0, 0.0),
                      "(D)": (3.0, 3.0)}
    total_weight, tree_edges = prims_algorithm(node_positions)
    print("Minimum spanning tree:")
    for parent, child, weight in tree_edges:
        print(f"{parent} -> {child}: {weight}")
    print(f"Total weight: {total_weight}")

if __name__ == "__main__":
    main()
