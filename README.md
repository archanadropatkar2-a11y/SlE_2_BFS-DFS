# SLE-2: BFS vs DFS Profiling

## Course
02AML204 – Introduction to Artificial Intelligence

## Experiment
Empirical Performance Analysis of BFS and DFS

## Problem
BFS and DFS were applied to the same graph-search problem.

## Profiling Method
- Programming Language: Python
- Profiling method: time.perf_counter()
- Number of runs: 10,000
- Metrics: Execution time and nodes expanded

## Results

| Metric | BFS | DFS |
|---|---:|---:|
| Number of Runs | 10,000 | 10,000 |
| Total Time (ms) | 27.6190 | 11.8701 |
| Average Time (ms) | 0.0027619 | 0.0011870 |
| Nodes Expanded | 15 | 4 |

## Observation

For this particular graph and goal, DFS expanded fewer nodes than BFS.
DFS also recorded a lower total and average execution time in this experiment.

## Conclusion

The experiment demonstrated how profiling can be used to compare search algorithms using actual measurements. The results show that algorithm performance can depend on the structure of the problem and the location of the goal node.