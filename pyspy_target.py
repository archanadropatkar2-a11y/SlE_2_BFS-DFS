from graph_data import graph, START_NODE, GOAL_NODE
from sle2_profiling import bfs, dfs
import time


def run_profiling():
    while True:
        bfs(graph, START_NODE, GOAL_NODE)
        dfs(graph, START_NODE, GOAL_NODE)
        time.sleep(0.01)


if __name__ == "__main__":
    run_profiling()