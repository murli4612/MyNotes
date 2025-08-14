def iterative_bfs(graph,source):
    queue = [source]
    visited = set()
    visited.add(source)
    
    while queue:
        current = queue.pop(0)
        # if current not in visited:
        print(current)
        # visited.add(current)
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
    
graph = {
    'A': ['B', 'C'],
    'B': ['D' ,'A'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}
iterative_bfs(graph,"A")
        
        
# def recursive_bfs(graph, queue, visited):
#     if not queue:
#         return

#     current = queue.pop(0)
#     print(current)

#     for neighbor in graph[current]:
#         if neighbor not in visited:
#             visited.add(neighbor)
#             queue.append(neighbor)

#     recursive_bfs(graph, queue, visited)

# # Graph with a cycle: B -> A
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'A'],  # cycle back to A
#     'C': ['E'],
#     'D': ['F'],
#     'E': [],
#     'F': []
# }

# print("Recursive BFS:")
# recursive_bfs(graph, ['A'], set(['A']))



# ⏱ Time Complexity: O(V + E)
# Where:

# V = number of vertices (nodes)

# E = number of edges (connections)

# Why?
# Each node is visited exactly once (O(V)).

# Each edge is checked once (when visiting its node) → O(E).

# Hence: O(V + E).

# 🧠 Space Complexity: O(V)
# Includes:
# Visited set: stores each node once → O(V)

# Queue: can hold up to O(V) nodes in the worst case

# Call stack: in recursion, the depth will also be O(V) in the worst case

# So total space is:
# 🔹 Visited: O(V)
# 🔹 Queue: O(V)
# 🔹 Call Stack: O(V)
# ➤ Overall: O(V)

# | Factor           | Iterative BFS | Recursive BFS      |
# | ---------------- | ------------- | ------------------ |
# | Time Complexity  | `O(V + E)`    | `O(V + E)`         |
# | Space Complexity | `O(V)`        | `O(V)`             |
# | Stack Usage      | `O(1)` (loop) | `O(V)` (recursion) |
# | Queue Usage      | `O(V)`        | `O(V)`             |


def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)  # Dequeue from front
        print(node, end=' ')  # Process the node

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)  # Enqueue at end

# Example graph as adjacency list (dict)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')
# Output: A B C D E F
