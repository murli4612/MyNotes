from collections import defaultdict

def directedPath(edges, src, dst):
    graph = buildDirectedGraph(edges)
    print(graph)
    visited = set()
    return hasPath(graph, src, dst, visited)

def buildDirectedGraph(edges):
    adjacency_list = defaultdict(list)
    for from_node, to_node in edges:
        adjacency_list[from_node].append(to_node)
    return adjacency_list

def hasPath(graph, src, dest, visited):
    if src == dest:
        return True
    if src in visited:
        return False
    visited.add(src)

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dest, visited):
            return True
    return False

# Example usage
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(directedPath(edges, 'l', 'm'))  # Output: False
print(directedPath(edges, 'm', 'l'))  # Output: True (m -> k -> l)
