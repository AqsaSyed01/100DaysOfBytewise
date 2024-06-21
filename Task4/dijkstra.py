import heapq

def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    priority_queue = [(0, start)]
    # Dictionary to store the shortest path to each node
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0

    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)

        # If the cost of the current node is greater than the recorded shortest path, skip it
        if current_cost > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_cost + weight

           
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths

# input graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Starting node
start_node = 'A'

# Get the shortest paths from the starting node
shortest_paths = dijkstra(graph, start_node)
print(f"Shortest paths from node {start_node}: {shortest_paths}")
