# Breadth-First Search (BFS)

# Breadth-First Search (BFS) is a graph traversal algorithm that explores a graph or tree level by level, starting from a given source node.

# How BFS Works:

# Choose a starting node: Select a node in the graph as the starting point.
# Create a queue: Create a queue to hold the nodes to be visited.
# Enqueue the starting node: Add the starting node to the queue.
# Mark the node as visited: Mark the starting node as visited to avoid visiting it again.
# Dequeue a node: Remove a node from the queue.
# Visit the node's neighbors: Visit all the neighbors of the dequeued node that have not been visited yet.
# Enqueue the neighbors: Add the neighbors to the queue.
# Repeat the process: Repeat steps 5-7 until the queue is empty.
# Example:

# Suppose we have the following graph:

# Code
# CopyInsert
#     A
#    / \
#   B   C
#  / \   \
# D   E   F
# If we start at node A, the BFS traversal would be:

# Code
# CopyInsert
# A, B, C, D, E, F
# Types of BFS:

# Unweighted BFS: All edges have the same weight.
# Weighted BFS: Edges have different weights.
# Applications of BFS:

# Finding the shortest path: BFS can be used to find the shortest path between two nodes in an unweighted graph.
# Web crawlers: BFS can be used to crawl the web and index web pages.
# Social network analysis: BFS can be used to analyze social networks and find the shortest path between two individuals.
# Code Example:

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

start_node = 'A'
traversal_order = bfs(graph, start_node)
print(traversal_order)  # Output: ['A', 'B', 'C', 'D', 'E', 'F']