import heapq
from collections import deque

graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu', 97), ('Bucharest', 101), ('Craiova', 138)],
    'Craiova': [('Rimnicu', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

h = {
    'Arad': 366, 'Zerind': 374, 'Oradea': 380, 'Sibiu': 253, 'Fagaras': 176,
    'Rimnicu': 193, 'Pitesti': 100, 'Craiova': 160, 'Drobeta': 242,
    'Mehadia': 241, 'Lugoj': 244, 'Timisoara': 329, 'Bucharest': 0
}

def greedy_bfs(start, goal):
    pq = [(h[start], start, [start])]
    visited = {start}
    explored = 0
    while pq:
        _, node, path = heapq.heappop(pq)
        explored += 1
        if node == goal:
            return path, explored
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                heapq.heappush(pq, (h[neighbor], neighbor, path + [neighbor]))
    return None, explored

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    explored = 0
    while queue:
        node, path = queue.popleft()
        explored += 1
        if node == goal:
            return path, explored
        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, explored

s = input("Start city (default Arad): ") or "Arad"
g = "Bucharest"

g_path, g_exp = greedy_bfs(s, g)
b_path, b_exp = bfs(s, g)

print("Greedy BFS Path:", g_path, "| Explored:", g_exp)
print("Standard BFS Path:", b_path, "| Explored:", b_exp)
