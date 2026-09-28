def dfs_maze(maze, start, dest):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = {start}

    while stack:
        (r, c), path = stack.pop()
        if (r, c) == dest:
            return path
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))
    return None

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
dest = (4, 4)
print("Maze start:", start, "dest:", dest)
path = dfs_maze(maze, start, dest)
print("DFS Maze Path:", path)
