def hasPath(graph, src, dst):
    if src == dst:
        return True
    
    for neighbour in graph[src]:
        if hasPath(graph,neighbour,dst) == True:
            return True
    return False

graph = {
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}
print(hasPath(graph,'f','j'))


# This is a depth-first search (DFS) to check if a path exists from src to dst.

# It explores all possible paths recursively without tracking visited nodes
# (so it can revisit nodes in case of cycles — this is unsafe for cyclic graphs).

# ⏱ Time Complexity: O(V + E) in the best case (acyclic), but worse if revisiting nodes
# V = number of vertices (nodes)

# E = number of edges

# In an acyclic graph (like the one you gave):
# The function visits each node and edge at most once in a depth-first manner.

# So the worst-case time complexity is O(V + E).

# ⚠️ In a cyclic graph:
# There is no visited set, so the function may go into infinite recursion or revisit nodes multiple times.

# In that case, the time complexity can degrade to exponential in the worst case.


# 🧠 Space Complexity: O(V) (in case of acyclic graph)
# Due to:
# Call stack depth: In the worst case (a deep linear graph), the recursion stack can grow up to O(V).

# If you add a visited set (as in safe DFS):
# Space would still be O(V) for:

# visited set

# Recursion stack

# There is no path from 'f' to 'j' in this graph.

# The function explores all reachable paths from 'f', so it will traverse:

# 'f' → 'g' → 'h'

# 'f' → 'i' → 'g' → 'h' → 'k'

# Total nodes visited: f, g, h, i, k = 5 nodes
# Total edges followed: up to 5

# So the function executes in linear time for this input.

# | Metric             | Complexity |
# | ------------------ | ---------- |
# | Time               | `O(V + E)` |
# | Space (call stack) | `O(V)`     |



