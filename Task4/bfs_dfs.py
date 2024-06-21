from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return visited

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return visited

# Example input graph
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Performing BFS and DFS starting from node 2
bfs_result = bfs(graph, 2)
dfs_result = dfs(graph, 2)

print(f"BFS starting from node 2: {bfs_result}")
print(f"DFS starting from node 2: {dfs_result}")
