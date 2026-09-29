from graph_data import graph, START_NODE, GOAL_NODE
from sle2_profiling import bfs, dfs
import time
import sys


def run_bfs():
    while True:
        bfs(graph, START_NODE, GOAL_NODE)
        time.sleep(0.001)


def run_dfs():
    while True:
        dfs(graph, START_NODE, GOAL_NODE)
        time.sleep(0.001)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use: python pyspy_target.py bfs")
        print("or:  python pyspy_target.py dfs")
        sys.exit()

    if sys.argv[1].lower() == "bfs":
        run_bfs()

    elif sys.argv[1].lower() == "dfs":
        run_dfs()

    else:
        print("Invalid option. Use bfs or dfs.")