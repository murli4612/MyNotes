# def dfs_iterative(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     stack.append(neighbor)

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'A'],  # cycle back to A
#     'C': ['E'],
#     'D': ['F'],
#     'E': [],
#     'F': []
# }

# print("\nIterative DFS:")
# dfs_iterative(graph, 'A')

def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs_recursive(graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'A'],  # cycle back to A
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}

print("\nRecursive DFS:")
dfs_recursive(graph, 'A')


# ⏱ Time Complexity: O(V + E)
# Where:

# V = number of vertices (nodes)

# E = number of edges

# Why?
# Each node is visited once → O(V)

# For each node, we loop over its neighbors → all edges are explored once → O(E)

# So overall: O(V + E)

# 🧠 Space Complexity: O(V)
# Common to both versions:
# Visited set: stores up to V nodes → O(V)

# 🔁 Iterative DFS:
# Stack: can grow up to O(V) (e.g., deep linear graph like a chain)

# ➤ Total Space: O(V)

# 🌀 Recursive DFS:
# Call stack depth in worst case = O(V) (e.g., skewed or deep graph)

# ➤ Total Space: O(V)

# | DFS Type      | Time Complexity | Space Complexity | Notes                       |
# | ------------- | --------------- | ---------------- | --------------------------- |
# | Recursive DFS | `O(V + E)`      | `O(V)`           | Call stack grows with depth |
# | Iterative DFS | `O(V + E)`      | `O(V)`           | Stack used explicitly       |





