def hasPath(graph, src, dst, visited=None):
    if visited is None:
        visited = set()
        
    if src == dst:
        return True
    
    if src in visited:
        return False  # Avoid cycles by not revisiting nodes
    
    visited.add(src)
    
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited):
            return True
    
    return False


# Example graph with a cycle: A -> B -> C -> A
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A', 'D'],  # Cycle here back to 'A'
    'D': []
}

# Test cases
print(hasPath(graph, 'A', 'D'))  # True, path: A -> B -> C -> D
print(hasPath(graph, 'D', 'A'))  # False, no path from D to A
print(hasPath(graph, 'A', 'E'))  # False, 'E' not in graph (would error unless you add a check)

# Explanation:
# The graph contains a cycle: A -> B -> C -> A.

# The function avoids infinite recursion by tracking visited nodes in the visited set.

# It successfully finds a path from 'A' to 'D' through the cycle without getting stuck.

# It correctly returns False when no path exists (e.g., 'D' to 'A').


# Time Complexity: O(V + E)
# V = number of vertices (nodes)

# E = number of edges

# Why?
# Each node is visited at most once because of the visited set.

# For each node, all its neighbors (edges) are explored once.

# Total work is proportional to visiting all nodes and edges → linear time.

# Space Complexity: O(V)
# Visited set: stores up to V nodes → O(V)

# Call stack: recursion depth in worst case is O(V) (if the graph is a linear chain)

# Total space is dominated by these two → O(V)

# | Aspect | Complexity | Explanation                        |
# | ------ | ---------- | ---------------------------------- |
# | Time   | `O(V + E)` | Each node and edge visited once    |
# | Space  | `O(V)`     | Visited set + recursion call stack |

