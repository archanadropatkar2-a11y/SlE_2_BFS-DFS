from collections import deque
import time

# Larger graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}


def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)

    return nodes_expanded


def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    nodes_expanded = 0

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


runs = 10000

# BFS profiling
start_time = time.perf_counter()

for i in range(runs):
    bfs_nodes = bfs(graph, 'A', 'O')

end_time = time.perf_counter()

bfs_total_time = (end_time - start_time) * 1000
bfs_average = bfs_total_time / runs


# DFS profiling
start_time = time.perf_counter()

for i in range(runs):
    dfs_nodes = dfs(graph, 'A', 'O')

end_time = time.perf_counter()

dfs_total_time = (end_time - start_time) * 1000
dfs_average = dfs_total_time / runs


# Display results
print("SLE-2: BFS vs DFS Profiling")
print("----------------------------")

print("Number of runs:", runs)

print()
print("BFS Total Time:", bfs_total_time, "ms")
print("BFS Average Time:", bfs_average, "ms")
print("BFS Nodes Expanded:", bfs_nodes)

print()
print("DFS Total Time:", dfs_total_time, "ms")
print("DFS Average Time:", dfs_average, "ms")
print("DFS Nodes Expanded:", dfs_nodes)