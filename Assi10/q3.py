from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': ['F']
}

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    explored = 0
    while queue:
        node, path = queue.popleft()
        explored += 1
        if node == goal:
            return path, explored
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, explored

print("Available Nodes:", list(graph.keys()))
s = input("Start node: ").upper()
g = input("Goal node: ").upper()
path, count = bfs(graph, s, g)

print("Path:", path)
print("Nodes explored:", count)
