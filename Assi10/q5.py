import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    h = 0
    for i, val in enumerate(state):
        if val != 0:
            tr, tc = divmod(val - 1, 3)
            cr, cc = divmod(i, 3)
            h += abs(tr - cr) + abs(tc - cc)
    return h

def get_neighbors(state):
    idx = state.index(0)
    r, c = divmod(idx, 3)
    res = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr * 3 + nc
            new_s = list(state)
            new_s[idx], new_s[nidx] = new_s[nidx], new_s[idx]
            res.append(tuple(new_s))
    return res

def a_star(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = {start: 0}
    explored = 0
    while pq:
        f, g, state, path = heapq.heappop(pq)
        explored += 1
        if state == GOAL:
            return path + [state], g, explored
        for nxt in get_neighbors(state):
            ng = g + 1
            if nxt not in visited or ng < visited[nxt]:
                visited[nxt] = ng
                heapq.heappush(pq, (ng + manhattan(nxt), ng, nxt, path + [state]))
    return None, 0, explored

start = (1, 2, 3, 4, 0, 5, 7, 8, 6)
path, cost, explored = a_star(start)

print("Initial State:", start)
print("Goal State:", GOAL)
print("Total Moves (Cost):", cost)
print("States Explored:", explored)
print("Intermediate Steps Count:", len(path))
