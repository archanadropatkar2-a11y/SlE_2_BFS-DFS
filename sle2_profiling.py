import timeit
from graph_data import graph, START_NODE, GOAL_NODE


def bfs(graph, start, goal):
    queue = [start]
    visited = set()
    nodes_expanded = 0

    while queue:
        node = queue.pop(0)

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

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)

    return nodes_expanded


def profile_algorithm(algorithm, name):
    runs = 10000

    total_time = timeit.timeit(
        lambda: algorithm(graph, START_NODE, GOAL_NODE),
        number=runs
    )

    average_time = (total_time / runs) * 1000
    nodes = algorithm(graph, START_NODE, GOAL_NODE)

    print(name)
    print(f"Total time for {runs} runs: {total_time * 1000:.6f} ms")
    print(f"Average time per run: {average_time:.6f} ms")
    print(f"Nodes expanded: {nodes}")
    print()


if __name__ == "__main__":
    profile_algorithm(bfs, "BFS")
    profile_algorithm(dfs, "DFS")