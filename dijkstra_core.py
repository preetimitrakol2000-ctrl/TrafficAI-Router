class PathOptimizer:
    def __init__(self, intersections_count):
        self.size = intersections_count

    def calculate_optimal_route(self, graph_matrix, starting_point):
        unvisited_nodes = list(range(self.size))
        shortest_path_map = [float('inf')] * self.size
        shortest_path_map[starting_point] = 0

        while unvisited_nodes:
            # Locate the unvisited node with the lowest distance weight
            current_node = min(unvisited_nodes, key=lambda node: shortest_path_map[node])
            unvisited_nodes.remove(current_node)

            for neighbor in range(self.size):
                weight = graph_matrix[current_node][neighbor]
                if weight > 0: # Verify an active link exists in the adjacency grid matrix
                    calculated_distance = shortest_path_map[current_node] + weight
                    if calculated_distance < shortest_path_map[neighbor]:
                        shortest_path_map[neighbor] = calculated_distance

        return shortest_path_map
