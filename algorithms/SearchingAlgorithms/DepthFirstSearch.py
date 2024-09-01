# Depth-First Search (DFS)

# Depth-First Search (DFS) is a graph traversal algorithm that explores a graph or tree by visiting a node and then visiting all of its neighbors before backtracking.

# How DFS Works:

# Choose a starting node: Select a node in the graph as the starting point.
# Mark the node as visited: Mark the starting node as visited to avoid visiting it again.
# Explore the node's neighbors: Visit all the neighbors of the starting node that have not been visited yet.
# Repeat the process: Recursively repeat the process for each neighbor until all nodes have been visited.
# Backtrack: When all neighbors of a node have been visited, backtrack to the previous node.
# Example:

# Suppose we have the following graph:

# Code
# CopyInsert
#     A
#    / \
#   B   C
#  / \   \
# D   E   F
# If we start at node A, the DFS traversal would be:

# Code
# CopyInsert
# A, B, D, E, C, F
# Types of DFS:

# Pre-order DFS: Visit the node before visiting its neighbors.
# In-order DFS: Visit the node after visiting its left neighbor and before visiting its right neighbor.
# Post-order DFS: Visit the node after visiting all its neighbors.
# Applications of DFS:

# Topological sorting: DFS can be used to perform topological sorting on a directed acyclic graph (DAG).
# Finding strongly connected components: DFS can be used to find strongly connected components in a graph.
# Testing whether a graph is connected: DFS can be used to test whether a graph is connected.
# Code Example:

def dfs(graph, start):
    visited = set()
    traversal_order = []

    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
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
traversal_order = dfs(graph, start_node)
print(traversal_order)  # Output: ['A', 'B', 'D', 'E', 'C', 'F']



