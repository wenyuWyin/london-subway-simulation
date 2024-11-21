# London Subway Route Recommended System
### Overview
This project involves the development of a comprehensive system to represent and analyze London subway networks, with multiple features to add functionality and enhance usability. The implementation is built around graph-based representations and algorithms to solve practical transportation and planning problems.

#### Graph Representation of Subway Data
The system implemented in this project processes subway network data provided in CSV format and represents it as a graph data structure. The graph uses nodes to represent subway stations and edges to represent connections between them, including associated travel times or distances as weights.
#### Shortest Path Calculation
The primary feature is finding the shortest route between any two stations using:
1. Dijkstra's Algorithm - for finding the shortest path based on total travel time.
2. A* Algorithm - incorporates heuristic functions for faster computation in specific scenarios.
#### Subway Patrol Planning
The feature is to determine an efficient patrol route covering a subset of critical stations (e.g., event hotspots), solving a variation of the Travelling Salesman Problem.
#### Urbanism Planning
Added functionality for Zones and Connected Components Analysis, which identifies isolated "transportation islands" within zones and analyze their interconnections. Addressed scenarios like zones containing disconnected clusters requiring cross-zone travel.
#### Random Graph Generation
Developed a Graph Generator to create synthetic networks for unbiased testing. Supported degree distribution (uniform, normal) to simulate station connectivity.
#### Realistic Transportation Graphs
Incorporated transportation-specific metrics like centrality and graph diameter to simulate realistic zones and interconnections. Validated the realism and computational efficiency of generated graphs.
