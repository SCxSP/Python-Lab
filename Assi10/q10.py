from collections import deque
import heapq, time

GRID = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

START, GOAL = (0, 0), (4, 4)

def h(p): return abs(p[0] - GOAL[0]) + abs(p[1] - GOAL[1])

def get_neighbors(p):
    r, c = p
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5 and GRID[nr][nc] == 0:
            yield (nr, nc)

def run_bfs():
    q = deque([(START, [START])])
    vis = {START}
    exp = 0
    t0 = time.time()
    while q:
        curr, path = q.popleft()
        exp += 1
        if curr == GOAL:
            return path, exp, time.time() - t0
        for nxt in get_neighbors(curr):
            if nxt not in vis:
                vis.add(nxt)
                q.append((nxt, path + [nxt]))
    return None, exp, time.time() - t0

def run_astar():
    pq = [(h(START), 0, START, [START])]
    vis = {START: 0}
    exp = 0
    t0 = time.time()
    while pq:
        f, g, curr, path = heapq.heappop(pq)
        exp += 1
        if curr == GOAL:
            return path, exp, time.time() - t0
        for nxt in get_neighbors(curr):
            if nxt not in vis or g + 1 < vis[nxt]:
                vis[nxt] = g + 1
                heapq.heappush(pq, (g + 1 + h(nxt), g + 1, nxt, path + [nxt]))
    return None, exp, time.time() - t0

print("Navigation Comparison (Grid 5x5):")
b_path, b_exp, b_time = run_bfs()
a_path, a_exp, a_time = run_astar()

print(f"BFS Path Cost: {len(b_path)-1} | Explored: {b_exp} | Time: {b_time*1000:.3f}ms")
print(f"A*  Path Cost: {len(a_path)-1} | Explored: {a_exp} | Time: {a_time*1000:.3f}ms")
print("\nPEAS:")
print("P: Shortest path & safety | E: 2D Grid | A: Move (U/D/L/R) | S: Coordinate sensor")
