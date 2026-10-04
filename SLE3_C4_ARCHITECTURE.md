\# SLE-3: C4 Architecture Design



\## BFS and DFS Graph Search System



\### 1. System Overview



The BFS and DFS Graph Search System is a Python-based graph search system

that implements Breadth First Search (BFS) and Depth First Search (DFS).



The system accepts a graph, starting node, and target node and performs

the selected search algorithm to find the target.



This SLE-3 architecture extends the SLE-2 performance analysis by

showing the system structure using the C4 model.



\---



\## 2. C4 Level 1 – System Context



The Context diagram shows the complete system and its interaction with

the user.



\### User



The user:



\- Provides the graph.

\- Selects the starting node.

\- Provides the target node.

\- Selects BFS or DFS.

\- Receives the search result.



\### Diagram



!\[C4 Context Diagram](diagrams/context-diagram.jpg)



\---



\## 3. C4 Level 2 – Container



The Container diagram shows the major parts of the BFS and DFS system.



\### Main Containers



\- Input Module

\- Graph Data

\- Search Engine

\- BFS Module

\- DFS Module

\- Result Output



\### Diagram



!\[C4 Container Diagram](diagrams/container-diagram.jpg)



\---



\## 4. C4 Level 3 – Component



The Component diagram focuses on the Search Engine and shows its

internal responsibilities.



\### Main Components



\- Frontier Manager

\- Visited Manager

\- Goal Test

\- Path Manager



The Frontier Manager uses a queue for BFS and a stack for DFS.

The Visited Manager prevents unnecessary revisiting of nodes.

The Goal Test checks whether the target node has been reached.



\### Diagram



!\[C4 Component Diagram](diagrams/component-diagram.jpg)



\---



\## 5. C4 Level 4 – Code



The Code-level view shows the main program modules and functions

used to implement the BFS and DFS search system.



\### Main Code Elements



\- Graph Module

\- BFS Module

\- DFS Module

\- SLE-2 Module

\- Search functions

\- Performance measurement functions



\### Diagram



!\[C4 Code Diagram](diagrams/code-diagram.jpg)



\---



\## 6. Design Decisions



1\. BFS and DFS are implemented as separate modules.

2\. Graph data is kept separately from search algorithms.

3\. A queue is used for BFS traversal.

4\. A stack is used for DFS traversal.

5\. Visited nodes are maintained to avoid repeated traversal.

6\. Performance measurement from SLE-2 is retained.

7\. The C4 model separates system context, containers, components,

&#x20;  and code-level details.



\---



\## 7. Relationship with SLE-2



SLE-2 focused on empirical performance analysis of BFS and DFS.



SLE-3 extends the same system by representing its architecture using

the four C4 levels:



\*\*Context → Container → Component → Code\*\*



The architecture therefore remains connected to the BFS and DFS

implementation and its SLE-2 performance evaluation.



\---



\## 8. Conclusion



The C4 architecture provides a clear view of the BFS and DFS Graph

Search System at different levels of abstraction.



It improves understanding of the system structure, responsibilities,

interactions, and implementation modules.

