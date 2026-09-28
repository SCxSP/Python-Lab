import tkinter as tk
from collections import deque
import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_neighbors(state):
    idx = state.index(0)
    r, c = divmod(idx, 3)
    res = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            nidx = nr * 3 + nc
            new_s = list(state)
            new_s[idx], new_s[nidx] = new_s[nidx], new_s[idx]
            res.append(tuple(new_s))
    return res

def manhattan(state):
    h = 0
    for i, val in enumerate(state):
        if val != 0:
            tr, tc = divmod(val - 1, 3)
            cr, cc = divmod(i, 3)
            h += abs(tr - cr) + abs(tc - cc)
    return h

def solve_bfs(start):
    queue = deque([(start, [])])
    visited = {start}
    explored = 0
    while queue:
        state, path = queue.popleft()
        explored += 1
        if state == GOAL:
            return path + [state], explored
        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [state]))
    return None, explored

def solve_astar(start):
    pq = [(manhattan(start), 0, start, [])]
    visited = {start: 0}
    explored = 0
    while pq:
        f, g, state, path = heapq.heappop(pq)
        explored += 1
        if state == GOAL:
            return path + [state], explored
        for nxt in get_neighbors(state):
            ng = g + 1
            if nxt not in visited or ng < visited[nxt]:
                visited[nxt] = ng
                heapq.heappush(pq, (ng + manhattan(nxt), ng, nxt, path + [state]))
    return None, explored

class EightPuzzleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Puzzle Solver GUI")
        self.state = (1, 2, 3, 4, 0, 5, 7, 8, 6)
        self.labels = []
        frame = tk.Frame(root)
        frame.pack(pady=10)
        for i in range(9):
            lbl = tk.Label(frame, text=str(self.state[i] or " "), font=('Arial', 24), width=4, height=2, relief="solid")
            lbl.grid(row=i//3, column=i%3)
            self.labels.append(lbl)
        
        self.info = tk.Label(root, text="Initial State Ready", font=('Arial', 11))
        self.info.pack(pady=5)
        
        btn_f = tk.Frame(root)
        btn_f.pack()
        tk.Button(btn_f, text="Solve BFS", command=self.run_bfs).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_f, text="Solve A*", command=self.run_astar).pack(side=tk.LEFT, padx=5)

    def run_bfs(self):
        path, explored = solve_bfs(self.state)
        self.info.config(text=f"BFS: {len(path)-1} moves | Explored: {explored}")

    def run_astar(self):
        path, explored = solve_astar(self.state)
        self.info.config(text=f"A*: {len(path)-1} moves | Explored: {explored}")

if __name__ == "__main__":
    root = tk.Tk()
    EightPuzzleGUI(root)
    root.mainloop()
