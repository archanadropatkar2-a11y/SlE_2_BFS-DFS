from collections import deque
import time

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return len(visited)

        queue.extend(graph[node])

    return len(visited)


def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return len(visited)

        stack.extend(reversed(graph[node]))

    return len(visited)


runs = 10000

start = time.perf_counter()

for _ in range(runs):
    bfs_nodes = bfs(graph, 'A', 'F')

bfs_time = time.perf_counter() - start


start = time.perf_counter()

for _ in range(runs):
    dfs_nodes = dfs(graph, 'A', 'F')

dfs_time = time.perf_counter() - start


print("BFS")
print("Total time:", bfs_time * 1000, "ms")
print("Nodes expanded:", bfs_nodes)

print("\nDFS")
print("Total time:", dfs_time * 1000, "ms")
print("Nodes expanded:", dfs_nodes)