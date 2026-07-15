"""
Problem link: https://open.kattis.com/problems/islandhopping
Problem source: Greg Hamerly / Baylor Competitive Learning
"""

import math
import sys

def prims_algorithm(vertices):
    number_of_vertices = len(vertices)
    if number_of_vertices <= 1:
        return 0.0, []
    explored = [False] * number_of_vertices
    cheapest_cost = [math.inf] * number_of_vertices
    cheapest_parent = [None] * number_of_vertices
    start_vertex = 0
    cheapest_cost[start_vertex] = 0.0
    total_weight = 0.0
    result_edges = []
    for _ in range(number_of_vertices):
        current_vertex = -1
        for vertex in range(number_of_vertices):
            if (not explored[vertex] and (current_vertex == -1 or cheapest_cost[vertex] < cheapest_cost[current_vertex])):
                current_vertex = vertex
        explored[current_vertex] = True
        total_weight += cheapest_cost[current_vertex]
        parent = cheapest_parent[current_vertex]
        if parent is not None:
            result_edges.append((vertices[parent], vertices[current_vertex], cheapest_cost[current_vertex]))
        for neighbor in range(number_of_vertices):
            if not explored[neighbor]:
                ax, ay = vertices[current_vertex][0], vertices[current_vertex][1]
                bx, by = vertices[neighbor][0], vertices[neighbor][1]
                edge_weight = ((bx-ax)**2+(by-ay)**2)**(1/2)
                if edge_weight < cheapest_cost[neighbor]:
                    cheapest_cost[neighbor] = edge_weight
                    cheapest_parent[neighbor] = current_vertex
    return total_weight, result_edges

def main() -> None:
    test_cases = int(sys.stdin.readline())
    for _ in range(test_cases):
        number_of_islands = int(sys.stdin.readline())
        island_positions = []
        for _ in range(number_of_islands):
            x, y = map(float, sys.stdin.readline().split())
            island_positions.append((x, y))
        total_bridge_length, _ = prims_algorithm(island_positions)
        print(total_bridge_length)

if __name__ == "__main__":
    main()