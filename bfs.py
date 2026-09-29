from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        node = queue.popleft()
        nodes_expanded += 1

        if node == goal:
            return nodes_expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return nodes_expanded