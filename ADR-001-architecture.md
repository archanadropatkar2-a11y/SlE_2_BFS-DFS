\# ADR-001: BFS and DFS Graph Search Architecture



\## Status



Accepted



\## Context



The SLE-2 project implements Breadth First Search (BFS) and

Depth First Search (DFS) for graph traversal and performance analysis.



For SLE-3, the system needs a clear architecture that separates

the graph data, search algorithms, input, and output.



\## Decision



The system is designed using the C4 architecture model:



1\. System Context

2\. Container

3\. Component

4\. Code



BFS and DFS are maintained as separate search modules.



\### BFS



BFS uses a queue-based traversal approach and explores nodes

level by level.



\### DFS



DFS uses a stack/recursive traversal approach and explores

one branch before moving to another.



\## Architecture Structure



The main parts of the system are:



\- Input

\- Graph Data

\- Search Engine

\- BFS Module

\- DFS Module

\- Result Output



\## Design Reason



Separating BFS and DFS makes the implementation easier to

understand, test, and compare.



Keeping graph data separate from the algorithms also allows

the same graph representation to be used by both searches.



The architecture remains connected to the SLE-2 performance

analysis.



\## Consequences



\### Advantages



\- Clear separation of responsibilities.

\- Easier maintenance.

\- BFS and DFS can be tested independently.

\- Architecture can be understood at multiple C4 levels.

\- SLE-2 performance results remain connected to SLE-3.



\### Limitation



The system is focused on BFS and DFS graph search and does

not include advanced search algorithms such as A\*.



\## Relationship with SLE-2



SLE-2 evaluates the empirical performance of BFS and DFS.



SLE-3 represents the architecture of the same BFS and DFS

system using the C4 model.

