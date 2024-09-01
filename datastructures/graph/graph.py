class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def display_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, "->", self.adjacency_list[vertex])

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]
        visited.add(start_vertex)
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        visited.add(start_vertex)
        while stack:
            vertex = stack.pop()
            print(vertex, end=" ")
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

# Example usage:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")

# Common operations:
print("Common operations:")
print("------------------")

print("1. Display Graph:")
graph.display_graph()
# Output:
# A -> ['B', 'C']
# B -> ['A', 'D']
# C -> ['A', 'E']
# D -> ['B', 'E']
# E -> ['C', 'D']

print("\n2. BFS:")
graph.bfs("A")
# Output: A B C D E

print("\n3. DFS:")
graph.dfs("A")
# Output: A B D E C