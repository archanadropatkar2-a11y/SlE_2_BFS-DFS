# SLE-2: BFS vs DFS Profiling

## Course
02AML204 – Introduction to Artificial Intelligence

## Project
Empirical Performance Analysis of BFS and DFS

## Objective
To compare BFS and DFS using actual execution time
and number of nodes expanded.

## Technologies Used
- Python
- GitHub
- GitHub Copilot
- Visual Studio Code

## Algorithms
- Breadth First Search (BFS)
- Depth First Search (DFS)

## Profiling Method
- Python time.perf_counter()
- 10,000 runs
- Execution time
- Nodes expanded

## Project Structure

- sle2_bfs_vs_dfs.py – Main profiling program
- bfs.py – BFS implementation
- dfs.py – DFS implementation
- CONTRIBUTIONS.md – AI contribution log
- bfs_dfs_flowchart.png – Algorithm flowchart

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Runs | 10,000 | 10,000 |
| Total Time | 27.6190 ms | 11.8701 ms |
| Average Time | 0.0027619 ms | 0.0011870 ms |
| Nodes Expanded | 15 | 4 |

## Observation

For the selected graph and goal, DFS expanded fewer nodes
and recorded a lower measured execution time than BFS.

## Conclusion

The experiment demonstrates that profiling can be used to
compare search algorithms using actual measurements.
Performance can vary depending on graph structure and
goal location.

## AI Usage

GitHub Copilot was used to assist with code structure,
documentation, and development. The generated suggestions
were reviewed, modified, and tested.

## Author

Archana Dropatkar